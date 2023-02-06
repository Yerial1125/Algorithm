# 이진 검색

## 함수
import random

def binSearch(ary, fdata) :
    pos = -1
    start = 0
    end = len(ary)-1
    while (start <= end) :
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
dataAry = [random.randint(50, 190) for _ in range(10)]
findData = random.choice(dataAry)
dataAry.sort()

## 메인
print('데이터 -->', dataAry)

position = binSearch(dataAry, findData)
if (position != -1):
    print(findData, '는', position, '위치에 있음')
else:
    print('없어요')
