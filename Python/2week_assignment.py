# 문제 1번
def sum(a,b):
    c = a + b
    return c

# 문제 2번
def sub(a,b):
    c = a - b
    return c

# 문제 3번
def mul(a,b):
    c = a * b
    return c

# 문제 4번
def div(a,b):
    c = a/b
    return c

# 문제 5번
def distance(x1,y1,x2,y2):
    c = ((x2-x1)**2+(y2-y1)**2)**0.5
    return c

# 문제 6번
def short():
    lylic = "life is short art is long"
    return lylic[8:13]

# 문제 7번
def myReverse(string):
    return string[::-1]

# 문제 8번
def letMeIntroduceMyself():
    name = input("이름을 입력하시오:")
    hobby = input("취미를 입력하시오:")
    univ = input("재학중인 대학을 입력하시오:")
    birth = input("생일을 입력하시오(예시:981128):")
    return print("제 이름은 "+name+"입니다. 제 취미는 "+hobby+"이구요. 저는 "+univ+"를 다니고 있습니다. 제 생일은 "+birth[2:4]+"월 "+birth[4:]+"일 입니다.")

# 문제 9번
def calcAI():
    a = int(input("첫 번째 숫자를 입력하시오:"))
    b = int(input("두 번째 숫자를 입력하시오:"))
    return print("두 수의 합은 {0}입니다." .format(a+b))