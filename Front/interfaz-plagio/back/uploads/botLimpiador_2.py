from mesa import Agent, Model
from mesa.space import MultiGrid
from mesa.time import BaseScheduler
import sys
import random
import time

from mesa.visualization.modules import CanvasGrid
from mesa.visualization.ModularVisualization import ModularServer
from mesa.visualization.UserParam import Slider, Checkbox


class Incinerator(Agent):
    burned_garbage = 0
    BURNING = 0
    NOT_BURNING = 1
    
    def checkAgentType(self, agentList):
        contBots = 0
        contGarbages = 0
        
        for agent in agentList:
            if isinstance(agent, Bot):
                contBots += 1
            elif isinstance(agent, Garbage):
                contGarbages += 1
        return [contBots, contGarbages]
        
    def __init__(self, model: Model, pos: tuple):
        super().__init__(model.next_id(), model)
        self.pos = pos
        self.condition = self.NOT_BURNING
        self.hasGarbage = False
        self.burning_time = 0
        self.burning_duration = 1

    def step(self):
        agentList = self.model.grid.get_cell_list_contents(self.pos)
        filterAgents = self.checkAgentType(agentList)

        for agent in agentList:
            if isinstance(agent, Garbage) and filterAgents[0] == 0 and filterAgents[1] > 0:
                self.model.grid.remove_agent(agent)
                self.condition = self.BURNING
                self.burning_time = time.time()

            if self.condition == self.BURNING and time.time() - self.burning_time >= self.burning_duration:
                self.condition = self.NOT_BURNING
                self.burning_time = 0


class Garbage(Agent):
    def __init__(self, model: Model, pos: tuple):
        super().__init__(model.next_id(), model)
        self.pos = pos
        
    def step(self):  
        pass

class Bot(Agent):
    OCUPADO = 0
    LIBRE = 1
    cleaner_bots_list = list()

    def __init__(self, model: Model, pos):       
        super().__init__(model.next_id(), model)
        self.condition = self.LIBRE
        self.garbage = None
        self.pos = pos
        
        if self.pos is None:
            self.pos = [0, 0]
            self.pos[0] = self.random.randint(0, model.grid.width - 1)
            self.pos[1] = self.random.randint(0, model.grid.height - 1)
            self.pos = tuple(self.pos)

        Bot.cleaner_bots_list.append(self)

    def moveToIncinerator(self):
        middle_x = self.model.grid.width // 2
        middle_y = self.model.grid.height // 2
        incineratorPosition = (middle_x, middle_y)

        if self.pos[1] < incineratorPosition[1]:
            newPosition = (self.pos[0], self.pos[1] + 1)
        elif self.pos[1] > incineratorPosition[1]:
            newPosition = (self.pos[0], self.pos[1] - 1)
        elif self.pos[0] < incineratorPosition[0]:
            newPosition = (self.pos[0] + 1, self.pos[1])
        elif self.pos[0] > incineratorPosition[0]:
            newPosition = (self.pos[0] - 1, self.pos[1])
        else:
            newPosition = self.pos
                
        return newPosition
                
    
    def step(self):
        agentList = self.model.grid.get_cell_list_contents(self.pos)

        if self.condition == self.LIBRE:
            thatGarbageAgent = None
            for agent in agentList:
                if isinstance(agent, Garbage):
                    thatGarbageAgent = agent
                    break
                
            if thatGarbageAgent is not None and self.garbage is None:
                self.condition = self.OCUPADO
                self.garbage = thatGarbageAgent
            else:           
                next_moves = self.model.grid.get_neighborhood(self.pos, moore=False)
                next_move = self.random.choice(next_moves)
                self.model.grid.move_agent(self, next_move)
                    
        elif self.condition == self.OCUPADO:
            newpos = self.moveToIncinerator()
            self.model.grid.move_agent(self, newpos)
            self.model.grid.move_agent(self.garbage, newpos)
            
            for agent in agentList:
                if isinstance(agent, Incinerator):
                    self.model.grid.move_agent(self, (newpos[0], newpos[1] + 1))
                    self.garbage = None
                    self.condition = self.LIBRE
                    break

    @classmethod
    def displayListOfCleaners(cls):
        for bot in cls.cleaner_bots_list:
            print(f"Cleaner Bot ID: {bot.unique_id}, Coords: ({bot.pos[0]}, {bot.pos[1]})")

class Maze(Model):
    def __init__(self, density=0.2, board_size_big=True, initial_dirty_percentage=0.2, max_steps=1000, max_execution_time=2.0):
        super().__init__()
        self.schedule = BaseScheduler(self)

        self.density = density
        self.initial_dirty_percentage = initial_dirty_percentage
        self.max_steps = max_steps
        self.current_step = 0
        
        self.max_execution_time = max_execution_time * 60.0  # Convertir minutos a segundos
        self.start_time = time.time()  # Guardar el tiempo de inicio de la simulación

        self.board_size_big = board_size_big
        self.update_grid_size()
        
        middle_x_coord = self.grid.width // 2
        middle_y_coord = self.grid.height // 2
        middle_coords_list = [(middle_x_coord, middle_y_coord)]
        
        for _, (x, y) in self.grid.coord_iter():
            if self.random.random() < density and (x, y) not in middle_coords_list:
                garbages = Garbage(self, (x, y))
                self.grid.place_agent(garbages, (x, y))
                self.schedule.add(garbages)

        Bot.cleaner_bots_list = []        
        
        bot_1 = Bot(self, (0, 0))
        bot_2 = Bot(self, (0, self.grid.width - 1))
        bot_3 = Bot(self, (self.grid.height - 1, 0))
        bot_4 = Bot(self, (self.grid.height - 1, self.grid.width - 1))
        bot_5 = Bot(self, None)
        
        Bot.displayListOfCleaners()
        for bot in Bot.cleaner_bots_list:
            x = self.random.randint(0, self.grid.width - 1)
            y = self.random.randint(0, self.grid.height - 1)
            self.grid.place_agent(bot, (x, y))
            self.schedule.add(bot)
            
        _incinerator = Incinerator(self, (middle_x_coord, middle_y_coord))
        self.grid.place_agent(_incinerator, _incinerator.pos)
        self.schedule.add(_incinerator)

    def update_grid_size(self):
        if self.board_size_big:
            self.grid = MultiGrid(51, 51, torus=False)
        else:
            self.grid = MultiGrid(21, 21, torus=False)

   
    def step(self):
        if self.current_step >= self.max_steps - 1:
            return  # Detener la simulación si se alcanzó el número máximo de pasos

        elapsed_time = time.time() - self.start_time
        if elapsed_time >= self.max_execution_time:
            return  # Detener la simulación si se ha alcanzado el tiempo de ejecución máximo

        self.schedule.step()
        self.current_step += 1  # Incrementa el contador de pasos en cada iteración

def agent_portrayal(agent):
    if isinstance(agent, Bot):
        return {"Shape": "bot.png", "Layer": 0}
    elif isinstance(agent, Garbage):
        return {"Shape": "circle", "Filled": "true", "r": 1, "Color": "black", "Layer": 0}
    elif isinstance(agent, Incinerator):
        if agent.condition == Incinerator.NOT_BURNING:
            return {"Shape": "basurero.png", "Layer": 0}
        elif agent.condition == Incinerator.BURNING:
            if time.time() - agent.burning_time <= agent.burning_duration:
                return {"Shape": "circle", "Filled": "true", "r": 1, "Color": "red", "Layer": 0}
            else:
                return {"Shape": "basurero.png", "Layer": 0}

def get_grid_size(board_size_big):
    if board_size_big:
        return 51, 51
    else:
        return 21, 21

def update_grid_size(change):
    global grid
    board_size_big = change["new"]
    height, width = get_grid_size(board_size_big)
    grid = CanvasGrid(agent_portrayal, height, width, 500, 500)

    

    server.quit()
    server.launch()

# Create the CanvasGrid based on the initial checkbox state
initial_board_size_big = True
initial_height, initial_width = get_grid_size(initial_board_size_big)
grid = CanvasGrid(agent_portrayal, initial_height, initial_width, 500, 500)

if __name__ == "__main__":
    density = 0.2
    board_size_big = True
    max_steps = "max_steps"
    max_execution_time = 2.0  # Valor inicial del tiempo de ejecución en minutos

    server = ModularServer(Maze, [grid], "Cleaning Simulation", {
        "density": Slider("Garbage Density", 0.2, 0.01, 1.0, 0.01),
        "board_size_big": Checkbox("Use Big Grid (51x51)", board_size_big),
        "max_steps": Slider("Max Steps", 1000, 1, 1000, 1),
        "max_execution_time": Slider("Max Execution Time (min)", max_execution_time, 0.1, 5.0, 0.1)  # Agregar un slider para el tiempo de ejecución

    })

    server.port = 8517
    server.launch()
