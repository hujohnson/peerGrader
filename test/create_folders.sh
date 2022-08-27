
mkdir Users
mkdir Collections
cat users.txt | while read line 
do
    mkdir Users/$line
    mkdir Collections/$line
done
mkdir json
mkdir Assignments
