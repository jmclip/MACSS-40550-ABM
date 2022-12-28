from mesa import Model, Agent
from mesa.time import RandomActivation
from mesa.space import SingleGrid

from agents import ConwayAgent

 
class ConwayModel(Model):
    """
    Model class for the Conway GOL model.
    """

    def __init__(self, height, width, num_alive):
        """ 
        Add agents to the grid
        """
        self.height = height
        self.width = width
        self.num_alive = num_alive
        self.schedule = RandomActivation(self)
        self.grid = SingleGrid(width, height, torus = False)
        Model.reset_randomizer(self, seed=10) #comment this out -- helps for replicability

        
        # Set up agents
        k = 0
        for i in range(height):
            for j in range (width):
                k = k + 1
                
                if k <= num_alive:
                    status = 1
                     
                else:
                    status = 0

                agent = ConwayAgent((i, j), self, status)
                #self.grid.position_agent(agent, (i, j) ) #notice what this can do!
                self.grid.place_agent(agent, (i,j))
                #print("x: ", str(i), "y: ", str(j), "  status: ", str(status), str(agent.pos))
                self.schedule.add(agent)

        

 

    def step(self):
        """
        Run one step of the model. 
        """
        self.schedule.step()



