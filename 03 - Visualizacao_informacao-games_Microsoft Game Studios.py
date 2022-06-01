import seaborn as sns
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
plt.rcdefaults()

game = pd.read_csv("vgsales.csv")

names = game["Name"]
vendas = game["Global_Sales"]
indice = np.arange(len(names))

gameFiltrado = game.loc[game["Publisher"] == "Microsoft Game Studios"]
gameFiltrado = gameFiltrado.loc[gameFiltrado["Global_Sales"] > 5.0]

gameFiltrado = gameFiltrado.fillna(0)
print(gameFiltrado)

pop = list(gameFiltrado["Global_Sales"]*1000000)
nome = list(gameFiltrado["Name"])
ind = np.arange(len(nome))

plt.bar(ind, pop, color=sns.color_palette("Greens"))
plt.xticks(ind, nome, rotation=90)
plt.subplots_adjust(right=2)
plt.ylabel("Sales")
plt.title("Jogos da publisher 'Microsoft Game Studios' com mais de 5 milhões de unidades vendidas")

plt.show()
