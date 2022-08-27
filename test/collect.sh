
echo "Assignment is $1"
cat users.txt | while read line 
do
    cp -R Users/$line/$1 Collections/$line/$1
done
