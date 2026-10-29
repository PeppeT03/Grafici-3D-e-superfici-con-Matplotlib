import numpy as np
import matplotlib.pyplot as plt

# Impostiamo il seme per ottenere sempre gli stessi dati casuali
np.random.seed(42)

# Definiamo il numero di stazioni meteorologiche
n_stations = 200

# Generiamo le coordinate X delle stazioni
# Ogni stazione avrà una posizione casuale tra 0 e 100
x = np.random.uniform(0, 100, size=n_stations)

# Generiamo le coordinate Y delle stazioni
# Anche queste sono comprese tra 0 e 100
y = np.random.uniform(0, 100, size=n_stations)

# Generiamo l'altitudine Z di ogni stazione
# I valori sono compresi tra 0 e 50 metri
z = np.random.uniform(0, 50, size=n_stations)

# Generiamo la temperatura di ogni stazione
# Le temperature sono comprese tra -10 e 35 °C
temperature = np.random.uniform(-10, 35, size=n_stations)


# Creiamo la figura con dimensioni 10 x 7
fig = plt.figure(figsize=(10, 7))

# Creiamo un asse tridimensionale
# 111 indica una griglia con una riga, una colonna
# e un solo grafico nella prima posizione
ax = fig.add_subplot(111, projection="3d")

# Creiamo lo scatter plot 3D
# x, y, z definiscono la posizione di ciascuna stazione
# c=temperature associa il colore alla temperatura
# cmap="coolwarm" usa colori freddi e caldi
# s=50 imposta la dimensione dei punti
# alpha=0.6 rende i punti semitrasparenti
sc = ax.scatter(
    x, y, z,
    c=temperature,
    cmap="coolwarm",
    s=50,
    alpha=0.6
)

# Aggiungiamo la barra dei colori
# Permette di interpretare i colori in base alla temperatura
fig.colorbar(sc, ax=ax, label="Temperatura (°C)")

# Impostiamo i nomi degli assi
ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_zlabel("Altitudine (m)")

# Aggiungiamo il titolo
ax.set_title("Stazioni meteorologiche - temperatura e densità")

# Sistemiamo gli spazi del grafico
plt.tight_layout()

# Visualizziamo il grafico
plt.show()