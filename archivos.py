import pandas as pd
from numpy import float64 as fl

filepath = "calificaciones.csv"
cal_data = pd.read_csv(filepath, sep=";")

print(cal_data.head())

# Simple function to attain to conditions of the csv
def to_float(value):
    str_value = str(value)
    final_string = str_value.replace(",", ".").replace("nan", "0")
    final_float = float(final_string)
    return float(final_float)


# Hemos considerado que la información que se pide a pasar a la lista es toda la que se halla en el csv,
# no he comprendido bien si querían que se suprimiese alguna
def alumni_info(data: pd.DataFrame) -> list:
    my_list = []
    for index in range(len(data.index)):
        values = data.iloc[index]
        my_dict = dict(zip(data.columns, values))
        my_list.append(my_dict)

    my_list.sort(key= lambda x: x["Apellidos"])

    return my_list

my_alumni_info = alumni_info(cal_data)

#! YA FUNCIONA
def add_final_mark(data: list):
    """Return the same data with final mark"""
    for row in data:
        n1 = (to_float(row["Parcial1"]) + to_float(row["Parcial2"])) * 0.3
        n2 = to_float(row["OrdinarioPracticas"]) * 0.4
        row["NotaFinal"] = n1 + n2

a = my_alumni_info
tf = to_float

n1 = (tf(a[0]["Parcial1"]) + tf(a[0]["Parcial2"])) * 0.3
n2 = tf(a[0]["OrdinarioPracticas"]) * 0.4

print(n1 + n2)



add_final_mark(my_alumni_info)

for i in my_alumni_info:
    print(i)

