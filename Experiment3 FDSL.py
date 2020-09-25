# Experiment 3
#COMPLETE

print('''\n
    1 : Accept FDS Marks
    2 : Average score of class
    3 : Highest score and lowest score of class
    4 : Count of students who were absent for the test
    5 : Display marks with highest frequency
    6 : Exit\n
    ''')

def accept():
    fds=[]
    n=int(input("Enter the students count of class: "))
    for i in range(n):
        print("Enter the marks scored in FDS for students %i: "%(i+1))
        var=int(input())
        fds.append(var)
    print("\n1. Marks scored in fds: ")
    for i in range(n):
        print("Student %i:"%(i+1),fds[i])
    return fds

def average(fds):

    sum=0
    for i in range(len(fds)):
        if(fds[i]!=-1):
            sum=sum+fds[i]
    avg=sum/len(fds)
    print("2. Average score of class: ",avg)
    print("SUM= ", sum)

def highlow(fds):
    print("3. Highest score and lowest score of class: ")
    large=fds[0]
    for i in range(len(fds)):
        if(large<fds[i]):
            large=fds[i]
    print("Highest marks of class: ",large)

    for i in range (len(fds)):
        if(fds[i]!=-1):
            small=fds[i]
            break
    for j in range(len(fds)):
        if(fds[j]!=-1):
            if(small>fds[j]):
                small=fds[j]
    print("Smallest marks of class: ",small)

def absent(fds):
    count=0
    print("4. Count of students who were absent for the test: ")
    for i in range(len(fds)):
        if(fds[i]==-1):
            count=count+1
            print("Absent Student roll is :%i"%(i+1))

    print("Absent student count is: ",count)

def highfre(fds):
    max1=0

    for i in range(len(fds)):
        if(fds[i]!=-1):
            var=fds.count(fds[i])
            if(var>max1):
                max1=var
                res=fds[i]

    print("5. Mark highest frequency: ",res)
    print("count:",max1)


while True:
    ch=int(input("Enter your choice: "))
    if(ch==1):
        fds=accept()
    elif(ch==2):
        average(fds)
    elif(ch==3):
        highlow(fds)
    elif (ch == 4):
        absent(fds)
    elif (ch == 5):
        highfre(fds)
    if (ch == 6):
        break