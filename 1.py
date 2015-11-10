class Point:
        def __init__(self, x = 0, y = 0):
               

                if type(x) ==str:
                        a=x.split(',')
                        if len(a)==2:
                                self.x = int(a[0])
                                self.y = int(a[1])
                else:
                      self.x = x
                      self.y = y

        def print(self):
                print(self.x, self.y)
        def __str__(self):
                return '(' + str(self.x) +','+ str(self.y) + ')'
        def __lt__(self, other):
                return self.x < other.x or self.x == other.x and self.y < other.y
        def __add__(self, other):
                return Point(self.x + other.x, self.y + other.y)

        def __sub__(self, other):
                return Point(self.x-other.x, self.y-other.y)
        def __gt__(self,other):
                if (self.x**2+self.y**2)>(other.x**2+other.y**2):
                    return True
                else:
                    return False
        def __truediv__(self,N):
                return Point(self.x/N, self.y/N)

