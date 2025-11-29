import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO,format='[%(asctime)s]: %(message)s:')
project_name = "MLOpsProject"

list_of_files = [
    ".github/workflows/.gitkeep",  #used to store GitHub Actions CI/CD workflows
    f"src/{project_name}/__init__.py",  #Python package with imports
    f"src/{project_name}/components/__init__.py",  #components folder a Python package.Components usually include data ingestion, data transformation, model trainer, model evaluation, etc
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/utils/common.py",  #Common helper functions (read yaml, save object, load model, logging utilities, etc.)
    f"src/{project_name}/config/__init__.py",#Configuration package to manage configuration settings
    f"src/{project_name}/config/configuration.py", #Responsible for reading and parsing configuration files (config.yaml, params.yaml).
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/entity/config_entity.py",#Defines Python data classes for configuration objects.
    f"src/{project_name}/constants/__init__.py",
    "config/config.yaml",#main configuration file for the project
    "params.yaml",#parameters file to store hyperparameters and other settings
    "schema.yaml",#schema file to define the structure of input data
    "main.py", #Entry point for training and evaluating the ML model 
    "app.py",#Entry point for the application (Flask, FastAPI, etc.)
    "Dockerfile",#Docker configuration file for containerizing the application
    "requirements.txt",
    "setup.py",#Setup file for packaging and distributing the project.Makes your project pip-installable as a package.
    "research/trials.ipynb"#Jupyter notebook for experimentation and prototyping
    "templates/index.html"#HTML template for web application
]

for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)

    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory: {filedir} for file: {filename}")

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as fp:
            pass
        logging.info(f"Creating empty file: {filepath}")
    else:
        logging.info(f"File already exists: {filepath}, skipping creation.")