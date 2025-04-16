import AVL
import Procedimientos
import ArtistClass
import json
import API
from TreeVisualizer import AVLTreeVisualizer
import webbrowser

songsTree = AVL.AVLTree()
popularityTree = AVL.AVLTree()
artistsTree = AVL.AVLTree()
api = API.API()
playlist = "https://open.spotify.com/playlist/3sWwKAETNrcp41VnrfKeT1?si=OYwNXh0fRrGYMuIAS5kODA"
opcion = '10'
count = 0
while opcion != 0:
    if count == 0:
        print("\n" + "="*60)
        print("🎵 BIENVENIDO A STATIFY - Análisis de Árboles AVL 🎵")
        print("="*60)
        print("Para comenzar a usar el programa debe decidir si utilizar nuestra playlist predeterminada o si ingresar la suya.")
    
    if count != 0:
        print("\n📊 MENÚ PRINCIPAL - STATIFY 📊")
        print("1. Mostrar artista con más canciones")
        print("2. Mostrar artista con mayor popularidad")
        print("3. Mostrar niveles de canciones del artista más popular")
        print("4. Mostrar alturas de los árboles")
        print("5. Mostrar número de rotaciones al construir árbol de canciones")
        print("6. Mostrar canciones con duración mayor al promedio")
        print("7. Buscar canciones por artista")
        print("8. Mostrar N canciones más populares")
        print("9. Visualizar los árboles en SVG")
        print("10. Consultar otra playlist.")
        print("0. Salir")
        
        opcion = input("Escriba el número correspondiente a la opción que desea utilizar:")

    print()
    process = Procedimientos.Process()
    if opcion == '1':
        artista = process.artista_con_mas_canciones(songsTree)
        print(f"🎤 El artista con más canciones es: {artista}")
    elif opcion == '2':
        artista = process.artista_mas_popular(songsTree)
        print(f"🔥 El artista con mayor popularidad es: {artista}")
    elif opcion == '3':
        artista = process.artista_mas_popular(songsTree)
        niveles = process.mostrar_niveles_mayor_popularidad(songsTree)
        print(f"🎼 El artista con mayor popularidad ({artista}) tiene sus canciones en los niveles: {niveles}")
    elif opcion == '4':
        alturaSongs, alturaArtists = process.alturas(songsTree, artistsTree)
        print(f"📏 Altura del árbol de canciones: {alturaSongs}")
        print(f"🎨 Altura del árbol de artistas: {alturaArtists}")
    elif opcion == '5':
        print(f"🔄 Rotaciones del árbol de canciones: {process.rotacionesSongs(songsTree)}")
    elif opcion == '6':
        canciones = process.cancionesConDuracionMayorAlPromedio(songsTree.root)
        print(f"🎶 Canciones con duración mayor al promedio:\n{canciones}")
    elif opcion == '7':
        nombre = input("🎧 Ingrese el nombre del artista a buscar: ").strip()
        canciones = process.canciones_artista(songsTree, artistsTree, nombre)
        if canciones:
            print(f"🎵 Canciones de {nombre}: {canciones}")
        else:
            print(f"⚠️ No se encontraron canciones del artista {nombre}.")
    elif opcion == '8':
        while True:
            try:
                N = int(input("🔢 Ingrese la cantidad de canciones más populares a mostrar: "))
                if N <= 0:
                    print("⚠️ Ingrese un número mayor a cero.")
                    continue
                break
            except ValueError:
                print("❌ Ingrese un número válido.")
        canciones = process.obtener_n_canciones_populares(popularityTree, N)
        print(f"🎉 Top {N} canciones más populares:")
        for c in canciones:
            print(f"   - {c}")
    elif opcion == '9':
        print("🧐 ¿Qué árbol deseas visualizar?")
        print("1. Árbol de artistas")
        print("2. Árbol de canciones")
        print("3. Árbol de canciones por popularidad")
        arbol_opcion = input("Elige una opción (1, 2, 3): ").strip()

        if arbol_opcion == '1':
            AVLTreeVisualizer(artistsTree, False, False).render("AVL_artists")
            print("✅ Árbol de artistas generado.")
            webbrowser.open("AVL_artists.svg")
        elif arbol_opcion == '2':
            AVLTreeVisualizer(songsTree, True, True).render("AVL_songs")
            print("✅ Árbol de canciones generado.")
            webbrowser.open("AVL_songs.svg")
        elif arbol_opcion == '3':
            AVLTreeVisualizer(popularityTree, True, True).render("AVL_popularity")
            print("✅ Árbol de canciones por popularidad generado.")
            webbrowser.open("AVL_popularity.svg")
        else:
            print("❌ Opción no válida. Volviendo al menú principal.")
    
    elif opcion == '10':
        condicion = input("Escriba s para usar una playlist suya o n para utilizar la predeterminada: ")
        if (condicion == 's'):
            playlist = input("Inserte la url de su playlist: ")
        api.startAPI(playlist)

        with open('playlist.json', 'r', encoding='utf-8') as jsonFile:
            # Se carga el archivo JSON que contiene la información de la playlist
            jsonPlaylist = json.load(jsonFile)

            # Se recorre la lista de respuestas en JSON y se obtiene el id de la playlist
        artistas_unicos = {} #lista de artistas totales del árbol como objetos
        for i in range(len(jsonPlaylist)):
            for j in range(len(jsonPlaylist[i]['items'])):
                artistList = []
                #if jsonPlaylist[i]['items'][j]['tracks'] == None:
                #    continue
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

        count +=1
        print("Playlist encontrada! Ahora puede realizar alguna de las siguientes consultas sobre su playlist.")
    elif opcion == '0':
        print("👋 ¡Gracias por usar Statify! Hasta la próxima.")
        break
    else:
        print("❌ Opción no válida. Por favor, intente de nuevo.")