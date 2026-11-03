from typing import Any, Optional
from queue_ import Queue

class Node():

    def __init__(self, value = None, other_values = None):
        self.value = value
        self.left = None
        self.right = None
        self.other_values = other_values
        self.height = 0

    def __str__(self):
        return self.value

class BinaryTree():

    def __init__(self):
        self.root = None

    def height(self, root):
        if root is None:
            return -1
        else: 
            return root.height

    def update_height(self,root):
        if root is not None:
            left_height = self.height(root.left)
            right_height = self.height(root.right)
            root.height = (left_height if left_height > right_height else right_height) + 1 
    
    def insert_node(self, value: Any, other_value = None) -> None:

        def __insert_node(root, value, other_value=None):
            if root is None:
                #print(f"Lugar vacio inserte {value}")
                root = Node(value,other_value)
            elif value < root.value:
                #print(f"Ir a la izquierda de: {root.value}")
                root.left = __insert_node(root.left, value, other_value)
            else:
                #print(f"Ir a la derecha de: {root.value}")
                root.right = __insert_node(root.right, value, other_value)

            root = self.auto_balance(root)
            self.update_height(root)
            return root
        
        self.root = __insert_node(self.root, value, other_value)

        
    def delete_node(self, value: Any) -> Optional[Any]:
        def __replace(root):
            # print(root.value)
            aux = None
            if root.right is None:
                # print('mayor encontrado')
                return root.left, root
            else:
                # print('segui buscando a la derecha')
                root.right, aux = __replace(root.right)
            return root, aux

        def __delete_node(root, value):
            x = None
            other_value = None
            if root is not None:
                if value < root.value:
                    # print('ir a la izq')
                    # input()
                    root.left, x, other_value = __delete_node(root.left,value)
                elif value > root.value:
                    # print('ir a la derecha')
                    # input()
                    root.right, x, other_value = __delete_node(root.right, value)
                else:
                    # print('valor encontrado')
                    # input()
                    x = root.value
                    other_value = root.other_values
                    aux = None
                    if root.left is None:
                        # print('no tiene hijo izquierdo')
                        # input()
                        return root.right, x, other_value
                    elif root.right is None:
                        # print('no tiene hijo derecho')
                        # input()
                        return root.left, x, other_value
                    else:
                        # print('buscar remplazo')
                        # input()
                        root.left, aux = __replace(root.left)
                        root.value = aux.value

            root = self.auto_balance(root)
            self.update_height(root)
            return root, x, other_value

        other_value = None
        self.root, x, other_value = __delete_node(self.root, value)

        return x, other_value


    def search(self,value) -> Optional[Any]:
        def __search(root, value):
            aux = None
            if root is not None:
                if root.value == value:
                    aux = root
                elif value < root.value:
                    aux = __search(root.left, value)
                else:
                    aux = __search(root.right, value)
            return aux

        return __search(self.root, value)



    def auto_balance(self,root):
        if root is not None:
            if self.height(root.left) - self.height(root.right) == 2:
                if self.height(root.left.left) >= self.height(root.left.right):
                    root = self.simple_rotation(root, True)
                else:
                    root = self.double_rotation(root,True)
            elif self.height(root.right) - self.height(root.left) == 2:
                if self.height(root.right.right) >= self.height(root.right.left):
                    root = self.simple_rotation(root, False)
                else:
                    root = self.double_rotation(root, False)
        return root

    def simple_rotation(self, root, control):
        if control: 
            aux = root.left
            root.left = aux.right
            aux.right = root
        else:
            aux = root.right
            root.right = aux.left
            aux.left = root

        self.update_height(root)
        self.update_height(aux)
        root = aux
        return root

    def double_rotation(self, root, control):
        if control:
            root.left = self.simple_rotation(root.left, False)
            root = self.simple_rotation(root, True)
        else: 
            root.right = self.simple_rotation(root.right, True)
            root = self.simple_rotation(root, False)
        return root



    def inorder(self) -> None:

        def __inorder(root):
            if root.left is not None:
                __inorder(root.left)
            print(root.value, root.height)
            if root.right is not None:
                __inorder(root.right)

        __inorder(self.root)

    def postorder(self) -> None:

        def __postorder(root):
            if root.right is not None:
                __postorder(root.right)
            print(root.value)
            if root.left is not None:
                __postorder(root.left)

        __postorder(self.root)


    def preorder(self) -> None:

        def __preorder(root):
            print(root.value)
            if root.left is not None:
                __preorder(root.left)
            if root.right is not None:
                __preorder(root.right)

        __preorder(self.root)

    def by_level(self) -> None:

        pendings = Queue()

        if self.root is not None:
            pendings.arrive(self.root)
            # print(f'queue')
            # pendings.show()
            # input()
            while pendings.size() > 0:
                node = pendings.attention()
                print(node.value)
                # input()
                if node.left is not None:
                    pendings.arrive(node.left)
                if node.right is not None:
                    pendings.arrive(node.right)
                # print(f'queue ')
                # pendings.show()
                # input()



    def proxy_search(self, prefix: str) -> None:
        
        def __proxy_search(root, prefix):
            if root.left is not None:
                __proxy_search(root.left, prefix)
            if prefix.lower() in root.value.lower():
                print(root.value, root.other_values)
            if root.right is not None:
                __proxy_search(root.right, prefix)

        __proxy_search(self.root, prefix)


    def inorden_villain(self) -> None:
        
        def __inorden_villain(root):
            if root.left is not None:
                __inorden_villain(root.left)
            if root.other_values['is_villain']:
                print(root.value)
            if root.right is not None:
                __inorden_villain(root.right)

        __inorden_villain(self.root)

    def postorden_hero(self):
    
        def __postorden_hero(root):
            if root.right is not None:
                __postorden_hero(root.right)
            if not root.other_values['is_villain']:
                print(root.value)
            if root.left is not None:
                __postorden_hero(root.left)

        __postorden_hero(self.root)


    def inorden_hero_starts_with(self, prefix: str) -> None:
        
        def __inorden_hero_starts_with(root, prefix):
            if root.left is not None:
                __inorden_hero_starts_with(root.left, prefix)
            if root.value.startswith(prefix) and not root.other_values['is_villain']:
                print(root.value)
            if root.right is not None:
                __inorden_hero_starts_with(root.right, prefix)

        __inorden_hero_starts_with(self.root, prefix)


    def count_heroes(self) -> None:
        def __count_heroes(root):
            count = 0
            if root is not None:
                if root.left is not None:
                    count += __count_heroes(root.left)
                if not root.other_values['is_villain']:
                    count += 1
                if root.right is not None:
                    count += __count_heroes(root.right)
            return count

        count = __count_heroes(self.root)
        return count

    def count_mega(self) -> None:
        def __count_mega(root):
            count = 0
            if root is not None:
                if root.left is not None:
                    count += __count_mega(root.left)
                if root.other_values['mega']:
                    count += 1
                if root.right is not None:
                    count += __count_mega(root.right)
            return count

        count = __count_mega(self.root)
        return count

    def count_giga(self) -> None:
        def __count_giga(root):
            count = 0
            if root is not None:
                if root.left is not None:
                    count += __count_giga(root.left)
                if root.other_values['gigamax']:
                    count += 1
                if root.right is not None:
                    count += __count_giga(root.right)
            return count

        count = __count_giga(self.root)
        return count

    def count_type(self, tipo) -> int:
        def __count_type(root, tipo):
            count = 0
            if root is not None:
                if root.left is not None:
                    count += __count_type(root.left, tipo)
                if root.value == tipo:
                    count += 1
                if root.right is not None:
                    count += __count_type(root.right, tipo)
            return count

        count = __count_type(self.root, tipo)
        return count


    def bosque_hero_villano(self, villain_tree, super_heroes_tree) -> None:
        def __bosque_hero_villano(root):
            if root.left is not None:
                __bosque_hero_villano(root.left)
            if root.other_values['is_villain']:
                villain_tree.insert_node(root.value, root.other_values)
            else:
                super_heroes_tree.insert_node(root.value, root.other_values)

            if root.right is not None:
                __bosque_hero_villano(root.right)

        __bosque_hero_villano(self.root)