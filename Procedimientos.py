from AVL import AVLTree
from ArtistClass import Artist

class Process:
    #PUNTO 1 = ¿Qué artista tiene mayor número de canciones en la playlist?
    #Contador es un diccionario
    def contar_canciones_por_artista(self, songsTree, artistsTree, songsTreeRoot, artistsTreeRoot, contador):
        """
        Recorre el árbol de canciones y cuenta cuántas veces aparece cada artista en la playlist.

        Parámetros:
        - songsTree: Árbol AVL de canciones.
        - artistsTree: Árbol AVL de artistas.
        - songsTreeRoot: Nodo raíz del árbol de canciones.
        - artistsTreeRoot: Nodo raíz del árbol de artistas.
        - contador: Diccionario donde se almacena la cantidad de canciones por artista.
        """
        if songsTreeRoot is None:
            return
        
        # Recorre los artistas por cada canción
        for artist in songsTreeRoot.artists:
                if artistsTree.search(artistsTree.root, artist) in contador:
                    contador[artist] += 1 #Si ya está en el diccionario este artista, le suma 1
                else:
                    contador[artist] = 1 #Si no está en el diccionario, lo pone con valor incial 1
        
        self.contar_canciones_por_artista(songsTree, artistsTree, songsTreeRoot.left, artistsTreeRoot, contador)
        self.contar_canciones_por_artista(songsTree, artistsTree, songsTreeRoot.right, artistsTreeRoot, contador)

    def artista_con_mas_canciones(self, songsTree, artistsTree):
        """
        Determina qué artista tiene más canciones registradas en la playlist.
        
        Parámetros:
        - songsTree: Árbol AVL de canciones.
        - artistsTree: Árbol AVL de artistas.
        Retorna:
        - El nombre del artista con mayor número de canciones o None si el árbol está vacío.
        """
        contador = {}
        self.contar_canciones_por_artista(songsTree, artistsTree, songsTree.root, artistsTree.root, contador)
        
        if not contador:
            return None  # Si el árbol está vacío
        
        return max(contador, key=contador.get)

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
    
    #Punto 3 = ¿En qué niveles del árbol AVL se encuentran las canciones del artista con mayor popularidad?
    def buscar_niveles(self, songsTree, artistsTree, songsTreeRoot, artistsTreeRoot, contador, artistMayor, c):
        if songsTreeRoot is None:
            return contador

        c = c + 1
        nivel = "Nivel " + str(c)
        for artist in songsTreeRoot.artists:
            if artist == artistMayor: #AÑADIR MÉTODO SEARCH
                if nivel in contador:
                    contador[nivel] += 1  # Si el artista ya existe, sumamos la popularidad de esta cancion
                else:
                    contador[nivel] = 1  # Si no existe, lo agregamos con su popularidad

        self.buscar_niveles(songsTree, artistsTree, songsTreeRoot.left, artistsTreeRoot, contador, artistMayor, c)
        self.buscar_niveles(songsTree, artistsTree, songsTreeRoot.right, artistsTreeRoot, contador, artistMayor, c)

    def mostrar_niveles_mayor_popularidad(self, songsTree, artistsTree):
        artistMayor = self.artista_mas_popular(songsTree, artistsTree)
        contador = {}
        c = 0
        self.buscar_niveles(songsTree, artistsTree, songsTree.root, artistsTree.root, contador, artistMayor, c)
        if not contador:
            return None
        niveles = ""
        for nivel in contador:
            niveles = niveles + ", " + nivel

        return niveles
    
    #Punto 4 = ¿Cuál es la altura del árbol AVL de canciones? ¿Y del árbol AVL de artistas?
    def alturas(self, songsTree, artistsTree):
        return songsTree.height(songsTree.root), artistsTree.height(artistsTree.root)
    
    #Punto 5 = ¿Cuántas rotaciones fueron necesarias para balancear el árbol AVL de canciones durante su construcción?
    def rotacionesSongs(self, songsTree):
        return songsTree.getRotaciones()
    
    #Punto 6 = ¿Qué canciones tienen una duración superior al promedio de duración de todas las canciones en la playlist?
    def recorridoAcumulacion(self, songsTreeRoot):
        if songsTreeRoot is None:
            return (0, 0)
        sumaIzq, cantIzq = self.recorridoAcumulacion(songsTreeRoot.left)
        sumaDer, cantDer = self.recorridoAcumulacion(songsTreeRoot.right)

        sumaTotal = songsTreeRoot.duracion + sumaIzq + sumaDer
        cantTotal = 1 + cantIzq + cantDer
        return (sumaTotal, cantTotal)
    
    def buscarCancionesConDuracionMayor(self, songsTreeRoot, promedio, lista_canciones):
        if songsTreeRoot is None:
            return
        
        self.buscarCancionesConDuracionMayor(songsTreeRoot.left, promedio, lista_canciones)
        if songsTreeRoot.duracion > promedio:
            lista_canciones.append(songsTreeRoot.name)
        self.buscarCancionesConDuracionMayor(songsTreeRoot.right, promedio, lista_canciones)
    
    def cancionesConDuracionMayorAlPromedio(self, songsTreeRoot):
        suma, cantidad = self.recorridoAcumulacion(songsTreeRoot)
        if cantidad == 0:
            return []  # Evitar división por cero si el árbol está vacío.
        
        promedio = suma / cantidad

        lista_canciones = []
        self.buscarCancionesConDuracionMayor(songsTreeRoot, promedio, lista_canciones)
        songs = ""
        for cancion in lista_canciones:
            songs = songs + ", " + str(cancion)
        return songs
    
    #Punto 7 = ¿Cuál es la complejidad temporal de buscar todas las canciones de un artista específico usando la estructura implementada? Justifica tu respuesta.
    def canciones_un_artista(self, songsTree, artistsTree, songsTreeRoot, artistsTreeRoot, contador, artist1):
        if songsTreeRoot is None:
            return
        
        for artist in songsTreeRoot.artists:
            if artist == artist1:
                contador.append(songsTreeRoot.name)
        
        self.canciones_un_artista(songsTree, artistsTree, songsTreeRoot.left, artistsTreeRoot, contador, artist1)
        self.canciones_un_artista(songsTree, artistsTree, songsTreeRoot.right, artistsTreeRoot, contador, artist1)

    def canciones_artista(self, songsTree, artistsTree, artistName):
        contador = []
        artist = artistsTree.searchByName(artistsTree.root, artistName)
        self.canciones_un_artista(songsTree, artistsTree, songsTree.root, artistsTree.root, contador, artist)

        if contador == None:
            return   # Si el árbol está vacío
        
        songs = ""
        for cancion in contador:
            songs = songs + ", " + str(cancion)
        return songs
    
    #Punto 9 = Implementa un algoritmo que permita obtener las N canciones más populares de la playlist en tiempo O(log(n) + N).
    def obtener_n_canciones_populares(self, arbol_popularidad, N: int):
        """
        Retorna una lista con las N canciones más populares.

        Como parámetros tiene el arbol de canciones organizado por popularidad y
        el número de canciones populares a buscar.

        La complejidad del algoritmo es O(log(n) + N).
        """
        resultado = []
        stack = [] # Pila auxiliar
        current = arbol_popularidad.root

        while (stack or current) and len(resultado) < N:
            # Mientras current no sea None, vamos siempre al subárbol derecho.
            if current:
                stack.append(current) # Nodos visitados
                current = current.right # Mayor popularidad
            else:
                # Cuando current es None, se saca el nodo en la cima de la pila
                current = stack.pop()
                resultado.append(current)
                # Luego se recorre el subárbol izquierdo
                current = current.left

        return resultado
