
echo "Assignment is $1"
cat users.txt | while read line 
do
    cp -R Assignments/$1 Users/$line/$1
done
