from mesa.visualization.modules import CanvasGrid
from mesa.visualization.ModularVisualization import ModularServer
from mesa.visualization.modules import ChartModule, TextElement
from mesa.visualization.UserParam import UserSettableParameter

from model import SegModel


# these next portions allow for the values
# to appear in the gui for the model
class HappyElement(TextElement):

    def render(self, model):
        return "% Happy agents: " + str(round(
            (model.happy / model.num_agents) * 100, 1)) + "%"


class SimilarElement(TextElement):

    def render(self, model):
        return "Avg. % similar neighbors: " + str(model.pct_neighbors) + "%"


class SimilarElement_g(TextElement):

    def render(self, model):
        return "Groups avg. % similar neighbors: (A) " + str(model.pct_neighbors0) + "%" + " (B) " + str(
            model.pct_neighbors1) + "%"


# define and set up agent visualization
def schelling_draw(agent):
    if agent is None:
        return
    portrayal = {"Shape": "circle", "r": 0.8, "Filled": "true", "Layer": 0}

    if agent.type == 0:
        portrayal["Color"] = "Maroon"

    else:
        portrayal["Color"] = "mediumpurple"

    return portrayal


# set up how and what we're calling for the gui
happy_element = HappyElement()
similar_element = SimilarElement()
similar_element_g = SimilarElement_g()
canvas_element = CanvasGrid(schelling_draw, 20, 20, 500, 500)
happy_chart = ChartModule([{"Label": "Pct Happy", "Color": "Black"}])
happy_chart0 = ChartModule([{"Label": "Pct Happy Group A", "Color": "Maroon"}])
happy_chart1 = ChartModule([{"Label": "Pct Happy Group B", "Color": "mediumpurple"}])

# set up how the visualization will look
model_params = {
    "height": 20,
    "width": 20,
    "width": 20,
    "num_agents": UserSettableParameter('slider', "Number Agents", 350, 10, 400, 10),
    "minority_pc": UserSettableParameter('slider', "% group B", 0.35, 0.00, 1.0, 0.05),
    "intolerance": UserSettableParameter('slider', "Intolerance: (Desired % of matching neighbors) ",
                                          0.375, 0, 1, 0.125),
}

# this is where we call the different elements we're going to be visualizing
# it includes the model, the graph/grid/world, and our various charts
# it also features a name for the model and our relevant parameter values
server = ModularServer(
    SegModel,
    [canvas_element, happy_element,
     similar_element, similar_element_g,
     happy_chart, ],
    "Schelling's Segregation Model",
    model_params
)
