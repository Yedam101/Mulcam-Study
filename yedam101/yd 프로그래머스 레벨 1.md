
### 부족한 금액 계산하기
```python

def solution(price, money, count):
    if money - sum([price*i for i in range(1, count +1)]) >= 0:
        return 0
    else:
        return -(money - sum([price*i for i in range(1, count +1)]))

```

### 3진법 뒤집기
```python

def solution(n):
    m = []
    while n > 2:
        m.append(str(n%3))
        n = n // 3
    m.append(str(n))
    num = ''.join(m)
    return int(num, 3)

```

### 예산
```python

def solution(d, budget):
    if sum(d) <= budget:
        return len(d)
    else:
        count = 0
        d = sorted(d)
        for i in range(len(d)):
            count += d[i]
            if count > budget:
                return i
```

### [1차] 비밀지도
```python

def solution(n, arr1, arr2):

    arr1 = [list(bin(i)[2:]) if len(bin(i)[2:]) == n else list('0'*(n-len(bin(i)[2:]))+bin(i)[2:]) for i in arr1]
    arr2 = [list(bin(i)[2:]) if len(bin(i)[2:]) == n else list('0'*(n-len(bin(i)[2:]))+bin(i)[2:]) for i in arr2]


    for i in range(n):
        for j in range(n):
            if arr1[i][j] == '0' and arr2[i][j] == '0':
                arr1[i][j] = ' '
            else:
                arr1[i][j] = '#'
    ans = []
    for i in arr1:
        ans.append(''.join(i))

    return ans

```

### 약수의 개수와 덧셈
```python

def solution(left, right):
    sqr = [i**2 for i in range(32) ]
    answer = 0
    for i in range(left, right+1):
        answer += i
        if i in sqr:
            answer -= 2*i
            
    return answer

```

### 숫자 문자열과 영단어
```python

def solution(s):
    
        nums = {'zero':'0', 'one':'1','two':'2','three':'3','four':'4',
                'five':'5','six':'6','seven':'7','eight':'8','nine':'9'}

        for key, value in nums.items():
            s = s.replace(key,value)

        answer = int(s)
        return answer

```

### 두 개 뽑아서 더하기
```python

from itertools import combinations
def solution(numbers):
    a = list(combinations(numbers, 2))
    ans = [sum(i) for i in a]
    
    return sorted(list(set(ans)))

```

```

### 실패율
```python

def solution(N, stages):
    res = [0]*(N+2)

    for i in stages:
        res[i] += 1

    for i in range(len(res)):
        if sum(res[i:]) != 0:
            res[i] = res[i]/sum(res[i:])
        else:
            pass

    ans = list(enumerate(res))
    ans.pop(0)
    ans.sort(key = lambda x: -x[1])
    ans = [i[0] for i in ans if i[0] < N+1]
    return ans

```

### [1차] 다트 게임
```python

def solution(dartResult):
    dartResult = dartResult + '0'
    dr = []
    start = 0
    for i in range(len(dartResult)):
        if i != 0 and dartResult[i].isdigit() and len(dartResult[start:i]) != 1:
            dr.append(list(dartResult[start:i]))
            start = i

    for i in range(len(dr)):
        if '0' in dr[i] and dr[i].index('0') != 0:
            dr[i][1] = '10'
            dr[i].remove('1')
        if 'S' in dr[i]:
            dr[i][0] = int(dr[i][0])
            dr[i].remove('S')
        elif 'D' in dr[i]:
            dr[i][0] = int(dr[i][0])**2
            dr[i].remove('D')
        elif 'T' in dr[i]:
            dr[i][0] = int(dr[i][0])**3
            dr[i].remove('T')
        if '#' in dr[i]:
            dr[i][0] = -int(dr[i][0])
            dr[i].remove('#') 
        if '*' in dr[i]:
            if i and i != 0:
                dr[i][0], dr[i-1][0] = int(dr[i][0])*2, int(dr[i-1][0])*2
                dr[i].remove('*') 
            else:
                dr[i][0] = int(dr[i][0])*2
                dr[i].remove('*') 

    return sum(sum(dr, []))

```

### 로또의 최고 순위와 최저 순위
```python

def solution(lottos, win_nums):
    
    n = lottos.count(0)
    m = len(set(lottos) & set(win_nums))

    ans = [7-(m+n), 7-(m)]
    for i in range(2):
        if ans[i] == 7:
            ans[i] = 6
    return ans

```

### 키패드 누르기
```python

def solution(numbers, hand):
    lx, ly = [3, 0]
    rx, ry = [3, 2]
    ans = []  

    for i in numbers:
        gx = (i-1) // 3
        gy = (i+2) % 3
        if i == 0:
            gx, gy = 3, 1
        if gy == 0:
            ans.append('L')
            lx, ly = gx, gy
        elif gy == 2:
            ans.append('R')
            rx, ry = gx, gy
        else:
            if abs(gx-lx)+abs(gy-ly) > abs(gx-rx)+abs(gy-ry):
                ans.append('R')
                rx, ry = gx, gy            
            elif abs(gx-lx)+abs(gy-ly) < abs(gx-rx)+abs(gy-ry):
                ans.append('L')
                lx, ly = gx, gy  
            else:
                ans.append(hand[0].upper())
                if hand[0] == 'r':
                    rx, ry = gx, gy
                else:
                    lx, ly = gx, gy
    return ''.join(ans)

```

### 크레인 인형뽑기 게임
```python

def solution(board, moves):
    board = list(map(list, zip(*board)))
    for i in board:
        while 0 in i:
            i.remove(0)

    moves = [i-1 for i in moves]
    ans = []
    count = 0

    for i in moves:
        if board[i]:
            ans.append(board[i].pop(0))
            if len(ans) > 1 and ans[-1] == ans[-2]:
                ans.pop(-1)
                ans.pop(-1)
                count += 2

    return count

```

### 신규 아이디 추천
```python

def solution(new_id): 
    new_id = new_id.lower()
    answer = ''
    for word in new_id:
        if word.isalnum() or word in '-_.':
            answer += word
    while '..' in answer:
        answer = answer.replace('..', '.')
    answer = answer[1:] if answer[0] == '.' and len(answer) > 1 else answer
    answer = answer[:-1] if answer[-1] == '.' else answer
    answer = 'a' if answer == '' else answer
    if len(answer) >= 16:
        answer = answer[:15]
        if answer[-1] == '.':
            answer = answer[:-1]
    if len(answer) <= 3:
        answer = answer + answer[-1] * (3-len(answer))
    return answer

```

### 성격 유형 검사하기
```python

def solution(survey, choices):
    char = {'R':0, 'T':0, 'C':0, 'F':0, 'J':0, 'M':0, 'A':0, 'N':0}

    for i in range(len(survey)):
        if choices[i] < 4:
            char[survey[i][0]] += abs(choices[i]-4)
        else:
            char[survey[i][1]] += choices[i]-4

    charlist = [['R','T'],['C','F'], ['J','M'], ['A','N']]
    result = []
    for i in charlist:
        if char[i[0]] >= char[i[1]]:
            result.append(i[0])
        elif char[i[0]] < char[i[1]]:
            result.append(i[1])

    answer = ''.join(result)
    return answer

```

### 신고 결과 받기
```python

def solution(id_list, report, k):

    report = set(report)
    idict = {i:0 for i in id_list}
    answer = {i:0 for i in id_list}
    report_list = []

    for i in report:
        report_list.append(i.split(' '))

    for i in report_list:
        idict[i[1]] += 1

    ans = [i for i in id_list if idict[i] >= k]

    for i in report_list:
        if i[1] in ans:
            answer[i[0]] += 1

    return list(answer.values())

```
