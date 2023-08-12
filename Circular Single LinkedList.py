# -*- coding: utf-8 -*-
"""
Created on Fri Aug 11 19:02:14 2023

@author: hamed
"""
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
class circularlinkedlist:
   def __init__(self):
       self.head = None
       self.end = None
   def insert_at_begin(self, data):
       new_node = Node(data)
       if self.head == None:
          
           self.head = new_node
           
           self.end = new_node
           
       else:
           new_node.next = self.head
           self.head = new_node
           self.end.next=self.head
           
   def insert_at_end(self, data):
       new_node = Node(data)
       if self.head == None:
                  
          self.head = new_node
                   
          self.end = new_node
                   
       else:
          new_node.next = self.head
          self.end.next = new_node
          self.end=new_node
           
   
   def insert_at_position(self, pos, data):
        if pos < 0 or pos >= self.length():
            raise 'Enter a valid postion'
        else:
            if pos == 0:
                self.insert_at_start(data)
            elif pos == self.length()-1:
                self.insert_at_end(data)
            else:
                temp = self.head
                for _ in range(pos-1):
                    temp = temp.next
                new_node = Node(data)
                new_node.next = temp.next
                temp.next = new_node
  
   
   
   def delete_from_start(self):
      if self.head:
        data = self.head.data
        self.head = self.head.next
        self.end.next = self.head
        return data
      else:
        raise Exception('Empty linked list')    
        
   def delete_from_end(self):
    if self.head:
        current = self.head
        previous = self.head
        while current.next != self.head:
            previous = current
            current = current.next
        previous.next = self.head
        current.next = None
        return current.data
    else:
        raise Exception('Empty linked list')     
   
   def delete_at_position(self, pos):
    current = self.head
    previous = self.head

    if pos < 0 or pos >= self.length():
        raise 'Enter a valid postion'
    else:
        if pos == 0:
            return self.delete_from_start()
        elif pos == self.length()-1:
            return self.delete_from_end()
        else:
            for _ in range(pos):
                previous = current
                current = current.next
            data = current.data
            previous.next = current.next
            return data 
   
   def length(self):
        count = 1
        temp = self.head
        while temp.next != self.head:
            temp = temp.next
            count += 1
            
        return count  
   def printlist(self):
       if self.head == None:
           print('list is emptey')
       else:
           temp = self.head
           while temp != None:
               print(temp.data)
               temp = temp.next
               if temp == self.head:
                   break
cll = circularlinkedlist()
cll.insert_at_begin(5) 
cll.insert_at_begin(4)
cll.insert_at_begin(3)
cll.insert_at_end(6)
cll.insert_at_end(7)
cll.insert_at_end(8)
cll.insert_at_position(2, 2)
cll.insert_at_position(4, 10)
cll.delete_from_start()
cll.delete_from_end()
cll.delete_at_position(3)
cll.printlist()
print('length list ',cll.length())              