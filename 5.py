class Point:
    def __init__(self,stroka='0,0',mass=1):
        self.x=float(stroka[:stroka.index(',')])
        self.y=float(stroka[stroka.index(',')+1:])
        self.mass=mass
        
    def __str__(self):
        return '('+str(self.x)+','+str(self.y)+')'
    def __add__(self,other):
        return Point(str(self.x+other.x)+','+str(self.y+other.y))
    def __sub__(self,other):
        return Point(str(self.x-other.x)+','+str(self.y-other.y))
    def russt(self,other):
        return ((self.x-other.x)**2+(self.y-other.y)**2)**0.5
    def c_mass(self,other):
        x=self.x+(other.x-self.x)/(self.mass+other.mass)
        y=self.y+(other.y-self.y)/(self.mass+other.mass)
        return Point(str(x)+','+str(y),self.mass+other.mass)
    def Triangle_Perimetr(self,other,onemore):
        return self.russt(other)+self.russt(onemore)+other.russt(onemore)
    def Triangle_Square(self,other,onemore):
        p=self.Triangle_Perimetr(other,onemore)/2
        a=self.russt(other)
        b=self.russt(onemore)
        c=other.russt(onemore)
        return (p*(p-c)*(p-b)*(p-a))**0.5
        
        
        
N=int(input())
A=[]
maximum=None
B=[Point()]*3
for i in range(N):
    A.append(Point(input()))
for i in range(N-2):
    for j in range(i+1,N-1):
        for k in range(j+1,N):
            if maximum==None or maximum<A[i].Triangle_Square(A[j],A[k]):
                B[0],B[1],B[2]=A[i],A[j],A[k]
                maximum=A[i].Triangle_Square(A[j],A[k])
                
print(*B)
