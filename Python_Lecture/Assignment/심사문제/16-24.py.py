### 심사 문제 from 코딩도장
#### 16 구구단 출력
number = int(input())
for i in range (1,10):
    print(number, '*', i, '=',number*i)

#### 17 교통카드 잔액 출력
cardamount = int(input())
while cardamount >= 1350 :
    cardamount -= 1350
    print(cardamount)

#### 18 While Loop
start, stop = map(int, input().split())

i = start

while True:
    if i % 10 == 3:
        i += 1
        continue
    if i > stop:
        break
    print(i, end=' ')
    i += 1

#### 19 별 출력
num = int(input())
for i in range(1, num+1):
    print(" "*(num-i), "*"*(2*i-1))


for i in range(5):
    for j in range(5):
        if  i >=j       :
            print('*', end='')
    print()

#### 20
a,b = map(int,input().split())
for i in range(a,b+1):
    if i % 5 == 0 and i % 7 == 0:
        print("FizzBuzz")
    elif i % 7 == 0 :
        print("Buzz")
    elif i % 5 == 0 :
        print("Fizz")
    else:
        print(i)

#### 21 Turtle  *** Needs Checking***  Cannot run
import turtle as t

n, line = map(int, input().split())
t.shape('turtle')
t.speed('fastest')
a, b = map(int, input().split())
for i in range(a):
    t.forward(b)
    t.right((360 / a) * 2)
    t.forward(b)
    t.left(360 / a)


#### 22

a,b = map(int, input().split())
listab = []
for i in range(a,b+1):
    ans = 2 ** i
    listab.append(ans)
listab.pop(1)
listab.pop(-2)
print(listab)

#### 23 mine sweeper
from pprint import pprint

col, row = map(int, input().split())
matrix = []
for i in range(row):
    matrix.append(list(input()))
pprint(matrix, indent=2)


def countMines(i, k):
    if matrix[i][k] == '*':
        return '*'

    count = 0
    for r in range(i - 1, i + 2):
        for c in range(k - 1, k + 2):
            if r < 0 or c < 0 or r >= row or c >= col:
                continue
            if matrix[r][c] == "*":
                count += 1
    return count


for i in range(row):
    for k in range(col):
        print(countMines(i, k), end='')
    print()


#### 24

thecount = []
thecount = input().split()
a = 0
for i in range(len(thecount)):
    if thecount[i].strip(",.") == 'the':
        a += 1
print(a)

lista = []
lista = map(int,input().split(";"))
lista = list(lista)
lista.sort(reverse=True)
for i in range(len(lista)):
    print('%9s' % format(lista[i],','))