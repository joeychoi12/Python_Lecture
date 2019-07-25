#9
a = [1,3,5,7,9]
b = list(map(lambda x: x**2, a))
print(b)

#8
from pprint import pprint
import random as rm
row = 5
col = 5

matrix = []

for i in range(row):
    numList = []
    for k in range(col):
        numList.append(str(rm.randint(1,4)))

    matrix.append(list(numList))
pprint(matrix,indent=2)

###
tile = []
for i in range(5):
    row =5


def converter(i, k):
    if matrix[i][k] == matrix[i - 1][k] and matrix[i][k] == matrix[i+1][k]:
        return '*'
    if matrix[i][k] == matrix[i][k-1] and matrix[i][k] == matrix[i][k + 1]:
        return '*'
    else:
        return matrix[i][k]


for i in range(row):
     for k in range(col):
         print(converter(i, k), end='')
         print()

#7
def isPalindrome(a):
    for i in range(len(a)//2):
        if a[i] != a[-1-i]:
            return False
    return True

maxNum = 0
for i in range(100, 1000):
    for k in range(i, 1000):
        if isPalindrome(str(i*k)):
            if i*k > maxNum:
                maxNum = i*k
                maxA = i
                maxB = k
print(maxA, maxB)

#6
vegatables = {'가지':800, '오이':600, '수박': 15000, '호박':1000,
              '깻잎':500}

sorted(vegatables.values())
for key, value in sorted(vegatables.items(), key=lambda item: item[1],reverse=True):
    print("%s: %s" % (key, value) )

#5
bts = ['RM','진','슈가','제이홉','지민','뷔','정국']
#(1)
print(bts[5])
#(2)
print(bts[:1])
#(3)
print(bts[5:])
#(4)
print(bts[2:5])

#(5)
print(bts[::2])

#4
#연 복리 이자율을 입력 (단위 %) 원금이 2배가 되는데 최소 몇녀 걸리는 지 출력
int_rate = input("연 복리 이자율(%): ")
money= int(input("원금 입력: "))
int_rate = int((int_rate).strip("%"))/100
year = 1
doublemoney = money *2
while money <= doublemoney:
    money += money*int_rate
    year += 1
print(year)

#3
# get 2 int from small number to big num add the num of odd num
a,b = map(int,input("Input integer: ").split())
ab = []
if b>a :
    if a % 2 == 1:
        for i in range(a,b+1,2):
            ab.append(i)
    else:
        for i in range(a,b+1):
            if i % 2 == 1:
                ab.append(i)
else:
    if b % 2 == 1:
        for i in range(b,a+1,2):
            ab.append(i)
    else:
        for i in range(b,a+1,2):
            if i % 2 == 1:
                ab.append(i)

print(sum(ab))
