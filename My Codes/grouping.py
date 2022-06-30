import random
student_list = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
random.shuffle(student_list)

# Grouping students into groups of 3
group_list = []
for i in range(0, len(student_list), 4):
    group_list.append(student_list[i:i+4])

for i in range(len(group_list)):
    random.shuffle(group_list[i])
    print(f"Group {i+1}: {group_list[i]}")