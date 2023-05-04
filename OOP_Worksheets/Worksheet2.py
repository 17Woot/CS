class Shapes(object):
    def __init__(self,fill,outline_colour, outline_thickness):
        self.fill = fill
        self.outline_colour = outline_colour
        self.outline_thickness = outline_thickness

    def Rotate(self, angle):
        print("Rotating by", angle , "degrees")

    def Copy(self):
        print("Copied")

    def Enlarge(self, percentage):
        print("Enlarged by", percentage, "%")


class Circle(Shapes):
    def __init__(self, radius, centre,fill,outline_colour,outline_thickness):
        self.radius = radius
        self.centre = centre
        super().__init__(fill,outline_colour,outline_thickness)


    def Change_Outline_Colour(self, new_colour):
        self.outline_colour = new_colour


class Rectangle(Shapes):
    def __init__(self, length, width,fill,outline_colour,outline_thickness):
        self.length = length
        self.width = width
        super().__init__(fill, outline_colour, outline_thickness)


    def Add_Text(self, text):
        print("Added text:", text)

if __name__ == "__main__":
    circle_1 = Circle(3,(0,0),"green","red","10")
    print(circle_1.fill)



