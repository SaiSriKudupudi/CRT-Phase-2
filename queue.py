def enqueue(q, ele):
    q.append(ele)
    print(ele, "inserted into queue successfully")

def dequeue(q):
    if len(q) == 0:
        print("queue is empty")
        return
    print(q[0], "deleted successfully")
    q.pop(0)

q=[]
enqueue(q, 1)
enqueue(q, 2)
enqueue(q, 3)
enqueue(q, 4)
enqueue(q, 5)
print(q)

dequeue(q)
dequeue(q)
dequeue(q)
dequeue(q)
dequeue(q)
print(q)
