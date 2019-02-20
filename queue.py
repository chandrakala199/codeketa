print("queue implementation")
queue=[]
while True:
    print("what operation would you like to perform?\n 1.enqueue 2.dequeue 3.size 4.empty 5.exit")
    c=int(input())
    if c==1:
        print("Enter the element to be inserted:")
        l=int(input())
        queue.append(l)
        print(" the element in the queue  are",) 
    elif c==2:
        if queue ==[]:
            print("the queue is empty")
        else:
          queue.pop(0)
          print("the element in the queue are",queue)
    elif c==3:
        print("the size of the queue  is",len(queue))
        print(" the element in the stack are",queue)
    elif c==4:
        if queue ==[1]:
            print("the element is empty")
        else:
            print("the element in the queue are",queue)
    elif c==5:
            print("exit")
            break
