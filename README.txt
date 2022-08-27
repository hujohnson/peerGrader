## Peer grading system

### Setup

You need a directory called `Users` with one subdirectory for each student in the class.  The subdirectory corresponding to a student is shared with that student through Dropbox or some other means. 

Example:
```
[hunter@metis test]$ ls Users/
A@B.com/ C@D.edu/ E@F.io/
```
In the examples we use in this README the "students" are represented by their "email addresses", A@B.com, C@D.com, and E@F.com.  You do not have to name the directories after the email addresses -- it could be their actual names, student IDs, etc.

You need a file `users.txt` which contains the subdirectory names in `Users`.  If you start with `Users` you can make `users.txt` as `ls Users > users.txt`.  If you are starting instead with `users.txt`, the script `create_folders.sh` will create the Users directory and appropriate subdirectories (see below).

Example:

```
[hunter@metis test]$ cat users.txt
A@B.com
C@D.edu
E@F.io
```

### Creating directories

The `create_folders.sh` script is a simple bash script for creating necessary directories. It may complain benignly if some of the directories already exist.

```
[hunter@metis test]$ cat create_folders.sh

mkdir Users
mkdir Collections
cat users.txt | while read line
do
    mkdir Users/$line
    mkdir Collections/$line
done
mkdir json
mkdir Assignments



[hunter@metis test]$ tree
.
├── Assignments
│   ├── Exercise1
│   │   └── hi.py
│   └── Exercise2
│       ├── a_mule.txt
│       └── blatherskite.bin
├── Collections
│   ├── A@B.com
│   ├── C@D.edu
│   └── E@F.io
├── Users
│   ├── A@B.com
│   ├── C@D.edu
│   └── E@F.io
├── assign.sh
├── assign_peers.py
├── clearAssignments.sh
├── clearCollections.sh
├── clearUsers.sh
├── collect.sh
├── create_folders.sh
├── json
├── make_user_masks.py
├── peer_collect.py
└── users.txt

12 directories, 13 files
```

### Creating Assignments

Put assignments for distribution inside the Assignments directory.

For example 

```
[hunter@metis test]$ tree
.
├── Assignments
│   ├── Exercise1
│   │   └── hi.py
│   └── Exercise2
│       ├── a_mule.txt
│       └── blatherskite.bin
```

### Make user masks

To make peer grading double blind, each student will have a random alias for each assignment.

At setup time you must run `make_user_masks.py` to create random numbers for each student which will be used in this process.  These numbers must be kept hidden from the students to stop them from discovering one another's identities during peer grading. 

Run the script `make_user_masks.py`. The random values created will be written to the file `user_masks.txt`.  The mapping between students and random numbers is accomplished by matching line numbers in `user_masks.txt` and `users.txt`.  Do not permute user order in `users.txt` or it will break the association.

Example: 

```
[hunter@metis test]$ python3 make_user_masks.py
['A@B.com', 'C@D.edu', 'E@F.io']
[hunter@metis test]$ cat user_masks.txt
278189791997560362482686459475653195890
158555902892529754309329290008356525273
314983665354795714846349708801057837316
```

### Distributing an Assignment

To distribute an assignment to students, use the `assign.sh` script. It takes as a parameter the name of the corresponding subdirectory of `Assignments`.

Example:

```
[hunter@metis test]$ bash assign.sh Exercise1
Assignment is Exercise1
[hunter@metis test]$ tree
.
├── Assignments
│   ├── Exercise1
│   │   └── hi.py
│   └── Exercise2
│       ├── a_mule.txt
│       └── blatherskite.bin
├── Collections
│   ├── A@B.com
│   ├── C@D.edu
│   └── E@F.io
├── Users
│   ├── A@B.com
│   │   └── Exercise1
│   │       └── hi.py
│   ├── C@D.edu
│   │   └── Exercise1
│   │       └── hi.py
│   └── E@F.io
│       └── Exercise1
│           └── hi.py
├── assign.sh
├── assign_peers.py
├── clearAssignments.sh
├── clearCollections.sh
├── clearUsers.sh
├── collect.sh
├── create_folders.sh
├── json
├── make_user_masks.py
├── peer_collect.py
├── user_masks.txt
└── users.txt

15 directories, 17 files
```


### Students do the Assignment

At this stage we assume that students actually complete the assignment.  There is nothing for the administrator to do at this stage.

### Collect Student Work

After students have completed their work, their work can be collected.  Do this with the `collect.sh` script. This script takes the name of the assignment (as a subdirectory of `Assignments`) as a parameter.  It copies student work into appropriate subdirectory ofthe `Collections` directory.

Example

```
[hunter@metis test]$ bash collect.sh Exercise1
Assignment is Exercise1
[hunter@metis test]$ tree
.
├── Assignments
│   ├── Exercise1
│   │   └── hi.py
│   └── Exercise2
│       ├── a_mule.txt
│       └── blatherskite.bin
├── Collections
│   ├── A@B.com
│   │   └── Exercise1
│   │       └── hi.py
│   ├── C@D.edu
│   │   └── Exercise1
│   │       └── hi.py
│   └── E@F.io
│       └── Exercise1
│           └── hi.py
├── Users
│   ├── A@B.com
│   │   └── Exercise1
│   │       └── hi.py
│   ├── C@D.edu
│   │   └── Exercise1
│   │       └── hi.py
│   └── E@F.io
│       └── Exercise1
│           └── hi.py
├── assign.sh
├── assign_peers.py
├── clearAssignments.sh
├── clearCollections.sh
├── clearUsers.sh
├── collect.sh
├── create_folders.sh
├── json
├── make_user_masks.py
├── peer_collect.py
├── user_masks.txt
└── users.txt

18 directories, 20 files
```

The work in the Collections folder is no longer modifiable by any student.  

### Assign Peer Graders

We now assign the work of each student at random to two other students.  It is assured that the graders do not get the same gradee twice, and that the gradee and the grader are never identical.

This job is done by the `assign_peers.py` script.  It takes the name of the assignment (as a subdirectory of Assignments) as an argument. Assignments to be graded appear for the student in their user directory.

Example:

```
[hunter@metis test]$ python assign_peers.py Exercise1
assignment = Exercise1
[hunter@metis test]$ tree
.
├── Assignments
│   ├── Exercise1
│   │   └── hi.py
│   └── Exercise2
│       ├── a_mule.txt
│       └── blatherskite.bin
├── Collections
│   ├── A@B.com
│   │   └── Exercise1
│   │       └── hi.py
│   ├── C@D.edu
│   │   └── Exercise1
│   │       └── hi.py
│   └── E@F.io
│       └── Exercise1
│           └── hi.py
├── Users
│   ├── A@B.com
│   │   ├── Exercise1
│   │   │   └── hi.py
│   │   ├── Exercise1_peer_grade_0
│   │   │   ├── grade
│   │   │   └── hi.py
│   │   └── Exercise1_peer_grade_1
│   │       ├── grade
│   │       └── hi.py
│   ├── C@D.edu
│   │   ├── Exercise1
│   │   │   └── hi.py
│   │   ├── Exercise1_peer_grade_0
│   │   │   ├── grade
│   │   │   └── hi.py
│   │   └── Exercise1_peer_grade_1
│   │       ├── grade
│   │       └── hi.py
│   └── E@F.io
│       ├── Exercise1
│       │   └── hi.py
│       ├── Exercise1_peer_grade_0
│       │   ├── grade
│       │   └── hi.py
│       └── Exercise1_peer_grade_1
│           ├── grade
│           └── hi.py
├── assign.sh
├── assign_peers.py
├── clearAssignments.sh
├── clearCollections.sh
├── clearUsers.sh
├── collect.sh
├── create_folders.sh
├── json
│   ├── Exercise1_gradermap.json
│   └── Exercise1_usermasks.json
├── make_user_masks.py
├── peer_collect.py
├── user_masks.txt
└── users.txt

24 directories, 34 files
```

When this script is run, two files are added to the peer grading directory (eg `Exercise1_peer_grade_0`): `grade.txt` and `.user`.

The file `.user` contains the base64 encoding of the first 8 bytes of

```
SHA256(<username>|<r>|<assignment name>)
```

where <r> is the random number associated to the user in the `user_masks.txt` file. 

Example:

```
[hunter@metis test]$ cat Users/A\@B.com/Exercise1_peer_grade_1/.user
RoPgVqnWuow=
```

This means that user `A@B.com` is grading the work of the user corresponding to the identifier `RoPgVqnWuow=`.  Because of the dependence on the assignment name, users will have different secret identifiers for each assignment. 

The mappings are stored in the `json` directory in the file `json/<assignment_name>_usermasks.json`.

Example:

```
[hunter@metis test]$ ls json
Exercise1_gradermap.json  Exercise1_usermasks.json
[hunter@metis test]$ cat json/Exercise1_usermasks.json
{"A@B.com": "iHwDsiNlNjk=", "C@D.edu": "RoPgVqnWuow=", "E@F.io": "qXeKID8UvF8="}
```

Thus in our example `A@B.com` is grading `C@D.com`, though neither student is aware of this relationship. 

The gradee is associated with both his or her graders via the file `json/<assignment_name>_gradermap.json`. 

Example:
```
[hunter@metis test]$ cat json/Exercise1_gradermap.json
{"A@B.com": ["C@D.edu", "E@F.io"], "C@D.edu": ["E@F.io", "A@B.com"], "E@F.io": ["A@B.com", "C@D.edu"]}
```

### Students Perform Peer Grading

At this stage we assume that students actually perform the task of peer grading one another.

When they have made their evaluation (possibly with a provided key or rubric) the indicate their grade in the following way.

They open the file `grade.txt` and put their grade in the indicated loction.

Example (before grade is added by grader):

```
$ cat Users/A\@B.com/Exercise1_peer_grade_0/grade.txt
grade for this assignment:
```

Example (after grade is added by grader):

```
$ cat Users/A\@B.com/Exercise1_peer_grade_0/grade.txt
grade for this assignment: A+
```


### Collecting the Peer Grading

We must now "harvest" the grades assigned by the peer graders.  This work is done by the `peer_collect.py` script.

The output might look something like the following:

```
hunter@metis classManager]$ python3 peer_collect.py Exercise1
assignment = Exercise1
{'ZDMsKAKBzFE=': 'A@B.com', '5VEdxsXjeaA=': 'C@D.edu', 'tCJJMDPyHpo=': 'E@F.io'}
A@B.com graded C@D.edu

grade for this assignment: C

C
C@D.edu graded E@F.io

grade for this assignment: A

A
E@F.io graded A@B.com

grade for this assignment: A+

A+
A@B.com graded E@F.io

grade for this assignment: B

B
C@D.edu graded A@B.com

grade for this assignment: D+

D+
E@F.io graded C@D.edu

grade for this assignment: B-

B-
{'A@B.com': ['E@F.io gives A+', 'C@D.edu gives D+'], 'C@D.edu': ['A@B.com gives C', 'E@F.io gives B-'], 'E@F.io': ['C@D.edu gives A', 'A@B.com gives B']}
```

At the bottom of the output you can see in `json` form a simple association from each gradee to the grades supplied by the two graders.  This is also stored in the `json` directory as the file `<assignment_name>_grades.json`.

Example:

```
$ cat json/Exercise1_grades.json
{"A@B.com": ["E@F.io gives A+", "C@D.edu gives D+"], "C@D.edu": ["A@B.com gives C", "E@F.io gives B-"], "E@F.io": ["C@D.edu gives A", "A@B.com gives B"]}[
```

You can then manually enter the grade you think appropriate in the gradebook for the course, perhaps after consulting the work of each student. 


