from graphviz import Digraph

class AVLTreeVisualizer:
    # Funcion constructor
    def __init__(self, avl_tree):
        self.tree = avl_tree # Objeto de tipo arbol AVL 
        self.dot = Digraph() # Herramienta para definir nodos y aristas en un grafico 

        # Personalización global del gráfico
        self.dot.attr(bgcolor='lightgrey', label='Árbol AVL Visualizado', fontsize='20', fontname='Helvetica')

    def _add_nodes_edges(self, node):
        if node is None:
            return

        label = f"{node.name}"  

        # Personalización del nodo
        self.dot.node(
            name=label,
            label=label,
            shape='plaintext',         # Forma del nodo
            style='filled',          # Estilo de relleno
            fillcolor='lightblue',   # Color de fondo
            fontcolor='black',       # Color del texto
            fontname='Arial',        # Tipo de letra
            fontsize='12'            # Tamaño de letra
        )

        # Nodos ubicados a la izquierda de su padre
        if node.left:
            left_label = f"{node.left.name}"
            self.dot.edge(label, left_label, color='blue', penwidth='4')
            self._add_nodes_edges(node.left)

        # Nodos ubicados a la derecha de su padre
        if node.right:
            right_label = f"{node.right.name}"
            self.dot.edge(label, right_label, color='green', penwidth='4')
            self._add_nodes_edges(node.right)

    # Funcion renderizadora
    def render(self, filename="avl_tree"):
        self._add_nodes_edges(self.tree.root) # Agrega los nodos enlazados a aristas al grafico
        self.dot.render(filename, format="png", cleanup=True) # Generar una imagen PNG
        print(f"Árbol AVL guardado como {filename}.png")
