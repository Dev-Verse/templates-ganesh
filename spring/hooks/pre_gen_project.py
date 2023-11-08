import requests
import os
import zipfile


def generate_project():
    api_url = "https://start.spring.io/starter.zip"
    project_data1 = {
        "type": "gradle-project",
        "language": "java",
        "bootVersion": "3.1.5",
        "groupId": "com.techverito",
        "artifactId": "ServiceCatalog",
        "name": "ServiceCatalog",
        "description": "Demo project for Spring Boot",
        "packageName": "com.techverito.ServiceCatalog",
        "packaging": "jar",
        "javaVersion": "17",
        "dependencies": "lombok,web,postgresql,testcontainers,data-jpa,devtools",
    }

    project_data = {
        "type": "{{cookiecutter.type}}",
        "language": "{{cookiecutter.language}}",
        "bootVersion": "{{cookiecutter.bootVersion}}",
        "groupId": "{{cookiecutter.groupId}}",
        "artifactId": "{{cookiecutter.artifactId}}",
        "name": "{{cookiecutter.artifactId}}",
        "description": "{{cookiecutter.description}}",
        "packageName": "{{cookiecutter.packageName}}",
        "packaging": "{{cookiecutter.packaging}}",
        "javaVersion": "{{cookiecutter.javaVersion}}",
        "dependencies": "{{cookiecutter.dependencies}}",
    }
    response = requests.get(api_url, params=project_data)

    if response.status_code == 200:
        with open(os.path("project.zip"), "wb") as f:
            f.write(response.content)

        with zipfile.ZipFile(os.path("project.zip"), "r") as zip_ref:
            zip_ref.extractall()

        os.remove(os.path.join("project.zip"))

        print("Project generated successfully.")
    else:
        print("Failed to generate the project.")


if __name__ == "__main__":
    generate_project()
