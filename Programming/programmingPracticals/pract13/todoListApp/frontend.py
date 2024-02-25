from tkinter import *
from backend import TaskList


class TodoListApp:
    def __init__(self, todoList):
        self.todoList = todoList

        self.win = Tk()
        self.win.title("Todo List App")

        self.mainFrame = Frame(self.win)
        self.mainFrame.grid(row=0, column=0, padx=10, pady=10)

        self.newTask = StringVar()
        self.newTask.set("Enter task here")

        self.taskWidgets = []

    def run(self):
        self.createWidgets()
        self.win.mainloop()

    def createWidgets(self):
        self.delAllWidgets()

        numTasks = self.todoList.getNumTasks()
        for i in range(numTasks):
            task = self.todoList.getTaskMsgByIndex(i)

            lblTask = Label(
                self.mainFrame,
                text=task,
            )
            lblTask.grid(row=i, column=0, sticky="w")
            self.taskWidgets.append(lblTask)

            btnEdit = Button(
                self.mainFrame,
                text="Edit",
                command=lambda index=i: self.editTask(index)
            )
            btnEdit.grid(row=i, column=1, padx=5, pady=5)
            self.taskWidgets.append(btnEdit)

            btnDelete = Button(
                self.mainFrame,
                text="Delete",
                command=lambda index=i: self.removeTask(index)
            )
            btnDelete.grid(row=i, column=2, padx=5, pady=5)
            self.taskWidgets.append(btnDelete)

        entryTask = Entry(
            self.mainFrame,
            textvariable=self.newTask,
            width=40
        )
        entryTask.grid(row=numTasks, column=0)
        self.taskWidgets.append(entryTask)

        btnAddTask = Button(
            self.mainFrame,
            text="Add",
            command=self.addTask
        )
        btnAddTask.grid(row=numTasks, column=1, padx=5, pady=5)
        self.taskWidgets.append(btnAddTask)

    def addTask(self):
        task = self.newTask.get()
        self.todoList.addTaskByMsg(task)

        self.newTask.set("Enter task here")
        self.createWidgets()

    def editTask(self, index):
        win = Tk()
        win.title("Edit Task")

        frame = Frame(win)
        frame.grid(row=0, column=0, padx=10, pady=10)

        def edit():
            msg = entryEditTask.get()
            win.destroy()
            self.todoList.setTaskMsgAtIndex(index, msg)
            self.createWidgets()

        entryEditTask = Entry(
            frame,
            width=35
        )
        entryEditTask.grid(row=0, column=0)

        btnConfirm = Button(
            frame,
            text="Confirm",
            command=edit
        )
        btnConfirm.grid(row=0, column=1, padx=5, pady=5)

    def removeTask(self, index):
        self.todoList.removeTaskAtIndex(index)
        self.createWidgets()

    def delAllWidgets(self):
        for widget in self.taskWidgets:
            widget.destroy()
        self.taskWidgetsWidgets = []


def testTodoList():
    taskList = TaskList()
    taskList.addTaskByMsg("Buy Milk")
    taskList.addTaskByMsg("Buy eggs")
    taskList.addTaskByMsg("Go to work")
    taskList.addTaskByMsg("Do the coursework")

    todoList = TodoListApp(taskList)
    todoList.run()


testTodoList()
