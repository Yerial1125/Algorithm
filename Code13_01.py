# 순차 검색

## 함수
import random

def seqSearch(ary, fdata) :
    pos = -1
    for i in range(len(ary)) :
        if (ary[i] == fdata) :
            pos = i
            break
    return pos


## 전역
dataAry = [random. randint(50, 190) for _ in range(10)]
findData = random.choice(dataAry)

## 메인
print('데이터 -->', dataAry)

position = seqSearch(dataAry, findData)
if (position != -1) :
    print(findData,'는', position,'위치에 있음')
else:
    print('없어요')