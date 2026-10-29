import numpy as np
import matplotlib.pyplot as plt

# Creiamo 500 valori di tempo distribuiti tra 0 e 10
t = np.linspace(0, 10, num=500)

# Simuliamo gli spostamenti orizzontali della mongolfiera
# np.cos e np.sin generano variazioni della direzione
# np.cumsum accumula gli spostamenti nel tempo
x = np.cumsum(np.cos(t / 2))
y = np.cumsum(np.sin(t / 3))

# Simuliamo la salita della mongolfiera
# L'altezza aumenta in modo regolare con il tempo
z = t * 10

# Calcoliamo le variazioni delle coordinate
# np.gradient stima quanto cambia ogni coordinata
# tra i punti consecutivi della traiettoria
dx = np.gradient(x)
dy = np.gradient(y)
dz = np.gradient(z)

# Calcoliamo la velocità complessiva
# Combiniamo le tre componenti con la formula
# della distanza in tre dimensioni
speed = np.sqrt(dx**2 + dy**2 + dz**2)

# Creiamo la figura
fig = plt.figure(figsize=(10, 6))

# Creiamo un asse tridimensionale
# 111 indica una griglia di 1 riga e 1 colonna,
# con un solo grafico nella prima posizione
ax = fig.add_subplot(111, projection="3d")

# Disegniamo la traiettoria con una linea blu
ax.plot(
    x, y, z,
    color="blue",
    label="Traiettoria mongolfiera"
)

# Disegniamo punti colorati in base alla velocità
# c=speed associa un colore a ciascun valore di velocità
# cmap="viridis" sceglie la scala di colori
# s=20 imposta la dimensione dei punti
sc = ax.scatter(
    x, y, z,
    c=speed,
    cmap="viridis",
    s=20
)

# Aggiungiamo i nomi dei tre assi
ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_zlabel("Altezza")

# Aggiungiamo la barra che permette di interpretare
# i colori in base ai valori di velocità
fig.colorbar(sc, ax=ax, label="Velocità")

# Aggiungiamo il titolo
ax.set_title("Traiettoria 3D di una mongolfiera")

# Mostriamo la legenda
ax.legend()

# Sistemiamo gli spazi e visualizziamo il grafico
plt.tight_layout()
plt.show()