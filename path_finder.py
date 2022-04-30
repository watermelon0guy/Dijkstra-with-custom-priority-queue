import data_structures as ds


def print_path(start: str, goal: str, path):
    cur_node = goal
    print(f'\nиз {goal} в {start}: \n {goal} ', end='')
    while cur_node != start:
        cur_node = path[cur_node]
        print(f'--->>> {cur_node} ', end='')


def dijkstra(start, goal, graph):
    queue = []
    ds.pq_push(queue, (0, start))
    cost_visited = {start: 0}
    visited = {start: None}

    while queue:
        cur_cost, cur_vertex = ds.pq_pull(queue)
        if cur_vertex == goal:
            break

        next_vertexes = graph[cur_vertex]
        for next_node in next_vertexes:
            neighbour_cost, neighbour_node = next_node
            new_cost = cost_visited[cur_vertex] + neighbour_cost

            if neighbour_node not in cost_visited or new_cost < cost_visited[neighbour_node]:
                ds.pq_push(queue, (new_cost, neighbour_node))
                cost_visited[neighbour_node] = new_cost
                visited[neighbour_node] = cur_vertex
    return visited
