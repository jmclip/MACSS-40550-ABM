import mesa

# new method for analyzing similarity of neighbors
# note this is one of multiple options you might try
def calc_similarity(model):
    neighbor_sim = [agent.similar for agent in model.schedule.agents]
    N = model.density*model.width*model.height
    return sum(neighbor_sim) / (N)

class SchellingAgent(mesa.Agent):
    """
    Schelling segregation agent
    """

    def __init__(self, unique_id, model, agent_type, similar):
        """
        Create a new Schelling agent.

        Args:
           unique_id: Unique identifier for the agent.
           x, y: Agent initial location.
           agent_type: Indicator for the agent's type (minority=1, majority=0)
        """
        super().__init__(unique_id, model)
        self.type = agent_type
        self.similar = similar
        
    def step(self):
        self.similar = 0 #reset to zero each step
        for neighbor in self.model.grid.iter_neighbors(
            self.pos, moore=True, radius=self.model.radius
        ):
            if neighbor.type == self.type:
                self.similar += 1

        # If unhappy, move:
        if self.similar < self.model.homophily:
            self.model.grid.move_to_empty(self)
        else:
            self.model.happy += 1
    


class Schelling(mesa.Model):
    """
    Model class for the Schelling segregation model.
    """

    def __init__(
        self,
        height=20,
        width=20,
        homophily=3,
        radius=1,
        density=0.8,
        minority_pc=0.2,
        seed=None,
    ):
        """
        Create a new Schelling model.

        Args:
            width, height: Size of the space.
            density: Initial Chance for a cell to populated
            minority_pc: Chances for an agent to be in minority class
            homophily: Minimum number of agents of same class needed to be happy
            radius: Search radius for checking similarity
            seed: Seed for Reproducibility
        """

        super().__init__(seed=seed)
        self.height = height
        self.width = width
        self.density = density
        self.minority_pc = minority_pc
        self.homophily = homophily
        self.radius = radius

        self.schedule = mesa.time.RandomActivation(self)
        self.grid = mesa.space.SingleGrid(width, height, torus=True)

        self.datacollector = mesa.DataCollector(
            model_reporters={"happy": "happy", "Avg Similarity": "similarity"},  # Model-level count of happy agents
            agent_reporters={"Number of Similar Neighbors": "similar", 
            "Agent type": "type"}
        )

        # Set up agents
        # We use a grid iterator that returns
        # the coordinates of a cell as well as
        # its contents. (coord_iter)
        for _, pos in self.grid.coord_iter():
            if self.random.random() < self.density:
                agent_type = 1 if self.random.random() < self.minority_pc else 0
                agent = SchellingAgent(self.next_id(), self, agent_type, 0) 
                self.grid.place_agent(agent, pos)
                self.schedule.add(agent)
        self.happy = 0
        self.similarity = 0
        self.datacollector.collect(self)
        


    def step(self):
        """
        Run one step of the model.
        """
        self.happy = 0  # Reset counter of happy agents
        self.schedule.step()
        self.similarity = round(calc_similarity(self),2)
        #print(calc_similarity(self)) # in case you want to get a sense of this (hint: how else to track)
        self.datacollector.collect(self)

        if self.happy == self.schedule.get_agent_count():
            self.running = False
