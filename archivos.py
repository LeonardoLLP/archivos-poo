import pandas as pd

filepath = "calificaciones.csv"
data = pd.read_csv(filepath, sep=";")

print(data.head())

def alumni_info(data: pd.DataFrame):
    my_list = []
    for index in range(len(data.index)):
        values = data.iloc[index]
        my_dict = dict(zip(data.columns, values))
        my_list.append(my_dict)

    # my_list.sort()

    return my_list

ups = alumni_info(data)
for i in ups:
    print(i)