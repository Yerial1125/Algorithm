# 이진 검색 _ count 검색 횟수 세기

## 함수
import random

def binSearch(ary, fdata) :
    global count
    pos = -1
    start = 0
    end = len(ary)-1
    while (start <= end) :
        count += 1
        mid = (start+end) // 2
        if (ary[mid] == fdata) :
            pos = mid
            break
        elif (ary[mid] < fdata) :
            start = mid + 1
        else:
            end = mid - 1

    return pos

## 전역
count = 0
dataAry = [random.randint(0, 100000000) for _ in range(1000000)]
findData = random.choice(dataAry)
dataAry.sort()

## 메인
print('데이터 -->', dataAry[:10])

position = binSearch(dataAry, findData)
if (position != -1):
    print(findData, '는', position, '위치에 있음', count)
else:
    print('없어요')
