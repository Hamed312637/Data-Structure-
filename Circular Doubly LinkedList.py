# -*- coding: utf-8 -*-
"""
Created on Fri Aug 11 19:04:25 2023

@author: hamed
"""
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class circular_doubly_list:
    def __init__(self):
        self.head = None
        self.end = None
    def is_empty(self):
        return self.head is None
    def insert_at_first(self, data):
        new_node = Node(data)
        if self.is_empty():
            self.head = new_node
            self.end = new_node
            new_node.next = new_node
            new_node.prev = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
            new_node.prev = self.end
            self.end.next = new_node
            
    def insert_at_position(self, pos, data):
        new_node = Node(data)

        if pos < 0 or pos > self.get_length():
            raise Exception('Enter a valid postion')
        else:
            if pos == 0:
                self.insert_at_start(data)
            elif pos == self.get_length()-1:
                self.insert_at_end(data)
            else:
                temp = self.head
                for _ in range(pos-1):
                    temp = temp.next
                new_node.next = temp.next
                temp.next = new_node
                new_node.prev = temp
    
    
    def insert_at_last(self, data):
        new_node = Node(data)
        if self.is_empty():
            self.insert_at_first()
        else:
            new_node.prev = self.head
            self.end.next = new_node
            self.end = new_node
            new_node.next = self.head
            self.head.prev = new_node
    def delete_from_first(self):
        if self.is_empty():
            return
        if self.head == self.end:
            self.head = self.end = None
        else:
            self.head = self.head.next
            self.head.prev = self.end
            self.end.next = self.head
            
    def delete_at_position(self, pos):
        if pos < 0 or pos >= self.get_length():
            raise Exception('Enter a valid postion')
        else:
            if pos == 0:
                return self.delete_from_first()
            elif pos == self.get_length()-1:
                return self.delete_from_last()
            else:
                temp = self.head
                for _ in range(pos):
                    temp = temp.next
                data = temp.data
                prev_node = temp.prev
                prev_node.next = temp.next
                temp= prev_node
                return data

        
    def delete_from_last(self):
        if self.is_empty():
           return

        if self.head == self.end:
           self.delete_from_first()
        else:
         current = self.head
         previous = self.head
         while current.next != self.head:
             previous = current
             current = current.next
         previous.next = self.head
         self.head.prev = previous
         self.end = previous
         
         return current.data
    def get_length(self):
        count = 1
        temp = self.head
        while temp.next != self.head:
            temp = temp.next 
            count +=1
            
        return count
   
    
    
    
    def print_list(self):
        if self.is_empty():
           print("The list is empty.")
           return       
        temp = self.head
        print('The list is')
        while temp != None:
            print(temp.data)
            temp = temp.next
            if temp == self.head:
                break
            
            
cdl = circular_doubly_list()
cdl.insert_at_first(3)
cdl.insert_at_first(2)
cdl.insert_at_first(1)
cdl.insert_at_last(7)
cdl.insert_at_last(8)
cdl.insert_at_position(3, 4)
cdl.insert_at_position(4, 5)
cdl.insert_at_position(5, 6)
cdl.delete_from_first()
cdl.delete_from_last()
cdl.delete_from_last()
cdl.insert_at_last(10)
cdl.delete_at_position(2)
cdl.print_list()
print('length is ', cdl.get_length())  