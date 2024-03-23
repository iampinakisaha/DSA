#Binary Tree Module with Linked List

#Importing Queue module from DSA/Qeueu/ directory

#import sys
#sys.path.append('C:\\Users\\pinak\\DSA')
#from Queue.QueueLinkedList import Queue


from Queue.QueueLinkedList import Queue

#Creating Tree class
class TreeNode:
    def __init__(self,data):
        self.data = data
        self.leftChild = None
        self.rightChild = None

    #preorder traversal
    def preOrderTraversal(self,rootNode):
        if not rootNode:
            return
        print(rootNode.data)
        self.preOrderTraversal(rootNode.leftChild)
        self.preOrderTraversal(rootNode.rightChild)

    #inorder traversal
    def inOrderTraversal(self,rootNode):
        if not rootNode:
            return
        self.preOrderTraversal(rootNode.leftChild)
        print(rootNode.data)
        self.preOrderTraversal(rootNode.rightChild)

    #postorder traversal
    def postOrderTraversal(self,rootNode):
        if not rootNode:
            return
        self.preOrderTraversal(rootNode.leftChild)
        self.preOrderTraversal(rootNode.rightChild)
        print(rootNode.data)
    
    #level order traversal
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

    #search for a value
    def searchBT(self,rootNode,target):
        if not rootNode:
            return
        else:
            customQueue = Queue()
            customQueue.enqueue(rootNode)
            while not customQueue.isEmpty():
                root = customQueue.dequeue()
                if root.value.data == target:
                    return "Success"
                if root.value.leftChild is not None:
                    customQueue.enqueue(root.value.leftChild)
                if root.value.rightChild is not None:
                    customQueue.enqueue(root.value.rightChild)
        return "Not Found"

    #Insert a New Node Into Binary Tree
    def insertNodeBT(self,rootNode,value):
        newNode = TreeNode(value)
        if not rootNode:
            self.rootNode = newNode
        else:
            customQueue = Queue()
            customQueue.enqueue(rootNode)
            while not customQueue.isEmpty():
                root = customQueue.dequeue()
                if root.value.leftChild is not None:
                    customQueue.enqueue(root.value.leftChild)
                else:
                    root.value.leftChild = newNode
                    break
                if root.value.rightChild is not None:
                    customQueue.enqueue(root.value.rightChild)
                else:
                    root.value.rightChild = newNode
                    break
        return "Successfully inserted new Node"
    
    #Delete a Node from Binary Tree
    def deepestNodeBT(self,rootNode):
        if not rootNode:
            return 
        else:
            customQueue = Queue()
            customQueue.enqueue(rootNode)
            while not customQueue.isEmpty():
                root = customQueue.dequeue()
                #print(root.value.data)
                if root.value.leftChild is not None:
                    customQueue.enqueue(root.value.leftChild)
                if root.value.rightChild is not None:
                    customQueue.enqueue(root.value.rightChild)
        return root.value
    
    def deleteDepeestNodeBT(self,rootNode,target):
        if not rootNode:
            #print("Binary tree not found")
            return 
        else:
            customQueue = Queue()
            customQueue.enqueue(rootNode)
            while not customQueue.isEmpty():
                root = customQueue.dequeue()
                if root.value is target:
                    root.value = None
                    #print("node deleted")
                    return
                if root.value.rightChild:
                    if root.value.rightChild is target:
                        root.value.rightChild = None
                        #print("node deleted")
                        return
                    else:
                        customQueue.enqueue(root.value.rightChild)
                if root.value.leftChild:
                    if root.value.leftChild is target:
                        root.value.leftChild = None
                        #print("node deleted")
                        return
                    else:
                        customQueue.enqueue(root.value.leftChild)

    def deleteNodeBT(self,rootNode,target):
        if not rootNode:
            return "The BT does not exist"
        else:
            customQueue = Queue()
            customQueue.enqueue(rootNode)
            while not customQueue.isEmpty():
                root = customQueue.dequeue()
                if root.value.data == target:
                    dNode = self.deepestNodeBT(rootNode)
                    root.value.data = dNode.data
                    self.deleteDepeestNodeBT(rootNode, dNode)
                    return "The node has been successfully deleted"
                if (root.value.leftChild is not None):
                    customQueue.enqueue(root.value.leftChild)
            
                if (root.value.rightChild is not None):
                    customQueue.enqueue(root.value.rightChild)
        return "Failed to delete"

    def delete(self,rootNode):
        rootNode.data = None
        rootNode.leftChild = None
        rootNode.rightChild = None
        return "The binary tree has been successfully deleted"

            
if __name__ == '__main__':

    newBT = TreeNode("Drinks")

    hot = TreeNode("Hot")
    cold = TreeNode("cold")
    newBT.leftChild = hot
    newBT.rightChild = cold

    coffee = TreeNode("Coffee")
    tea = TreeNode("Tea")
    hot.leftChild = coffee
    hot.rightChild = tea

    print("\n--Pre-Order Traversal--")
    newBT.preOrderTraversal(newBT)

    print("\n--In-Order Traversal--")
    newBT.inOrderTraversal(newBT)
    
    print("\n--Post-Order Traversal--")
    newBT.postOrderTraversal(newBT)
    
    print("\n--Level-Order Traversal--")
    newBT.levelOrderTraversal(newBT)

    print("\n--Search for a value--")
    print(newBT.searchBT(newBT,"Cola"))

    print("\n--Insert a new node--")
    print(newBT.insertNodeBT(newBT,"Cola"))

    print("\n--Level-Order Traversal--")
    newBT.levelOrderTraversal(newBT)

    """
    print("\n--deepest Node Check--")
    print(newBT.deepestNodeBT(newBT).data)

    print("\n--delete deepest Node check--")
    target = newBT.deepestNodeBT(newBT)
    newBT.deleteDepeestNodeBT(newBT,target)
    newBT.levelOrderTraversal(newBT)
    """
    print("\n--Binary tree after deleting a node--")
    newBT.deleteNodeBT(newBT,"Coffee")
    newBT.levelOrderTraversal(newBT)

    print("\n--Binary tree after deleting check--")
    print(newBT.delete(newBT))
    newBT.levelOrderTraversal(newBT)