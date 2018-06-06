class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class LinkedList:
    def __init__(self):
        self.head=None

    def push(self,new_data):
        new_node = Node(new_data)
        if self.head == None:
            self.head=new_node
            return
        temp=self.head
        while temp.next:
            temp=temp.next
        temp.next=new_node

    def printlist(self):
        temp=self.head
        while temp:
            print temp.data
            temp=temp.next

# detecting loop using flyod cycle
    def detectcycle(self):
        prev =self.head
        succ =self.head
        while prev and succ and succ.next:
            if prev==succ:
                return self.countnodes(prev)
            prev=prev.next
            succ=succ.next.next

    def countnodes(self,node):
        temp=node
        res=1
        while temp.next != node:
            res=res+1
            temp =temp.next
        return res



ll = LinkedList()
ll.push(10)
ll.push(20)
ll.push(30)
ll.push(40)

ll.printlist()

ll.head.next.next.next.next=ll.head

m = ll.detectcycle()

print ("loop length is %d" %(m))
    
