import path_finder

graph_1 = {'A': [(2, 'M'), (3, 'P')],
           'M': [(2, 'A'), (2, 'N')],
           'N': [(2, 'M'), (2, 'B')],
           'P': [(3, 'A'), (4, 'B')],
           'B': [(4, 'P'), (2, 'N')]}

graph_2 = {'A': [(5, 'B'), (4, 'C')],
           'B': [(5, 'A'), (5, 'D'), (5, 'C')],
           'C': [(4, 'A'), (5, 'B'), (1, 'E')],
           'E': [(1, 'C'), (1, 'D')],
           'D': [(5, 'B'), (1, 'E')]}

start = 'A'
goal = 'B'
visited = path_finder.dijkstra(start, goal, graph_1)

path_finder.print_path(start, goal, visited)

start = 'A'
goal = 'D'
visited = path_finder.dijkstra(start, goal, graph_2)

path_finder.print_path(start, goal, visited)
