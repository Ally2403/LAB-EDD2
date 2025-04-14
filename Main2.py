import AVL
import Procedimientos
import ArtistClass

"""
MINI ÁRBOL PARA HACER PRUEBAS EN EL CÓDIGO
"""

songsTree = AVL.AVLTree()
popularityTree = AVL.AVLTree()
artistsTree = AVL.AVLTree()
# Diccionario para evitar instancias duplicadas de artistas
artistas_unicos = {}

# Función para obtener o crear una instancia única de un artista
def get_artist(id, nombre):
    if nombre not in artistas_unicos:
        artistas_unicos[nombre] = ArtistClass.Artist(id, nombre)
        artistsTree.generateArtistsTree(artistas_unicos[nombre])
    return artistas_unicos[nombre]

# Lista de datos de canciones usando instancias únicas de artistas
songs_data = [
    ("Song 1", [get_artist(1, "Artist A"), get_artist(2, "Artist B")], 200, 80),
    ("Song 2", [get_artist(2, "Artist B")], 220, 750),
    ("Song 3", [get_artist(1, "Artist A")], 180, 85),
    ("Song 4", [get_artist(4, "Artist D"), get_artist(1, "Artist A")], 210, 90),
    ("Song 5", [get_artist(5, "Artist E")], 190, 2),
    ("Song 6", [get_artist(6, "Artist F"), get_artist(3, "Artist C")], 205, 95),
    ("Song 7", [get_artist(7, "Artist G")], 195, 88),
    ("Song 8", [get_artist(8, "Artist H"), get_artist(1, "Artist A")], 230, 920),
    ("Song 9", [get_artist(9, "Artist I")], 240, 78),
    ("Song 10", [get_artist(10, "Artist J"), get_artist(1, "Artist A")], 215, 85)
]


i = 0
for song in songs_data:
    i = i + 1
    songsTree.generateSongsTree(i, song[0], song[1], song[2], song[3], popularityTree)
    

print()
process = Procedimientos.Process()
artista_mas_popular = process.artista_con_mas_canciones(songsTree)
print(f"El artista con más canciones es: {artista_mas_popular}")
print()
artistaMayorPopularidad = process.artista_mas_popular(songsTree)
print(f"El artista con mayor popularidad es: {artistaMayorPopularidad}")
print()
nivelesMayorPopularidad = process.mostrar_niveles_mayor_popularidad(songsTree)
print(f"El artista con mayor popularidad {artistaMayorPopularidad} tiene sus canciones en los niveles {nivelesMayorPopularidad}")
print()
alturaSongs, alturaArtists = process.alturas(songsTree, artistsTree)
print(f"la altura del árbol de canciones es {alturaSongs}, La altura del árbol de artistas es {alturaArtists}")
print()
print(f"El número de rotaciones necesarias a la hora de construir el árbol de canciones es {process.rotacionesSongs(songsTree)}")
print()
cancionesMayores = process.cancionesConDuracionMayorAlPromedio(songsTree.root)
print(f"Las canciones con duración mayor al promedio son {cancionesMayores}")
print()
artistaBuscado = "Artist B"
cancionesArtista = process.canciones_artista(songsTree, artistsTree, artistaBuscado)
print(f"Las canciones del artista {artistaBuscado} son {cancionesArtista}")
print()
# Imprimir el árbol en preorden
#print("\nÁrbol de popularidad en Preorden:")
#popularityTree.pre_order(popularityTree.root)
print()
N = 8
print(f"Las {N} canciones más populares son")
lista_canciones = process.obtener_n_canciones_populares(popularityTree, N)
    
# Ahora 'lista_canciones' contendrá las 5 canciones de mayor popularidad en la playlist.
for cancion in lista_canciones:
    print(cancion)
