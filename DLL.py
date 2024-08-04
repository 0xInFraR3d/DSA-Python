"""
**Doubly Linked List**
"""
class Node:
    def __init__(self, prev=None, item=None, next=None):
        # Initialize a Node with previous node pointer, item value, and next node pointer
        # prev: Reference to the previous node in the list
        # item: The data value stored in this node
        # next: Reference to the next node in the list
        self.prev = prev
        self.item = item
        self.next = next

class DLL:
    def __init__(self):
        # Initialize the doubly linked list with a start node, which initially is None
        # start: Reference to the first node in the list
        self.start = None

    def is_empty(self):
        # Check if the list is empty by checking if the start node is None
        return self.start is None

    def insert_at_start(self, data):
        # Create a new node with the given data and set its next pointer to the current start node
        n = Node(None, data, self.start)
        if not self.is_empty():
            # If the list is not empty, update the previous pointer of the current start node
            # to point back to the new node
            self.start.prev = n
        # Update the start node to be the new node, effectively inserting it at the beginning
        self.start = n

    def insert_at_last(self, data):
        # Initialize a temporary pointer to traverse the list starting from the start node
        temp = self.start
        if self.start is not None:
            # Traverse to the last node in the list
            while temp.next is not None:
                temp = temp.next
        # Create a new node with the given data, previous pointer as the last node, and next as None
        n = Node(temp, data, None)
        if temp is None:
            # If the list was empty, set the new node as the start node
            self.start = n
        else:
            # Otherwise, update the next pointer of the last node to point to the new node
            temp.next = n

    def search(self, data):
        # Initialize a temporary pointer to traverse the list
        temp = self.start
        # Traverse the list until the end
        while temp is not None:
            # If the current node's item matches the search data, return the node
            if temp.item == data:
                return temp
            # Move to the next node
            temp = temp.next
        # If the data is not found, return None
        return None

    def insert_after(self, temp, data):
        # If the given node (temp) is not None, proceed with insertion
        if temp is not None:
            # Create a new node with the given data, previous pointer as temp, and next as temp's next
            n = Node(temp, data, temp.next)
            # If temp's next is not None, update the previous pointer of the next node to point to the new node
            if temp.next is not None:
                temp.next.prev = n
            # Update temp's next pointer to point to the new node
            temp.next = n

    def print_list(self):
        # Initialize a temporary pointer to traverse the list
        temp = self.start
        # Traverse the list until the end
        while temp is not None:
            # Print the current node's item followed by a space
            print(temp.item, end=' ')
            # Move to the next node
            temp = temp.next
        # Print a newline character after the list is printed
        print()

    def delete_first(self):
        # Check if the list is not empty
        if self.start is not None:
            # Update the start node to the next node
            self.start = self.start.next
            # If the list is not empty after deletion, update the new start's previous pointer to None
            if self.start is not None:
                self.start.prev = None

    def delete_last(self):
        # Check if the list is empty
        if self.start is None:
            return
        # If there's only one node, set start to None, effectively deleting the only node
        if self.start.next is None:
            self.start = None
        else:
            # Traverse to the last node
            temp = self.start
            while temp.next is not None:
                temp = temp.next
            # Update the previous node's next pointer to None, effectively removing the last node
            temp.prev.next = None

    def delete_item(self, data):
        # Check if the list is empty
        if self.start is None:
            return
        # Initialize a temporary pointer to traverse the list
        temp = self.start
        # Traverse the list to find the node with the given data
        while temp is not None:
            # If the current node's item matches the data
            if temp.item == data:
                # If the node to be deleted is not the first node, update the previous node's next pointer
                if temp.prev is not None:
                    temp.prev.next = temp.next
                # If the node to be deleted is not the last node, update the next node's previous pointer
                if temp.next is not None:
                    temp.next.prev = temp.prev
                # If the node to be deleted is the start node, update the start node
                if temp == self.start:
                    self.start = temp.next
                break
            # Move to the next node
            temp = temp.next

    def __iter__(self):
        # Return an iterator object for the doubly linked list
        return self.DLLIterator(self.start)

    class DLLIterator:
        def __init__(self, start):
            # Initialize the iterator with the current node set to the start node
            self.current = start

        def __iter__(self):
            # Return the iterator object itself
            return self

        def __next__(self):
            # If the current node is None, raise StopIteration to end iteration
            if not self.current:
                raise StopIteration
            # Store the data of the current node
            data = self.current.item
            # Move to the next node
            self.current = self.current.next
            # Return the stored data
            return data
