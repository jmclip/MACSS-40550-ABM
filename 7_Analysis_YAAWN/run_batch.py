from wolf_sheep.model import WolfSheep
from mesa.batchrunner import FixedBatchRunner
from mesa import DataCollector

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
        "wolf_gain_from_food": [*range(18,28,2)]
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
                            model_reporters={"Wolves": lambda m: m.schedule.get_type_count("Wolf"),
                            "Sheep": lambda m: m.schedule.get_type_count("Sheep")}, 
                                max_steps=1)

# run the batches of your model with the specified variations
batch_run.run_all()


## NOTE: to do data collection, you need to be sure your pathway is correct to save this!
# Data collection
# extract data as a pandas Data Frame
batch_df = batch_run.get_model_vars_dataframe()
#batch_df_a = batch_run.get_agent_vars_dataframe()

# export the data to a csv file for graphing/analysis
batch_df.to_csv("./data/seg_model_batch_run_data.csv")
#batch_df_a.to_csv(".data/seg_agent_batch_run_data.csv")