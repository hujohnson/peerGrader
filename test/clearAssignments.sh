cat users.txt | while read line 
do
    rm -rf Users/$line
    mkdir Users/$line
done
