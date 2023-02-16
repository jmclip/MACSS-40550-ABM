import mesa
import random 

from .agent import PDAgent


class PdGrid(mesa.Model):
    """Model class for iterated, spatial prisoner's dilemma model."""
    
    schedule_types = {
        "Sequential": mesa.time.BaseScheduler,
        "Random": mesa.time.RandomActivation,
        "Simultaneous": mesa.time.SimultaneousActivation,
    }

    # This dictionary holds the payoff for this agent,
    # keyed on: (my_move, other_move)

    payoff = {("C", "C"): 1, ("C", "D"): 0, ("D", "C"): 2, ("D", "D"): 0}

    def __init__(
        self, 
        width=50, 
        height=50, schedule_type="Random", payoffs=None, 
        seed=None, # can incorporate any # seed you want here or leave at None for random 
        ):  
        super().__init__()
        self.reset_randomizer(seed)
        print(f"Running with seed {self._seed}")

        """
        Create a new Spatial Prisoners' Dilemma Model.

        Args:
            width, height: Grid size. There will be one agent per grid cell.
            schedule_type: Can be "Sequential", "Random", or "Simultaneous".
                           Determines the agent activation regime.
            payoffs: (optional) Dictionary of (move, neighbor_move) payoffs.
        """

        self.grid = mesa.space.SingleGrid(width, height, torus=True)
        self.schedule_type = schedule_type
        self.schedule = self.schedule_types[self.schedule_type](self)
        
        

        # Create agents
        for x in range(width):
            for y in range(height):
                agent = PDAgent((x, y), self)
                self.grid.place_agent(agent, (x, y))
                self.schedule.add(agent)

        self.datacollector = mesa.DataCollector( model_reporters=
            {
                "Cooperating_Agents": lambda m: len(
                    [a for a in m.schedule.agents if a.move == "C"]
                ),
                "Simulation Seed": self.return_seed,
            }
        )
                

        self.running = True
        self.datacollector.collect(self)

    def step(self):
        self.schedule.step()
        # collect data
        self.datacollector.collect(self)

    def run(self, n):
        """Run the model for n steps."""
        for _ in range(n):
            self.step()

    @staticmethod
    def return_seed(model): #borrowed from J. Helbing...working on connecting to Mesa documentation
        return model._seed