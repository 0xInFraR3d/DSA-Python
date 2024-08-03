"""
A module implementing a singly linked list and an iterator for it.
"""

class Node:
    """ 
    A class representing a node in a singly linked list.
    
    Attributes:
        item: The data stored in the node.
        next: A reference to the next node in the list.
    """
    def __init__(self, item=None, next=None):
        """ Initialize a new node with optional data and next node reference. """
        self.item = item
        self.next = next

class SLL:
    """ 
    A class representing a singly linked list.
    
    Attributes:
        start: The starting node of the list.
    """
    def __init__(self, start=None):
        """ Initialize the linked list with an optional starting node. """
        self.start = start

    def is_empty(self):
        """ Check if the linked list is empty. """
        return self.start is None

    def insert_at_start(self, data):
        """ 
        Insert a new node with the given data at the beginning of the list.
        
        Args:
            data: The data to be stored in the new node.
        """
        n = Node(data, self.start)
        self.start = n
    
    def insert_at_last(self, data):
        """ 
        Insert a new node with the given data at the end of the list.
        
        Args:
            data: The data to be stored in the new node.
        """
        n = Node(data)

        if not self.is_empty():
            # Traverse to the last node
            temp = self.start
            while temp.next is not None:
                temp = temp.next
            temp.next = n
        else:
            # If the list is empty, set the new node as the start
            self.start = n

    def search(self, data):
        """ 
        Search for a node containing the specified data.
        
        Args:
            data: The data to be searched for in the list.
        
        Returns:
            The node containing the data, or None if not found.
        """
        temp = self.start
        while temp is not None:
            if temp.item == data:
                return temp
            temp = temp.next
        return None

    def insert_after(self, temp, data):
        """ 
        Insert a new node with the given data after a specified node.
        
        Args:
            temp: The node after which the new node should be inserted.
            data: The data to be stored in the new node.
        """
        if temp is not None:
            n = Node(data, temp.next)
            temp.next = n

    def print_list(self):
        """ Print all items in the list. """
        temp = self.start
        while temp is not None:
            print(temp.item, end=" ")
            temp = temp.next

    def delete_first(self):
        """ Delete the first node of the list. """
        if self.start is not None:
            self.start = self.start.next

    def delete_last(self):
        """ Delete the last node of the list. """
        if self.start is None:
            pass
        elif self.start.next is None:
            # If there's only one node, set start to None
            self.start = None
        else:
            # Traverse to the second last node
            temp = self.start
            while temp.next.next is not None:
                temp = temp.next
            temp.next = None

    def delete_item(self, data):
        """ 
        Delete the first node containing the specified data.
        
        Args:
            data: The data to be deleted from the list.
        """
        if self.start is None:
            pass
        elif self.start.next is None:
            # If there's only one node, check if it's the target
            if self.start.item == data:
                self.start = None
        else:
            # Traverse the list to find the target node
            temp = self.start
            if temp.item == data:
                self.start = temp.next
            else:
                while temp.next is not None:
                    if temp.next.item == data:
                        temp.next = temp.next.next
                        break
                    temp = temp.next

    def __iter__(self):
        """ Return an iterator for the list. """
        return SLLIterator(self.start)

class SLLIterator:
    """ 
    An iterator for the singly linked list.
    
    Attributes:
        current: The current node being iterated over.
    """
    def __init__(self, start):
        """ Initialize the iterator with the starting node. """
        self.current = start

    def __iter__(self):
        """ Return the iterator object itself. """
        return self
    
    def __next__(self):
        """ 
        Return the next item in the list.
        
        Raises:
            StopIteration: If there are no more items to iterate over.
        
        Returns:
            The data of the current node.
        """
        if not self.current:
            raise StopIteration
        data = self.current.item
        self.current = self.current.next
        return data
