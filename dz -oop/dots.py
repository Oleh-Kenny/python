x = int(input("Enter x: "))
y = int(input("Enter y: "))
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def show_cord(self):
        print("\nx = ", self.x)
        print("\ny = ", self.y)
        

new_point = Point(x, y)
new_point.show_cord()

        

