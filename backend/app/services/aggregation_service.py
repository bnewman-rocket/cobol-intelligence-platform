def build_system_graph(ea_data):

    graph = {}

    for prog in ea_data:
        graph[prog["program"]] = prog["calls"]

    return graph