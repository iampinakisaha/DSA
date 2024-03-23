#program to demostrate binary search tree operations

from Queue.QueueLinkedList import Queue
#creating BSTNode class
class BSTNode:
    def __init__(self,data):
        self.data = data
        self.leftChild = None
        self.rightChild = None
    

    def insertBST(self,rootNode,value):
        if rootNode.data == None:
            rootNode.data = value
        else:
            newNode = BSTNode(value)
            if value <= rootNode.data:
                if rootNode.leftChild is None:
                    rootNode.leftChild = newNode
                    return
                else:
                    self.insertBST(rootNode.leftChild,value)
            else:
                if rootNode.rightChild is None:
                    rootNode.rightChild = newNode
                    return
                else:
                    self.insertBST(rootNode.rightChild,value)
        return "The node has been successfully inserted"
            

    def searchNode(self,rootNode, nodeValue):
        if rootNode.data == nodeValue:
            print("The value is found")
        elif nodeValue < rootNode.data:
            if rootNode.leftChild.data == nodeValue:
                print("The value is found")
            else:
                self.searchNode(rootNode.leftChild, nodeValue)
        else:
            if rootNode.rightChild.data == nodeValue:
                print("The value is found")
            else:
                self.searchNode(rootNode.rightChild, nodeValue)



    def preOrderTraversal(self,rootNode):
        if not rootNode:
            return
        print(rootNode.data)
        self.preOrderTraversal(rootNode.leftChild)
        self.preOrderTraversal(rootNode.rightChild)

    def inOrderTraversal(self,rootNode):
        if not rootNode:
            return
        
        self.preOrderTraversal(rootNode.leftChild)
        print(rootNode.data)
        self.preOrderTraversal(rootNode.rightChild)

    def postOrderTraversal(self,rootNode):
        if not rootNode:
            return
        
        self.preOrderTraversal(rootNode.leftChild)
        self.preOrderTraversal(rootNode.rightChild)
        print(rootNode.data)

    def levelOrderTraversal(self,rootNode):
        if not rootNode:
            return
        else:
            customQueue = Queue()
            customQueue.enqueue(rootNode)
            while not customQueue.isEmpty():
                root = customQueue.dequeue()
                print(root.value.data)
                if root.value.leftChild is not None:
                    customQueue.enqueue(root.value.leftChild)
                if root.value.rightChild is not None:
                    customQueue.enqueue(root.value.rightChild)


    def minValueNode(self,bstNode):
        current = bstNode
        while (current.leftChild is not None):
            current = current.leftChild
        return current


    def deleteNode(self,rootNode, nodeValue):
        if rootNode is None:
            return rootNode
        if nodeValue < rootNode.data:
            rootNode.leftChild = self.deleteNode(rootNode.leftChild, nodeValue)
        elif nodeValue > rootNode.data:
            rootNode.rightChild = self.deleteNode(rootNode.rightChild, nodeValue)
        else:
            if rootNode.leftChild is None:
                temp = rootNode.rightChild
                rootNode = None
                return temp
            
            if rootNode.rightChild is None:
                temp = rootNode.leftChild
                rootNode = None
                return temp
            
            temp = self.minValueNode(rootNode.rightChild)
            rootNode.data = temp.data 
            rootNode.rightChild = self.deleteNode(rootNode.rightChild, temp.data)
        return rootNode
    
    def deleteBST(self,rootNode):
        rootNode.data = None
        rootNode.leftChild = None
        rootNode.rightChild = None
        return "The BST has been successfully deleted"
if __name__ == '__main__':

    newBST = BSTNode(70)

    #newBST.value = 70
    newBST.leftChild = BSTNode(50)
    newBST.rightChild = BSTNode(90)

    print("Pre-Order Traversal")
    newBST.preOrderTraversal(newBST)

    print("In-Order Traversal")
    newBST.inOrderTraversal(newBST)

    print("Post-Order Traversal")
    newBST.postOrderTraversal(newBST)

    print("Level-Order Traversal")
    newBST.levelOrderTraversal(newBST)

    print("Insert into BST")
    print(newBST.insertBST(newBST,30))
    print(newBST.insertBST(newBST,60))
    print(newBST.insertBST(newBST,80))
    print(newBST.insertBST(newBST,100))
    print(newBST.insertBST(newBST,20))
    print(newBST.insertBST(newBST,40))
    print(newBST.insertBST(newBST,10))
    print(newBST.insertBST(newBST,95))

    print("Level-Order Traversal")
    newBST.levelOrderTraversal(newBST)

    print("Search Value")
    newBST.searchNode(newBST,10)

    print("Delete node")
    newBST.deleteNode(newBST,40)

    print("Level-Order Traversal")
    newBST.levelOrderTraversal(newBST)

    print("Delete BST")
    newBST.deleteBST(newBST)

    print("Level-Order Traversal")
    newBST.levelOrderTraversal(newBST)