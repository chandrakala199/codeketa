print("stack implementation")
stack=[]
while True:
    print("what operation would you like to perform?\n 1.push 2.pop 3.size 4.empty 5.exit")
    c=int(input())
    if c==1:
        print("Enter the element to be inserted:")
        l=int(input())
        stack.append(l)
        print(" the element in the stack  are",stack) 
    elif c==2:
        if stack ==[]:
            print("the stack is empty")
        else:
          stack.pop(0)
          print("the element in the stack are",stack)
    elif c==3:
        print("the size of the stack  is",len(stack))
        print(" the element in the stack are",stack)
    elif c==4:
        if stack ==[1]:
            print("the element is empty")
        else:
            print("the element in the queue are",stack)
    elif c==5:
            print("exit")
            break
    
