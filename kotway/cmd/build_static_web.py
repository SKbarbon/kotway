import importlib.util
import os, shutil

def build_static_web (command_args: list[str]):
    """Build a static web project for a kotway app."""
    # STEP: Get target path.
    selected_path: str = "./" # The path where the project folder is at.

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

    # STEP: Validate project
    required_files = [
        os.path.join(selected_path, "main.py"),
        os.path.join(selected_path, "requirements.txt")
    ]
    for f in required_files:
        if not os.path.isfile(f): 
            raise Exception(f"The project folder need to have {os.path.basename(f)}")

    # STEP: create dist folder.
    print("Creating..")
    dist_path = os.path.join(selected_path, "dist")
    if os.path.isdir(dist_path):
        shutil.rmtree(dist_path)
    os.mkdir(dist_path)

    # STEP: Copy web folder, and paste it 
    spec = importlib.util.find_spec("kotway")
    kotway_path = spec.submodule_search_locations[0]
    web_path = os.path.join(kotway_path, "web")
    project_assets_path = os.path.join(selected_path, "assets")
    index_file_path = os.path.join(web_path, "index.html")

    shutil.copytree(web_path, dist_path, dirs_exist_ok=True)
    # Copy assets to the web app's assets
    if os.path.isdir(project_assets_path):
        print(f"Copying project assets at: {project_assets_path}")
        shutil.copytree(project_assets_path, os.path.join(dist_path, "assets"), dirs_exist_ok=True)

    # STEP: Modify index.html
    # The modification tells the index to use pyodide adapter.
    index_file_content: str = open(index_file_path, encoding="utf-8").read()
    index_file_content = index_file_content.replace("//<--isPyodide-->",
    'sessionStorage.setItem("isPyodide", "true");')

    new_index_path = os.path.join(dist_path, "index.html")
    open(os.path.join(new_index_path), "w+", encoding="utf-8").write(index_file_content)

    # STEP: copy contents of project to a "dist/app/" folder, zip it, then delete "app/" folder.
    temp_app_path = os.path.join(dist_path, "app")
    app_module_path = os.path.join(temp_app_path, "app")
    os.mkdir(temp_app_path)
    os.mkdir(app_module_path)

    for p in os.listdir(selected_path):
        if p != "dist":
            fp = os.path.join(selected_path, p)
            dist_fp = os.path.join(app_module_path, p)
            if os.path.isdir(fp):
                shutil.copytree(fp, dist_fp, dirs_exist_ok=True)
            elif os.path.isfile(fp):
                shutil.copy2(fp, dist_fp)

    app_zip_path = os.path.join(dist_path, "app")
    shutil.make_archive(app_zip_path, 'zip', temp_app_path)
    shutil.rmtree(temp_app_path)
    print("The web app is built successfully!")
    print(f"You can find it in your project under '/dist'")