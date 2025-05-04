
from action import Actions, taskList , progressTask

while(True):
    print('Choose an action: \n')
    print('[A] ADD [R] REMOVE [U] UPDATE \n')
    print('[L] VIEW ALL TASK  [O] VIEW ON-GOING TASK  [DN] VIEW DONE TASK \n')
    print('[M] MARK TASK \n')
    print('[D] EMPTY LIST \n')
    print('[E] END \n ')

    action = str(input(':'))
    if(action != ''):
        action = action.lower()
        task = ""
        task2 = ""
        match action:
            case 'a':
                task = input("Insert new task: ")
            case 'r':
                if(len(taskList['list']) == 0):
                    print('No task is listed')
                else:
                    print(f" Task List : {taskList['list']} \n")
                    task = input("Remove ? :")
            case 'u':
                print(f"Task list: {taskList['list']} \n")
                task = input("Insert task to update : \n")
                task2 = input("New task : ")
            case 'e':
                break
            case 'd':
                task = input('Are you sure [Y/N] : ')
                print('\n')
            case 'l' | 'o' | 'dn':
                print('')
            case 'm':
                print('[P] SET PROGRESS TASK \n')
                print('[D] SET DONE TASK \n')
                taskProgress = input(':')
                task = taskProgress.lower()
                progress = progressTask['task-flow']
                match task:
                    case 'p':
                        print(f"Open tasks: {taskList['list']}")
                        print(f"On-going tasks: {progress['on-progress']}")
                        setProgress = input("Set task in progress: ")
                        task2 = setProgress
                    case 'd':
                        print(f"On-going tasks: {progress['on-progress']} \n")
                        print(f"Done Task {progress['done']}")
                        setDone = input("Set done task: ")
                        task2 = setDone
            case _:
                print('Invalid choice.')
        print('\n')
        action_methods = Actions(task,task2,action)
        if(action in ['l','o','dn']):
            print(action_methods)
        else:
            action_methods.actions()
        




    
