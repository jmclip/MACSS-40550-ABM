from model import SegModel
from mesa.batchrunner import FixedBatchRunner

# parameters that will remain constant
fixed_parameters = {
    "height": 20,
    "width": 20,
    "num_agents": 350,
    "minority_pc": 0.4,
}

# parameters you want to vary
# can also include combinations here
parameters_list = [{"intolerance": 0.125},
                   {"intolerance": 0.25},
                   {"intolerance": 0.375},
                   {"intolerance": 0.5},
                   {"intolerance": 0.625},
                   {"intolerance": 0.75}]

# what to run and what to collect
# iterations is how many runs per parameter value
# max_steps is how long to run the model
batch_run = FixedBatchRunner(SegModel, parameters_list,
                             fixed_parameters, iterations=10,
                             model_reporters={"Pct Happy": lambda m: round(100 * m.happy / m.num_agents, 1),
                                              "Pct Happy Group A": lambda m: round(100 * m.happy0 / m.num_agents0, 1),
                                              "Pct Happy Group B": lambda m: round(100 * m.happy1 / m.num_agents1, 1),
                                              "Avg pct similar neighbors": lambda m: m.pct_neighbors,
                                              "Avg pct similar neighbors (A)": lambda m: m.pct_neighbors0,
                                              "Avg pct similar neighbors (B)": lambda m: m.pct_neighbors1,
                                              "Avg pct similar neighbors (count empty)": lambda m: m.pct_neighbors_e,
                                              "Avg pct similar neighbors (A) (count empty)": lambda
                                                  m: m.pct_neighbors_e0,
                                              "Avg pct similar neighbors (B) (count empty)": lambda
                                                  m: m.pct_neighbors_e1,
                                              "Num Agents": lambda m: m.num_agents,
                                              "Num Agents (A)": lambda m: m.num_agents0,
                                              "Num Agents (B)": lambda m: m.num_agents1},
                             max_steps=150)

# run the batches of your model with the specified variations
batch_run.run_all()


## NOTE: to do data collection, you need to be sure your pathway is correct to save this!
# Data collection
# extract data as a pandas Data Frame
batch_df = batch_run.get_model_vars_dataframe()

# export the data to a csv file for graphing/analysis
batch_df.to_csv("data/seg_model_batch_run_data.csv")
