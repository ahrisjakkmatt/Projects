import math

class Shape:
    def __init__(self,nodes, sides):
        self.nodes = nodes
        self.sides = sides

    def Area(self):
        print("Area")

    def Perimeter(self):
        print("Perimeter")

class Circle(Shape):
    def __init__(self, radius, nodes=0, sides=1):
        super(Circle, self).__init__(nodes, sides)
        self.radius = radius

    def Area(self):
        print(f"Area is "+str(math.pi*self.radius**2))

    def Perimeter(self):
        print(f"Perimeter is " + str(2*math.pi*self.radius))

class Oval(Shape):
    def __init__(self, longestR, shortestR, nodes=0, sides=1):
        super(Oval, self).__init__(0, 1)
        self.longest = longestR
        self.shortest = shortestR

    def Area(self):
        print(f"Area is "+str(math.pi*self.longest*self.shortest))

    def Perimeter(self):
        diffR = self.longest-self.shortest
        sumR =  self.longest+self.shortest
        adj_radius = (3*(diffR**2/(sumR**2*(math.sqrt(-3*(diffR**2/sumR**2)+4)+10)))+1)
        print(f"Perimeter is " + str(math.pi*(self.longest+self.shortest)*adj_radius))

class Polygon(Shape):
    pass

class Triangle(Polygon):
    def __init__(self, height, base, dif_sides=False, right_angle=True, nodes=3, sides=3):
        super(Triangle, self).__init__(3, 3)
        self.height = height
        self.base = base
        self.dif_sides = dif_sides
        self.right_angle = right_angle
        
    def Area(self):
        print(f"Area is "+str(self.base*self.height/2))

    def Perimeter(self):
        hypoteneuse = math.sqrt((self.height**2+self.base**2))
        print(f"Perimeter is " + str(self.height+self.base+hypoteneuse))

class Quadrilateral(Polygon):
    def __init__(self, longest, shortest, dif_sides = False, right_angle = True, nodes=4, sides=4):
        super(Quadrilateral, self).__init__(nodes,sides)
        self.right_angle = right_angle
        self.dif_sides = dif_sides
        self.longest = longest
        self.shortest = shortest

class Square(Quadrilateral):
    def __init__(self, longest, shortest=False, dif_sides = False, right_angle = True, nodes=4, sides=4):
        super(Square, self).__init__(longest, shortest, False, True, 4, 4)

    def Area(self):
        print(f"Area is "+str(self.longest**2))

    def Perimeter(self):
        print(f"Perimeter is " + str(4*self.longest))


class Rectangle(Quadrilateral):
    def __init__(self,longest, shortest, dif_sides = True, right_angle = True, nodes=4, sides=4):
        super(Rectangle, self).__init__(longest, shortest, True, True, 4, 4)

    def Area(self):
        print(f"Area is " + str(self.longest*self.shortest))

    def Perimeter(self):
        print(f"Perimeter is " + str((2 * self.longest)+(2*self.shortest)))

class Parallelogram(Quadrilateral):
    def __init__(self, longest, shortest, dif_sides=False, right_angle=True,  nodes=4, sides=4):
        super(Parallelogram, self).__init__(longest, shortest, True, False, 4, 4)
        self.height = math.sqrt(self.longest**2-self.shortest**2)

    def Area(self):
        print(f"Area is " + str(self.shortest*self.height))

    def Perimeter(self):
        print(f"Perimeter is " + str((2 * self.longest)+(2*self.shortest)))
    
    
class Rhombus(Quadrilateral):
    def __init__(self, longest, shortest=False, dif_sides=False, right_angle=True, nodes=4, sides=4):
        super(Rhombus, self).__init__(longest, False, False, True, 4, 4)

    def Area(self):
        print(f"Area is " + str(self.longest**2))

    def Perimeter(self):
        print(f"Perimeter is " + str(4 * self.longest))

class Pentagon(Polygon):
    def __init__(self, side_length):
        super(Pentagon, self).__init__(5, 5)
        self.side_length = side_length

    def Area(self):
        deg_36 = math.pi/5
        height = .5*self.side_length/math.tan(deg_36)
        triangle_tenth = 0.5*(0.5*self.side_length)*height
        print(f"Area is " + str(10*triangle_tenth))

    def Perimeter(self):
        print(f"Perimeter is " + str(5 * self.side_length))

# circle = Circle(5)
# circle.Area()
# circle.Perimeter()

# oval = Oval(5,2)
# oval.Area()
# oval.Perimeter()

# triangle = Triangle(12, 4)
# triangle.Area()
# triangle.Perimeter()

# square = Square(10)
# square.Area()
# square.Perimeter()

# rect = Rectangle(100,20)
# rect.Area()
# rect.Perimeter()

# par = Parallelogram(10,2)
# par.Area()
# par.Perimeter()

# rhom = Rhombus(12)
# rhom.Area()
# rhom.Perimeter()

pent = Pentagon(7)
pent.Area()
pent.Perimeter()