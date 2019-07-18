import turtle as t
t.shape('turtle')
t.forward(100)
t.right(90)
t.forward(100)

aList = [10,20,30,40,50]
for a in aList:
    print(a)

for letter in "Python":
    print(letter)

fruits = ("applee", "banana", "orange")
for a in fruits :
    print(a)

lux = dict(zip(['health','mana','meelee'],[490,334,550]))
for key in lux:
    print(key, '=', lux[key])


sum = 0
for i in range(1,101):
    sum += i
print(sum)

factorial = 1
for i in range(1,11):
    factorial *= i
nominator = factorial
facotiral = 1
for i in range(1,6):
    factorial *= i

denom = factorial
print(nominator / (denom * denom))

import random as rd
i = 0
while i !=3:
    i=rd.randint(1,6)

while True:
    dice = rd.randint(1,6)
    print(dice)
    if dice == 3:
        break

while True:
    dice = rd.randint(1,6)
    print(dice)
    if dice == 3:
         break

print("2 Dice is larger than 10 break ")
i = 0
while True:
    dice = rd.randint(1,6)
    dice2 = rd.randint(1,6)
    print(dice, " + ", dice2, " = ", dice + dice2)
    i += 1
    if (dice + dice2) >= 10 :
        print('loop = ', i)
        break

# 홀수만 출력
for i in range(100) :
    if i % 2 == 0 :
        continue
    print(i, end= ' ')

#별 출력
for i in range(6):
    for k in range(i):
        print("*" , end = '')
    print()


for i in range(5):
    for j in range(5):
        if j == i:
            print("*", end = "")
        else:
            print('',end = " ")
    print()

for i in range(5):
    for j in range(5):
        print('j:', j, sep='', end=' ')
    print('i:', i, '\\n', sep='')

#Revuerse diagonal
for i in reversed(range(5)):
    for k in range(i):
        print(' ', end='')
    print('*')

#Bubble Sort
aList = [5,4,21,11,15, 22,23,2,1,55,835]

for i in range(len(aList)-1):
    for k in range(i+1, len(aList)):
        if aList[i] > aList[k]:
            aList[i], aList[k] = aList[k],aList[i]
print(aList)


# 오름차순 버블 소트
#aList = list[5,4,21,3,15,2,666,23,142,2]
#aList = list(map(int,input("Enter Number: ").split()))
print(aList)

for i in range(0, len(aList)-1):
    for k in range(i+1, len(aList)):
        if aList[i] > aList[k]:
            aList[i],aList[k] = aList[k], aList[i]
print(aList)

#
print("Loop for FIzzBuzz")
for i in range(1,101): # 1부터 100까지 반복
    if i % 3 == 0 and i % 5 == 0 :
        print('FizzBuzz')
    elif i % 3 == 0: #3의 배수
        print('Fizz')
    elif i % 5 == 0 :
        print("Buzz")

    else:
        print(i)

# Code_Golf.py
print("Code Golf")
for i in range(1,101):
    print('Fizz' * (i % 3 == 0) + 'Buzz' * (1% 5 == 0) or i)



def solution(n):
    answer = []
    a = list(str(n))
    answer = sorted(list(map(int,a)),reverse = True)
    return answer

print(solution(5555321))
print(solution(12345677892130123))