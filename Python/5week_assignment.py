# your code 부분에 코딩하여 문제를 풀이해주세요.
# print 함수가 포함되어 있으면 주차 점수 0점 처리하겠습니다. 5주차 과제에는 출력을 요구하는 문제가 없습니다.
# input 함수가 포함되어 있으면 주차 점수 0점 처리하겠습니다. 5주차 과제에는 입력을 요구하는 문제가 없습니다.
# result 변수를 사용하여 문제를 풀이하세요. 반환값은 result 변수입니다.
# 함수 내에서 컴파일 에러, 런타임 에러가 발생하면 해당 문제 점수 0점 처리하겠습니다.
# 함수명 변경하지 마세요. 변경 시 해당 문제 점수 0점 처리하겠습니다.
# 제출 기한: 2022년 4월 12일 23시 59분.
# 지각 제출 기한: 2022년 4월 13일 23시 59분. 주차 점수에서 20% 감점

import math

def calculator(order):
    answer = 0
    log = order.split(" ")
    if "원넓이" in order :
        answer = calcCircleArea(float(log[1]))
    elif "로그" in order :
        if "e" in log[1]:
            if "e" in log[2]:
                answer = calcLog(math.e, math.e)
            answer = calcLog(math.e, float(log[2]))
        elif "e" in log[2]:
            answer = calcLog(float(log[1]), math.e)
        else : answer = calcLog(float(log[1]), float(log[2]))
    elif "사인" in order :
        answer = calcSin(float(log[1]))
    elif "팩토리얼" in order:
        answer = calcFactorial(int(log[1]))
    elif "조합" in order :
        answer = calcCombination(int(log[1]), int(log[2]))
    else : return 0
    '''[1]'''
    return answer

def calcCircleArea(r):
    result = float()
    result = r**2*math.pi
    result = round(result, 2)
    '''[2]'''
    return result
def calcLog(a, b):
    result = float()
    result = math.log(b, a)
    result = round(result, 2)
    '''[3]'''
    return result
def calcSin(x):
    result = float()
    result = math.sin(x)
    result = round(result, 2)
    '''[4]'''
    return result
def calcFactorial(x):
    result = int()
    result = math.factorial(x)
    '''[5]'''
    return result
def calcCombination(n, r):
    result = int()
    result = math.comb(n, r)
    '''[6]'''
    return result

print(calculator("원넓이: 10"))
print(calculator("로그: e 10"))
print(calculator("사인: 100"))
print(calculator("팩토리얼: 5"))
print(calculator("조합: 3 2"))