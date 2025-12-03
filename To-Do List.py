class Task:
    def __init__(self, title, text, done=False): 
        self.title = title
        self.text = text
        self.done = done

    def mark_done(self):
        self.done = True
      

    def __repr__(self):
        if self.done:
            return f"✔ - Task: {self.text}"
        else:
            return f"✗ - \nTask: {self.text}"
class ToDoList:

    def __init__(self, name):
        self.tasks = dict()
        self.name = name

    def __repr__(self):
        return f"{self.name}"

    def add(self, task):
        self.tasks[task.title] = task

    def list(self):
        return f"{self} - {self.tasks}"
    
    def mark_done(self, title):
        if title in self.tasks:
            self.tasks[title].mark_done()
    
task1 = Task("cake", "bake a cake")
task2 = Task("dinner", "cook dinner")
task3 = Task("dishes", "wash the dishes")

todo1 = ToDoList("todo1")

todo1.add(task1)

todo1.add(task2)

todo1.add(task3)
print(todo1.list())
    
todo1.mark_done("cake")

print(todo1.list())






        
        