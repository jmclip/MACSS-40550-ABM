import mesa

from .model import BoidFlockers
from .SimpleContinuousModule import SimpleCanvas
from mesa.visualization import UserParam


color_list = ["wheat", "navajowhite", "blanchedalmond", "gold", "lemonchiffon", "khaki", 
            "palegoldenrod", "darkkhaki", "yellow", "cornsilk", "goldenrod", "bisque",
            "darkgoldenrod"]


def boid_draw(agent):
    return {"Shape": "circle", "r": 0.5, "Filled": "true", 
            "Layer": 0, "Color": color_list[agent.unique_id % 13]}



boid_canvas = SimpleCanvas(boid_draw, 500, 500)

canvas_element = mesa.visualization.CanvasGrid(
    boid_draw,
    grid_width=20,
    grid_height=20,
    canvas_width=500,
    canvas_height=500,
)
model_params = {
    "width": 200,
    "height": 200,
    "speed": 1,

}

server = mesa.visualization.ModularServer(
    BoidFlockers, [canvas_element], "Boids", model_params
)
