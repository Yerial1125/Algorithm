## 원형 큐
# % SIZE : 매직코드?

def isQueueFull():
    global SIZE, queue, front, rear
    # 원형큐는 1칸을 사용 못함! 왜냐하면 꽉 찰 경우에도 front == rear
    # 따라서 rear 다음이 front일 때 꽉 찬 것으로 인식하도록!
    if ((rear+1) % SIZE == front) : # 마지막값 다음이 0이어야
        return True
    else:
        return False

def enQueue(data) :
    global SIZE, queue, front, rear
    if (isQueueFull()) :
        print('큐 꽉 찼다!')
        return
    rear = (rear + 1) % SIZE
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
    front = (front+1) % SIZE
    data = queue[front]
    queue[front] = None
    return data

def peek():
    global SIZE, queue, front, rear
    if (isQueueEmpty()) :
        print('큐 비었다!')
        return None
    return queue[(front+1) % SIZE]

## 전역
SIZE = 5
queue = [None for _ in range(SIZE)]
front = rear = 0

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

enQueue('정국')
print('출구 <--', queue, '<-- 입구')

enQueue('길동')
print('출구 <--', queue, '<-- 입구')