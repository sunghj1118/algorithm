def read_input():
    # Function to read input from the user
    input_lines = []
    previous_line = ""

    while True:
        current_line = input()
        if current_line == "#" and previous_line == "#":
            break
        input_lines.append(current_line)
        previous_line = current_line

    return '\n'.join(input_lines)


def parse_input(input_string):
    # Function to parse the input into a list of parties
    # Split lines into parties
    parties = input_string.strip('#').split('#\n')
    all_parties = []

    # Check for ends of parties
    for party in parties:
        # Split party into pairs
        pairs = party.strip().split('\n')
        all_parties.append([tuple(pair.split(' ')) for pair in pairs])

    return all_parties


def create_directed_graphs(parties):
    # Function to create a directed graph for each party
    graphs = []

    for party in parties:
        graph = {}

        for giver, receiver in party:
            if giver not in graph:
                graph[giver] = []
            graph[giver].append(receiver)

            # Ensure all guests are represented in the graph
            if receiver not in graph:
                graph[receiver] = []

        graphs.append(graph)

    return graphs


def dfs(graph, node, visited, path, cycles):
    if node in path:
        # Detect a cycle and add to list of cycles
        cycle_start_index = path.index(node)
        cycles.append(path[cycle_start_index:])
        return

    if node in visited:
        return

    visited.add(node)
    path.append(node)

    # Visit all neighbours
    for neighbour in graph[node]:
        dfs(graph, neighbour, visited, path, cycles)

    # Remove the node from the path when all neighbours have been visited
    path.pop()


def find_cycles_in_party(graph):
    visited = set()
    cycles = []

    # Call DFS for each node in the graph
    for node in graph:
        dfs(graph, node, visited, [], cycles)

    return cycles


# Read the input from the user and create the graphs
input_string = read_input()
parsed_parties = parse_input(input_string)
party_graphs = create_directed_graphs(parsed_parties)

# Find the cycles in each party
for index, party in enumerate(party_graphs):
    print("Party number", index + 1)
    cycles = find_cycles_in_party(party)
    # Print the cycles for every party
    for cycle in cycles:
        cycle_string = ' to '.join(cycle)
        cycle_string += ' to ' + cycle[0] + '.'
        print(cycle_string)
    print()
