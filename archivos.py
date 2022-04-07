import pandas as pd
from numpy import float64 as fl

filepath = "calificaciones.csv"
data = pd.read_csv(filepath, sep=";", dtype={
    "Parcial1": fl,
    "Parcial2": fl,
    "Parcial3": fl,
})

print(data.head())

# Hemos considerado que la información que se pide es toda la que se halla en el csv, no he comprendido bien si querían que se suprimiese alguna
def alumni_info(data: pd.DataFrame) -> list:
    my_list = []
    for index in range(len(data.index)):
        values = data.iloc[index]
        my_dict = dict(zip(data.columns, values))
        my_list.append(my_dict)

    my_list.sort(key= lambda x: x["Apellidos"])

    return my_list

my_alumni_info = alumni_info(data)



def add_final_mark(data: list) -> list:
    """Return the same data with final mark"""
    for row in data:
        row["NotaFinal"] = (float(row["Parcial1"]) + float(row["Parcial2"])) * 0.3 + float(row["OrdinarioPracticas"]) * 0.4

add_final_mark(my_alumni_info)
row = my_alumni_info[0]

