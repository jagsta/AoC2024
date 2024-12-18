# Dijkstra is surely the way to go here, using a minheap to keep all untravelled nodes
# Need to understand how to account for turns on path

#First attempt - some dude has written a modified dijkstra implementation which can calculate with turn penalties
import networkx as nx
from shortest_path_util import penalty_turns
from shortest_path_turn_penalty import shortest_path_turn_penalty

