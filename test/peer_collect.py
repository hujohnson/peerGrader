import json
import sys

import sys
try:
    assignment = sys.argv[1]
    print(f"assignment = {assignment}")
except:
    print("error.  did you name an assignment? \nusage: $ python peer_grade.py <assignment name>\n quitting.")
    sys.exit()

with open("json/"+assignment+"_usermasks.json","r") as handle:
    assignment_masks=json.load(handle)

mask_decoder = {v:k for (k,v) in assignment_masks.items()}

print(mask_decoder)

graders = []
with open("users.txt","r") as handle:
    graders = handle.readlines()

graders = [g.strip() for g in graders]
grades = {g:[] for g in graders}
for i in [0,1]:
    for g in graders:
        userfile = rf"Users/{g}/{assignment}_peer_grade_{i}/.user"
        gradefile = rf"Users/{g}/{assignment}_peer_grade_{i}/grade.txt"
        with open(userfile,"r") as handle:
            usermask = handle.read().strip()
        gradee = mask_decoder[usermask]
        print(f"{g} graded {gradee}\n")
        with  open(gradefile,"r") as handle:
            gradeline = handle.readline()
        print(gradeline)
        grade = gradeline[gradeline.find(":")+1:].strip()
        print(grade)
        grades[gradee].append(g+" gives "+grade)

print(grades)

with open("json/"+assignment+"_grades.json","w") as handle:
    assignment_masks=json.dump(grades,handle)

