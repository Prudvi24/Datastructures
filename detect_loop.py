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

# Detecting loop using Hash map
    
''' def detectloop(self):
        s=set()
        temp=self.head
        while temp:
            if temp in s:
                return 1
            else:
                s.add(temp)
                temp=temp.next
        return 0                    '''       
                
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
                return 1
            prev=prev.next
            succ=succ.next.next



ll = LinkedList()
ll.push(10)
ll.push(20)
ll.push(30)
ll.push(40)

ll.printlist()

ll.head.next.next.next.next=ll.head

m = ll.detectcycle()

if m==1:
    print "Found loop"
else:
    print "No loop"
