import pandas as pd


# Load the training data
train_df = pd.read_csv("train.csv")

# Define mappings for categorical variables
planet_mapping = {"Earth": 1, "Europa": 2, "Mars": 3} #il faudra peut êrte changer les valeurs car à priori on ne sait pas si Earth est plus proche que Mars Europa ou Mars on un odre d'importance
cryo_sleep_mapping = {False: 0, True: 1}
destination_mapping = {"TRAPPIST-1e": 1, "55 Cancri e": 2, "PSO J318.5-22": 3} #idem
vip_mapping = {False: 0, True: 1}
transported_mapping = {False: 0, True: 1}

# Modify data according to mappings
train_df["HomePlanet"] = train_df["HomePlanet"].map(planet_mapping)
train_df["CryoSleep"] = train_df["CryoSleep"].map(cryo_sleep_mapping)
train_df["Destination"] = train_df["Destination"].map(destination_mapping)
train_df["VIP"] = train_df["VIP"].map(vip_mapping)
train_df["Transported"] = train_df["Transported"].map(transported_mapping)

# Print modified DataFrame
print(train_df.head())

# Save the modified DataFrame to a new CSV file
train_df.to_csv("modified_train.csv", index=False)
