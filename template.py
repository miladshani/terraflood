import os
from pathlib import Path
import logging

logging.basicConfig(Level=logging.INFO, format='[%(asctime)s]: %(message)s:')

project_name = "terraflood"

list_of_files = [

    "requirements.txt",
    "setup.py",
    "research/trials.ipynb"

    ".github/workflows/.gitkeep",
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/utils/common.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/entity/config_entity.py",
    f"src/{project_name}/constants/__init__.py",
]

# Generating the structure
for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.slit(filepath)

    if filedir != "":
        
