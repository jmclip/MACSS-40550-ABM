---
marp: true
theme: 
paginate: true


---
# Agent-Based Modeling: Week 4
## Winter 2023
Jean Clipperton


---
# Agenda: 
* Review of server file
* Data Collector
* Model: Greedy cows

---
# Review: Server file

Relevant elements:
* Header: what we import
* Agent portrayal
* Any reporting elements to display
* Canvas / grid
* Elements in the vizualization
* Set up the server



---
# Data collection and reporting
This is where things will get a bit complicated. We're going to work backwards by starting with what information we WANT to display / have available, and then we'll go over how to get it. 

The short of it is that you are able to report / generate charts based on the underlying data you have already tracked / collected using the **data collector**. 

---

# Reporting
Here, we're talking about general ways to display what and how we want to do things. 

The main options you have are some combination of 
* **Charts**: thinking about tracking statistics in real-time
* **Values / text elements**: here, you might put up a counter, for example, of how many of X are alive / available, etc

---
# Reporters during the simulation

---
# Reporters: Text Element
You can generate text elements (I think of this as value reporters) to give live / immediate feedback on some value in the model. 

## When to use this? 
If you have some kind of metric or stat that you want to include. Maybe there's a measure or indext that relates to the analysis -- that would be great to include. 


---
# Reporters: Example pseudocode
To include your reporter, consider whether you want just one value, the value next to another, any text, etc. 

```[Python]
class ElementName(TextElement):
    def render(self, model):
        return (whatever you want it to return)
```

---
# Reporters: Example code
Here's a simple reporter followed by a more complicated one:

```Python
class SimilarElement(TextElement):
    def render(self, model):
        return "Avg. % similar neighbors: " + str(model.pct_neighbors) + "%"
```

```Python
class SimilarElement_g(TextElement):
    def render(self, model):
        return "Groups avg. % similar neighbors: (A) " + str(model.pct_neighbors0) + "%" 
            + " (B) " + str(model.pct_neighbors1) + "%"
```

---
# But wait, there's more!
You ALSO need to call the new element later in your server file. 

**Step 1**: you refer to your text elements
```python
similar_element = SimilarElement()
```

**Step 2**: you call these elments in setting up the server
```python
server = ModularServer(
    SegModel,
    [canvas_element, happy_element,
     similar_element, similar_element_g,
     happy_chart, ],
    "Schelling's Segregation Model",
    model_params
)
```

---
# Reporters: ChartModule
These modules are for tracking something over time -- it can be the same statistic you're choosing to report in the text element reports or something different entirely. 

## When to use this? 
This is valuable when you're trying to not only look at some value but how it changes and/or interacts with other elements. 


---
# Chartmodule Example: pseudocode

---
# Chartmodule Example: code


---
# Datacollector: getting the data you want

---
# Server file

Relevant elements:
* Header: what we import
* Agent portrayal
* Any reporting elements to display
* Canvas / grid
* Elements in the vizualization
* Set up the server


---
# How nice should it be?
This is a tough question to ask and depends on the following components:

1) Your own preferences (some people want things to be always polished)
2) The audience for the model (will the model be used by anyone other than you, for example)
3) The kind of project (is this a proof of concept approach, is this going to be how you generate findings, etc)


