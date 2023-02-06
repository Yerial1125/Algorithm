# ★★정렬 코드★★

## 함수
import random

def selectionSort(ary) :
    n = len(ary)
    for i in range(n-1) :
        minIdx = i
        for k in range(i+1, n):
            if (ary[minIdx] > ary[k]):
                minIdx = k
        ary[i], ary[minIdx] = ary[minIdx], ary[i]

    return ary

## 전역
dataAry = [random. randint(50, 190) for _ in range(10)]


## 메인
print('정렬 전 -->', dataAry)
dataAry = selectionSort(dataAry)
print('정렬 후 -->', dataAry)