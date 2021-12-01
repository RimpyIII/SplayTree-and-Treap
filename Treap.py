import random

class Node:
    def __init__(self, val, prior,right = None, left = None, parent = None):
        self.val = val
        self.right = right
        self.left = left
        self.parent = parent
        self.min = val
        self.prior = prior

class Treap:
    def __init__(self):
        self.treap = None
        self.contador = 0
    
    def rotDir(self, node):
        aux = node.left
        node.left = aux.right
        aux.right = node
        aux.parent = node.parent
        if node.left != None:
            node.left.parent = node
        aux.right.parent = aux
        if node.left == None:
            node.min = node.val
        else:
            node.min = node.left.min
        if aux.parent != None:
            if node == aux.parent.left:
                aux.parent.left = aux
            else:
                aux.parent.right = aux
        return aux

    def rotEsq(self, node):
        aux = node.right
        node.right = aux.left
        aux.left = node
        aux.parent = node.parent
        if node.right != None:
            node.right.parent = node
        aux.left.parent = aux
        aux.min = aux.left.min
        if aux.parent != None:
            if node == aux.parent.left:
                aux.parent.left = aux
            else:
                aux.parent.right = aux
        return aux

    def insert(self, x):
        if self.treap == None:
            self.treap = Node(x, prior = random.randint(0, 10000))
        else:
            self.insertAux(x, self.treap)
    
    def insertAux(self, x, node):
        if node.min > x:
                node.min = x
        if x < node.val:
            if node.left == None:
                node.left = Node(x, parent = node, prior = random.randint(0, 10000))
                self.sobe(node.left)
            else:
                self.insertAux(x, node.left)
        else:
            if node.right == None:
                node.right = Node(x, parent = node, prior = random.randint(0, 10000))
                self.sobe(node.right)
            else:
                self.insertAux(x, node.right)
        root = self.treap
        while root.parent != None:
            root = root.parent
        self.treap = root

    def delete(self, x):
        self.deleteAux(x, self.treap)
    
    def deleteAux(self, x, node):
        if x > node.val:
            self.deleteAux(x, node.right)
        elif x < node.val:
            self.deleteAux(x, node.left)
        else:
            if node.right == None:
                if node.parent == None:
                    self.treap = node.left
                    return
                else:
                    if node.parent.left == node:
                        node.parent.left = node.left
                    else:  
                        node.parent.right = node.left
                if node.left != None:
                    node.left.parent = node.parent
                return node.parent
            node.val = node.right.min
            node.prior = self.delMin(node.right)
        if node.left == None:
            node.min = node.val
        else:
            node.min = node.left.val
        if node.parent != None:
            if node.parent.prior < node.prior:
                self.sobe(node)
            else:
                self.desce(node)
        else:
            self.desce(node)
        root = self.treap
        while root.parent != None:
            root = root.parent
        self.treap = root

    def delMin(self, node):
        if node.left == None:
            if node.parent == None:
                self.ST = node.right
                return
            else:
                if node.parent.left == node:
                    node.parent.left = node.right
                else:
                    node.parent.right = node.right
            if node.right != None:
                node.right.parent = node.parent
            return node.prior
        else:
            prior = self.delMin(node.left)
            if node.left == None:
                node.min = node.val
            else:
                node.min = node.left.min
            return prior

    def sobe(self, node):
        if node == None:
            return
        if node.parent == None or node.parent.prior > node.prior:
            return
        else:
            if node.parent.left == node:
                self.sobe(self.rotDir(node.parent))
            else:
                self.sobe(self.rotEsq(node.parent))

    def desce(self, node):
        if node.left == None:
            if node.right == None:
                return
            else:
                if node.right.prior < node.prior:
                    return
                else:
                    self.desce(self.rotEsq(node).left)
        else:
            if node.left.prior < node.prior:
                if node.right == None:
                    return
                else:
                    if node.right.prior < node.prior:
                        return
                    else:
                        self.desce(self.rotEsq(node).left)
            else:
                self.desce(self.rotDir(node).right)

    def Print(self):
        self.PrintAux(self.treap, 0)
    
    def PrintAux(self, node, d):
        if node == None:
            return
        self.PrintAux(node.right, d + 1)
        for i in range(d):
            print("     ", end = "")
        print(node.val, ":", node.prior)
        self.PrintAux(node.left, d + 1)
    
    def Min(self):
        if self.treap == None:
            return None
        return self.treap.min

    def search(self, x):
        return self.searchAux(x, self.ST)
    
    def searchAux(self, x, node):
        self.contador += 1
        if x == node.val:
            return True
        if x > node.val:
            if node.right == None:
                return False
            else:
                return self.searchAux(x, node.right)
        else:
            if node.left == None:
                return False
            else:
                return self.searchAux(x, node.left)
    
    def contador(self):
        return self.contador
        