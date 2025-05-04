import os , json
taskList = {'list': {}}
progressTask = {
        'task-flow': {
            'on-progress':{} , 
            'done': []
        }
    }
if os.path.exists('taskTracker/task.json') and os.path.getsize('taskTracker/task.json') > 0:
    with open('taskTracker/task.json','r') as file:
        taskList = json.loads(file.read())
        progressTask['task-flow'].update(taskList['task-flow'])
        taskList.pop('task-flow')
class Actions:
    def __init__(self,task,newtask,action):
        self.task = task
        self.action = action
        self.newtask = newtask
        self.filePath = "taskTracker/task.json";
    def __str__(self):
        match self.action:
            case 'l':
                if len(taskList['list']) == 0:
                    return ' - No task listed -'
                return f"{taskList['list']}"
            case 'o':
                if len(progressTask['task-flow']['on-progress']) == 0:
                    return ' - No On-Going task -'
                return f"{progressTask['task-flow']['on-progress']}"
            case 'dn':
                if len(progressTask['task-flow']['done']) == 0:
                    return ' - No task Done -'
                return f"{progressTask['task-flow']['done']}"
    def __getattribute__(self, name):
        attr = super().__getattribute__(name)
        if callable(attr):
            def wrapped(*args, **kwargs):
                result = attr(*args, **kwargs)
                with open(self.filePath,'w') as file:
                    taskList.update(progressTask)
                    json.dump(taskList, file, indent=4, sort_keys=True)
                    file.write('\n')
                return result
            return wrapped
        return attr
    def actions(self):
        match self.action:
            case "a":
                self.add()  
            case "r":
                self.remove()   
            case "u":
                self.update() 
            case "d":
                self.removeAllTask()  
            case 'm':
                if self.task == 'p':
                    self.setOnGoing()
                else:
                    self.setDone()
    def createOrUpdate(self,data):
            with open(self.filePath,'w') as file:
                json.dump(data, file, indent=4, sort_keys=True)
                file.write('\n')  
    def add(self):
        if self.task in taskList['list'].values():
            print('Task is already in the list')
            return False
        index = "T1" if len(taskList['list']) == 0 else f"T{len(taskList['list']) + 1}"
        taskList['list'][index] = self.task 
    def remove(self):
        if len(taskList['list']) > 0:
            if self.task not in taskList['list']:
                print('This task is not in the list!')
            else:
                print('Removing task....')
                del taskList['list'][self.task]
                print('Successfully removed.\n')
    def update(self):
        if self.task in taskList['list'].values():
            print('Task is already exist.')
            return False
        
        if self.task not in taskList['list']:
            print('Task does not exist in the list!')
        else:
            taskList['list'][self.task] = self.newtask
            print('Successfully updated the task \n')
            print(taskList['list'].values())
    def removeAllTask(self):
        t = self.task
        match t.lower():
            case 'y':
                if len(progressTask['task-flow']['on-progress']) > 0:
                    print('Unable to clear list because of on-going tasks.')
                    return False
                if len(taskList['list']) == 0:
                    print('List is already empty.')
                else:
                    taskList['list'].clear()
                    print('ALL LIST REMOVED!')
            case 'n':
                print('\n')
            case _:
                print('Invalid choice.')
    def setOnGoing(self):
        if len(taskList['list']) > 0:
            progress = progressTask['task-flow']
            if taskList['list'][self.newtask] in progress['on-progress'].values():
                print('Task is already in progress.')
                return False;
            if self.newtask not in taskList['list']:
                print('Task is invalid. Task is not in the list.')
                return False
            if taskList['list'].get(self.newtask) and self.newtask not in progress['on-progress'] :
                index = "O1" if len(progress['on-progress']) == 0 else f"O{len(progress['on-progress'])}"
                progress['on-progress'][index] = taskList['list'][self.newtask]
                print(f"{progress['on-progress']} \n")
        else:
            print('No Task listed.')
    def setDone(self):
        if len(taskList['list']) > 0:
            progress = progressTask['task-flow']
            if self.newtask in progress['on-progress']:
                progress['done'].append(progress['on-progress'][self.newtask])
                del progress['on-progress'][self.newtask]
            else:
                print('Task is not in the progress list!')
        else:
            print('No Task listed.')