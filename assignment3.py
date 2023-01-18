dict={}                         #question 1
a=input("enter string")         #string has more than one word
l=a.split()
print(l)
for i in l:
    c=l.count(i)
    dict.update({i:c})
print(dict)


b=input("enter string")    #string has one word
alpha=["a","b","c","d","e","f"]
for letter in alpha:
    if b.count(letter)>0:

     print("the letter occurs",b.count(letter))

day=int(input("Enter day: "))                #question2
month = int(input("Enter month(integer):"))
year = int(input("Enter year:"))
if month >= 1 and month <= 12 and day >= 1 and day <= 31 and year >= 1800 and year <= 2025:
    print()
else:
    print("Wrong input... not supported")
    exit()
###if the date is not the end of a month(i.e btw 1 and 27)
if day <= 27:
    day = day + 1
    print("Next date is ", day, "/", month, "/", year)
### if the date is 28 of Feb
elif day == 28 and month == 2:
    ###And year is a leap year
    if year % 4 == 0:
        if year%100==0:
          if year%400==0:
           print("Next date is 29/02/", year)
    else:
        print("Next date is 01/03/", year)
elif day == 30:
    ###For months having 30 days
    if month in [4, 6, 9, 11]:
        print("Next date is 01/", month + 1, "/", year)
    else:
        print("Next date is 31/", month, "/", year)
elif day == 31:
    ###if 31st of december
    if month == 12:
        print("Next date is 01/01/", year + 1)
    else:
        print("Next date is 01/", month + 1, "/", year)




#question3
l=list()
x=int(input("enter number"))
y=int(input("enter number"))
z=int(input("enter number"))

l.append(x)
l.append(y)
l.append(z)
print(l)
list2=[]
for i in l:
    t=(i,i*i)
    list2.append(t)
print(list2)


grade_point=int(input("enter grade point:"))            #question4
dic={10:"your grade is A+ and outstanding performance",
     9:"your grade is A and excellent performance",
     8:"your grade is B+ and very good performance",
     7:"your grade is B and Good performance",
     6:"your grade is C+ and average performance",
     5:"your grade is C and below average performance",
     4:"your grade is D and poor performance"}

if grade_point>=4 and grade_point<=10:
    print(dic.get(grade_point))

else:
    print("out of range")



s="ABCDEFGHIJK"                     #question 5
j=0
while len(s) - j*2>=1:
    print(s[0:len(s)-j*2])
    j+=1

    repeat = "Y"                  #question6
    dic = {}

    liste = ["Y", "y", "N", "n"]
    while repeat == "Y" or repeat == "y":
        name = str(input("enter student name:"))
        sid = int(input("enter student sid:"))
        if sid < 0:
            print("error")
        else:
            dic.update({sid: name})

            repeat = str(input("enter Y to continue or N to end:"))
            if repeat == "N" or repeat == "n":
                break

    print(dic)

    enter_sid = int(input("enter sid:"))
    output = dic.get(enter_sid)
    print(output)

n= int(input("Enter the number of fibonacci numbers you wish to average out:"))   #question7
if n<1:
    print("Not supported")
    exit()
###Fibonacci terms
ft=1
prevTerm = 0
###A variable to strore the sum of all the numbers
sumOfNum = 0
print("Fibpnacci series")
for k in range(0,n):
    ###store the sum of fibonacci terms in sumofNum
    sumOfNum += prevTerm
    print(prevTerm,end = " " )
    ###keep adding previous term to get next term
    c = ft
    ft += prevTerm
    prevTerm = c
print("\nAverage of first ",n,"terms is ",sumOfNum/n)







set1 = {1, 2, 3, 4, 5}                   #question 8
set2 = {2, 4, 6, 8}
set3 = {1, 5, 9, 13, 17}

set4 = set1.symmetric_difference(set2)  #a
print(set4)

set_u1 = set1.union(set2)             #b
set_uf = set_u1.union(set3)

set_i1 = set1 & (set2)
set_i2 = set2 & (set3)
set_i3 = set1 & (set3)
set_if = set_i1 & (set3)

set5 = set_uf - set_i1 - set_i2 - set_i3
print(set5)

s_1 = set1 & set3                 #c
s_2 = set2 & set3

s_f = set1.union(set2)
set6 = s_f - s_1 - s_2
print(set6)

setd = set()        #d
for i in range(1, 11):
    setd.add(i)

print(setd)
set7 = setd - set1
print(set7)

setf = set()             #e

for i in range(1, 11):
    setf.add(i)

set8 = setf - set_uf
print(set8)





