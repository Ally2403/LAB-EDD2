import AVL
import Procedimientos

songsTree = AVL.AVLTree()
songs_data = [
    ("Song 1", ["Artist A", "Artist B"], 200, 80),
    ("Song 2", ["Artist B"], 220, 75),
    ("Song 3", ["Artist C"], 180, 85),
    ("Song 4", ["Artist D", "Artist A"], 210, 90),
    ("Song 5", ["Artist E"], 190, 7000),
    ("Song 6", ["Artist F", "Artist C"], 205, 95),
    ("Song 7", ["Artist G"], 195, 88),
    ("Song 8", ["Artist H", "Artist A"], 230, 92),
    ("Song 9", ["Artist I"], 240, 78),
    ("Song 10", ["Artist J", "Artist E"], 215, 85)
]

for song in songs_data:
    songsTree.generateSongsTree(*song)

# Imprimir el árbol en preorden
print("\nÁrbol en Preorden:")
songsTree.pre_order(songsTree.root)

artistsTree = AVL.AVLTree()
artists_data = [
    ("Artist A"),
    ("Artist B"),
    ("Artist C"),
    ("Artist D"),
    ("Artist E"),
    ("Artist F"),
    ("Artist G"),
    ("Artist H"),
    ("Artist I"),
    ("Artist J")
]

for artist in artists_data:
    artistsTree.generateArtistsTree(artist)

# Imprimir el árbol en preorden
print("\nÁrbol en Preorden:")
artistsTree.pre_order(artistsTree.root)

print()
process = Procedimientos.Process()
artista_mas_popular = process.artista_con_mas_canciones(songsTree.root)
print(f"El artista con más canciones es: {artista_mas_popular}")
print()
artistaMayorPopularidad = process.artista_mas_popular(songsTree.root)
print(f"El artista con mayor popularidad es: {artistaMayorPopularidad}")