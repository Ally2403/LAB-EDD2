import AVL
import Procedimientos
import ArtistClass
import json
import API
from TreeVisualizer import AVLTreeVisualizer

songsTree = AVL.AVLTree()
popularityTree = AVL.AVLTree()
artistsTree = AVL.AVLTree()
api = API.API()
playlist = "https://open.spotify.com/playlist/3sWwKAETNrcp41VnrfKeT1?si=OYwNXh0fRrGYMuIAS5kODA"
#Solo funciona si no
condicion = input("¿Desea usar una playlist nueva? (s/n): ")
if (condicion == 's'):
    playlist = input("Inserte la playlist: ")
api.startAPI(playlist)


with open('playlist.json', 'r', encoding='utf-8') as jsonFile:
    # Se carga el archivo JSON que contiene la información de la playlist
    jsonPlaylist = json.load(jsonFile)

    # Se recorre la lista de respuestas en JSON y se obtiene el id de la playlist
artistas_unicos = {} #lista de artistas totales del árbol como objetos
for i in range(len(jsonPlaylist)):
    for j in range(len(jsonPlaylist[i]['items'])):
        artistList = []
        for k in range(len(jsonPlaylist[i]['items'][j]['track']['artists'])):
            artist = jsonPlaylist[i]['items'][j]['track']['artists'][k]['name']
            artistID = jsonPlaylist[i]['items'][j]['track']['artists'][k]['id']
            if artist not in artistas_unicos:
                artistas_unicos[artist] = ArtistClass.Artist(artistsTree.convertAscii(artistID), artist)
            artistList.append(artistas_unicos[artist]) #Lista de artistas de una cancion como objetos

#---------------------------------------------------------------------------------------------------------------
            artistsTree.generateArtistsTree(artistas_unicos[artist])

        songID = jsonPlaylist[i]['items'][j]['track']['id']
        songName = jsonPlaylist[i]['items'][j]['track']['name']
        songDuration = jsonPlaylist[i]['items'][j]['track']['duration_ms']
        songPopularity = jsonPlaylist[i]['items'][j]['track']['popularity']
        songsTree.generateSongsTree(songsTree.convertAscii(songID), songName, artistList, songDuration, songPopularity, popularityTree)

# Imprimir el árbol en preorden
#print("\nÁrbol de canciones en Preorden:")
#songsTree.pre_order(songsTree.root)


# Imprimir el árbol en preorden
#print("\nÁrbol de artistas en Preorden:")
#artistsTree.pre_order(artistsTree.root)

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
artistaBuscado = "Bad Bunny"
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

visualizerArtistas = AVLTreeVisualizer(artistsTree, False, False)
visualizerArtistas.render("AVL1")
visualizerCanciones = AVLTreeVisualizer(songsTree, True, True)
visualizerCanciones.render("AVL2")
visualizerPopularity = AVLTreeVisualizer(popularityTree, True, True)
visualizerPopularity.render("AVL3")