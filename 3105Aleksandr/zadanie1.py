import math

class Point:

    def __init__(self):
        self.x = int()
        self.y = int()

    def setPoint(self, x, y):
        self.x = x
        self.y = y

    def getPoint(self):
        return (self.x, self.y)

class Line:

    def __init__(self):
        self.a = Point()
        self.b = Point()

    def setLine(self, a, b):
        self.a = a
        self.b = b

    def getLine(self):
        return (a,b)

    def getLength(self):
        dx = abs(self.a.getPoint()[0] - self.b.getPoint()[0])
        dy = abs(self.a.getPoint()[1] - self.b.getPoint()[1])
        length = math.sqrt(dx*dx + dy*dy)
        return length

    def isPointInLine(self, point):
        dx = abs(self.a.getPoint()[0] - self.b.getPoint()[0] + 1)/abs(point.getPoint()[0] - self.b.getPoint()[0] + 1)
        dy = abs(self.a.getPoint()[1] - self.b.getPoint()[1] + 1)/abs(point.getPoint()[1] - self.b.getPoint()[1] + 1)
        if dx == dy:
            return True
        else:
            return False

    def isPointInMiddleInLine(self, point):
        if self.isPointInLine(point):
            dx = abs(self.a.getPoint()[0] + self.b.getPoint()[0])/2
            dy = abs(self.a.getPoint()[1] + self.b.getPoint()[1])/2
            if dx == point.getPoint()[0] and dy == point.getPoint()[1]:
                return True
            else:
                return False
    def squareWithPoint(self, point):
        s1 = Line()
        s1.setLine(self.a, point)
        a = s1.getLength()
        s2 = Line()
        s2.setLine(self.b, point)
        b = s2.getLength()
        c = self.getLength()
        p = (a + b + c)/2
        s = math.sqrt(p*(p-a)*(p-b)*(p-c))
        return s

points = []
file = open("points.txt", "r")
for i in file.readlines():
    points.append(Point())
file.close()
file = open("points.txt", "r")
lines = file.readlines()
for i in range(len(points)):
    s = lines[i].replace("\n", "").split(" ")
    points[i].setPoint(int(s[0]),int(s[1]))
file.close()

length = len(points)
maxSquare = 0
a = Point()
b = Point()
c = Point()
buffLine = Line()
for i in range(length):
    for j in range(i+1, length):
        buffLine.setLine(points[i], points[j])
        for k in range(j+1, length):
            buffSquare = buffLine.squareWithPoint(points[k])
            if maxSquare < buffSquare:
                maxSquare = buffSquare
                a = points[i]
                b = points[j]
                c = points[k]

print(maxSquare)
print(a.getPoint())
print(b.getPoint())
print(c.getPoint())
