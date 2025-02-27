# Social Network Analysis – Measures of Centrality

![Badge Concluído](https://img.shields.io/badge/Status-Completed-green) ![Badge Python](https://img.shields.io/badge/Python-3.x-blue)

# Project Description
This project was developed for the Algorithms and Data Structures II course in the Computer Engineering program. The goal is to calculate centrality measures in a Facebook ego network.

The system builds a graph from a data file (e.g., facebook_combined.txt) and performs structural analysis of the network by computing key metrics such as:

## Features

- **Graph Construction**:  
  Reads the data file to create a class containing sets of nodes and a list of edges, and generates an adjacency matrix for the graph.

- **Pathfinding Algorithms**:  
  Implements Dijkstra’s algorithm to compute shortest path distances and a modified Breadth-First Search (BFS) to retrieve all shortest paths between two nodes.

- **Centrality Calculations**:  
  - `Degree`: The number of direct connections for each node.
  - `Closeness`: The average proximity of a node to all other nodes in the network.
  - `Betweenness`: How often a node appears on the shortest paths between pairs of nodes.

- **Interactive Menu**:  
  Uses [InquirerPy](https://github.com/kazhala/InquirerPy) to display an interactive menu where you can choose operations such as:
  - Calculating degree, closeness, and betweenness.
  - Searching for a specific node using BFS.
  - Visualizing the graph with either a simple or metric-enhanced layout.

- **Visualizations**:  
  Generates visualizations with [Matplotlib](https://matplotlib.org/) and [NetworkX](https://networkx.org/). The graphs display the network structure, highlighting nodes based on the selected centrality measure (using size, color, and labels).

## Prerequisites

- Required Python libraries:
  - [matplotlib](https://matplotlib.org/)
  - [networkx](https://networkx.org/)
  - [InquirerPy](https://github.com/kazhala/InquirerPy)



