cat users.txt | while read line 
do
    rm -rf Collections/$line
    mkdir Collections/$line
done
