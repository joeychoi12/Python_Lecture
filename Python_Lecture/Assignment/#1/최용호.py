# Python Assignment 1


#7
seconds = 0
secondsHour = 0
secondsMinutes = 0
for i in range(0,25):
    if '3' in str(i):
        secondsHour += (60*60)
for j in range(0,60):
    if '3' in str(j) :
        secondsMinutes += 60
seconds = secondsHour + secondsMinutes
print(seconds,"seconds")


#10
naturalNum = int(input("Enter a Natural Number:"))
sumOfNum = 0
sumSquared = 0
sumOfSquared = 0
for i in range(1,naturalNum+1):
    sumOfSquared += (i ** 2)
    sumOfNum += i
ans = (sumOfNum ** 2) - sumOfSquared
print(ans)


# 9 완전수 Generator
num = int(input("Enter a number: "))
num_list = []
perfect_num = []

for i in range(1,num):
    sum_num = 0
    for j in range (1, i):
        if i % j == 0 :
            sum_num += j
    if i == sum_num :
        perfect_num.append(i)

print(perfect_num)







#8
numbers = [0] *10
for i in range(1,1001):  #1~1000
    for j in str(i):
        numbers[int(j)]+=1
for i in range(10):
    print(i,":", numbers[i])



count={ x:0 for x in range(0,10) }

for x in range(1,1001):
    for i in str(x):
        count[int(i)]+=1

print(count)



#7
seconds = 0
secondsHour = 0
secondsMinutes = 0
for i in range(0,24):
    if '3' in str(i):
        secondsHour += 60*60
for j in range(0,60):
    if '3' in str(j) :
        secondsMinutes += 60
seconds = secondsHour + secondsMinutes
print(seconds,"seconds")

#6


line = int(input("Diamond 의 길이를 입력하세요 : "))
line = line -2
for x in range(1, line * 2, 2):
        print((" " * ( (line * 2 - 1 - x) // 2 )) + ("*" * x))

for y in range(line * 2-3, 0, -2):
        print((" " * ( (line * 2 - 1 - y) // 2 )) + "*" * y)






# 반 복 문


#5
testCase = input('Test Case Num: ')
for i in range(1, int(testCase)+1 ):
    a,b = map(int,input("Enter Num: ").split())
    print("Case #",i,"\n",a, " + ",  b, " = ", a+b)

print("goodbye")


# 조 건 문

#4
a = 0
b = 0
c = 0
for i in range(1,500):
    for j in range (1, 500):
        for k in range(1,500):
            if i + j + k == 1000:
                if (i + j) > k:
                    if i**2 + j**2 == k**2:
                        a = i
                        b = j
                        c = k
print(a, b, c)

#3
a,b,c = map(int, input("Enter 3 numbers: ").split())
ans = 0
if a > b :
    ans = a
elif b > a :
    ans = b
if c>ans :
    ans = c
print('the biggest number is: ', ans)


#2
hour,time = input("Enter Time: ").split(':')
hour = int(hour)
time = int(time)
if time < 45:
    hour -= 1
    time += (60 - 45)
else:
    time -= 45
if time == 0:
    time = "00"
if hour == 0:
    hour = 24
print(hour,":",time)

# 1

exit1 = False
while exit1 == False:
    year = int(input("Enter Year to check Leap year: "))
    check = False
    if year %  400 == 0 :
       check = True
    elif year % 100 == 0 :
         check = False
    elif year % 4 == 0 :
        check = True
    if check:
        print(year, "is a Leap Year")
    else:
        print(year, "is not a Leap Year")
    y_n = input("again? (Y/N)")
    if y_n == "n" or y_n == "no" :
        exit1 = True
    else:
        exit1 = False


