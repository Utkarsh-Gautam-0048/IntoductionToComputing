#QUES1

print("\nANS 1\n")

def tower_hanoi(n,a,b,c):
    if n==1:
        print("Shift 1st disc from",a,"to",c,"\n")
        return
    tower_hanoi(n-1,a,c,b)
    print("Shift disc",n,"from",a,"to",c,"\n")
    tower_hanoi(n-1,b,a,c)
    return

n=int(input("Enter the number of dics = "))
a=input("Enter the name of source = ")
b=input("Enter the name of helper = ")
c=input("Enter the name of destination = ")
tower_hanoi(n,a,b,c)

#_________________________________________________________________________________________________________________________________________


#QUES-2

print("\nANS 2\n")

#input rows
n = int(input("Enter the number of rows in Pascal's Triangle: "))

#using recursions
print("\nUsing recursions:\n")
def pascal(n, originaln=n):
    if n == 0:
        return
    
    pascal(n-1,originaln)

    #printing the spaces
    print('  '*(originaln-n), end='')

    #first number is always 1
    entry = 1
    for i in range(1, n+1):

        print(entry, end ='   ')

        #using Binomial Coefficient
        entry = entry * (n - i) // i
    print()
pascal(n)

#using loops
print("\nUsing loops:\n")
for line in range(1, n+1):

    #everything else same as recursion
    print('  '*(n - line), end='')

    x = 1
    for i in range(1, line+1):

        print(x, end='   ')

        x = x * (line - i) // i
    print()
print("")

#__________________________________________________________________________________________________________________________________________


#QUES-3

print("\nANS 3\n")

a=int(input("Enter the first integer: "))
b=int(input("Enter the second integer: "))
c=a%b
d=a//b
print("Remainder is: ", c)
print("Quotient is: ",d)
if(c!=0):
    if (d!=0):
        print("Both values are non zero")
    else:
        print("One value is zero")
else:
    if (d!=0):
        print("One value is zero")
    else:
        print("Both values are zero")
set1=set()
for i in range (4,7):
    f=c+i
    g=d+i
    if(f>4):
        set1.add(f)
        print(set1)
    if(g>4):
        set1.add(g)
        print(set1)

print(set1)
set2=frozenset(set1)
print("Immutable set: ", frozenset(set1))
print("Largest value in the set: ", max(set2))
k=max(set2)
print("Hash value: ", hash(k))
print("")

#_________________________________________________________________________________________________________________________________________


#QUES-4

print("\nANS 4\n")

class Student:
    def __init__(self, student, sid):
        self.name = student
        self.sid = sid
    
    def __del__(self):
        print("Object destroyed")

#creating object
student1 = Student("Utkarsh Gautam", 21105067)
print("Object created")

#printing the assigned values
print(f"The name of the student it {student1.name} and SID is {student1.sid}.")

#deleting object
del student1

#_________________________________________________________________________________________________________________________________________


#QUES-5

print("\nANS 5\n")



class Employee:                                                                                         
    def __init__(self,name,salary):        
        self.name = name
        self.salary = salary
    def print_data(self):
        print("%s has a salary of %d rupees" % (self.name,self.salary))
employee1 = Employee("Mehak",40000)                                                                     #Creating instances for different employees
employee2 = Employee("Ashok",50000)
employee3 = Employee("Viren",60000)
print("The current database is:")                                                                       #Printing the initial values
for i in [employee1,employee2,employee3]:
    i.print_data()

print("\na. Updated the salary of %s from %d to " % (employee1.name,employee1.salary), end = "")        #Updating salary of Mehak to 70000
employee1.salary = 70000
print(employee1.salary)

print("\nb. Deleted the record of %s(whose salary is %d)" % (employee3.name,employee3.salary))
del employee3

print("\nThe final database is:")                                                                      
for i in [employee1,employee2]:
    i.print_data()


#_____________________________________________________________________________________________________________________________________



#QUES-6


print("\nANS 6\n")


def ana(in1,in2):
    list1=[]
    list2=[]
    sum1=0
    sum2=0
    
    for i in in1:
        list1.append(i)
        sum1+=ord(i)
    for z in in2:
        list2.append(z)
        sum2+=ord(z)
    list1.sort()
    list2.sort()
    if list1==list2  and  sum1==sum2:
         print("STRONG FRIENDSHIP")
    else:
        print("FAKE FRIENDSHIP")
        
    
    
in1=input("Enter the first word here -  ")
in2=input("Enter the second word here -  ")
ana(in1,in2)