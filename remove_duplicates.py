class Node:

	def __init__(self,data):
		self.data=data
		self.next=None

class LinkedList:

	def __init__(self):
		self.head=None

	def append_node(self,new_data):
		new_node=Node(new_data)

		if self.head is None:
			self.head=new_node
			return 
		else:
			temp=self.head
			while temp.next:
				temp=temp.next
			temp.next=new_node

	def remove_duplicate(self):
		temp =self.head
		if temp is None:
			return 

		while temp.next:
			if temp.data == temp.next.data:
				prev=temp.next.next
				temp.next=prev
			else:
				temp=temp.next

	def printlist(self):
		current=self.head
		while current:
			print current.data
			current=current.next

ll = LinkedList()
ll.append_node(10)
ll.append_node(20)
ll.append_node(20)
ll.append_node(30)
ll.append_node(40)
ll.append_node(40)

ll.remove_duplicate()

ll.printlist()
