# The dictionary will look something like:
# {'Andrew Chalkley': ['jQuery Basics', 'Node.js Basics'],
#  'Kenneth Love': ['Python Basics', 'Python Collections']}
#
# Each key will be a Teacher and the value will be a list of courses.
#
# Your code goes below here.

def num_teachers(d):
    count = 0
    for teachers in d:
        count+=1
    print(count)

def num_teachers2(d):
    print(len(d))
    
teachers ={'Andrew Chalkley': ['jQuery Basics', 'Node.js Basics'],'Kenneth Love': ['Python Basics', 'Python Collections']}

num_teachers(teachers)
num_teachers2(teachers)

