import requests
import os
import zipfile


def generate_project():
    api_url = "https://start.spring.io/starter.zip"
    project_data = {
        "type": "{{cookiecutter.buildTool}}",
        "language": "{{cookiecutter.language}}",
        "bootVersion": "{{cookiecutter.bootVersion}}",
        "groupId": "{{cookiecutter.groupId}}",
        "artifactId": "{{cookiecutter.artifact_name}}",
        "name": "{{cookiecutter.artifact_name}}",
        "description": "{{cookiecutter.description}}",
        "packageName": "{{cookiecutter.packageName}}",
        "packaging": "{{cookiecutter.packaging}}",
        "javaVersion": "{{cookiecutter.javaVersion}}",
        "dependencies": "{{cookiecutter.dependencies}}",
    }
    response = requests.get(api_url, params=project_data)

    if response.status_code == 200:
        with open(os.path.join("project.zip"), "wb") as f:
            f.write(response.content)

        with zipfile.ZipFile(os.path.join("project.zip"), "r") as zip_ref:
            zip_ref.extractall()

        os.remove(os.path.join("project.zip"))

        print("Project generated successfully.")
    else:
        error_message = (
            f"Failed to generate the project. Status Code: {response.status_code}"
        )
        raise Exception(error_message)


if __name__ == "__main__":
    try:
        generate_project()
    except Exception as e:
        print(f"Error: {e}")
        # Optionally, exit the script with a non-zero status code
        exit(1)
