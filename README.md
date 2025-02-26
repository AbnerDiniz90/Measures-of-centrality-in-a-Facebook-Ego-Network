# Social Network Analysis – Measures of Centrality

This project aims to calculate key centrality measures in an ego network from Facebook. Using data from a file (e.g., `facebook_combined.txt`), the code builds a graph and computes the following metrics:

- **Degree**: The number of direct connections for each node.
- **Closeness**: The average proximity of a node to all other nodes in the network.
- **Betweenness**: How often a node appears on the shortest paths between pairs of nodes.

## Features

- **Graph Construction**:  
  Reads the data file to create a class containing sets of nodes and a list of edges, and generates an adjacency matrix for the graph.

- **Pathfinding Algorithms**:  
  Implements Dijkstra’s algorithm to compute shortest path distances and a modified Breadth-First Search (BFS) to retrieve all shortest paths between two nodes.

- **Centrality Calculations**:  
  Provides functions to compute degree, closeness, and betweenness centrality for each node.

- **Interactive Menu**:  
  Uses [InquirerPy](https://github.com/kazhala/InquirerPy) to display an interactive menu where you can choose operations such as:
  - Calculating degree, closeness, and betweenness.
  - Searching for a specific node using BFS.
  - Visualizing the graph with either a simple or metric-enhanced layout.

- **Visualizations**:  
  Generates visualizations with [Matplotlib](https://matplotlib.org/) and [NetworkX](https://networkx.org/). The graphs display the network structure, highlighting nodes based on the selected centrality measure (using size, color, and labels).

## Prerequisites

- Python 3.x

- Required Python libraries:
  - [matplotlib](https://matplotlib.org/)
  - [networkx](https://networkx.org/)
  - [InquirerPy](https://github.com/kazhala/InquirerPy)



