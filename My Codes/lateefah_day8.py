import collections
import time

split_sentence = "You don’t matter as much as you think you do, anyway" #input("Enter a sentence: ").split()
split = collections.deque(split_sentence)
direction = "f" #input("Do you want to move it forward or backwards? Type 'F' or 'B':  ").lower()
for words in range(len(split_sentence)):
    if direction == 'f':
        split.rotate(-1)
    elif direction == "b":
        split.rotate(1)
    shifted_list = list(split)
    time.sleep(1)
    print(" ".join(shifted_list))