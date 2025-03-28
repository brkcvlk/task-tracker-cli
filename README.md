


# Task Tracker CLI
### Task Tracker CLI app from [roadmap.sh/](https://roadmap.sh/projects/task-tracker)

## How To Run

- Clone the repository
```

  git clone https://github.com/brkcvlk/task-tracker-cli.git

```
- Create a Virtual Environment
```

    python -m venv venv

```

- Activate the Virtual Environment
```

    venv\Scripts\activate

```
- Install Module
```

    pip install -r requirements.txt

```
- Run the Code
```

    python main.py

```

## Commands 
- ```add <description>``` -> Add a task to List
- ```update <id> <description>``` -> Update the description of task with task id
- ```delete <id>``` -> Delete the task from List
- ```mark_done <id>``` -> Mark the task as done
- ```mark_in_progress <id>``` -> Mark the task as in progress
- ```list``` -> Show the all tasks in list \
        -- ```list done``` -> Show tasks with done status \
        -- ```list in_progress```-> Show tasks with in-progress status \
        -- ```list todo```-> Show tasks with todo status
- ```quit``` -> Quit from app
- ```help``` -> Show the commands

