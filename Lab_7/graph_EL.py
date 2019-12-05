"""
COURSE: CS 2302 Data Structures
AUTHOR: Elisa Jimenez Todd
ASSIGNMENT: Lab 6 - Edge List Graph
INSTRUCTOR: Olac Fuentes
TA: Anindita Nath
DATE: 11/15/2019
Program: implementation of Edge List graph.
Inserting edges, deleting edges, displaying the table, breadth-first search,
and depth first search.
"""
# Edge list representation of graphs
import numpy as np
import matplotlib.pyplot as plt
import math
from scipy.interpolate import interp1d

class Edge:
    def __init__(self, source, dest, weight=1):
        self.source = source
        self.dest = dest
        self.weight = weight
        
class Graph:
    # Constructor
    def __init__(self,  vertices, weighted=False, directed = False):
        self.vertices = vertices
        self.el = []
        self.weighted = weighted
        self.directed = directed
        self.representation = 'EL'
        
    def insert_edge(self,source,dest,weight=1):
        self.el.append(Edge(source, dest, weight)) #insert edge with all info
        if not self.directed and source!=dest: #double if not directed
            self.el.append(Edge(dest, source, weight))
    
    def delete_edge(self,source,dest):
        i = 0
        for edge in self.el: #find edges
            if edge.source == source and edge.dest == dest: #if edge and dest correspond, this is the edge we are looking for
                self.el.pop(i) #remove edge
                break;
            i+=1
        if not self.directed:#double if not directed
            i=0
            for edge in self.el:
                if edge.source == dest and edge.dest == source: #destiny as source
                    self.el.pop(i)
                    return True
                i+=1
        return False
    
    def display(self):
        print('[',end='') #all inside brackets
        for i in self.el:
            print('(' + str(i.source) + ','+ str(i.dest) + ',' + str(i.weight) + ')',end='') #each edge inside parentheses
        print(']') 
        return
    
    def in_degree(self, v):
        deg = 0
        for edge in self.el:
            if edge.dest == v:
                deg += 1
        return deg