import numpy as np
import matplotlib.pyplot as plt

# Creiamo le coordinate X e Y
# Entrambe vanno da -5 a 5 con 100 valori
x = np.linspace(-5, 5, 100)
y = np.linspace(-5, 5, 100)

# Costruiamo una griglia bidimensionale
# Ogni coppia X, Y rappresenta un punto del terreno
X, Y = np.meshgrid(x, y)

# Calcoliamo l'altezza Z in ogni punto della griglia
# La funzione esponenziale crea una collina:
# è alta al centro e scende progressivamente verso i bordi
Z = np.exp(-0.1 * (X**2 + Y**2)) * 50

# Creiamo una figura con due grafici affiancati
fig = plt.figure(figsize=(12, 6))

# PRIMO GRAFICO: superficie piena
# 121 significa una riga, due colonne, primo grafico
ax1 = fig.add_subplot(121, projection="3d")

# Disegniamo la superficie della collina
# cmap="terrain" sceglie la mappa di colori
# alpha=0.9 imposta una leggera trasparenza
surf = ax1.plot_surface(
    X, Y, Z,
    cmap="terrain",
    alpha=0.9
)

# Aggiungiamo il titolo al primo grafico
ax1.set_title("Surface plot")

# SECONDO GRAFICO: rete di linee
# 122 indica una riga, due colonne, secondo grafico
ax2 = fig.add_subplot(122, projection="3d")

# Disegniamo la stessa collina usando una griglia di linee
# color="brown" imposta il colore delle linee
# linewidth=1 imposta il loro spessore
ax2.plot_wireframe(
    X, Y, Z,
    color="brown",
    linewidth=1
)

# Aggiungiamo il titolo al secondo grafico
ax2.set_title("Wireframe plot")

# Aggiungiamo la barra dei colori alla superficie
# shrink=0.5 riduce la dimensione della barra
# aspect=10 regola il rapporto tra lunghezza e larghezza
fig.colorbar(
    surf,
    ax=ax1,
    shrink=0.5,
    aspect=10
)

# Impostiamo l'angolo di visualizzazione dei due grafici
# elev controlla l'inclinazione verticale
# azim controlla la rotazione orizzontale
ax1.view_init(elev=30, azim=45)
ax2.view_init(elev=30, azim=45)

# Sistemiamo gli spazi tra i grafici
plt.tight_layout()

# Lasciamo più spazio nella parte superiore per i titoli
fig.subplots_adjust(top=0.88)

# Visualizziamo i grafici
plt.show()

# Analisi dei risultati
print("Analisi:")
print(
    "Il plot_surface evidenzia meglio il volume e la colorazione "
    "della collina, mentre il wireframe mostra solo la struttura geometrica."
)
print(
    "L'uso di alpha e colorbar aiuta a percepire profondità "
    "e variazioni di altezza in scenari complessi."
)