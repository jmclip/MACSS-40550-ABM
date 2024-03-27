# Basic cheat sheet for Mesa

## GUI
Nest these within the `model_params = {}` portion of the server file. Be sure to call them in the server command. 

### Input options [source](https://github.com/projectmesa/mesa/issues/2085#issuecomment-2016673828)
#### Checkboxes: 
`"varname": mesa.visualization.Checkbox("display name", True)` 
* Code example: `"grass": mesa.visualization.Checkbox("Grass Enabled", True)`

#### Sliders:
`"varname": mesa.visualization.Slider("display name", defaultvalue, min, max, increment)` 
* Code example: `"dispersion_coefficient": mesa.visualization.Slider( "dispersion_coefficient", 20, 0, 100, 1 )`

#### Numeric inputs
`varname: mesa.visualization.NumberInput(varname, range)`
* Code example: `"max_coefficient": mesa.visualization.NumberInput("max_coefficient", 100)`

#### Choice inputs
`varname: mesa.visualization.Choice(displaytext, default value, choicelist)`
* Code example: `"schedule_type": mesa.visualization.Choice(
        "Scheduler type", value="Random", choices=list(PdGrid.schedule_types.keys()), )`

## Visualizing: agent portrayal
Within the agent portrayal, you can specify the size, color, shape. Notice that this is a dictionary, so you can set up different portrayals for different types of agents. 

* [Code example source](https://mesa.readthedocs.io/en/stable/overview.html#): 
```
def agent_portrayal(agent):
    portrayal = {"Shape": "circle",
                 "Filled": "true",
                 "Layer": 0,
                 "Color": "red",
                 "r": 0.5}
    return portrayal
```

### Agent Shape
 
| Shape | Elements | Details / Attributes |
| :----: | :------: | :-----|
| Circle 'circle' | “r”: The radius, defined as a fraction of cell size. | r=1 will fill the entire cell.
| | “xAlign”, “yAlign”: Alignment of the circle within the cell. | Defaults to 0.5 (center).
| Rectangle / Square 'rect' | “w”, “h”: The width and height of the rectangle | in fractions of cell width and height
| |“xAlign”, “yAlign”: Alignment of the rectangle within the cell. | Defaults to 0.5 (center).
| Arrowhead* 'arrowHead'| “scale”: Proportion scaling as a fraction of cell size. 
|           | “heading_x”: represents x direction unit vector. 
|           |    “heading_y”: represents y direction unit vector.
| Image* 'image'| has the attributes “x”, “y”, “scale”, “text” and “text_color” | image must be placed in the same directory from which the server is launched.

*Note* * denotes more advanced options

### Colors and fill
“Color”: The color to draw the shape in; needs to be a valid HTML
color, e.g.”Red” or “#AA08F8”

“Filled”: either “true” or “false”, and determines whether the shape is
filled or not.

“Layer”: Layer number of 0 or above; higher-numbered layers are drawn
above lower-numbered layers.

“text”: The text to be inscribed inside the Shape. Normally useful for
showing the unique_id of the agent.

“text_color”: The color to draw the inscribed text. Should be given in
conjunction of “text” property.

