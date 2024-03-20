import mesa 
from mesa.visualization.modules import CanvasGrid
from mesa.visualization.ModularVisualization import ModularServer
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
    "num_alive": mesa.visualization.Slider(
         name="Number of cells", value=18, min_value=0, max_value=100, step=2
    ),
    "height": 10,
    "width": 10
    
}

# this is where we call the different elements we're going to be visualizing
# it includes the model, the graph/grid/world, and our various charts
# it also features a name for the model and our relevant parameter values
server = ModularServer(
    ConwayModel,
    [canvas_element ],
    "Conways's Game of Life!",
    model_params
)
