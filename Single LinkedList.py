# -*- coding: utf-8 -*-
"""
Created on Fri Aug 11 18:56:35 2023

@author: hamed
"""
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
        
class LinkedList:
    def __init__(self):
        self.head = None
    
    def insert_at_start(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
        
    def inser_at_end(self, data):
       new_node = Node(data)
       if self.head :
           temp = self.head
           while temp.next:
               temp = temp.next
           temp.next = new_node
       else:
           self.head = new_node
    
    def insert_in_position(self, pos, data):        
       if pos < 0 or pos >= self.length():
           raise Exception('Enter a valid')
       else:
           if pos == 0:
               self.insert_at_start(data)
               
           elif pos == self.length()-1:
               self.inser_at_end(data)
           else:
               temp = self.head
               for i in range(pos-1):
                   temp = temp.next
               new_node = Node(data)
               new_node.next = temp.next
               temp.next = new_node
               
    def delete_from_start(self):
        if self.head:
            data = self.head.data
            self.head = self.head.next
            return data
        else:
            raise Exception('LinkedList is Empty')
    def delete_from_end(self):
        if self.head:
            current = self.head
            previous = self.head
            while current.next != None:
                previous = current
                current = current.next
            previous.next = None
            return current.data
    def delete_from_position(self, pos):
        current = self.head
        previous = self.head
        if pos < 0 or pos >= self.length():
            raise Exception(' Enter a vaild position')
        else:
           if pos == 0:
               self.delete_from_start()
           elif pos == self.length()-1:
               self.delete_from_end()
           else:
               for i in range(pos):
                   previous = current
                   current = current.next
               data = current.data
               previous.next = current.next
               return data
    def get_first(self):
        if self.head:
            return self.head.data
        else:
            raise Exception(' LinkedList is Empty')
    def get_last(self):
        if self.head:
            current = self.head
            while current.next != None:
                current = current.next
            return current.data
        else:
            raise Exception(' LinkedList is Empty') 
            
    def get_position(self, pos):        
        if pos < 0 or pos >= self.length():
            raise Exception('Enter a vaild position ')
        current = self.head
        for _ in range(pos):
            current = current.next
        return current.data
                
    def traverse(self):
       if self.head:
          temp = self.head

          while temp is not None:
               print(temp.data)
               temp = temp.next
       else:
           print(None)
    def length(self):
        count = 0
        temp = self.head
        while temp:
            temp = temp.next
            count += 1
        return count
        
ll = LinkedList()
ll.insert_at_start(1)
ll.insert_at_start(2)
ll.insert_at_start(3)
ll.insert_at_start(4)
ll.inser_at_end(5)
ll.inser_at_end(6)
ll.inser_at_end(7)
ll.inser_at_end(8)
ll.insert_in_position(2, 10)
ll.delete_from_position(2)
ll.delete_from_start()
ll.delete_from_end()
print(ll.get_first())