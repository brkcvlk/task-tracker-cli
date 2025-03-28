from cmd import Cmd
from rich import print as pprint
import datetime
import json
from rich.table import Table
from rich.console import Console

data = []
count = 0

def id():
    global count
    count += 1
    return count

count2 = 0
def IdForJson():
    global count2
    count2 += 1
    return count2

def Update(id, description):
    for d in data:
        if d["id"] == int(id):
            d["description"] = description
            with open('article.json', 'w') as file:
                json.dump(data, file, indent=4)
                pprint(f"[green]Task updated successfully[/green] (ID : {d['id']})")


def Delete(id):
    for d in data:
        if d["id"] == int(id):
            data.remove(d)
            with open('article.json', 'w') as file:
                json.dump(data, file, indent=4)
                pprint('[green]Task deleted successfully[/green]')


def MarkDone(id):
    for d in data:
        if d["id"] == int(id):
            d["status"] = "done"
            with open('article.json', 'w') as file:
                json.dump(data, file, indent=4)

def MarkInProgress(id):
    for d in data:
        if d["id"] == int(id):
            d["status"] = "in-progress"
            with open('article.json', 'w') as file:
                json.dump(data, file, indent=4)

def ListAll():
    table = Table(title="Tasks")
    table.add_column("Id", justify='center', style="red")
    table.add_column("Description", justify="center", style="cyan")
    table.add_column("Status", justify="center", style="green")
    table.add_column("Date", justify="center")
    for d in data:
        table.add_row(f"{d['id']}", f"{d['description']}", f"{d['status']}", f"{d['date']}")
    
    console = Console()
    console.print(table)

def ListDone():
    table = Table(title="Tasks")
    table.add_column("Id", justify='center', style="red")
    table.add_column("Description", justify="center", style="cyan")
    table.add_column("Status", justify="center", style="green")
    table.add_column("Date", justify="center")
    for d in data:
        if d["status"] == "done":
            table.add_row(f"{d['id']}", f"{d['description']}", f"{d['status']}", f"{d['date']}")
        else:
            continue
    
    console = Console()
    console.print(table)

def ListTodo():
    table = Table(title="Tasks")
    table.add_column("Id", justify='center', style="red")
    table.add_column("Description", justify="center", style="cyan")
    table.add_column("Status", justify="center", style="green")
    table.add_column("Date", justify="center")
    for d in data:
        if d["status"] == "todo":
            table.add_row(f"{d['id']}", f"{d['description']}", f"{d['status']}", f"{d['date']}")
        else:
            continue
    
    console = Console()
    console.print(table)


def ListInProgress():
    table = Table(title="Tasks")
    table.add_column("Id", justify='center', style="red")
    table.add_column("Description", justify="center", style="cyan")
    table.add_column("Status", justify="center", style="green")
    table.add_column("Date", justify="center")
    for d in data:
        if d["status"] == "in-progress":
            table.add_row(f"{d['id']}", f"{d['description']}", f"{d['status']}", f"{d['date']}")
        else:
            continue
    
    console = Console()
    console.print(table)

class App(Cmd):
    Cmd.intro = pprint("[blue]Welcome to the Task Tracker CLI![/blue] \n[blue]Type help to see command list.[/blue]")

    def do_add(self, args):
        'Adding a task to list, task-cli add <description>'
        global data
        data.append(Task(description=args).__dict__)
        with open('article.json', 'w') as file:
            json.dump(data, file, indent=4)

    def do_quit(self, args):
        'Quit from Run Server, task-cli quit'
        pprint('[red]Quitting..[/red]')
        raise SystemExit
    
    def do_update(self, args):
        'Update the description with using id, task-cli update <id> <description>'
        id = args.split()[0]
        description = args.split()[1]
        Update(id=id, description=description)

    def do_delete(self, args):
        'Delete the task from list, task-cli delete <id>'
        id = args
        Delete(id=id)

    def do_mark_done(self, args):
        'Mark the task as done, task-cli mark_done <id>'
        id = args
        MarkDone(id=id)
    
    def do_mark_in_progress(self, args):
        'Mark the task as in-progress, task-cli mark_in_progress <id>'
        id = args
        MarkInProgress(id=id)
    
    def do_list(self, args):
        'List tasks -> task-cli list,  List Status Done Tasks -> task-cli list done,   List Status Todo Tasks -> task-cli list todo,   List Status In-Progress Tasks -> task-cli list in-progress'

        if args == "done":
            ListDone()
        elif args == "todo":
            ListTodo()
        elif args == "in-progress":
            ListInProgress()
        else:
            ListAll()
    
class Task(App):
    def __init__(self, description):
        self.description = description
        self.id = id()
        self.status = "todo"
        self.date = str(datetime.datetime.now())
        pprint(f"[green]Task added successfully[/green] (ID : {self.id})")
    

if __name__ == '__main__':
    prompt = App()
    prompt.prompt = "task-cli "
    prompt.cmdloop(pprint('[green]Starting..[/green]'))