#Python program for queue data structure with Linked List

#creating node class
class Node:
    def __init__(self,value = None):
        self.value = value
        self.next = None

    def __str__(self):
        return str(self.value)
    
#creating LinkedList class
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    def __iter__(self):
        current = self.head
        while current is not None:
            yield current
            current = current.next

#creating Queue class
class Queue:
    def __init__(self):
        self.LinkedList = LinkedList()

    def __str__(self):
        values = [str(x) for x in self.LinkedList]
        return ' '.join(values)
    
    def enqueue(self,value):
        newNode = Node(value)
        if self.LinkedList.head == None:
            self.LinkedList.head = newNode
            self.LinkedList.tail = newNode
        else:
            self.LinkedList.tail.next = newNode
            self.LinkedList.tail = newNode
    
    def isEmpty(self):

        if self.LinkedList.head == None:
            return True
        else:
            return False
        
    def dequeue(self):
        if self.isEmpty():
            return "There is no element to dequeue"
        else:
            current = self.LinkedList.head
            if self.LinkedList.head == self.LinkedList.tail:
                self.LinkedList.head = None
                self.LinkedList.tail = None
            else:
                self.LinkedList.head = self.LinkedList.head.next

            return current
        
    def peek(self):
        if self.isEmpty():
            return "There is no element in the queue"
        else:
            return self.LinkedList.head
        
    def delete(self):
        self.LinkedList.head = None
        self.LinkedList.tail = None


if __name__ == '__main__':

    customQueue = Queue()
    print("--Custom Queue has been created--")

    print("\n--Check if Queue is empty--", end= " ")
    print(customQueue.isEmpty())

    print("\n--Enqueue--",end=" ")
    customQueue.enqueue(10)
    customQueue.enqueue(20)
    print(customQueue)

    print("\n--Dequeue--", end=" ")
    print(customQueue.dequeue())

    print("\n--Check customQueue--", end=" ")
    print(customQueue)


    