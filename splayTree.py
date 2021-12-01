class Node:
    def __init__(self, val, right = None, left = None, parent = None):
        self.val = val
        self.right = right
        self.left = left
        self.parent = parent
        self.min = val

class ST:
    def __init__(self):
        self.ST = None
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
        if self.ST == None:
            self.ST = Node(x)
        else:
            self.insertAux(x, self.ST)

    def insertAux(self, x, node):
        if node.min > x:
                node.min = x
        if x < node.val:
            if node.left == None:
                node.left = Node(x, parent = node)
                self.splay(node.left)
            else:
                self.insertAux(x, node.left)
        else:
            if node.right == None:
                node.right = Node(x, parent = node)
                self.splay(node.right)
            else:
                self.insertAux(x, node.right)

    def delete(self, x):
        aux = self.deleteAux(x, self.ST)
        if aux != None:
            self.splay(aux)

    def deleteAux(self, x, node):
        if x > node.val:
            resp = self.deleteAux(x, node.right)
        elif x < node.val:
            resp = self.deleteAux(x, node.left)
        else:
            if node.right == None:
                if node.parent == None:
                    self.ST = node.left
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
            resp = self.delMin(node.right)
        if node.left == None:
            node.min = node.val
        else:
            node.min = node.left.val
        return resp

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
            return node.parent
        else:
            resp = self.delMin(node.left)
            if node.left == None:
                node.min = node.val
            else:
                node.min = node.left.min
            return resp

    def search(self, x):
        return self.searchAux(x, self.ST)
    
    def searchAux(self, x, node):
        self.contador += 1
        if x == node.val:
            self.splay(node)
            return True
        if x > node.val:
            if node.right == None:
                self.splay(node)
                return False
            else:
                return self.searchAux(x, node.right)
        else:
            if node.left == None:
                self.splay(node)
                return False
            else:
                return self.searchAux(x, node.left)
    
    def splay(self, node):
        if node == None:
            return
        if node.parent == None:
            self.ST = node
            return
        else:
            y = node.parent
            if y.left == node:
                if y.parent == None:
                    self.ST = self.rotDir(y)
                    return
                else:
                    z = y.parent 
                    if z.left == y:
                        self.rotDir(z)
                        self.splay(self.rotDir(y))
                    else:      
                        self.rotDir(z)
                        self.splay(self.rotEsq(y))
            else:
                if y.parent == None:
                    self.ST = self.rotEsq(y)
                    return
                else:
                    z = y.parent
                    if z.left == y:
                        self.rotEsq(z)
                        self.splay(self.rotDir(y))
                    else:
                        self.rotEsq(z)
                        self.splay(self.rotEsq(y))

    def Print(self):
        self.PrintAux(self.ST, 0)
    
    def PrintAux(self, node, d):
        if node == None:
            return
        self.PrintAux(node.right, d + 1)
        for i in range(d):
            print("     ", end = "")
        print(node.val)
        self.PrintAux(node.left, d + 1)
    
    def Min(self):
        if self.ST == None:
            return None
        return self.ST.min

    def contador(self):
        return self.contador
    


