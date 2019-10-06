from algo_tasks import task_num_107
from algo_tasks import task_num_243_a
from algo_tasks import task_num_243_b

if __name__ == '__main__':

    hash_of_tasks = {
        "Task 243 a": task_num_243_a,
        "Task 243 b": task_num_243_b,
        "Task 107": task_num_107
    }


def console_log_task_by_name():
    input_name_of_task = str(input(" Task example(Task 243 a) : "))
    if input_name_of_task not in hash_of_tasks:
        return "Choose another task"
    return hash_of_tasks[input_name_of_task]()


while True:
    print(console_log_task_by_name())

