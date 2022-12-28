import mesa

from .model import BoidFlockers
from .SimpleContinuousModule import SimpleCanvas
from mesa.visualization import UserParam


color_list = ["wheat", "navajowhite", "blanchedalmond", "gold", "lemonchiffon", "khaki", 
            "palegoldenrod", "darkkhaki", "yellow", "cornsilk", "goldenrod", "bisque",
            "darkgoldenrod"]


def boid_draw(agent):
    return  {"Shape": "rect", "h": 0.02, "w":0.022, "Filled": "true", 
            "Layer": 0, "Color": color_list[agent.unique_id % 13]}


boid_canvas = SimpleCanvas(boid_draw, 500, 500)
model_params = {
    "population": UserParam.Slider("Population Size",
                                      int(0.01 * 100 ** 2), 0, 0.1*100 ** 2, 10), 
    "width": 200,
    "height": 200,
    "speed": 1,
    "vision": UserParam.Slider("Vision", 10, 0, 25, 1),
    "separation": UserParam.Slider("Separation", 1.2, 0, 2, 0.05),
    "cohere": UserParam.Slider("Cohesion", 0.8, 0, 4, 0.1),
    "jiggle": UserParam.Checkbox("Jiggle Points", True ),
    "use_seed_10": UserParam.Checkbox("Set seed to 10?", True )
}

server = mesa.visualization.ModularServer(
    BoidFlockers, [boid_canvas], "Boids", model_params
)