from mesa import Model
from mesa.time import RandomActivation
from mesa.space import ContinuousSpace
from mesa.datacollection import DataCollector
import random 

from agents import FlockAgent


class FlockModel(Model):
    #height = 50
    #width = height


        # adding agents to the world
    def __init__(self, width, height, population, vision, minimum_separation, 
                  align_turn, cohere_turn, separate_turn):
        self.population = population
        self.vision = vision
        self.minimum_separation = minimum_separation
        self.align_turn = align_turn
        self.cohere_turn = cohere_turn
        self.separate_turn = separate_turn
        self.width = width
        self.height = height
        self.space = ContinuousSpace(width, height, torus=True)
        self.schedule = RandomActivation(self)

        # placing agents at random in the world

        for i in range(population):
            posi = random.uniform(0,self.height-1), random.uniform(0,self.height-1)
            agent = FlockAgent(posi, self)
            self.space.place_agent(agent, agent.pos)
            self.schedule.add(agent)


        self.running = True  # need this for batchrunner

        self.datacollector = DataCollector()


    def step(self):
        self.schedule.step()
        self.datacollector.collect(self)