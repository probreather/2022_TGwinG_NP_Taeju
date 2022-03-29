# 이번 주차부터는 컴파일 에러 등으로 프로그램 자체가 실행되지 않을 시에는 과제 점수 0점 처리합니다.
# 문제에서 요구하는 입출력 외에는 절대 포함해서 제출하지 마세요. 0점 처리합니다.
# 문제에서 요구하는 출력 형식, 반환 형식을 "모두" 지켜주세요. 지키지 않으면 오답처리 됩니다.
# 한 파일에 모든 문제를 풀이해서 제출하세요. 분리 제출 시 채점자 PC기준 최상위에 정렬되는 파일만 채점합니다.
# 제출 마감일: 2022-03-29 23:59, 지각 제출 시 점수에서 20% 감점입니다.

# 문제 1번
def question1():
    a = "next"
    return a

# 문제 2번
def leapYear(year):
    a = "윤년입니다."
    b = "윤년이 아닙니다."
    if year % 4 ==0 and year % 100 !=0 :
        return a
    elif year % 400 == 0 :
        return a
    else : return b

# 문제 3번
def alarm(time):
    a = time // 100
    b = time % 100
    if time // 1000 == 0 :
        if (b - 45) >= 0 :
            b -= 45
            c = "오전 "+str(a)+"시 "+str(b)+"분"
        else :
            if a > 0 :
                a -= 1
                b += 15
                c = "오전 "+str(a)+"시 "+str(b)+"분"
            else : 
                a = 23
                b += 15
                c = "오후 "+str(a)+"시 "+str(b)+"분"
    else :
        if a > 12 :
            if (b - 45) >= 0 :
                b -= 45
                c = "오후 "+str(a)+"시 "+str(b)+"분"
            else :
                a -= 1
                b += 15
                c = "오후 "+str(a)+"시 "+str(b)+"분"
        elif a == 12 :
            if (b - 45) >= 0 :
                b -= 45
                c = "오후 "+str(a)+"시 "+str(b)+"분"
            else :
                a -= 1
                b += 15
                c = "오전 "+str(a)+"시 "+str(b)+"분"
        else : 
            if (b - 45) >= 0 :
                b -= 45
                c = "오전 "+str(a)+"시 "+str(b)+"분"
            else :
                a -= 1
                b += 15
                c = "오전 "+str(a)+"시 "+str(b)+"분"
    return c

# 문제 4번
def findDaesun(x1,y1,r1,x2,y2,r2):
    a = ((x1-x2)**2+(y1-y2)**2)**0.5
    b = r1 + r2
    if r1 > r2 :
        d = r1 - r2
    elif r1 < r2 :
        d = r2 - r1
    else : d = 0
    if a == 0 :
        if r1 == r2 :
            c = "어딘지 모르겠다 오바"
        else : c = 0
    elif a < b :
        if a == d :
            c = 1
        elif a < d :
            c = 0
        else : c = 2
    elif a == b :
        c = 1
    else : c = 0
    return c