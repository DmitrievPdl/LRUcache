# A linked list node 
class Node: 
  
    # Constructor to create a new node 
    def __init__(self, key, value): 
        self.key = key
        self.value = value
        self.next = None
        self.prev = None

    def __repr__(self):
        return 'Node [%s, %s]' % (str(self.key), str(self.value))
  
# Class to create a Doubly Linked List 
class DoublyLinkedList: 
  
    # Constructor for empty Doubly Linked List 
    def __init__(self, capacity: int=10):
        self.len = 0
        self.capacity = capacity

        self.head = Node(0, 0)
        self.tail = Node(0, 0)

        self.tail.prev = self.head
        self.tail.next = None
        self.head.next = self.tail
        self.head.prev = None
    
    # Adds new node to the beginning
    def push(self, new_node):
        if self.len == 0:
            self.head.next = new_node
            new_node.prev = self.head
            new_node.next = self.tail
            self.tail.prev = new_node

            self.len += 1

        elif self.len < self.capacity:
            old_first = self.head.next

            self.head.next = new_node
            new_node.prev = self.head
            new_node.next = old_first
            old_first.prev = new_node

            self.len += 1

        else:
            old_first = self.head.next

            self.head.next = new_node
            new_node.prev = self.head
            new_node.next = old_first
            old_first.prev = new_node

            old_last = self.tail.prev

            self.tail.prev = old_last.prev
            old_last.prev.next = self.tail
            old_last.next = None
            old_last.prev =None

    def remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

        self.len -= 1

    def print_list(self): 
        printval = self.head.next
        string = ''
        for i in range(self.len):
            string += ' %s : %s ,' % (printval.key, printval.value)
            printval = printval.next
        return '{ ' + string + ' }' 


class LRUCache:

    def __init__(self, capacity: int=10) -> None:
        self.capacity = capacity
        self.hash_table = {}
        self.linked_list = DoublyLinkedList(capacity)

    def set(self, key: str, value: str) -> None:
        new_node = Node(key, value)
        if key not in self.hash_table.keys():
            if len(self.hash_table) < self.capacity:
                self.hash_table[key] = new_node
                self.linked_list.push(new_node)
            elif len(self.hash_table) == self.capacity:
                # remove last
                last_node = self.hash_table.pop(self.linked_list.tail.prev.key)
                self.linked_list.remove(last_node)

                # at new node
                self.hash_table[key] = new_node
                self.linked_list.push(new_node)
            else:
                pass
        else:
            old_node = self.hash_table.pop(key)
            self.linked_list.remove(old_node)
            self.linked_list.push(new_node)

            self.hash_table[key] = new_node

    def get(self, key):
        if key in self.hash_table.keys():
            value = self.hash_table[key].value
            new_node = Node(key, value)
            self.linked_list.remove(self.hash_table[key])
            self.linked_list.push(new_node)
            return value
        return '' 

    def delete(self, key: str) -> None:
        deleted_node = self.hash_table.pop(key)
        self.linked_list.remove(deleted_node)
    
    def __str__(self):
        return self.linked_list.print_list()
