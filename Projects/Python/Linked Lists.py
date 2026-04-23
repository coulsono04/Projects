
# Learning about Linked Lists


class Node:
    def __init__(self, data=None):
        self.data=data  # Stores last data point
        self.next=None  # Stores pointer to next node

class Linked_list:
    def __init__(self):
        self.head = Node() # always have head node available, not accessible, just a placeholder to point to 1st element in list

    def append(self, data):   # To add a new node?
        new_node = Node(data)  # Creates the new node as an object
        currently_looking_at = self.head # start at left most point of list
        while currently_looking_at.next != None:      # While the next of currently looking at is not none (the end)
            currently_looking_at = currently_looking_at.next
        currently_looking_at.next = new_node

    def length(self):
        currently_looking_at = self.head
        total = 0  # conatins total number of nodes seen
        while currently_looking_at.next!=None:  # iterate until the end
            total+=1   # incremendting total
            currently_looking_at = currently_looking_at.next  # traverses to the next node
        return total   # a return of this total
    
    def display(self):
        elements_seen = []
        currently_looking_at = self.head
        while currently_looking_at.next != None:  #While the current element of the node is NOT equal to 1
            currently_looking_at=currently_looking_at.next
            elements_seen.append(currently_looking_at.data)  # Append data of current node to list of the elements we've seen
        print(elements_seen)

    def get(self, index):     # extractor function to pull out datapoint from an index
        if index>=self.length():   # To make sure index is in the length/range
            print("Error: get index out of range")
            return None
        current_index = 0
        currently_looking_at = self.head
        while True:
            currently_looking_at=currently_looking_at.next  # Moves to the next
            if current_index==index:  # If the current index is the same as the one provided by the user
                return currently_looking_at.data
            current_index+=1   # Incrementing
    
    def erase(self,index):
        if index >=self.length():
            print("error, out of range")
            return
        current_index = 0
        currently_looking_at = self.head
        while True:
            last_node = currently_looking_at # when we earse a node, have to do to point properly
            currently_looking_at = currently_looking_at.next
            if current_index==index:
                last_node.next = currently_looking_at.next
                return
            current_index += 1




my_list = Linked_list()

my_list.display()

my_list.append(1) # added in elements, OUR made function
my_list.append(2)

my_list.display()

print("Element at 2nd index:")   # Finds the element at the 1st index (2)
print(my_list.get(1))

my_list.erase(1)  # runs the erase function and removes it
my_list.display()