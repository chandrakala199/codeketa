place=("tambaram","adyar","ambathur")
dist=[30,40,50]
print("where you want to go?\n 1.tambaram,2.aydar,3.ambathur")
n=int(input())
if n==1:
    kms=dist[0]
    print("the place you hve choosed is tambaram")
elif n==2:
    kms=dist[1]
    print("the place you hve choosed is adyar")
elif n==3:
    kms=dist[2]
    print("the place you hve choosed is ambathur")
cab=["micro","mini","prime"]
price=[6,7,8]
print("what cab would you prefect?\n 1.micro 2.mini 3.prime")
c=int(input())
if c==1:
    rate=price[0]
    print("the cab you hve choosed is micro")
elif c==2:
    rate=price[1]
    print("the cab you hve choosed is mini")
elif c==3:
    rate=price[2]
    print("the cab you hve choosed is prime")
print("the estimated amount is ", kms*rate)
print("do you want to confirm your booking?\n 1.yes 2.no")
d=int(input())
if d==1:
    print("thanks for booking")
elif d==2:
    print("meet you soon")
