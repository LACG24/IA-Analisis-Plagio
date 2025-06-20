import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
import copy
import sys
import json
import jinja2
from typing import List, Dict, Any, Union
from pathlib import Path


def _obtain_information(X: pd.DataFrame, 
                  tree_model: Any,
                  target_names: List[str], 
                  target_colors: List[str],
                  color_map: str) -> Dict[str, Any]:
    binary_attrs = [col for col in X.columns if set(X[col].unique()) == {0, 1}]
    int_attrs = [col for col in X.columns if X[col].dtype in ['int64', 'int32'] and col not in binary_attrs]

    if not isinstance(target_names, list) or len(target_names) != tree_model.tree_.n_classes:
        raise ValueError(f"target_names should be a list of length {tree_model.tree_.n_classes}.")

    target_colors = target_colors or [matplotlib.colors.rgb2hex(plt.get_cmap(color_map or 'tab20')(i))
                                    for i in range(tree_model.tree_.n_classes[0])]

    return {
        'tree_model': tree_model,
        'features': [X.columns[i] for i in tree_model.tree_.feature],
        'binary_features': binary_attrs,
        'int_features': int_attrs, 
        'target_names': target_names,
        'target_colors': target_colors
    }


def _analyze_tree(node_id: int,
                parent: Union[int, str],
                pos: str,
                tree_info: Dict[str, Any]) -> Dict[str, Any]:
    tree_model = tree_info['tree_model']
    features = tree_info['features']
    binary_attrs = tree_info['binary_features']
    int_attrs = tree_info['int_features']
    target_names = tree_info['target_names']

    node: Dict[str, Any] = {}
    
    if parent == 'null':
        node['name'] = "HEAD"
    else:
        feature = features[parent]
        threshold = tree_model.tree_.threshold[parent]
        
        if feature in binary_attrs:
            node['name'] = f"{feature}: {'0' if pos == 'left' else '1'}"
        else:
            comparison = "<=" if pos == 'left' else ">"
            threshold_val = int(threshold) if feature in int_attrs else round(threshold, 3)
            node['name'] = f"{feature} {comparison} {threshold_val}"

    node['parent'] = int(parent) if isinstance(parent, (int, float)) else parent
    node['self'] = int(node_id)
    node['sample'] = int(tree_model.tree_.n_node_samples[node_id])
    node['impurity'] = round(tree_model.tree_.impurity[node_id], 3)
    node['value'] = [int(v) for v in tree_model.tree_.value[node_id][0]]
    node['predict'] = target_names[np.argmax(node['value'])]
    node['color'] = tree_info['target_colors'][np.argmax(node['value'])]
    node['pos'] = pos

    left_child = tree_model.tree_.children_left[node_id]
    right_child = tree_model.tree_.children_right[node_id]
    
    if left_child != -1 or right_child != -1:
        node['children'] = []
        if left_child != -1:
            node['children'].append(_analyze_tree(left_child, node_id, 'left', tree_info))
        if right_child != -1:
            node['children'].append(_analyze_tree(right_child, node_id, 'right', tree_info))

    return node


def _extract_rules(node_id: int,
                  parent: Union[int, str],
                  pos: str, 
                  tree_rules: Dict[int, Dict],
                  tree_info: Dict[str, Any]) -> Dict[int, Dict]:
    features = tree_info['features']
    tree_model = tree_info['tree_model']

    tree_rules[node_id] = {'features': {}}

    if parent != "null":
        tree_rules[node_id]['features'] = copy.deepcopy(tree_rules[parent]['features'])
        
        feature = features[parent]
        threshold = tree_model.tree_.threshold[parent]
        
        if feature not in tree_rules[node_id]['features']:
            tree_rules[node_id]['features'][feature] = [-sys.maxsize, sys.maxsize]
            
        if pos == "left":
            tree_rules[node_id]['features'][feature][1] = min(threshold, 
                                                            tree_rules[node_id]['features'][feature][1])
        else:
            tree_rules[node_id]['features'][feature][0] = max(threshold,
                                                            tree_rules[node_id]['features'][feature][0])

    left_child = tree_model.tree_.children_left[node_id]
    right_child = tree_model.tree_.children_right[node_id]
    
    if left_child != -1:
        _extract_rules(left_child, node_id, "left", tree_rules, tree_info)
    if right_child != -1:
        _extract_rules(right_child, node_id, "right", tree_rules, tree_info)

    return tree_rules


def _clean_rules(tree_rules: Dict[int, Dict],
                tree_info: Dict[str, Any]) -> Dict[int, List[str]]:
    tree_rules_clean = {}
    
    for node_id, node in tree_rules.items():
        rules = []
        
        for feature, bounds in node['features'].items():
            lower_bound, upper_bound = bounds
            
            if feature in tree_info['binary_features']:
                rule = f"{feature}: {'0' if lower_bound == -sys.maxsize else '1'}"
            else:
                if lower_bound == -sys.maxsize:
                    threshold = int(upper_bound) if feature in tree_info['int_features'] else round(upper_bound, 3)
                    rule = f"{feature} <= {threshold}"
                elif upper_bound == sys.maxsize:
                    threshold = int(lower_bound) if feature in tree_info['int_features'] else round(lower_bound, 3)
                    rule = f"{feature} > {threshold}"
                else:
                    lower = int(lower_bound) if feature in tree_info['int_features'] else round(lower_bound, 3)
                    upper = int(upper_bound) if feature in tree_info['int_features'] else round(upper_bound, 3)
                    rule = f"{lower} < {feature} <= {upper}"
                    
            rules.append(rule)
            
        tree_rules_clean[int(node_id)] = sorted(rules, key=len)
        
    return tree_rules_clean


def generate_decision_tree(tree_model: Any,
               X: pd.DataFrame,
               target_names: List[str],
               save_path: Union[str, Path],
               target_colors: List[str] = None,
               color_map: str = 'tab10',
               width: int = 1200,
               height: int = 1000) -> None:
    save_path = Path(save_path)
    
    tree_info = _obtain_information(X, tree_model, list(target_names), target_colors, color_map)
    final_tree = _analyze_tree(0, "null", "null", tree_info)
    tree_rules = _extract_rules(0, "null", "null", {}, tree_info)
    tree_rules_clean = _clean_rules(tree_rules, tree_info)

    template = jinja2.Template((Path('./tree_template.html')).read_text())
    render_result = {
        'tree': json.dumps(final_tree),
        'rule': json.dumps(tree_rules_clean),
        'num_node': tree_info['tree_model'].tree_.capacity,
        'tree_depth': tree_info['tree_model'].tree_.max_depth,
        'width': width,
        'height': height,
        'n_classes': tree_info['tree_model'].n_classes_
    }
    
    save_path.write_text(template.render(render_result))
    print(f'Saved to {save_path}')


def generate_sankey_diagram(tree_model: Any,
                 X: pd.DataFrame, 
                 target_names: List[str],
                 save_path: Union[str, Path],
                 target_colors: List[str] = None,
                 color_map: str = 'tab10',
                 width: int = 1200,
                 height: int = 1000) -> None:
    save_path = Path(save_path)
    
    tree_info = _obtain_information(X, tree_model, list(target_names), target_colors, color_map)
    final_tree = _analyze_tree(0, "null", "null", tree_info)
    tree_rules = _extract_rules(0, "null", "null", {}, tree_info)
    tree_rules_clean = _clean_rules(tree_rules, tree_info)

    template = jinja2.Template((Path('./sankey_template.html')).read_text())
    render_result = {
        'tree': json.dumps(final_tree),
        'rule': json.dumps(tree_rules_clean),
        'num_node': tree_info['tree_model'].tree_.capacity,
        'tree_depth': tree_info['tree_model'].tree_.max_depth,
        'width': width,
        'height': height,
        'target_colors': tree_info['target_colors'],
        'max_samples': np.max(tree_info['tree_model'].tree_.n_node_samples),
        'min_samples': np.min(tree_info['tree_model'].tree_.n_node_samples)
    }
    
    save_path.write_text(template.render(render_result))
    print(f'Saved to {save_path}')