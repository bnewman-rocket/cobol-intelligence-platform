import os

def load_programs(directory):

    programs = {}

    for file in os.listdir(directory):
        if file.endswith(".cbl"):
            file_path = os.path.join(directory, file)

            with open(file_path, "r") as f:
                programs[file] = f.read()

    return programs