from Point import*
N=int(input())
A=Point(input())
i=1
while i<N:
    S=Point(input())
    A=A+S
    i+=1
print(A.__truediv__(N))
