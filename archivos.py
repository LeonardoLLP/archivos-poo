import pandas as pd

filepath = "calificaciones.csv"
data = pd.read_csv(filepath, sep=";")

print(data.head())

def alumni_info(data: pd.DataFrame):
    my_list = []
    for index in range(len(data.index)):
        keys = data.iloc[index, :2].tolist()
        values = data.iloc[index, 2:].tolist()
        my_dict = {"{}, {}".format(keys[0], keys[1]): values}
        my_list.append(my_dict)
    return my_list