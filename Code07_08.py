## 함수
# 모듈화
# : 자동차의 부품처럼 함수를 여러 개로 쪼개어 만드는 것!
# : 수정시 용이! ex. 자동차 전체가 아닌 부품만 갈아 끼우면 됨

def isQueueFull():
    global SIZE, queue, front, rear
    # Case1 : 뒤에 여유 있을 때
    if (rear != SIZE-1) :
        return False
    # Case2 : 진짜 꽉참!
    elif (rear == SIZE-1 and front == -1) :
        return True
    #Case # : 뒤는 꽉, 앞은 여유
    # elif (rear == SIZE-1 and front != -1) :
    else:
        for i in range(front+1, SIZE, 1) : # 한칸씩만 땡겨요.
            queue[i-1] = queue[i]
            queue[i] = None
        front -= 1
        rear -= 1
        return False

def enQueue(data) :
    global SIZE, queue, front, rear
    if (isQueueFull()) :
        print('큐 꽉 찼다!')
        return
    rear += 1
    queue[rear] = data

def isQueueEmpty():
    global SIZE, queue, front, rear
    if (front == rear):
        return True
    else :
        return False

def deQueue() :
    global SIZE, queue, front, rear
    if (isQueueEmpty()) :
        print('큐 비었다!')
        return None
    front += 1
    data = queue[front]
    queue[front] = None
    return data

def peek():
    global SIZE, queue, front, rear
    if (isQueueEmpty()) :
        print('큐 비었다!')
        return None
    return queue[front+1]

## 전역
SIZE = 5
queue = [None for _ in range(SIZE)]
front = rear = -1

## 메인

enQueue('화사')
enQueue('솔라')
enQueue('문별')
enQueue('휘인')
enQueue('선미')
print('출구 <--', queue, '<-- 입구')


retData = deQueue()
print('식사 손님:', retData)
retData = deQueue()
print('식사 손님:', retData)
print('출구 <--', queue, '<-- 입구')

enQueue('재남')
print('출구 <--', queue, '<-- 입구')
