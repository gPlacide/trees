'''
This file implements the AVL Tree data structure.
The functions in this file are considerably harder than the functions in the BinaryTree and BST files.
'''

from Trees.BinaryTree import BinaryTree, Node
from Trees.BST import BST

class AVLTree(BST):
    '''
    FIXME:
    AVLTree is currently not a subclass of BST.
    You should make the necessary changes in the class declaration line above 
    and in the constructor below.
    '''

    def __init__(self, xs=None):
        '''
        FIXME:
        Implement this function.
        '''
        #super().__init__()
        self.root = None

        if xs:
            self.insert_list(xs)

    def balance_factor(self):
        '''
        Returns the balance factor of a tree.
        '''
        return AVLTree._balance_factor(self.root)

    @staticmethod
    def _balance_factor(node):
        '''
        Returns the balance factor of a node.
        '''
        if node is None:
            return 0
        return BinaryTree._height(node.left) - BinaryTree._height(node.right)


    def is_avl_satisfied(self):
        '''
        Returns True if the avl tree satisfies that all nodes have a balance factor in [-1,0,1].
        '''
        return AVLTree._is_avl_satisfied(self.root)

    @staticmethod
    def _is_avl_satisfied(node):
        ''' 
        FIXME:
        Implement this function.
        '''
        if node is None:
            return True
        return AVLTree._balance_factor(node) in [1,0,-1] and AVLTree._is_avl_satisfied(node.left)  and AVLTree._is_avl_satisfied(node.right)

    @staticmethod
    def _left_rotate(node):
        '''
        FIXME:
        Implement this function.

        The lecture videos provide a high-level overview of tree rotations,
        and the textbook provides full python code.
        The textbook's class hierarchy for their AVL tree code is fairly different from our class hierarchy,
        however, so you will have to adapt their code.
        '''
        #newRoot = node.right
        #node.right = newRoot.left #if the new_root had a left child. it becomes the right child of the old node
        #newRoot.left = node



        new_node = Node(node.right.value) #the new root
        new_node.right = node.right.right #what was the grandchild becomes the right child of the  new root

        new_left = Node(node.value) #what was the root becomes the left child of a new root
        new_left.left = node.left #
        new_left.right = node.right.left #what was the left of the right child becomes the right of the old root

        new_node.left = new_left

        return new_node        
        
        
        
    @staticmethod
    def _right_rotate(node):
        '''
        FIXME:
        Implement this function.

        The lecture videos provide a high-level overview of tree rotations,
        and the textbook provides full python code.
        The textbook's class hierarchy for their AVL tree code is fairly different from our class hierarchy,
        however, so you will have to adapt their code.
        '''
        
        new_node = Node(node.left.value)
        new_node.left = node.left.left

        new_right = Node(node.value)
        new_right.right = node.right
        new_right.left = node.left.right

        new_node.right = new_right

        return new_node

    def insert(self, value):
        '''
        FIXME:
        Implement this function.

        The lecture videos provide a high-level overview of how to insert into an AVL tree,
        and the textbook provides full python code.
        The textbook's class hierarchy for their AVL tree code is fairly different from our class hierarchy,
        however, so you will have to adapt their code.

        HINT:
        It is okay to add @staticmethod helper functions for this code.
        The code should look very similar to the code for your insert function for the BST,
        but it will also call the left and right rebalancing functions.
        '''

        if self.root is None:
            self.root = Node(value)
        else:
            self.root = AVLTree._insert(value, self.root)

    def insert_list(self, xs):
        for x in xs:
            self.insert(x)

    @staticmethod
    def _insert(value, node):
        if value < node.value:
            if node.left is None:
                node.left = Node(value)
            else:
                AVLTree._insert(value, node.left)

        elif value > node.value:
            if node.right is None:
                node.right = Node(value)
            else:
                AVLTree._insert(value, node.right)

        else:
            print("Can't add because value is already in the tree")

  
