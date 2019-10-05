# -*- coding: utf-8 -*-
#"""
# COURSE: CS 2302 Data Structures
# AUTHOR: Elisa Jimenez Todd
# ASSIGNMENT: Lab 3: Sorted Linked Lists
# INSTRUCTOR: Olac Fuentes
# TA: Anindita Nath
# =============================================================================
# DATE: 10/04/2019
# =============================================================================
# 
# Program description: This program manages and creates sorted lists in 
# ascending order. The functions implented are: 
# 1)Print: prints the list in order
# 2)Insert: inserts a new node on the correct position
# 3)Delete: deletes an element from the list
# 4)Merge: merges two lists into the first
# 5)IndexOf: returns the index(position) of an element in the list
# 6)Clear: deletes all elements from the list
# 7)Min: returns smallest element
# 8)Max: returns largest element
# 9)HasDuplicate: Returns true or false if there are duplicate numbers
# 10)Select: returns kth smallest element on a list
#"""
import math
import random

class Node(object):
    # Constructor
    def __init__(self, data, next=None):  
        self.data = data
        self.next = next 
        
#List Functions
class SortedList(object):   
    # Constructor
    def __init__(self): 
        self.head = None
        self.tail = None

    def Print(self):
        # Prints list's items in order
        temp = self.head
        while temp is not None:
            print(temp.data, end=' ')
            temp = temp.next
        print()  # New line

    def Insert(self, i):
        #if list is empty
        if self.head == None:
            self.head = Node(i)
            self.tail = self.head
        #look for i's position
        else:
            currNode=self.head
            #if i is smaller than head, puts node as head
            if i<=currNode.data:
                self.head = Node(i)
                self.head.next = currNode
            #if i is larger than the elements at the list
            elif i>=self.tail.data:
                self.tail.next = Node(i)
                self.tail = self.tail.next
            #if i is larger than head looks for position
            else:
                while i>currNode.next.data:
                    currNode = currNode.next
                tempNode = currNode.next    #inserts the node
                currNode.next = Node(i)
                currNode.next.next = tempNode
                    
    def Delete(self,i):
        #if list is empty
        if self.head != None:
            #looks for i
            currNode = self.head
            if currNode.data == i:      #if i is head
                self.head = currNode.next
                return
            while currNode.next.data != i:  #look for position of i
                currNode = currNode.next 
                if currNode.next == None:
                    return
            if currNode.next.next == None:  #removes last node
                self.tail = currNode
                self.tail.next = None
            else:                           #removes node inside
                currNode.next = currNode.next.next
                
    def Merge(self,M):
        if self.head == None:   #makes M the list
            self.head = M.head
            self.tail = M.tail
        #if self has something to add
        elif M.head != None:    
            selfNode = self.head
            newNode = M.head
            #add before the start
            if newNode.data < selfNode.data:
                #removes node from M
                M.head = newNode.next
                #append before
                newNode.next = selfNode
                self.head = newNode
                newNode = M.head
            #reset
            selfNode = self.head
            newNode = M.head
            #merges
            while selfNode.next != None and newNode != None:
                #find position to merge M
                if newNode.data >= selfNode.data and newNode.data < selfNode.next.data:
                    #removes node from M
                    M.head = newNode.next
                    #inserts node of M to self
                    selfNode.next, newNode.next = newNode, selfNode.next
                #next values
                selfNode=selfNode.next
                newNode = M.head
            #adds rest of list if any
            if newNode != None:
                self.tail.next = newNode
                self.tail = M.tail
                
    def IndexOf(self,i):
        #i would not be on list if smaller than first element or larger than last
        if self.head == None or i> self.tail.data or i < self.head.data:
            return -1
        counter = 0 #index 
        currNode = self.head
        while currNode.data < i :   #iterate
            currNode = currNode.next
            counter += 1
            if currNode.data > i:   #does not have to traverse all list
                return -1
        return counter
    
    def Clear(self):
        self.head = None    #makes head and tail none
        self.tail = None
    
    def Min(self):  #returns first element, or math inf
        return math.inf if (self.head == None) else self.head.data
    
    def Max(self):  #returns last element, or -math inf
        return -math.inf if (self.tail == None) else self.tail.data
    
    def HasDuplicates(self):
        #if list is empty returs false
        if self.head == None:
            return False
        #iterates to find a duplicate
        currNode = self.head
        while currNode != self.tail:
            if currNode.data == currNode.next.data:
                return True
            currNode = currNode.next
        #found no duplicates, returns false
        return False
        
    def Select(self,k):
        #if list is empty returns math inf
        if self.head == None:
            return math.inf
        currNode = self.head
        #iterates to find k
        for i in range(k):
            currNode = currNode.next
            #k is greater than length
            if currNode == None:
                return math.inf
        return currNode.data
    
    def FillList(self, n):
        self.Clear()
        for i in range(int(n)):
            self.Insert(random.randint(-20,20))
        
#MAIN
stay = True #Stay on menu
print('Welcome to Sorted Lists!')
while stay:
    print('What would you like to do?')
    option1 =  input('\t1)Make a list to test\n\t2)Exit\n:')
    if option1 == '2':
        stay = False
    if option1 =='1':
        #creates list
        L = SortedList()
        listSize = input('How long would you like your list to be? ')
        L.FillList(listSize)
        print('This is your list to test: ', end = '')
        L.Print()
        #Testing portion
        while stay:
            #Displays menu options and stores user's answer
            option2 = input('What do you want to do?\n\t1)Make another list\n\t2)Print\n\t3)Insert\n\t4)Delete\n\t5)Merge\n\t6)IndexOf\n\t7)Clear\n\t8)Min\n\t9)Max\n\t10)HasDuplicate\n\t11)Select\n\t12)Quit\n:')
            #Make new list
            if option2 == '1':
                listSize = input('How long would you like your list to be? ')
                L.FillList(listSize) #Call to make new list
                print('This is your list to test: ', end = '')
                L.Print()
            #Print List
            elif option2 == '2':
                L.Print() #call to print
            #Insert
            elif option2 == '3':
                num = int(input('What number do you want to insert? '))
                L.Insert(num)   #Call to insert
                print('New list: ', end='')
                L.Print()
            #Delete
            elif option2 == '4':
                num = int(input('What number do you want to delete? '))
                L.Delete(num) #Call to delete
                print('New list: ', end='')
                L.Print()
            #Merge
            elif option2 == '5':
                L2 = SortedList()
                listSize2 = int(input('What size do you want the second list to be? '))
                L2.FillList(listSize2) #create new list to merge
                print('This is your second list: ', end = '')
                L2.Print()
                L.Merge(L2)     #Call to merge
                print('Merged list: ', end='')
                L.Print()
            #Index Of
            elif option2 == '6':
                num = int(input('What number are you looking for? '))
                print('Your index number is ' + str(L.IndexOf(num))) #Call to index of
            #Clear
            elif option2 == '7':
                print('Clearing list: ', end ='')
                L.Clear()   #Call to clear
                L.Print()
            #Min
            elif option2 == '8':
                print('The smallest element is: ', end ='')
                print(L.Min()) #Call to min
            #Max
            elif option2 == '9':
                print('The largest element is: ', end ='')
                print(L.Max()) #Call to max
            #Has Duplicate
            elif option2 == '10':
                if L.HasDuplicates():   #call to has duplicates
                    print('This list does have duplicates')
                else:
                    print('This list does not have duplicates')
            #Select
            elif option2 == '11':
                num = int(input('What kth smallest element are you looking for?'))
                print('The kth smallest element is: ' + str(L.Select(num))) #call to select
            #Quit
            elif option2 == '12':
                stay = False #Boolean false to exit the loop
            else:
                print('Invalid input. Type a number from 1 to 12')
    else:
            print('Invalid input. Type a number from 1 to 2')

