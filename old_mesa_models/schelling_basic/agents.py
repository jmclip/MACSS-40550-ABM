# can choose to just import mesa or to do these and streamline code a little
from mesa import Agent
from mesa.datacollection import DataCollector


# set up and initialize the agents
class SegAgent(Agent):
    def __init__(self, unique_id, agent_type, model):  # agents and their characteristics
        super().__init__(unique_id, model)
        # #self.pos = pos
        self.type = agent_type
        self.similar = 0  # agent-specific measures of neighbor similarity
        self.similar0 = 0
        self.similar1 = 0
        self.neighbors_a = 0  # count of neighbors for each agent (ignore empty squares)
        self.a_pct_similar = 0  # calculate neighbor percents

    # describe what happens in each step for the agents
    # agents check surroundings and count neighbors of the same type
    def step(self):
        self.similar = 0  # reset these counters each time step
        self.similar0 = 0
        self.similar1 = 0
        self.neighbors_a = 0
        self.a_pct_similar = 0

        for neighbor in self.model.grid.iter_neighbors(
            self.pos, moore=True, radius=self.model.radius
        ):
            self.neighbors_a +=1
            if neighbor.type == self.type:
                self.similar += 1
                if self.type == 1:
                    self.similar1 +=1  
                else: 
                    self.similar0 +=1 

        # If unhappy, move:
        if self.similar < 8*self.model.intolerance:
            self.model.grid.move_to_empty(self)
        else:
            self.model.happy += 1
            if self.type == 1:
                self.model.happy1 += 1 
            elif self.type == 0:
                self.model.happy0 += 1 



