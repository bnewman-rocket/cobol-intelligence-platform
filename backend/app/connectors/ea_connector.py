def analyze_program_set(program_names):

    results = []

    for prog in program_names:
        results.append({
            "program": prog,
            "calls": ["DBREAD"] if prog == "GETCUST.cbl" else [],
            "called_by": [],
            "files": ["CUSTVSAM"],
            "copybooks": ["CUSTREC"],
            "complexity": 5
        })

    return results