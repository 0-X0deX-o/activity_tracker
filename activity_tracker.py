from datetime import datetime, timedelta
import pickle 
def help():
    '''
    NAME

        activity_tracker - track a single instance of a user named task/create *.ics calendar events

    SYNOPSIS

        > python ./activity_tracker.py
        --- (Start Menu)
        Activity Tracker 1.0.0
        Type "help" for more information
        -> [OPTION...]

        -s, --start-task 
            name the new acivity instance and write the task name and start time to disk
        
        -e, --end-task 
            end the instance and output logged time to the terminal and tasks.log

        -v, --version 
            output the version number to terminal

        -q, --quit 
            exit the application

    EXAMPLE TERMINAL OUTPUT
        [TASK]:Write Log -> 0:00:03.291983 total time
    
    EXAMPLE LOG OUTPUT
        TASK LOG
        [TASK]:Task 2 -> 0:00:01.766871 total time
        [TASK]:Task 3 -> 0:00:02.459259 total time
        [TASK]:Task 6 -> 0:00:03.003836 total time
        [TASK]:Task 7 -> 0:00:02.314626 total time
        [TASK]:Task 8 -> 0:00:02.388613 total time
        [TASK]:Task 9 -> 0:00:01.744440 total time
        [TASK]:Task 10 -> 0:00:01.471993 total time
    '''
def activity_start():
    return datetime.now()

def activity_end():
    return datetime.now()


def compute_time_spent(start, end):
    time = (end - start)    
    return time 

def print_activity_tracker_menu():
    print(  'Activity Tracker 1.0.0')
    print('Type "help" for more information')
    
def transition_menu():
    print('Choose an option: -s, -e, -q, -c')
    return carriage_return()

def carriage_return():
        input_args = input('> ').strip()
        return menu_loop(input_args)

def add_task():
    return input("Enter the task name: ")

def menu_loop(input_args):
    while True:
        if input_args == '-s' or input_args == '--start-task':
            task_name = add_task()
            now = activity_start()
            entry = [task_name, now]
            with open('log.pickle', 'wb') as f:
                pickle.dump(entry, f)
                f.close()
            print('Task/Start time added')
            transition_menu()

        elif input_args == '-e' or input_args ==  '--end-task':
            now = activity_end()
            with open('log.pickle', 'rb') as f:
                entry = pickle.load(f)
                f.close()
            if entry == '':
                print('No Current Task')
                transition_menu()
            time  = (compute_time_spent(entry[1], now))
            output_string = f"[TASK]:{entry[0]} -> {time} total time"
            print(output_string)
            log_output_string = '\n' + output_string
            with open('tasks.log', 'a') as f:
                f.write(log_output_string)
                f.close()
            entry = ''
            with open('log.pickle', 'wb') as f:
                pickle.dump(entry, f)
                f.close()
            print('Log cleared')
            transition_menu()

        elif input_args == '-c' or input_args == 'clear':
            with open('tasks.log', 'w') as f:
                f.write('')
                f.close()
            print('Text log cleared')
            transition_menu()

        elif input_args == '-v' or input_args == '--version':
            print('Activity Tracker 1.0.0')
            transition_menu()

        elif input_args == 'help':
            print(help.__doc__)
            transition_menu()

        elif input_args == '-q' or input_args ==  '--quit':
            print('Goodbye!')
            quit()
        else:
            transition_menu()

print_activity_tracker_menu()
menu_loop(carriage_return())
