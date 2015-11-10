from Point import*
N=int(input())
max = Point(input())
for i in range(N-1):
    A=Point(input())
    if A>max:
        max = A
print(str(max))
