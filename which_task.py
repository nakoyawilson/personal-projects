import random

# Ask user to input list of tasks separated by commas
tasks = input("Input a list of the tasks you need to complete separated by commas:\n")

# Change tasks string into list format
task_list = tasks.split(",")

# Choose a random task from task_list and print selected task
to_do = random.choice(task_list)
print(f"Right now you should work on: {to_do}")
