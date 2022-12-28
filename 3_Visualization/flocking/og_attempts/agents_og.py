from mesa import Agent
from mesa import Model
from mesa.time import RandomActivation
from mesa.space import MultiGrid, ContinuousSpace
from mesa.datacollection import DataCollector

# set up and initialize the agents
class FlockAgent(Agent):
     def __init__(self, pos, model):  # agents and their characteristics
        super().__init__(pos, model)
        self.pos = pos

    
        def step(self):
            """
            The birds follow three rules: "alignment", "separation", and "cohesion".
            "Alignment" means that a bird tends to turn so that it is moving in the same direction that nearby birds are moving.
            "Separation" means that a bird will turn to avoid another bird which gets too close.
            "Cohesion" means that a bird will move towards other nearby birds (unless another bird is too close).
            When two birds are too close, the "separation" rule overrides the other two, which are deactivated until the minimum separation is achieved.
            The three rules affect only the bird's heading. Each bird always moves forward at the same constant speed."""
            pass
            print("HI")
        def move(self):
            pass