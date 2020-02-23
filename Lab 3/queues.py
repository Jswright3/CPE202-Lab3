"""
LAB3
John Wright
CPE202

"""
from array_list import ArrayList

class QueueArray:
    """Queue based on ArrayList
    Attributes:
        capacity (int): capacity of Queue
        front (int): pointer to first value of queue
        rear (int): pointer to last value in queue
        items (ArrayList): arraylist
    """
    def __init__(self, capacity):
        #the maximum number of items that can be stored in queue
        self.capacity = capacity
        self.front = 0 #pointer to the front of queue
        self.rear = 0 #pointer to the rear of queue
        self.items = ArrayList(capacity) #array whose size is the capacity
        self.num_items = 0 #number of items in array

    def is_empty(self):
        """
        Returns:
             (bool): whether queue is empty or not
        """
        if self.num_items == 0:
            return True
        return False

    def is_full(self):
        """
        Returns:
             (bool): whether queue is full or not
        """
        if self.num_items == self.capacity:
            return True
        return False

    def enqueue(self, item):
        """enqueues a value onto the arr
        """
        if self.capacity == self.num_items:
            raise IndexError
        self.items.arr[self.rear % self.capacity] = item
        self.rear += 1
        self.num_items += 1

    def dequeue(self):
        """dequeue first value in queue
        Returns:
             (int): value dequeued
        """
        if self.num_items == 0:
            raise IndexError
        temp = self.items.arr[self.front % self.capacity]
        self.front += 1
        self.num_items -= 1
        return temp

    def size(self):
        """
        Returns:
        the number of items in the queue
        """
        return self.num_items

#You must have the same functionalities for the Linked List Implementation

class Node:
    """Linked List is one of None or Node
    Attributes:
    val (int): an item in the list
    next (Node): a link to the next item in the list (Linked List)
    """
    def __init__(self, val, nxt=None):
        self.val = val
        self.next = nxt

    def __repr__(self):
        return "Node({},{})".format(self.val, self.next)

    def __eq__(self, other):
        if other is None:
            return False
        if isinstance(other, Node) is False:
            return False
        if other.val == self.val and other.next == self.next:
            return True
        return False

class QueueLinked:
    """Queue Class built on linked list
    Attributes:
    capacity (int): max capacity
    front (Node): Pointer to first Node in Queue
    rear (Node): Pointer to last Node in Queue
    num_items (int): number of items in linked list
    """
    def __init__(self, capacity):
        #the maximum number of items that can be stored in queue
        self.capacity = capacity
        self.front = None #pointer to the front of queue
        self.rear = None #pointer to the rear of queue
        self.num_items = 0 #number of items in array

    def is_empty(self):
        """returns bool if queue is empty
        Returns:
            (bool): if queue is empty
        """
        if self.num_items == 0:
            return True
        return False

    def is_full(self):
        """returns bool if queue is full
        Returns:
            (bool): if queue is full
        """
        if self.num_items == self.capacity:
            return True
        return False

    def enqueue(self, item):
        """enqueues a new Node item
        """
        if self.num_items == self.capacity:
            raise IndexError
        if self.rear is None:
            self.front = Node(item)
            self.rear = self.front
        else:
            self.rear.next = Node(item)
            self.rear = self.rear.next
        self.num_items += 1

    def dequeue(self):
        """dequeues a Node item from the front of the queue
        Returns:
            (int): value dequeued from list
        """
        if self.front is None:
            raise IndexError
        temp = self.front.val
        self.front = self.front.next
        self.num_items -= 1
        return temp

    def size(self):
        """returns the number of items in the queue
        returns:
            (int): size of Queue
        """
        return self.num_items
