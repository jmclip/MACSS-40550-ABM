from mesa.visualization.modules import CanvasGrid
from mesa.visualization.ModularVisualization import ModularServer
from mesa.visualization.modules import ChartModule, TextElement
from mesa.visualization.UserParam import UserSettableParameter

from model import ConwayModel



# define and set up agent visualization
def conway_draw(agent):
    if agent is None:
        return
    portrayal = {"Shape": "rect", "Filled": "true", "w": 0.8, "h": 0.8, "Layer": 0}

    if agent.status == 0:
        portrayal["Color"] = "gray"

    else:
        portrayal["Color"] = "yellow"

    return portrayal


# set up how and what we're calling for the gui
canvas_element = CanvasGrid(conway_draw, 10, 10, 500, 500)

# set up how the visualization will look
model_params = {
    "height": 10,
    "width": 10,
    "num_alive": UserSettableParameter('slider', "Number Agents", 18, 0, 100, 2),
}

# this is where we call the different elements we're going to be visualizing
# it includes the model, the graph/grid/world, and our various charts
# it also features a name for the model and our relevant parameter values
server = ModularServer(
    ConwayModel,
    [canvas_element  ],
    "Conways's Game of Life",
    model_params
)
