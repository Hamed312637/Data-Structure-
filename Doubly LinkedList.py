# -*- coding: utf-8 -*-
"""
Created on Fri Aug 11 18:59:11 2023

@author: hamed
"""
class Node:
    def __init__(self, data):
        self.prev = None
        self.data = data
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_at_start(self, data):
        new_node = Node(data)

        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    def insert_at_end(self, data):
        new_node = Node(data)

        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node

    def insert_at_position(self, pos, data):
        new_node = Node(data)

        if pos < 0 or pos > self.length():
            raise Exception('Enter a valid postion')
        else:
            if pos == 0:
                self.insert_at_start(data)
            elif pos == self.length()-1:
                self.insert_at_end(data)
            else:
                temp = self.head
                for _ in range(pos-1):
                    temp = temp.next
                new_node.next = temp.next
                temp.next = new_node
                new_node.prev = temp

    def delete_from_start(self):
        if self.head:
            if self.head is self.tail:
                data = self.head.data
                self.head = self.tail = None
            else:
                data = self.head.data
                self.head = self.head.next
                self.head.prev = None
            return data
        else:
            raise Exception('Empty linked list')

    def delete_from_end(self):
        if self.head:
            if self.head is self.tail:
                data = self.head.data
                self.head = self.tail = None
            else:
                data = self.tail.data
                self.tail = self.tail.prev
                self.tail.next = None
            return data
        else:
            raise Exception('Empty linked list')

    def delete_at_position(self, pos):
        if pos < 0 or pos >= self.length():
            raise Exception('Enter a valid postion')
        else:
            if pos == 0:
                return self.delete_from_start()
            elif pos == self.length()-1:
                return self.delete_from_end()
            else:
                temp = self.head
                for _ in range(pos):
                    temp = temp.next
                data = temp.data
                prev_node = temp.prev
                prev_node.next = temp.next
                temp.next.prev = prev_node
                return data

    def get_first(self):
        if self.head:
            return self.head.data
        else:
            raise Exception('Linked List is empty')

    def get_last(self):
        if self.tail:
            return self.tail.data
        else:
            raise Exception('Linked List is empty')

    def traverse(self):
        if self.head:
            temp = self.head
            while temp:
                print(temp.data)
                temp = temp.next
        else:
            print(None)

    def reverse_traverse(self):
        if self.tail:
            temp = self.tail
            while temp:
                print(temp.data)
                temp = temp.prev
        else:
            print(None)

    def length(self):
        temp = self.head
        count = 0
        while temp:
            count += 1
            temp = temp.next
        return count

dll = DoublyLinkedList()
dll.insert_at_end(1)
dll.insert_at_end(2)
dll.insert_at_end(3)
dll.insert_at_end(4)
dll.insert_at_end(5)
dll.insert_at_end(6)
dll.traverse()