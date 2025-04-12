from AVL import AVLTree
from ArtistClass import Artist

class Process:
    #PUNTO 1 = ¿Qué artista tiene mayor número de canciones en la playlist?
    #Contador es un diccionario
    def contar_canciones_por_artista(self, songsTree, artistsTree, songsTreeRoot, artistsTreeRoot, contador):
        if songsTreeRoot is None:
            return
        
        for artist in songsTreeRoot.artists:
            if(artistsTree.search(artistsTree.root, artist) != None): #AÑADIR MÉTODO SEARCH
                if artistsTree.search(artistsTree.root, artist) in contador:
                    contador[artist] += 1 #Si ya está en el diccionario este artista, le suma 1
                else:
                    contador[artist] = 1 #Si no está en el diccionario, lo pone con valor incial 1
        
        self.contar_canciones_por_artista(songsTree, artistsTree, songsTreeRoot.left, artistsTreeRoot, contador)
        self.contar_canciones_por_artista(songsTree, artistsTree, songsTreeRoot.right, artistsTreeRoot, contador)

    def artista_con_mas_canciones(self, songsTree, artistsTree):
        contador = {}
        self.contar_canciones_por_artista(songsTree, artistsTree, songsTree.root, artistsTree.root, contador)
        
        if not contador:
            return None  # Si el árbol está vacío
        
        return max(contador, key=contador.get)
                            #Devuelve la clave del artista con más canciones

    #Punto 2 = ¿Qué artista tiene mayor índice de popularidad? (Suma de popularidades de las canciones del artista)
    def contar_popularidad_artistas(self, songsTree, artistsTree, songsTreeRoot, artistsTreeRoot, contador):
        if songsTreeRoot is None:
            return contador

        for artist in songsTreeRoot.artists:
            if(artistsTree.search(artistsTree.root, artist) != None): #AÑADIR MÉTODO SEARCH
                if artistsTree.search(artistsTree.root, artist) in contador:
                    contador[artist] += songsTreeRoot.popularidad  # Si el artista ya existe, sumamos la popularidad de esta cancion
                else:
                    contador[artist] = songsTreeRoot.popularidad  # Si no existe, lo agregamos con su popularidad

        self.contar_popularidad_artistas(songsTree, artistsTree, songsTreeRoot.left, artistsTreeRoot, contador)
        self.contar_popularidad_artistas(songsTree, artistsTree, songsTreeRoot.right, artistsTreeRoot, contador)

    def artista_mas_popular(self, songsTree, artistsTree):
        # Obtener el diccionario con la suma de popularidades
        contador = {}
        self.contar_popularidad_artistas(songsTree, artistsTree, songsTree.root, artistsTree.root, contador)

        if not contador:
            return None

        # Encontramos el artista con mayor popularidad
        return max(contador, key=contador.get)
