from pd_grid.model import PdGrid 
from mesa.batchrunner import FixedBatchRunner
import json 
from itertools import product

# parameters that will remain constant
fixed_parameters = {
    "width": 50, 
    "height": 50,
    "payoffs": {("C", "C"): 1, ("C", "D"): 0, ("D", "C"): 2, ("D", "D"): 0}
}

# parameters you want to vary
# can also include combinations here
params = {"schedule_type": ["Random", "Sequential", "Simultaneous"]}

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
batch_run = FixedBatchRunner(PdGrid, parameters_list,
                             fixed_parameters, iterations=10,
                             model_reporters={
                                "Cooperating_Agents": lambda m: len(
                                    [a for a in m.schedule.agents if a.move == "C"]),
                                "Simulation Seed": lambda m: m.return_seed(m)},
                             max_steps=2)

# run the batches of your model with the specified variations
batch_run.run_all()

batch_dict = batch_run.get_collector_model()
batch_dict_save = {f'{key[0]}_{key[1]}':list(value['Cooperating_Agents']) for key,value in batch_dict.items()}
json.dump(batch_dict_save, open(".\\data\\batch_list.json", 'w'), indent = 4)

## NOTE: to do data collection, you need to be sure your pathway is correct to save this!
# Data collection
# extract data as a pandas Data Frame
batch_df = batch_run.get_model_vars_dataframe()
#batch_df_a = batch_run.get_agent_vars_dataframe()

# export the data to a csv file for graphing/analysis
batch_df.to_csv("data/PDgrid_model_batch_run_data.csv")
#batch_df_a.to_csv("data/PDgrid_model_agent_batch_run_data.csv")