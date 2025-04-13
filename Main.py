import AVL
import Procedimientos
import ArtistClass

songsTree = AVL.AVLTree()
popularityTree = AVL.AVLTree()
# Diccionario para evitar instancias duplicadas de artistas
artistas_unicos = {}

# Función para obtener o crear una instancia única de un artista
def get_artist(nombre):
    if nombre not in artistas_unicos:
        artistas_unicos[nombre] = ArtistClass.Artist(nombre)
    return artistas_unicos[nombre]

# Lista de datos de canciones usando instancias únicas de artistas
songs_data = [
    ("Song 1", [get_artist("Artist A"), get_artist("Artist B")], 200, 80),
    ("Song 2", [get_artist("Artist B")], 220, 750),
    ("Song 3", [get_artist("Artist A")], 180, 85),
    ("Song 4", [get_artist("Artist D"), get_artist("Artist A")], 210, 90),
    ("Song 5", [get_artist("Artist E")], 190, 2),
    ("Song 6", [get_artist("Artist F"), get_artist("Artist C")], 205, 95),
    ("Song 7", [get_artist("Artist G")], 195, 88),
    ("Song 8", [get_artist("Artist H"), get_artist("Artist A")], 230, 920),
    ("Song 9", [get_artist("Artist I")], 240, 78),
    ("Song 10", [get_artist("Artist J"), get_artist("Artist A")], 215, 85)
]

artistsTree = AVL.AVLTree()
for song in songs_data:
    songsTree.generateSongsTree(song[0], song[1], song[2], song[3], artistsTree, popularityTree)

# Imprimir el árbol en preorden
print("\nÁrbol de canciones en Preorden:")
songsTree.pre_order(songsTree.root)


# Imprimir el árbol en preorden
print("\nÁrbol de artistas en Preorden:")
artistsTree.pre_order(artistsTree.root)

print()
process = Procedimientos.Process()
artista_mas_popular = process.artista_con_mas_canciones(songsTree, artistsTree)
print(f"El artista con más canciones es: {artista_mas_popular}")
print()
artistaMayorPopularidad = process.artista_mas_popular(songsTree, artistsTree)
print(f"El artista con mayor popularidad es: {artistaMayorPopularidad}")
print()
nivelesMayorPopularidad = process.mostrar_niveles_mayor_popularidad(songsTree, artistsTree)
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
cancionesArtista = process.canciones_artista(songsTree, artistsTree, "Artist A")
print(f"Las canciones del artista A son {cancionesArtista}")
print()
# Imprimir el árbol en preorden
print("\nÁrbol de popularidad en Preorden:")
popularityTree.pre_order(popularityTree.root)
print()
N = 8
print(f"Las {N} canciones más populares son")
lista_canciones = process.obtener_n_canciones_populares(popularityTree, N)
    
# Ahora 'lista_canciones' contendrá las 5 canciones de mayor popularidad en la playlist.
for cancion in lista_canciones:
    print(cancion)