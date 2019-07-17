#12.4
a = input().split()
b = map(float,input().split())
print(dict(zip(a,b)))

#11.9
a = str(input().split())
b = str(input().split())
a[0::2] + b[1::2]
list(word)

#11.8
x = input().split()
print(tuple(x[:-5]))

#10.4
a = int(input())
print(list(range(-10,10,a)))

#9.4
s = ''' 'Python' is a "programming language"
that lets you work quickly 
and
integrate systems more effectively'''
print(s)
#8.4
kor, eng, math, sci = map(int,input('Enter Num: ').split())
kor >= 90 and eng > 80 and math > 85 and sci >= 80


# 7.4
year, month, day, hour, minute, second = input().split()
print(year, month, day, sep="-")
print(hour, minute, second, sep=':')


#6.8
kor, eng, math, sci = map(int,input('Enter Num: ').split())
print(int((kor + eng + math + sci) /4 ))


# 6.7
a = 50
b = 100
c = 'None'
print(a,"\n",b,"\n",c)