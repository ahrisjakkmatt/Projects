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
        self.area = math.pi*self.radius**2
        print(f"Area of a Circle with radius {self.radius} is "+str(self.area))

    def Perimeter(self):
        self.perimeter = 2*math.pi*self.radius
        print(f"Perimeter of a Circle with radius {self.radius} is " + str(self.perimeter))

class Oval(Shape):
    def __init__(self, longestR, shortestR, nodes=0, sides=1):
        super(Oval, self).__init__(0, 1)
        self.longest = longestR #longest radius
        self.shortest = shortestR #shortest radius

    def Area(self):
        self.area = math.pi*self.longest*self.shortest
        print(f"Area for an Oval with longest radius {self.longest} and shortest radius of {self.shortest} is "+str(self.area))

    def Perimeter(self):
        diffR = self.longest-self.shortest
        sumR =  self.longest+self.shortest
        adj_radius = (3*(diffR**2/(sumR**2*(math.sqrt(-3*(diffR**2/sumR**2)+4)+10)))+1)
        self.perimeter = math.pi*(self.longest+self.shortest)*adj_radius
        print(f"Perimeter for an Oval with longest radius {self.longest} and shortest radius of {self.shortest} is " + str(self.perimeter))

class Polygon(Shape):
    pass
    # This is a family of shapes where nodes = sides
    # for N-Gon for example Octagon, see N_Gon class in the end

class Triangle(Polygon):
    def __init__(self, height, base, dif_sides=False, right_angle=True, nodes=3, sides=3):
        super(Triangle, self).__init__(3, 3)
        self.height = height
        self.base = base
        self.dif_sides = dif_sides
        self.right_angle = right_angle
        # Assumption works only for Right Triangle, There are many options for triangles, with knowns and unknowns

    def Area(self):
        self.area = self.base*self.height/2
        print(f"Area of a Right Triangle of base {self.base} and height {self.height} is "+str(self.area))

    def Perimeter(self):
        hypoteneuse = math.sqrt((self.height**2+self.base**2))
        self.perimeter = self.height+self.base+hypoteneuse
        print(f"Perimeter of a Right Triangle of base {self.base} and height {self.height} is " + str(self.perimeter))

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
        self.area = self.longest**2
        print(f"Area of a Square of sides {self.longest} is "+str(self.area))

    def Perimeter(self):
        self.perimeter = 4*self.longest
        print(f"Perimeter of a Square of sides {self.longest} is " + str(self.perimeter))


class Rectangle(Quadrilateral):
    def __init__(self,longest, shortest, dif_sides = True, right_angle = True, nodes=4, sides=4):
        super(Rectangle, self).__init__(longest, shortest, True, True, 4, 4)

    def Area(self):
        self.area =  self.longest*self.shortest
        print(f"Area of a Rectangle of sides {self.shortest} and {self.longest} is " + str(self.area))

    def Perimeter(self):
        self.perimeter = (2 * self.longest)+(2*self.shortest)
        print(f"Perimeter of a Rectangle of sides {self.shortest} and {self.longest} is " + str(self.perimeter))

class Parallelogram(Quadrilateral):
    def __init__(self, longest, shortest, dif_sides=False, right_angle=True,  nodes=4, sides=4):
        super(Parallelogram, self).__init__(longest, shortest, True, False, 4, 4)
        self.height = math.sqrt(self.longest**2-self.shortest**2)

    def Area(self):
        self.area = self.shortest*self.height
        print(f"Area of Parallelogram of sides {self.shortest} and {self.longest} is " + str(self.area))

    def Perimeter(self):
        self.perimeter = (2 * self.longest)+(2*self.shortest)
        print(f"Perimeter of a Parallelogram of sides {self.shortest} and {self.longest} is " + str(self.perimeter))
    
    
class Rhombus(Quadrilateral):
    def __init__(self, longest, shortest=False, dif_sides=False, right_angle=True, nodes=4, sides=4):
        super(Rhombus, self).__init__(longest, False, False, True, 4, 4)

    def Area(self):
        self.area = self.longest ** 2
        print(f"Area of a Rhombus with side length {str(self.longest)} is " + str(self.area))

    def Perimeter(self):
        self.perimeter = 4 * self.longest
        print(f"Perimeter of a Rhombus with side length {str(self.longest)} is " + str(self.perimeter))

class Pentagon(Polygon):
    def __init__(self, side_length):
        super(Pentagon, self).__init__(5, 5)
        self.side_length = side_length

    def Area(self):
        deg_36 = math.pi/5
        height = .5*self.side_length/math.tan(deg_36)
        triangle_tenth = 0.5*(0.5*self.side_length)*height
        self.area = 10*triangle_tenth
        print(f"Perimeter of a Pentagon with side length of {str(self.side_length)} is " + str(10*triangle_tenth))

    def Perimeter(self):
        self.perimeter = 5 * self.side_length
        print(f"Perimeter of a Pentagon with side length of {str(self.side_length)} is " + str(self.perimeter))

class N_Gon(Polygon):
    def __init__(self, side_length,nodes,sides):
        super(N_Gon, self).__init__(nodes, sides)
        self.side_length = side_length

    def Area(self):
        deg_internal = math.pi/self.sides
        height = .5*self.side_length/math.tan(deg_internal)
        triangle_nth = 0.5*(0.5*self.side_length)*height
        self.area = 2*self.sides*triangle_nth
        print(f"Area of an N-Gon with {str(self.sides)} sides of length {str(self.side_length)} is " + str(self.area))

    def Perimeter(self):
        self.perimeter = self.sides * self.side_length
        print(f"Perimeter of an N-Gon with {str(self.sides)} sides of length {str(self.side_length)} is " + str(self.perimeter))


circle = Circle(5)
circle.Area()
circle.Perimeter()
print()

oval = Oval(5,2)
oval.Area()
oval.Perimeter()
print()

triangle = Triangle(12, 4)
triangle.Area()
triangle.Perimeter()
print()

square = Square(10)
square.Area()
square.Perimeter()
print()

rect = Rectangle(100,20)
rect.Area()
rect.Perimeter()
print()

par = Parallelogram(10,2)
par.Area()
par.Perimeter()
print()

rhom = Rhombus(12)
rhom.Area()
rhom.Perimeter()
print()

pent = Pentagon(7)
pent.Area()
pent.Perimeter()
print()

ngon = N_Gon(7,5,5) # Compare to Pentagon above
ngon.Area()
ngon.Perimeter()
print()

ngon = N_Gon(10,4,4) # Compare to Square above works but has a minimal rounding issue b/c of calculating triangles
ngon.Area()
ngon.Perimeter()
print()