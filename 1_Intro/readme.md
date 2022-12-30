# Conway's game of life

## Summary
This model follows a simple series of rules and demonstrates how, using a few simple rules, cells can live or die. This particular version of the model starts with agents on the upper left of the grid and then allows the 'Rules of Life' (below) to play out. 

### Rules
**For a space that is populated:**
1) Each cell with one or no neighbors dies, as if by solitude.

2) Each cell with four or more neighbors dies, as if by overpopulation.


3) Each cell with two or three neighbors survives.


**For a space that is empty or unpopulated:**
1) Each cell with three neighbors becomes populated.

## How to run
1) To install dependencies, use pip and the requirements.txt file in this directory 
 
```
    pip install -r requirements.txt
```
2) To run the model interactively, run ``python conway/run.py`` in this directory. e.g.

```
     python conway/run.py
```

Then open your browser to [http://127.0.0.1:8513/](http://127.0.0.1:8513/) and press Reset, then Start. (if you would like, you can change the number of agents, just click 'reset' after you change the number to set up the model.)



## Files
**agents.py** sets up agents (cellular automata) for the game, including the rules of living / dying

**model.py** sets up the model itself and calls on agents in each time step

**server.py** sets up visualization of agents

**run.py** launches and runs the model

## Other resources
* https://playgameoflife.com/info 
* https://ccl.northwestern.edu/netlogo/models/Life