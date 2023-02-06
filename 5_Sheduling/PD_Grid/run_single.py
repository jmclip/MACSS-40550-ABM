from pd_grid.model import PdGrid

# Set your parameter values for one run
# Reminder that the model takes on these parameter values:
# width, height, num_agents, minority_pc, intolerance
payoffs = {("C", "C"): 1, ("C", "D"): 0, ("D", "C"): 2, ("D", "D"): 0}

model = PdGrid(width=50, height=50, schedule_type="Random", payoffs=None, seed=None)
for t in range(3):
    model.step()
    print(model._seed)

# extract data as a pandas Data Frame
model_df = model.datacollector.get_model_vars_dataframe()

# export the data to a csv file for graphing/analysis
model_df.to_csv("data/PDgrid_model_single_run_data.csv")
