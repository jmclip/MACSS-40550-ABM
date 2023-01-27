from wolf_sheep.model import WolfSheep
from mesa.batchrunner import FixedBatchRunner

# parameters that will remain constant
fixed_parameters = {
    "height": 20,
    "width": 20,
    "initial_sheep": 100,
    "initial_wolves": 50,
    "sheep_reproduce": 0.04,
    "wolf_reproduce": 0.05,
    "wolf_gain_from_food": 20,
    "grass": False,
}

# parameters you want to vary
# can also include combinations here
parameters_list = [{"grass_regrowth_time": 30, "sheep_gain_from_food": 2},
                    {"grass_regrowth_time": 30, "sheep_gain_from_food": 3}, 
                    {"grass_regrowth_time": 30, "sheep_gain_from_food": 4},
                    {"grass_regrowth_time": 30, "sheep_gain_from_food": 5},                    
                   {"grass_regrowth_time": 35, "sheep_gain_from_food": 2},
                    {"grass_regrowth_time": 35, "sheep_gain_from_food": 3},
                    {"grass_regrowth_time": 35, "sheep_gain_from_food": 4},
                    {"grass_regrowth_time": 35, "sheep_gain_from_food": 5},
                     ]

# what to run and what to collect
# iterations is how many runs per parameter value
# max_steps is how long to run the model
batch_run = FixedBatchRunner(WolfSheep, parameters_list, 
                            fixed_parameters, iterations=10,
                            model_reporters={
                                "Wolves": lambda m: m.schedule.get_type_count("Wolf"),
                                "Sheep": lambda m: m.schedule.get_type_count("Sheep")}, 
                                max_steps=100)

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