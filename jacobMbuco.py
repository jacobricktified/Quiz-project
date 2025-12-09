""" 

1. Build a Simple To-Do List Program
Task:
Create a Python program that allows a user to:
Requirements
1. Add a task
2. View all tasks
3. Mark a task as done OR delete a task
4. Exit
Minimum concepts required
• Variables
• Lists
• If/else
• Loops
use file haandling to save the tasks to a file so that they persist between program runs.
with open("example.txt" , r+) as file:
file=(ope("",""))
fle.write("Hello World")
file.close()
if option ==3:
if not task:
print("No tasks to mark as done."
else:
for val , num in enumerate(task, start=1):
print(val,num)
nums = int(input("Enter the task to be deleted: "))
IF 1<=nums <len(task):
remove=task.pop(nums-1)
save_tasks(task)

"""
def load_tasks():
    try:
        with open("tasks.txt", "r") as file:
            tasks = [line.strip() for line in file.readlines()]
    except FileNotFoundError:
        tasks = []
    return tasks
def save_tasks(tasks):
    with open("tasks.txt", "w") as file:
        for task in tasks:
            file.write(task + "\n")
def main():
    tasks = load_tasks()
    while True:
        print("\nTo-Do List Menu:")
        print("1. Add a task")
        print("2. View all tasks")
        print("3. Mark a task as done")
        print("4. Exit")
        option = input("Choose an option (1-4): ")
        if option == "1":
            task = input("Enter the task: ")
            tasks.append(task)
            save_tasks(tasks)
            print(f'Task "{task}" added.')
        elif option == "2":
            if not tasks:
                print("No tasks available.")
            else:
                print("Tasks:")
                for idx, task in enumerate(tasks, start=1):
                    print(f"{idx}. {task}")
        elif option == "3":
            if not tasks:
                print("No tasks to mark as done.")
            else:
                for idx, task in enumerate(tasks, start=1):
                    print(f"{idx}. {task}")
                nums = int(input("Enter the task number to mark as done: "))
                if 1 <= nums <= len(tasks):
                    removed = tasks.pop(nums - 1)
                    save_tasks(tasks)
                    print(f'Task "{removed}" marked as done and removed.')
                else:
                    print("Invalid task number.")
        elif option == "4":
            print("Exiting the program.")
            break
        else:
            print("Invalid option. Please choose between 1-4.")
if __name__ == "__main__":
    main()






    


