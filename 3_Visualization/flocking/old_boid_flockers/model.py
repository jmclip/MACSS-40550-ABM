"""
Flockers
=============================================================
A Mesa implementation of Craig Reynolds's Boids flocker model.
Uses numpy arrays to represent vectors.
"""

import mesa
import numpy as np

from .boid import Boid


class BoidFlockers(mesa.Model):
    """
    Flocker model class. Handles agent creation, placement and scheduling.
    """
    jiggle = False
    use_seed_10 = True

    def __init__(
        self,
        population=100,
        width=500,
        height=500,
        speed=1,
        vision=10,
        separation=2,
        cohere=0.025,
        separate=0.25,
        match=0.04,
        jiggle = jiggle,
        use_seed_10 = use_seed_10
        ):

        """
        Create a new Flockers model.
        Args:
            population: Number of Boids
            width, height: Size of the space.
            speed: How fast should the Boids move.
            vision: How far around should each Boid look for its neighbors
            separation: What's the minimum distance each Boid will attempt to
                    keep from any other
            cohere, separate, match: factors for the relative importance of
                    the three drives."""
        super().__init__()
        self.population = population
        self.vision = vision
        self.speed = speed
        self.separation = separation
        self.jiggle = jiggle
        self.use_seed_10 = use_seed_10
        if self.use_seed_10: 
            mesa.Model.reset_randomizer(self, seed=10), #allows us to all run similar simulations
        self.schedule = mesa.time.RandomActivation(self)
        #self.space = mesa.space.ContinuousSpace(width, height, True)
        self.grid = mesa.space.MultiGrid(20, 20, True)
        self.factors = dict(cohere=cohere, separate=separate, match=match)
        self.make_agents()
        self.running = True

    

    def make_agents(self):
        """
        Create self.population agents, with random positions and starting headings.
        """
        for _, pos in self.grid.coord_iter(): #i in range(self.population):
            if self.random.randint(0,400) < self.population:
                velocity = np.random.random(2) * 2 - 1
                boid = Boid(
                    self.next_id(),
                    self,
                    pos,
                    self.speed,
                    velocity,
                    self.vision,
                    self.separation, 
                    **self.factors
                )

                self.grid.place_agent(boid, pos)  #self.space.place_agent(boid, pos)
            
                self.schedule.add(boid)

    def step(self):
        self.schedule.step()