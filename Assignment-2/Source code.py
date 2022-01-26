#______________________________________________________________________________________________________________________________________________________
#[QUES1]

print('ANS 1')

inp_str='Python is a case sensitive language'                                     #inp_str= input string

#(a)
print('\n(a)length of input string is:\n', len(inp_str))                            #printing the length of the given input string
#......................................................................................................................................................

#(b)
print('\n(b)string in reverse order is:\n', inp_str[::-1])                        #reversing the order of input string in one line code
#......................................................................................................................................................

#(c)
new_str=inp_str[10:26]                                                #storing 'a case sensitive' in a new string named new_str using slice function
print('\n(c)new_str=\n', new_str)                                               
#......................................................................................................................................................

#(d)
new_str2=inp_str[0:10]+'object oriented'+inp_str[27:]                    #replacing 'a case sensitive' with 'object oriented'
print('\n(d)new string after replacing:\n', new_str2)
#.......................................................................................................................................................

#(e)
index=inp_str.find("a")                                                  #finding index of substring "a" in the given input string
print('\n(e)The index of substring "a" is:\n', index)
#........................................................................................................................................................

#(f)
new_str3=inp_str.replace(' ', '')                                        #removing all white spaces from the given input string
print('\n(f)input string with white spaces removed:\n', new_str3)


#_________________________________________________________________________________________________________________________________________________________
#_________________________________________________________________________________________________________________________________________________________

#QUES2

print('ANS 2')

Name=input('Please enter your name:\n')
SID=int(input('\nPlease enter your SID:\n'))
Dep_name=input('\nPlease enter your Department name:\n')
CGPA=float(input('\nPlease enter your CGPA:\n'))

print('Hey, %s Here!'%(Name))
print('My SID is %d'%(SID))
print('I am from %s department and my CGPA is %f'%(Dep_name,CGPA))

#_________________________________________________________________________________________________________________________________________________________
#_________________________________________________________________________________________________________________________________________________________

#QUES 3

print('ANS 3')

a=56
b=10

#(a)
print('\n(a)  a&b =', a&b)

#.......................................................................................................................................................

#(b)
print('\n(b) a|b =', a|b)

#.......................................................................................................................................................

#(c)
print('\n(c) a^b =', a^b)

#........................................................................................................................................................

#(d)
print('\n(d)')
print('After left shift by 2-bits, a =', a<<2)
print('After left shift by 2-bits, b =', b<<2)

#........................................................................................................................................................

#(e)
print('\n(e)')
print('After right shift by 2-bits, a=', a>>2)
print('After right shift by 4-bits, b=',b>>4)

#_________________________________________________________________________________________________________________________________________________________
#_________________________________________________________________________________________________________________________________________________________

#QUES4

print('ANS 4')

# Taking input from user...

num1=int(input('\nEnter the first number-\n'))
num2=int(input('\nEnter the second number-\n'))
num3=int(input('\nEnter the thied number-\n'))

if num1>=num2 and num1>=num3:
    print('\nThe greatest number is-',num1)
    
elif num2>=num1 and num2>=num3:
    print('\nThe greatest number is-',num2)
else:
    print('\nThe greatest number is-',num3)

#_________________________________________________________________________________________________________________________________________________________
#_________________________________________________________________________________________________________________________________________________________

#QUES 5

print('ANS 5')


user_input=input('Enter the sentence/string -\n ')                                        
string1='name'
if string1 in user_input:
    print("/nYes")
else: 
    print("/nNo")

#_________________________________________________________________________________________________________________________________________________________
#_________________________________________________________________________________________________________________________________________________________

#QUES 6

print('ANS 6')

length_1=int(input('\nPlease enter the 1st length:\n'))
length_2=int(input('\nPlease enter the 2nd length:\n'))
length_3=int(input('\nPlease enter the 3rd length:\n'))

if length_1>(length_2+length_3) or length_2>(length_1+length_3) or length_3>(length_2+length_1):
	print('\nNO, the entered three lengths cannot form a triangle')
else:
	print('\nYES, the entered three length can form a triangle')
