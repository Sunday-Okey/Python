class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    # create new Node
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1
    
    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next
            
    # create new Node
    # add node to end
    def append(self, value):
        new_node = Node(value)
        if self.head is None:
             self.tail = new_node
             self.head = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
        return True
    
            
    
    #create new node
    # add node to the beginning
    def prepend(self, value):
        
    
    # create new node
    # insert node
    def insert(self, index, value):
        pass
    
node = {
    "value": 4,
    "next": None
}
    
    
my_linked_list = LinkedList(4)
print(my_linked_list.head.value)