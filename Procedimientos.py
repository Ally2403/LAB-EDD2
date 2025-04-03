from AVL import AVLTree
from ArtistClass import Artist

class Process:
    #PUNTO 1 = ¿Qué artista tiene mayor número de canciones en la playlist?
    #Contador es un diccionario
    def contar_canciones_por_artista(self, songsTree, artistsTree, contador):
        if songsTree is None:
            return
        
        for artist in songsTree.artists:
            if(artistsTree.search(artist) != None): #AÑADIR MÉTODO SEARCH
                if artistsTree.search(artist) in contador:
                    contador[artist] += 1 #Si ya está en el diccionario este artista, le suma 1
                else:
                    contador[artist] = 1 #Si no está en el diccionario, lo pone con valor incial 1
        
        self.contar_canciones_por_artista(songsTree.left, contador)
        self.contar_canciones_por_artista(songsTree.right, contador)

    def artista_con_mas_canciones(self, songsTree):
        contador = {}
        self.contar_canciones_por_artista(songsTree, contador)
        
        if not contador:
            return None  # Si el árbol está vacío
        
        return max(contador, key=contador.get)
                            #Devuelve la clave del artista con más canciones

    #Punto 2 = ¿Qué artista tiene mayor índice de popularidad? (Suma de popularidades de las canciones del artista)
    def contar_popularidad_artistas(self, songsTree, contador=None):
        if contador is None:
            contador = {}  # Diccionario donde guardaremos la suma de popularidad de cada artista

        if songsTree is None:
            return contador

        for artist in songsTree.artists:
            if artist in contador:
                contador[artist] += songsTree.popularidad  # Si el artista ya existe, sumamos la popularidad de esta cancion
            else:
                contador[artist] = songsTree.popularidad  # Si no existe, lo agregamos con su popularidad

        self.contar_popularidad_artistas(songsTree.left, contador)
        self.contar_popularidad_artistas(songsTree.right, contador)

        return contador

    def artista_mas_popular(self, songsTree):
        # Obtener el diccionario con la suma de popularidades
        contador = self.contar_popularidad_artistas(songsTree)

        if not contador:
            return None

        # Encontramos el artista con mayor popularidad
        return max(contador, key=contador.get)
