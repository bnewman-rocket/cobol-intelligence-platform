from app.connectors.file_loader import load_programs

def analyze(program_directory):

    code_map = load_programs(program_directory)

    return {
        "program_count": len(code_map),
        "programs": list(code_map.keys()),
        "sample_program": next(iter(code_map.values()))[:200]  # preview
    }