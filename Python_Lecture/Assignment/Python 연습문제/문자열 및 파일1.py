# #1
# def isPalindrome(a) :
#     for i in range(len(a)//2):
#         if a[i] != a[-1-i]:
#             return False
#     return True
# maxNum = 0
# for i in range(100,1000):
#     for k in range(100,1000):
#         if isPalindrome(str(i*k)):
#             if i*k > maxNum:
#                 maxNum = i * k
#                 maxA = i
#                 maxB = k
# print(maxNum, maxA,maxB)
#
# #2
# word, n = input('암호화할 문자열과 n값: ').split()
# word = [c for c in word]
# n = int(n)
#
# Letter_A = ord('A')
# Letter_Z = ord('Z')
# cypher = []
# for letter in word:
#     if ord(letter) + n > Letter_Z:
#         cypher.append(chr(Letter_A + ord(letter) + n - Letter_Z-1))
#     else:
#         cypher.append(chr(ord(letter) + n))
# print(''.join(cypher))
# word1, n = input ('암호화할 문자열과 n 값을 입력하시오: ').split()
# n = int(n)
# def topasscode(word) :
#     word = [i for i in word]
#     Letter_A = ord('A')
#     Letter_Z = ord('Z')
#     cypher = []
#     for letter in word:
#         if ord(letter) + n > Letter_Z:
#             cypher.append(chr(Letter_A + ord(letter) + n - Letter_Z - 1))
#         else:
#             cypher.append(chr(ord(letter) + n))
#     print(''.join(cypher))
# topasscode(word1)

# #Unix grep 명령어
# word, filename = input('찾고자 하는 문자열과 파일명: ').split()
# word = word.strip(",.")
# lineNo = 1
# with open(filename,'r',encoding ='UTF-8') as file:
#     for line in file:
#         if line.find(word) >= 0:
#             print('%2d: ' % lineNo, line, end = '')
#         lineNo += 1

# UNIX wc 명령어
# 구분자는 마침표(‘.’), 쉽표(‘,’), 공백(‘ ‘)
filename = input('파일 이름> ')
wordsDict = dict()

with open(filename, 'r') as file:
    for line in file:
        linewords = line.replace('(', ' ').replace(')', ' ')\
                        .replace(',', ' ').replace('.', ' ').split()
        #print(linewords)
        for word in linewords:
            count = wordsDict.get(word, 0)
            #print(count, end=' ')
            if count == 0:
                wordsDict.setdefault(word, 1)
            else:
                wordsDict.update(dict([(word, count+1)]))

print('총 단어수 =', len(wordsDict))
import operator
wordsList = sorted(wordsDict.items(), key=operator.itemgetter(1), reverse=True)
print('많이 나온 단어')
for i in range(10):
    print(wordsList[i])