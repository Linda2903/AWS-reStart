import requests

def get_projects():
    data=requests.get("http://127.0.0.1:8000/projects")
    print(data.json())

def get_task_by_project_id(project_id:str):
    data=requests.get(f"http://127.0.0.1:8000/tasks/{project_id}")
    print(data.json())


def main():
    # Assumiamo che il main lanci un menù con varie opzioni
    # Tra cui la lista dei progetti
    print("hello")
    #get_projects()
    get_task_by_project_id("5519014d-d572-4ae8-a380-f9165b8e4328")

main()
