# your code 부분에 코딩하여 문제를 풀이해주세요.
# print 함수가 포함되어 있으면 주차 점수 0점 처리하겠습니다. 4주차 과제에는 출력을 요구하는 문제가 없습니다.
# input 함수가 포함되어 있으면 주차 점수 0점 처리하겠습니다. 4주차 과제에는 입력을 요구하는 문제가 없습니다.
# answer 변수를 사용하여 문제를 풀이하세요. 반환값은 answer 변수입니다.
# 함수 내에서 컴파일 에러, 런타임 에러가 발생하면 해당 문제 점수 0점 처리하겠습니다.
# 함수명 변경하지 마세요. 변경 시 해당 문제 점수 0점 처리하겠습니다.
# 제출 기한: 2022년 4월 5일 23시 59분.
# 지각 제출 기한: 2022년 4월 6일 23시 59분. 주차 점수에서 20% 감점

# 문제 1번
def intervention(queue):
    answer = list()
    a = queue.index("성은")
    if a > 3 :
        queue.insert(a+1, "승호")
    else :
        queue.append("승호")

    answer = queue
    return answer

# 문제 2번
def pascal(n):
    answer = [[0 for i in range(30)] for i in range(30)]
    answer[0][0] = 1
    answer[0][1] = 0

    for i in range(0, n):
        i += 1
        for j in range(0, i):
            answer[i][j] = answer[i-1][j] + answer[i-1][j-1]

    del answer[0]
    for i in range(0, 30):
        for j in range(0, 29-i):
            answer[i].remove(0)

    for i in range(n, 29):
        i = n
        del answer[i]
    real = answer[n-1]
    answer = real

    return answer

# 문제 3번
def auto_complete(entry, searchWords):
    answer = list()
    search = [i for i in searchWords if entry in i]
    search.sort()
    answer = search

    return answer

# 문제 4번
def stock_price(stockChart):
    answer = str()
    log = list()
    total = 0
    a = len(stockChart)
    for i in range(0, a):
        log.append(total + stockChart[i])
        total += stockChart[i]
        
    b = log[0]

    for i in range(0, a):
        if b >= log[i]:
            b = log[i]
            c = i

    if c == a-1 :
        answer = "아니야 조금만 더 기다려"
    else :
        answer = str((a-c-1))+"일 전에 샀어야지 으이구"
    return answer

# 문제 5번
def decryption(letter):
    answer = str()
    for i in range(0, len(letter)):
        a = ord(letter[i])
        if a >= 100 and a <= 122:
            a -= 3
            answer += chr(a)
        elif a == 99 :
            answer += 'z'
        elif a == 98 :
            answer += 'y'
        elif a == 97 :
            answer += 'x'
        else : answer += letter[i]
    return answer