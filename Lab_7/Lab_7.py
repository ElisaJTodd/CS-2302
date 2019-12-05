# -*- coding: utf-8 -*-
"""
COURSE: CS 2302 Data Structures
AUTHOR: Elisa Jimenez Todd
ASSIGNMENT: Lab 7 - Algorithms
INSTRUCTOR: Olac Fuentes
TA: Anindita Nath
DATE: 12/4/2019
Program: This program lets the user implement finding a hamiltonian cycle on a
graph with randomization and backtracking. It lets the user use the default graph,
create a new graph, o generate a random graph. It returns the edges connected
that make the hamiltonian cycle or none if none was found. It also shows the
comparisons made and the time taken to complete.
This program also implements the edit distance algorythm with the exception that
only replacements between vowels or between consonants are allowed.
This prints the edit distance, the size of the matrix, and the time.
"""
import numpy as np
import graph_EL as graph
import connected_components as cc
import time

#randomized hamiltonian
def RandomizedHamiltonian(V,E): #receives number of vertices and edges
    comparisons = 0 #counts the comparisons of edges in a cycle
    for i in range(2**((len(E)*2)//2)): #number of tries
        comparisons +=1
        Eh = randomSet(V,E) #random subset of E of size V
        graphT = makeGraph(V,Eh) #makes graph with the edges Eh
        #if graph (V,Eh) has 1 connected component and the in-degree of every vertex in V is 2:
        if cc.connected_components(graphT) == 1 and checkDeg2(graphT):
            return Eh, comparisons # Eh forms a Hamiltonian cycle
    return None, comparisons # No Hamiltonian cycle was found

def randomSet(size, edges):
    elem = set() #edges to form the cycle
    while len(elem)<size:
        j = np.random.randint(len(edges)) #random index
        repeat = False
        for i in elem: #check if the edge has been already added
            if edges[j].source == i.dest and edges[j].dest == i.source:
                repeat = True
                break
        if not repeat:
            elem.add(edges[j]) #add edge
    return elem

def subsetsum(S,goal):
    if goal ==0:    #if goal has been reached
        return []
    if goal<0 or len(S)==0: # if results werent good
        return None
    ss = subsetsum(S[1:],goal-S[0]) #Take first item
    if ss is not None:      #if following results were good
        return [S[0]] + ss #return rest of list
    return subsetsum(S[1:],goal) #Do not take first item

#Backtracking Hamiltonian
def BacktrackingHamiltonian(V,E):
    bgraph = graph.Graph(V)
    return AuxBacktrackingHamiltonian(bgraph, list(E))

def AuxBacktrackingHamiltonian(bgraph, E):
    global bcomparisons
    if len(bgraph.el) == bgraph.vertices*2:
        bcomparisons += 1
        if cc.connected_components(bgraph) == 1 and checkDeg2(bgraph):    
            return []#if goal has been reached
        else:       #dod not make a hamiltonian cycle
            return None
    if len(E) <= 0: # No path could be formed
        return None
    edge = E[0]
    bgraph.insert_edge(edge.source, edge.dest)
    curEdges = AuxBacktrackingHamiltonian(bgraph,E[2:]) #Take first edge
    if curEdges is not None:
        return [edge] + curEdges
    bgraph.delete_edge(edge.source, edge.dest)
    return AuxBacktrackingHamiltonian(bgraph,E[2:]) #Do not take first edge
    

def makeGraph(V,Eh):
    ngraph = graph.Graph(V)
    for i in Eh:
        ngraph.insert_edge(i.source, i.dest) #inserts edges
    return ngraph

def checkDeg2(G):
    for i in range(G.vertices):
        if G.in_degree(i) != 2: #check in degree 2
            return False
    return True

#edit distance
def edit_distance(s1,s2):
    vowels = {'a','e','i','o','u'} #set of vowels
    d = np.zeros((len(s1)+1,len(s2)+1),dtype=int) #matrix size s1 x s2
    d[0,:] = np.arange(len(s2)+1) #s2 fills first row with int
    d[:,0] = np.arange(len(s1)+1) #s1 fills first column " " 
    for i in range(1,len(s1)+1): # traverse each row
        for j in range(1,len(s2)+1): # traverse each column
            if s1[i-1] == s2[j-1]: #if letter on s1 is same as letter on s2
                d[i,j] =d[i-1,j-1] #fill data with top left number
            else:
                n = [d[i,j-1],d[i-1,j-1],d[i-1,j]] #three adjacent numbers
                if min(n) == d[i-1,j-1]: #top left replace
                    if (not s1[i-1] in vowels and s2[j-1] in vowels) or (s1[i-1] in vowels and not s2[j-1] in vowels):
                        n = [d[i,j-1],d[i-1,j]]
                d[i,j] = min(n)+1 #fill data with min number + 1
    return d[-1,-1] #return matrix

def makeRandomGraph(G, E):
    V = G.vertices
    for i in range(E):
        G.insert_edge(np.random.randint(V),np.random.randint(V))
    return G

exit = False

g = graph.Graph(5)
g.insert_edge(0,1)
g.insert_edge(1,2)
g.insert_edge(1,4)
g.insert_edge(2,3)
g.insert_edge(3,4)
g.insert_edge(2,4)
g.insert_edge(4,0)

while(not exit):
    print("================================================")
    print("Choose an algorythm to test:\n\t1) Randomization Hamiltonian\n\t2) Backtracking Hamiltonian\n\t3) Dynamic Programming\n\t4) Exit")
    option = input(':')
    if option == "1":
        select = input("\t1) Test Default Graph\n\t2) Input Graph to test\n\t3) Create Random Graph\n:")
        if select == "1":
            gt = g
        elif select == "2":
            gt = graph.Graph(int(input("Vertices on graph:")))
            for i in range(int(input("Edges to add:"))):
                gt.insert_edge(int(input("source:")), int(input("destination:")))
        elif select == "3":
            gt = graph.Graph(int(input("Vertices on graph:")))
            gt = makeRandomGraph(gt, int(input("Edges to add:")))
        gt.display()
        start = time.time()
        hamiltonian, comparisons = RandomizedHamiltonian(gt.vertices, gt.el)
        end = time.time()
        print("Comparisons made:", comparisons)
        print("Time to find:", end-start)
        if hamiltonian != None:
            print("HAMILTONIAN CYCLE:")
            print('[',end = "")
            for i in hamiltonian:
                print("(", i.source, ",", i.dest, ")", end ="")
            print(']')
        else:
            print("No path found.")
    
    elif option == "2":
        select = input("\t1) Test Default Graph\n\t2) Input Graph to test\n\t3) Create Random Graph\n:")
        if select == "1":
            gt = g
        elif select == "2":
            gt = graph.Graph(int(input("Vertices on graph:")))
            for i in range(int(input("Edges to add:"))):
                gt.insert_edge(int(input("source:")), int(input("destination:")))
        elif select == "3":
            gt = graph.Graph(int(input("Vertices on graph:")))
            gt = makeRandomGraph(gt, int(input("Edges to add:")))
        gt.display()
        bcomparisons = 0
        start = time.time()
        bhamiltonian = BacktrackingHamiltonian(gt.vertices, gt.el)
        end = time.time()
        print("Comparisons made:", bcomparisons)
        print("Time to find:", end-start)
        if bhamiltonian != None:
            print("HAMILTONIAN CYCLE:")
            print('[',end = "")
            for i in bhamiltonian:
                print("(", i.source, ",", i.dest, ")", end ="")
            print(']')
        else:
            print("No path found.")
    elif option == "3":    
        select = input("\t1) Test default set of words\n\t2) Input words to test\n:")  
        if select == "1":      
            print("'sand', 'sound' :", edit_distance('sand', 'sound'))
            print("'abcd', 'abcd' :", edit_distance('abcd', 'abcd'))
            print("'sand', 'sound' :", edit_distance('races', 'race'))
            print("'races', 'race' :", edit_distance('aeiou', 'aaiiu'))
            print("'aeiou', 'aaiiu' :", edit_distance('aeiou', 'abicu'))
            print("'aeiou', 'bcdfg' :", edit_distance('aeiou', 'bcdfg'))
        else:
            s1 = input("first word: ")
            s2 = input("second word: ")
            start = time.time()
            dist = edit_distance(s1, s2)
            end = time.time()
            print("EDIT DISTANCE:",dist)
            print("# of operations :", len(s1)*len(s2))
            print("Time: ", end - start)
    elif option == "4":
        exit = True
    
    else:
        print("Select a number from 1 to 4.")
    
