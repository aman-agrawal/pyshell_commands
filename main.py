import sys,os,getpass,re,shlex,glob,difflib
from string import maketrans

def ls() :
    content = os.listdir(".")
    content.sort()
    for i in content : 
        print i

def pwd(cwd):
    print "pwd : ", cwd

def cat(str):
    with open(str) as x:
        for line in x:
            print line
    print  

def cd(str) :
    try:
        os.chdir(cwd+"/"+str)
    except:
        print "directory not found"  

def touch(str):
    filepath = cwd + "/" + str
    file= open(filepath,"w+")   
    print "operation successful" 

def grep(data,filename):
    file = open(filename, "r")
    for line in file:
         if re.search(data, line):
             print line

def head(filename):
    count=0
    with open(filename) as x:
        for line in x:
            if count<10:
                print line
                count=count+1

def tail(filename):
    count=0
    with open(filename) as x:
        for line in x:
                count=count+1                

    with open(filename) as x:
        if count<11:
            for line in x:
                print line
        else:
            rem=count-10       
            for line in x:
                if rem>0:
                    rem=rem-1
                else:
                    print line    
 
def sed(arr):
        sed_regex = arr[1].split('/')
        target = sed_regex[1]
        
        sub = sed_regex[2]
        
        with open(arr[2]) as f:
            for line in f:
                line_tokens = re.split(' |\n', line)
                for word in line_tokens:
                    if re.match(target, word):
                        print sub
                    else:
                        print word

def diff(arr):
    try:
            type(arr[1])
            type(arr[2])
            
            try:
                file1=open(arr[1],"r")
            except:
                print "Unable To Open ",arr[1]

            try:
                file2=open(arr[2],"r")
            except:
                print "Unable To Open ",arr[2]

            diff=difflib.ndiff(file1.readlines(),file2.readlines())
            while 1:
                try:
                    print diff.next(),
                except:
                    break

    except:
            print "Invalid Command"

def tr(arr):
    pattern1 = arr[1].replace('"' , '')
    pattern2 = arr[2].replace('"' , '')
    filename = arr[3]
    if os.path.exists(filename) == False:
        print "file dont exists"
        return
    try:
        file = open(filename , "r")
        for line in file :
            print re.sub(pattern1 , pattern2 , line)
    except:
        print "error"
    finally :
        file.close()

while 1:
    cwd = os.getcwd()
    str = raw_input(getpass.getuser()+"*****"+cwd+ "> ")
    arr = str.split(' ')

    if(arr[0] == "ls"):
        ls()
        # ls
    elif(arr[0] == "cd"):
        cd(arr[1])
        # cd .. or cd foldername
    elif(arr[0] == "head"):
        head(arr[1])
        # head customers.txt
    elif(arr[0] == "tail"):
        tail(arr[1])
        # tail customers.txt
    elif(arr[0] == "pwd"):
        pwd(cwd)
        # pwd
    elif(arr[0] == "touch"):
        touch(arr[1])
        # touch filename.txt
    elif(arr[0] == "grep"):
        grep(arr[1],arr[2]) 
        # grep aman customers.txt   
    elif(arr[0] == "sed"):
        sed(arr)
        # sed s/aman/sonu customers.txt
    elif(arr[0] == "diff"):
        diff(arr)
        # diff customers.txt products.txt
    elif(arr[0] == "tr"):
        tr(arr)
        # tr "aman" "ram" customers.txt
    elif(arr[0] == "cat"):
        cat(arr[1])
        # cat filename
    elif(arr[0] == "exit"):
        break
        # exit