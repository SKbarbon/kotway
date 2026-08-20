from importlib.metadata import distribution
import os

def get_kotway_pipname () -> str:
    dist = distribution("kotway")
    name = dist.metadata["Name"]
    version = dist.version
    return f"{name}=={version}"

def create_project (command_args: list[str]):
    """Create a kotway project."""
    # STEP: Get target path.
    selected_path: str = "./" # The path where the project folder will be created.

    if len(command_args) >= 1:
        selected_path = ""
        index = 0
        for p in command_args[0:]:
            selected_path = selected_path + p
            if index >= len(command_args): selected_path = selected_path + " "
            index = index + 1
    # validate the selected path.
    if not os.path.isdir (selected_path):
        raise Exception(f"The provided path `{selected_path}` is not a folder.")

    # STEP: Create the project folder, and its content.
    # check if a project already exists, create a new name.
    project_path: str = os.path.join(selected_path, "kotway_project")
    duplicate_num = 1
    while os.path.isdir(project_path):
        project_path = project_path + str(duplicate_num)
        duplicate_num = duplicate_num + 1
    os.mkdir(project_path)

    # create the assets folder.
    os.mkdir(os.path.join(project_path, "assets"))

    REQUIREMENTS = """flask
flask_cors
pydantic
"""
    REQUIREMENTS = REQUIREMENTS + get_kotway_pipname() + "\n"
    requirements_file_path = os.path.join(project_path, "requirements.txt")
    open(requirements_file_path, "w+", encoding="utf-8").write(REQUIREMENTS)

    EXAMPLE_APP = """
import kotway

def main (page: kotway.Page):
    page.current_view.add_control(kotway.Text("Hello, kotway!"))

kotway.App(main).run()"""
    main_file_path = os.path.join(project_path, "main.py")
    open(main_file_path, "w+", encoding="utf-8").write(EXAMPLE_APP)

    # STEP: Show results
    print("Project created!")
    print(f"Project Path: {project_path}")
    print("To quick run the project, do:")
    print(f"`cd {project_path}`")
    print("`python -m kotway run`")