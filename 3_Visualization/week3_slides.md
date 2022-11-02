---
marp: true
theme: 
paginate: true


---
# Agent-Based Modeling: Week 3
## Winter 2023
Jean Clipperton


---
# Agenda: 
* ODD + D framework 
* Visualization:
  * Server file
  * Elements
* 

---
# Grimm and Volker: ODD + D

* Puzzle / question 
* Theory / reasoning
* Framework
* Do I buy it / so what?

---
# GV: ODD + D Framework

|    **Overview**     | Purpose                         |
| :-----------------: | :------------------------------ |
|                     | State variables and scales      |
|                     | Process overview and scheduling |
| **Design Concepts** | Design concepts                 |
|     **Details**     | Implementation details          |
|                     | Initialization                  |
|                     | Input                           |
|                     | Submodels                       |

---
# GV: ODD + D Overview

* **Purpose** Who is the model for? (e.g. scientists, students / teachers, stakeholders, decision makers?)
* **Entities, state variables, and scales**: What kinds of entties are in the model, what state variables an dparameters do they have? 
* **Process overview and scheduling** Describe scheduling, names for the processes, how the update process works. 

---

# GV: Design Concepts
Here, give an overview of all the pieces that come together to create the model. For example, you will want to discuss What the agents are, how they interact with their environments, any learning they are able to (particularly w/r/t their environment), and what random processes exist within the model. 

---

# GV: Details
This is where you provide the technical details of the model. Think of it as the actual recipe: **can someone read this component and recreate the model themselves?** *If the answer is no, you need to provide addtional detail*

---
# Visualization: How do you want to represent your model?

We had some experience with this last week and we're going to think about it a bit more formally now. 

**Focus on how you want the user to interact with your model** *Later, we'll talk about exporting data but that will also factor in*

---
# Plan ahead!
Think about what you are hoping to use the model for, what you want to communicate, and what pieces you'll need. 

## LIFE IS EASIER WHEN YOU HAVE A PLAN

---
# One last consideration: Batch and Single runs

In our class, we've so far been doing what's called a *'single run'* vs a *'batch run'*. We'll dive into this more, but essentially a single run is just what it sounds like -- one run of the model. 

<br>

When we move to exporting data and doing different sorts of analyses on the model, we'll transition to batch runs. In the batch run scenario, the visualizations will play a small role but **the parameters you allow the user to set will still factor prominently.**

---
# Server file

Relevant elements:
* Header: what we import
* Agent portrayal
* Any reporting elements to display
* Canvas / grid
* Elements in the vizualization

---
# Server
As you know, there are different ways to import this

```
from mesa.visualization.modules import CanvasGrid
from mesa.visualization.ModularVisualization import ModularServer
from mesa.visualization.modules import ChartModule, TextElement
from mesa.visualization.UserParam import UserSettableParameter

from model import SegModel
```

---

# Elements of design

* Grid: how the elements appear
* User-inputs: parameter values the user can set
* Reporting elements: displayed statistics
* Graphics: in-the-moment graphs

We'll take these each in turn, but consider these factors when you're setting up your model. 

---
# Documentation
For mor information and detail, you can find Mesa's documentaion on this here: 
[Mesa Documentation](https://mesa.readthedocs.io/en/main/mesa.visualization.html)
<br>

Note that it's not always the most user friendly in how it's described or displayed. 

---
# Grid
The grid is how the actual model appears. 

---
# User inputs

---
# Reporting

---
# Graphics

---
# How nice should it be?



