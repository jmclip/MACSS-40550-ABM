from mesa.visualization.modules import CanvasGrid
from mesa.visualization.ModularVisualization import ModularServer
from mesa.visualization.modules import ChartModule, TextElement
from mesa.visualization.UserParam import UserSettableParameter
from SimpleContinuousModule import SimpleCanvas
import random
from model import FlockModel

color_list = ["gold", "lemonchiffon", "khaki", "palegoldenrod", "darkkhaki", "ivory", "beige", "lightyellow", "lightgoldenrodyellow", "yellow", "cornsilk", "goldenrod", "darkgoldenrod"]

# define and set up agent visualization
def flock_draw(agent):
    if agent is None:
        return
    portrayal = {"Shape": "rect", "Filled": "true", "w": 0.3, "h": 0.8, "Layer": 0, "Color": random.choice(color_list)}
    return {"Shape": "arrowHead", "scale": 0.9, "heading_x": 0, "heading_y": 1, "Filled": "true", "Color": random.choice(color_list)}
    
    return portrayal 



# text elements we're calling
# these next portions allow for the values
# to appear in the gui for the model

# set up how and what we're calling for the gui
# canvas itself
canvas_element = SimpleCanvas(flock_draw, FlockModel.height, FlockModel.width)


# text elements
# set up how the visualization will look
model_params = {
    "height": FlockModel.height,
    "width": FlockModel.width,
    "population": UserSettableParameter('slider', "Population Size",
                                      int(0.2 * FlockModel.height ** 2), 0, FlockModel.height ** 2, 10), 
    "vision": UserSettableParameter('slider', "Vision", 4, 0, 10, 1),
    "minimum_separation": UserSettableParameter('slider', "Minimum Separation", 5, 0, 10, 1),
    "cohere_turn": UserSettableParameter('slider', "Max Coherent Turn (degrees)", 3,  0, 20, 0.25),
    "separate_turn": UserSettableParameter('slider', "Max Separate Turn (degrees)", 4, 0, 20, 0.25),
    "align_turn": UserSettableParameter('slider', "Max Align Turn (degrees)", 3,  0, 20, 0.25)
}

# this is where we call the different elements we're going to be visualizing
# it includes the model, the graph/grid/world, and our various charts
# it also features a name for the model and our relevant parameter values
server = ModularServer(
    FlockModel, 
    [canvas_element ],
    "Flocking Model",
    model_params
)