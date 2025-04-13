import CancionClass
import ArtistClass

class AVLTree:
    def __init__(self):
        self.root = None
        self.rotaciones = 0

    def getRotaciones(self):
        return self.rotaciones

    def addNode(self, root, new_node):
        if root is None:
            return new_node
        
        if root.ID == new_node.ID:
            print("El elemento ya está")
            return root
        
        if new_node.ID > root.ID:
            root.right = self.addNode(root.right, new_node)
        else:
            root.left = self.addNode(root.left, new_node)
        
        root.balance = self.height(root.left) - self.height(root.right)
        
        if root.balance == 2:
            self.rotaciones += 1
            if root.left.balance == -1:
                self.rotaciones += 1
                root.left = self.rotate_right(root.left)
            return self.rotate_left(root)
        
        if root.balance == -2:
            self.rotaciones += 1
            if root.right.balance == 1:
                self.rotaciones += 1
                root.right = self.rotate_left(root.right)
            return self.rotate_right(root)
        
        return root
    
    def rotate_right(self, node):
        aux = node.right
        node.right = aux.left
        aux.left = node
        aux.balance = self.height(aux.left) - self.height(aux.right)
        node.balance = self.height(node.left) - self.height(node.right)
        return aux
    
    def rotate_left(self, node):
        aux = node.left
        node.left = aux.right
        aux.right = node
        aux.balance = self.height(aux.left) - self.height(aux.right)
        node.balance = self.height(node.left) - self.height(node.right)
        return aux
    
    def height(self, node):
        if node is None:
            return 0
        return 1 + max(self.height(node.left), self.height(node.right))
    
    def pre_order(self, node):
        if node is not None:
            print(node)
            self.pre_order(node.left)
            self.pre_order(node.right)
    
    def generateSongsTree(self, name, artistas, duracion, popularidad, artistsTree):
        new_node = CancionClass.Cancion(name, artistas, duracion, popularidad)
                # Agregar artistas al árbol sin duplicarlos
        for artist in artistas:
            artistsTree.generateArtistsTree(artist)

        # Agregar canción al árbol
        if self.root is None:
            self.root = new_node
            print(f"La raíz ha sido añadida {new_node.ID}")
        else:
            self.root = self.addNode(self.root, new_node)      

    def generateArtistsTree(self, artist):
        if self.root is None:
            self.root = artist
            print(f"La raíz ha sido añadida {artist.ID}")
        else:
            self.root = self.addNode(self.root, artist)

    def search(self, node, target):
        if node is None:
            return None
        elif node.ID == target.ID:  # Compara por valor, no por referencia
            return node
        elif target.ID < node.ID:
            return self.search(node.left, target)
        else:
            return self.search(node.right, target)
        
    def searchByName(self, node, name):
        if node is None:
            return None
        elif node.name == name:  # Compara por valor, no por referencia
            return node
        
        left_result = self.searchByName(node.left, name)
        if left_result:
            return left_result
        return self.searchByName(node.right, name)
