cat users.txt | while read line 
do
    rm -rf Users/$line
    rm -rf Collections/$line
done
