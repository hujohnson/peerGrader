users = []
with open("users.txt","r") as handle:
    users = handle.readlines()
users = [u.strip() for u in users]
print(users)
import random
with open("user_masks.txt","w") as handle:
    for u in users:
        r=random.getrandbits(128)
        handle.write(f"{r}\n")


