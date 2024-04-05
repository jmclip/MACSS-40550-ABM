import mesa
import math
import numpy as np


class Boid(mesa.Agent):
    """
    A Boid-style flocker agent.

    The agent follows three behaviors to flock:
        - Cohesion: steering towards neighboring agents.
        - Separation: avoiding getting too close to any other agent.
        - Alignment: try to fly in the same direction as the neighbors.

    Boids have a vision that defines the radius in which they look for their
    neighbors to flock with. Their speed (a scalar) and velocity (a vector)
    define their movement. Separation is their desired minimum distance from
    any other Boid.
    """

    def __init__(
        self,
        unique_id,
        model,
        pos,
        speed,
        velocity,
        separation,
        vision,
        cohere=0.025,
        separate=0.05,
        match=0.04
    ):
        """
        Create a new Boid flocker agent.

        Args:
            unique_id: Unique agent identifyer.
            pos: Starting position
            speed: Distance to move per step.
            heading: numpy vector for the Boid's direction of movement.
            vision: Radius to look around for nearby Boids.
            separation: Minimum distance to maintain from other Boids.
            cohere: the relative importance of matching neighbors' positions
            separate: the relative importance of avoiding close neighbors
            match: the relative importance of matching neighbors' headings
        """
        super().__init__(unique_id, model)
        self.pos = np.array(pos)
        self.speed = speed
        self.velocity = velocity
        self.vision = vision
        self.separation = separation
        self.cohere_factor = cohere
        self.separate_factor = separate
        self.match_factor = match

    def get_distance(self, pos_1, pos_2): #adapted from continuous space
        """Get the distance between two point, accounting for toroidal space.

        Args:
            pos_1, pos_2: Coordinate tuples for both points.
        """
        x1, y1 = pos_1
        x2, y2 = pos_2

        dx = abs(x1 - x2)
        dy = abs(y1 - y2)
        
        dx = min(dx, 20 - dx)
        dy = min(dy, 20 - dy)
        return math.sqrt(dx * dx + dy * dy)

    def cohere(self, neighbors):
        """
        Return the vector toward the center of mass of the local neighbors.
        """
        cohere = np.zeros(2)
        if neighbors:
            for neighbor in neighbors:
                cohere +=  self.get_distance(self.pos, neighbor.pos)
            cohere /= len(neighbors)
        return cohere

    def separate(self, neighbors):
        """
        Return a vector away from any neighbors closer than separation dist.
        """
        me = self.pos
        them = (n.pos for n in neighbors)
        separation_vector = np.zeros(2)
        for other in them:
            if self.get_distance(me, other) < self.separation:
                separation_vector -= self.get_distance(me, other)
        return separation_vector

    def match_heading(self, neighbors):
        """
        Return a vector of the neighbors' average heading.
        """
        match_vector = np.zeros(2)
        if neighbors:
            for neighbor in neighbors:
                match_vector += neighbor.velocity
            match_vector /= len(neighbors)
        return match_vector


    def pretty_plot(self, neighbors, new_pos):
        """
        Adjust boid placement in gui to reduce overlap    
        """

        me = new_pos
        them = (n.pos for n in neighbors)
        
        for other in them:
            if self.get_distance(me, other) < self.separation:
                new_pos += [2*(2*self.random.random()-1),2*(2*self.random.random()-1)] #hard coding in 2 here but could be tied to other factors
        
            #print(f"{self.separation= }  ; distance: {get_distance(me, other)= } ")
        
        #print(f"in method: agent {self.unique_id}, method new_pos {new_pos}")
        return new_pos

    
    def step(self):
        """
        Get the Boid's neighbors, compute the new vector, and move accordingly.
        """
        
        neighbors = self.model.grid.get_neighbors(self.pos, radius = self.vision, moore = True)
        self.velocity += (
            self.cohere(neighbors) * self.cohere_factor
            + self.separate(neighbors) * self.separate_factor
            + self.match_heading(neighbors) * self.match_factor
        ) / 2
        self.velocity /= np.linalg.norm(self.velocity)

        # way to bias direction
        #new_pos = (round(self.pos[0] + 2*np.random.random()), round(self.pos[1] + 3*np.random.random()))
        # move with intention across 
        #new_pos = (self.pos[0] + 1, self.pos[1]+1)

        # not perfect, but they otherwise cohere too much and cluster in a corner
        new_pos = (self.pos + (self.velocity + np.random.uniform(-0.75, 0.75))).astype(int)

        self.model.grid.move_agent(self, tuple(new_pos))
        #self.model.grid.move_to_empty(self)



        if self.model.jiggle:
            #print(f"in step before: {self.unique_id = }, method {new_pos =}")
            new_pos = self.pretty_plot(neighbors, new_pos)
            #print(f"after {self.unique_id = }, method {new_pos = }")

            
