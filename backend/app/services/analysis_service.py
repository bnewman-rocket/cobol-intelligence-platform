from app.connectors.ea_connector import analyze_program_set
from app.connectors.file_loader import load_programs
from app.services.aggregation_service import build_system_graph

def analyze(program_directory):

    code_map = load_programs(program_directory)
    program_names = list(code_map.keys())

    ea_data = analyze_program_set(program_names)
    graph = build_system_graph(ea_data)

    return {
        "programs": program_names,
        "dependency_graph": graph,
        "ea_data": ea_data
    }