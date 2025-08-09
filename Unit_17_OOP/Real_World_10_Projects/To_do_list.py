# 📌 Project 4 - To do list App (OOP + clean code)

class Task:
    """Represent a single task in the todo list."""
    def __init__(self, title):
        self.title = title
        self.completed = False # Default : not done yet

    def mark_done(self):
        """Mark this task as completed."""
        self.completed = True


class TodoList:
    """Manage the collection of tasks."""
    def __init__(self):
        self.tasks = [] # Store all task objects

    def add_task(self, title):
        """Add a new task to the list."""
        task = Task(title)
        self.tasks.append(task)
        print(f'✅ Task "{title}" added!.')

    def remove_task(self, index):
        """Remove a task by its index."""
        if 0 <= index < len(self.tasks):
            removed_task = self.tasks.pop(index)
            print(f'🗑️ Task "{removed_task.title} removed!" ')
        else:
            print('❌ Invalid task number.')

    def display_tasks(self):
        """Display all tasks with status."""
        if not self.tasks:
            print("No tasks in your list.")
            return
        print("\n 📋 Your todo list: ")
        for i, task in enumerate(self.tasks, start=1):
            status = "✅ Done" if task.completed else " Pending"
            print(f'{i}. {task.title} - {status}')

    def mark_task_done(self, index):
        """Mark a specific task as done"""
        if 0 <= index < len(self.tasks):
            self.tasks[index].mark_done()
            print(f'✅ Task "{self.tasks[index].title}" marked as done!.')
        else:
            print("❌ Invalid task number.")

# ===========Main=============
def main():
    todo_list = TodoList()

    while True:
        print('\n======Todo List Menu======')
        print('1. Add Task')
        print('2. View Task')
        print('3. Mark Task as Done')
        print('4. Remove Task')
        print('5. Exit')

        choice = input("Enter choice (1-5): ")
        if choice == "1":
            title = input("Enter ask title: ")
            todo_list.add_task(title)
        elif choice == "2":
            todo_list.display_tasks()
        elif choice == "3":
            todo_list.display_tasks()
            try:
                num = int(input("Enter task number to mark as done: ")) -1
                todo_list.mark_task_done(num)
            except ValueError:
                print('❌ Please enter a valid number.')
        elif choice == "4":
            todo_list.display_tasks()
            try:
                num = int(input("Enter task number to remove: ")) -1
                todo_list.remove_task(num)
            except ValueError:
                print("❌ Please enter a valid number.")
        elif choice == "5":
            print('👋 Goodbye!')
            break
        else:
            print('❌ Invalid choice, try again.')

if __name__ == "__main__":
    main()
            
            
                
        
        
        
        
        
        
            
            
            
        