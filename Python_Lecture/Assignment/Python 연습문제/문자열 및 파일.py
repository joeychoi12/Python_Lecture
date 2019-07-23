# Is Palindrome function
def isPalindrome(a):
    for i in range(len(a)//2):
        if a[i] != a[-1-i]:
            return False
    return True
maxNum = 0
for i in range(100, 1000):
    for k in range(100,1000):
        if isPalindrome(str(i*k)):
            if i*k > maxNum:
                maxNum = i*k
                maxA= i
                maxB=k
print(maxNum, maxA,maxB)



# 문자 암호
plain, n = input('암호화할 문자열과 N값: ').split()
plain = [c for c in plain]
n = int(n)

LETTER_A = ord('A')
LETTER_Z = ord('Z')
cypher = []
for letter in plain:
    if ord(letter) + n > LETTER_Z:
        cypher.append(chr(LETTER_A + ord(letter) + n - LETTER_Z -1))
    else:
        cypher.append(chr(ord(letter) + n))
print(''.join(cypher))

# 파일명 문자 찾기
word, filename = input("찾고자 하는 문자여로가 파일명: ").split()

lineNo = 1
with open(filename, 'r', encoding ='UTF-8') as file:
    for line in file:
        if line.find(word) >= 0:
            print('%2d: '% lineNo, line, end= '')
        lineno += 1


# Word Count
# UNIX wx
filename = input('파일이름: ')
wordsDict = dict()

with open(filename, 'r')as file:
    for line in file:
        linewords = line.replace('(', ' ').replace(')', ' ') \
            .replace(',', ' ').replace('.', ' ').split()

        # print linewords
        for word in linewords:
            count = wordsDict.get(word, 0)
            # print(count,end=' ')
            if count == 0:
                wordsDict.setdefault(word, 1)
            else:
                wordsDict.update(dict([(word, count + 1)]))
import operator

wordList = sorted(wordsDict.items(), key=operator.itemgetter(1), reverse=True)
for i in range(10):
    print(wordList[i])

# 5 Create Folder and File

import os
import random as rd
PATH = 'c:/Temp/Ex04'
os.mkdir(PATH)
os.chdir(PATH)
for dirname in ('low', 'mid', 'high'):
    os.mkdir(PATH + '/' + dirname)
    for num in ('1','2','3'):
        os.mkdir(PATH+'/'+dirname + '/'+num)

for i in range(100):
    filenumber = rd.randint(0,9999)
    content = str(rd.randint(1,3))
    if filenumber <= 3333:
        dirname = 'low'
    elif filenumber <= 6666:
        dirname = 'mid'
    else:
        dirname = 'high'
    filename = dirname + '/' + content + '/' + '%04d.txt' % filenumber
    file = open(filename, 'w')
    file.write(content)
    file.close()
