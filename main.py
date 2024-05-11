import os

# # print("hellow world")


# """
# """
# if not os.path.exists("Nikhil"):
#     os.mkdir("Nikhil")

for i in range(50, 101):
    os.mkdir(f"day {i} challenge")
    with open(f"day {i} challenge/main.py", "w") as file:
        file.write('print("Hello Nikhil")')
    with open(f"day {i} challenge/plan.txt", "w") as file:
        file.write('Hello Nikhil')
    with open(f"day {i} challenge/ref.py", "w") as file:
        file.write('print("Hello Nikhil")')
