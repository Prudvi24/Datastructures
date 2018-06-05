class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        
class LinkedList:
    def __init__(self):
        self.head=None
        
    def push(self,new_data):
        new_node=Node(new_data)
        new_node.next=self.head
        self.head=new_node
        
    def deleteNode(self,key):
        temp=self.head

        if temp is not None:
            if temp.data==key:
                self.head=temp.next
                temp=None
                return
        
        while temp is not None:
            if temp.data==key:
                break
            prev = temp
            temp = temp.next

        if temp==None:
            return
        if temp is not None:
            prev.next=temp.next
            temp=None
            
    def printList(self):
        temp=self.head
        while(temp):
            print temp.data
            temp=temp.next


lis = LinkedList()
lis.push(7)
lis.push(1)
lis.push(3)
lis.push(2)
lis.deleteNode(1)
lis.printList()










            
