
import os
users = []
with open("users.txt","r") as handle:
    users = handle.readlines()

users = [u.strip() for u in users]

masks = []
with open("user_masks.txt","r") as handle:
    masks = handle.readlines()
masks = [m.strip() for m in masks]

import sys
try:
    assignment = sys.argv[1]
    print(f"assignment = {assignment}")
except:
    print("error.  did you name an assignment? \nusage: $ python peer_grade.py <assignment name>\n quitting.")
    sys.exit()

import hashlib
import base64
assignment_masks = {u:0 for u in users}
for u,m in zip(users,masks):
    sha256sum = hashlib.sha256()
    sha256sum.update((u+m+assignment).encode())
    digest = sha256sum.digest()[:8]
    base64EncodedStr = base64.b64encode(digest)

    assignment_masks[u] = base64EncodedStr.decode()

import json
with open("json/"+assignment+"_usermasks.json","w") as handle:
    json.dump(assignment_masks,handle)

import numpy as np
### We now work on associating each user with two other users for the purposes of peer grading.
### We ensure 1) That the user is not assigned the same "other" person twice and
###           2) The user is not assigned him or herself

if len(users) < 3:
    print("Too few users for peer grading")
    assert(0==1)

users_np = np.array(users)
idmap = np.arange(len(users))
usermap2 = np.copy(idmap)
usermap1 = usermap2

while (usermap2==usermap1).any() or (usermap1==idmap).any() or (usermap2==idmap).any():
    usermap1 = np.random.choice(idmap,len(idmap),replace=False)
    usermap2 = np.random.choice(idmap,len(idmap),replace=False)

import shutil
umaps = [usermap1,usermap2]
grader_dict = {u:[] for u in users}
for i,mm in enumerate(umaps):
    for j,user in enumerate(users):
        grader = users[mm[j]]
        grader_dict[user].append(grader)  ## gradee mapped to graders
        src = rf"Collections/{user}/{assignment}"
        dst = rf"Users/{grader}/{assignment}_peer_grade_{i}"
        shutil.copytree(src, dst)
        with open(dst+"/.user","w") as handle:
            handle.write(assignment_masks[user])

        with open(dst+"/grade.txt","w") as handle:
            handle.write("grade for this assignment: \n")

with open("json/"+assignment+"_gradermap.json","w") as handle:
    json.dump(grader_dict,handle)
