from mesa import Model, Agent
from mesa.space import SingleGrid
from mesa.visualization import TextVisualization

class ConwayAgent(Agent):
    """
    Conway automata
    """

    def __init__(self, pos, model, status):
        """
        Create a new automata.

        Args:
            pos: where the agent is
           status: Indicator for the agent's type (alive=1, dead=0)
        """
        super().__init__(pos, model) # allows base class to work with pos + model
        self.pos = pos
        self.status = status


    def step(self):
        living_neighbors = 0
        for neighbor in self.model.grid.iter_neighbors(self.pos, True):
            if neighbor.status == 1:
                living_neighbors += 1


        # determine neighborhood crowding; die or come alive!
        if self.status == 0 and living_neighbors == 3:
            self.status = 1 #brought to life by living neighbors!

        elif self.status == 1:  # you're alive
            if living_neighbors < 2: 
                self.status = 0 #underpopulated
            elif living_neighbors > 3:
                self.status = 0 #overpopulated
            else:
                self.status = 1 #juuuust right


