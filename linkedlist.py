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
    def print_list(self):
        temp=self.head
        nodes=[]
        while temp:
            nodes.append(str(temp.data))
            temp=temp.next
        print("->".join(nodes))

    def 


