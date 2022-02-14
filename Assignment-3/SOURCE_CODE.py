#QUES1

print('ANS 1')

user_inp= input('enter the sentence/word: \n')

user_inp=user_inp.lower()

elements=user_inp.split()

freq={}  # creating an empty dictionary to store key value pairs of words/letters and their occurances

#logic for more than one word string
if len(elements)>1:
 	for n in range (0,len(elements)):
 		if elements[n] in freq:
 			freq[elements[n]]+=1
 		else:
 			freq[elements[n]]=1

#logic when only one word is entered by the user
 			
elif    len(elements)==1:
	single_element=list(user_inp)
	for n in range(0,len(single_element)):
		if single_element[n] in freq:
 			freq[single_element[n]]+=1
		else:
 			freq[single_element[n]]=1

#logic if user does not enter any string
else:
        print('''No string/word detected,
		please enter atleast a single word''')

#printing the occurance of words/letters of the string entered by the user 

print(str(freq))

__________________________________________________________________________________________________________________________________________________________________________________

#QUES2
print('ANS 2')

def is_leap_year(year: int) -> bool:                                                                                #Function for checking if the given year is a leap year or not
    if (year % 4 == 0) and (year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False
while True:
    date = int(input("Day - "))
    month = int(input("Month - "))
    year = int(input("Year - "))
    if (date < 1) or (date > 31) or (month < 1) or (month > 12) or (year < 1800) or (year > 2025):                  #Condition for given constraints in the question
        print("Please use the given conditions for entering the current date\nC1 : 1<=month<=12\nC2 : 1<=day<=31\nC3 : 1800<=year<=2025")
        continue
    if month in (4,6,9,11) and date == 31:                                                                          #Condition for 31 days in a 30 day month
        print("The given month has only 30 days\nPlease enter a valid date")
        continue
    elif month == 2 and date >= 29:                                                                                 #Condition for no. of days in February
        if is_leap_year(year) and date != 29:
            print("The given month has only 29 days\nPlease enter a valid date")
            continue
        elif not is_leap_year(year):
            print("The given month has only 28 days\nPlease enter a valid date")
            continue
    break
if month == 2:                                                                                                      #Setting no. of days in the given month
    if is_leap_year(year):
        max_days = 29
    else:
        max_days = 28
elif month in (4,6,9,11):
    max_days = 30
else:
    max_days = 31
if date == max_days:                                                                                                #Syntax for incrementing the date
    date = 1
    if month == 12:
        month = 1
        year += 1
    else:
        month += 1
else:
    date += 1
print("Next Date is: %d/%d/%d" % (date,month,year))

______________________________________________________________________________________________________________________________________________________________

#QUES3

print('ANS 3')

user_inp=eval(input('enter the list of integers'))
output=[]
for n in user_inp:
	output.append((n,n**2))

print('output: ', output)

_______________________________________________________________________________________________________________________________________________________________

#QUES 4

print('ANS 4')

'''given_table is a list of lists'''
given_table = [ ["A+","Outstanding",10],
                ["A","Excellent",9],
                ["B+","Very Good",8],
                ["B","Good",7],
                ["C+","Average",6],
                ["C","Below Average",5],
                ["D","Poor",4] ]
while True:                                                                                                     #loop for making sure the user inputs the value between 4 and 10
    grade_point = eval(input("Enter the grade point of the student: "))
    if 4 <= grade_point <= 10:
        break
    else:
        print("The grade point must be between 4 and 10")
for i in given_table:                                                                                           #i is for iterating through the lists in the list and j is for iterating through the elements of each list
    for j in i:
        if j == int(grade_point):
            print("Your Grade is '%s' and %s Performance" % (i[0],i[1]))

_________________________________________________________________________________________________________________________________________________________________________________________________________________________________________


#QUES 5

print('ANS 5')

string = "ABCDEFGHIJK"
j = 0
while len(string) - j*2 >= 1:
    print(" "*j + string[0 : len(string) - j*2])
    j += 1      

_____________________________________________________________________________________________________________________________________________________________________________________________________________


#QUES 6

print("ANS 6") 

name=""                                                 #global variable
SID=0                                                   #global variable
z_dict1=dict()                                          #directory created whose keys are SID’s and values are student’s name
while(1):                                               #infinite loop
 Ask_User=str(input("enter Y or N:"))                   
 if (Ask_User=='Y'):                                    #data gets entered in directory if user enters Y   
  name=str(input("enter name:"))                               
  SID=int(input("enter SID:"))
  z_dict1[str(SID)]=name                                   
 elif(Ask_User=='N'):                                                  
  break                                                 #loop breaks if N is entered  
 else:
  print("try again")
print("The Dictionary created is:",z_dict1) 
print("sorting using values:")                         
print(sorted(z_dict1.items(), key =
             lambda kv:(kv[1], kv[0])))                 #to print result of sorting using values 
print ("sorting using keys:")
for i in sorted (z_dict1) :
    print ((i, z_dict1[i]), end =" ")                   #to print result of sorting using keys
print()
D=int(input("enter SID to search:"))
if (str(D)) in z_dict1:
  print(z_dict1[str(D)])                                #to print name of student whose SID is searched for
else:
  print("Wrong SID. Try again") 


_________________________________________________________________________________________________________________________________________________________________________________________________________________________

#QUES 7

print('ANS 7')

'''a is first number, b is second number and c is the extra variable used for adding and reassigning the values'''
a = 0
b = 1
sum = 0
while True:                                                                                                         #While loop is just for asking the user to input the value again if user enters a -ve value
    num = int(input("Enter the no. of terms of the Fibonacci sequence: "))
    if num < 0:
        print("Number of terms must be non-negative\nPlease enter again\n")
        continue
    if num == 0:
        print("As the number of terms = 0, the average of all terms = 0")
        break
    else:
        print("The Fibonacci sequence is as follows:")
        print(a,end=" ")
        for i in range(1,num):
            sum += b
            print(b, end=" ")
            c = a + b
            a = b
            b = c
        print("\nThe average of the terms of Fibonacci sequence upto %d terms is %0.2f" % (num,sum/num))
        break


______________________________________________________________________________________________________________________________________________________________________________________________________________________________________

#QUES8

print('ANS 8')

set1 = {1,2,3,4,5}
set2 = {2,4,6,8}
set3 = {1,5,9,13,17}

print("(a). Set of all elements that are in Set1 and Set2 but not both:",end=" ")
set4 = set1^set2
print(set4)
print("(b). Set of all elements that are in only one of the three sets Set1, Set2 and Set3:",end=" ")
set5 = set1^set2^set3
print(set5)
print("(c). Set of elements that are in exactly two of the sets Set1, Set2 and Set3:",end=" ")
set6 = (set1|set2|set3) - (set1^set2^set3) - (set1&set2&set3)
print(set6)
print("(d). Set of all integers in the range 1 to 10 that are not in Set1:",end=" ")
set7 = set()
for i in range(1,11):
    if i not in set1:
        set7.add(i)
print(set7)
print("(e). Set of all integers in the range 1 to 10 that are not in Set1, Set2 and Set3:",end=" ")
set8 = set(range(1,11)) - (set1|set2|set3)
print(set8)