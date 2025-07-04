import json
import os
import datetime

def load_tasks():
    if not os.path.exists("file.txt"):
        return []
    with open("file.txt", "r") as file:
        return json.load(file)


def save_tasks(tasks):
    with open("file.txt", "w") as file:
        json.dump(tasks,file)


def create_task(title):
    tasks = load_tasks()

    if not tasks:
        id = 1
    else:
        id = tasks[-1]["id"] + 1

    task = {
    "id" : id,
    "title" : title,
    "done" : False,
    "created_at" : str(datetime.date.today()),
    "updated_at" : None
    }

    tasks.append(task)

    save_tasks(tasks)


def update_task(id, new_title):
    tasks = load_tasks()
    for task in tasks:
        if task["id"] == id:
            task["title"] = new_title
            task["updated_at"] = str(datetime.date.today())
            save_tasks(tasks)
            return True
    return False


def delete_task(id):
    tasks = load_tasks()
    for task in tasks:
        if task["id"] == id:
            tasks.remove(task)
            save_tasks(tasks)
            return True
    return False


def read_task(id):
    tasks = load_tasks()
    for task in tasks:
        if task["id"] == id:
            print(f"""
            The task with id {task['id']}
            title     : {task['title']}
            completed : {task['done']}
            created   : {task['created_at']}
            updated   : {task['updated_at']}
            """)
            return True
    print("No such task found")
    return False

def read_all_tasks():
    tasks = load_tasks()
    if not tasks:
        print("No tasks found.")
        return

    for task in tasks:
        print(f"""
        The task with id {task['id']}
        title     : {task['title']}
        completed : {task['done']}
        created   : {task['created_at']}
        updated   : {task['updated_at']}
        """)
        print()


def complete_task(id):
    tasks = load_tasks()
    for task in tasks:
        if task["id"] == id:
            task["done"] = True
            save_tasks(tasks)
            return True
    return False


if __name__ == "__main__":
    while True:
        print("""
        Welcome to our little CRUD taks app
        Choose you act from the following list:
        1. Create task
        2. Update task
        3. Delete task
        4. Read task
        5. Read all tasks
        6. Complete task
        7. Exit""")
        option = input()
        if option == "1":
            print("Type a task title:")
            create_task(input())
            print("You have created the task!:")
        elif option == "2":
            print("Type the id of the task you want to update:")
            task_id = int(input())
            print("What is your new title for the task?:")
            if update_task(task_id, input()):
                print("You have updated the task!")
        elif option == "3":
            print("Type the id of the task you want to delete:")
            task_id = int(input())
            if delete_task(task_id):
                print("You have deleted the task!")
        elif option == "4":
            print("Type the id of the task you want to read:")
            task_id = int(input())
            read_task(task_id)
        elif option == "5":
            read_all_tasks()
        elif option == "6":
            print("Type the id of the task you want to mark done:")
            task_id = int(input())
            if complete_task(task_id):
                print("You have completed the task!")
        elif option == "7":
            break
        else:
            print("The option is not valid")
            




