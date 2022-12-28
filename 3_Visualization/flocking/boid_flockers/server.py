import mesa

from .model import BoidFlockers
from .SimpleContinuousModule import SimpleCanvas
import random
from mesa.visualization.UserParam import UserSettableParameter


color_list = ["wheat", "navajowhite", "blanchedalmond", "gold", "lemonchiffon", "khaki", 
            "palegoldenrod", "darkkhaki", "yellow", "cornsilk", "goldenrod", "bisque",
            "darkgoldenrod"]


def boid_draw(agent):
    return  {"Shape": "rect", "h": 0.02, "w":0.022, "Filled": "true", 
            "Layer": 0, "Color": color_list[agent.unique_id % 13]}


boid_canvas = SimpleCanvas(boid_draw, 500, 500)
model_params = {
    "population": UserSettableParameter('slider', "Population Size",
                                      int(0.01 * 100 ** 2), 0, 0.1*100 ** 2, 10), 
    "width": 200,
    "height": 200,
    "speed": 1,
    "vision": UserSettableParameter('slider', "Vision", 10, 0, 25, 1),
    "separation": UserSettableParameter('slider', "Separation", 1.2, 0, 2, 0.05),
    "cohere": UserSettableParameter('slider', "Cohesion", 0.8, 0, 4, 0.1),
    "jiggle": UserSettableParameter('checkbox', "Jiggle Points", True ),
}

server = mesa.visualization.ModularServer(
    BoidFlockers, [boid_canvas], "Boids", model_params
)