
cat users.txt | while read line 
mkdir Users
mkdir Collections
do
    mkdir Users/$line
    mkdir Collections/$line
done
mkdir json
mkdir Assignments
