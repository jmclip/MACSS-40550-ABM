from wolf_sheep.model import WolfSheep
from mesa.batchrunner import FixedBatchRunner

import json 
import pandas as pd
from itertools import product

# parameters that will remain constant
fixed_parameters = {
    "height": 20,
    "width": 20,
    "initial_sheep": 100,
    "initial_wolves": 50,
    "sheep_reproduce": 0.04,
    "wolf_reproduce": 0.05,
    "grass": True,
}

# parameters you want to vary
# can also include combinations here
params = {"grass_regrowth_time": [*range(25,37,5)], 
        "sheep_gain_from_food": [*range(2,6,1)],
        "wolf_gain_from_food": [*range(18,27,2)]
        }

# combine all the parameters you want to combine using this function
def dict_product(dicts): #could just use the below but it's cleaner this way
    """
    >>> list(dict_product(dict(number=[1,2], character='ab')))
    [{'character': 'a', 'number': 1},
     {'character': 'a', 'number': 2},
     {'character': 'b', 'number': 1},
     {'character': 'b', 'number': 2}]
    """
    return (dict(zip(dicts, x)) for x in product(*dicts.values()))

parameters_list = [*dict_product(params)]

# what to run and what to collect
# iterations is how many runs per parameter value
# max_steps is how long to run the model
batch_run = FixedBatchRunner(WolfSheep, parameters_list, 
                            fixed_parameters, iterations=10,
                            model_reporters={
                                "Wolves": lambda m: m.wolves,
                                "Sheep": lambda m: m.sheep,
                                "Grass Growth": lambda m: m.grass_growth,
                            }, 
                                max_steps=50)

# run the batches of your model with the specified variations
batch_run.run_all()

############################
# get the data and export it!
#gather our data (dumps into dictionary)
batch_dict_steps = batch_run.get_collector_model()

# IMPORTANT: Think about how you want to use your data
# We're pulling the items into a dataframe and giving things 'nice' names
batch_dict_steps2 = pd.DataFrame([(key,key1,list(val1)) for key,val in batch_dict_steps.items() for key1,val1 in val.items()])

# get out the parameter values
params = pd.DataFrame(batch_dict_steps2[0].to_list()).rename(columns = {0:"Grass Regrowth", 1:"Sheep Gain", 2:"Wolf Gain", 3: "Run Num"})

# get the animal values
animals = pd.DataFrame(batch_dict_steps2[1].to_list()).rename(columns = {0:"Animal"})

#split the values from each step into a column:
steps = pd.DataFrame(batch_dict_steps2[2].to_list())

#bring the datasets together
batch_dict_steps2 = pd.concat([params, animals, steps], axis = 1)

#dump into a csv
batch_dict_steps2.to_csv("./data/seg_model_steps_batch_run_data.csv", index=False)

## NOTE you could do it this way if you wanted to go down
#batch_dict_steps2.explode(list([*range(0,len(batch_dict_steps2.columns))])).to_csv("batch_dict_steps_data.csv")


##############################
# Data collection: overall values
## NOTE: to do data collection, you need to be sure your pathway is correct to save this!

# extract data as a pandas Data Frame
batch_df = batch_run.get_model_vars_dataframe()
#batch_df_a = batch_run.get_agent_vars_dataframe()

# export the data to a csv file for graphing/analysis
batch_df.to_csv("./data/seg_model_batch_run_data.csv", index=False) 
#batch_df_a.to_csv(".data/seg_agent_batch_run_data.csv")