from abc import ABC,abstractmethod
from tkinter import*
class Shape:
    """This is the abstract class"""
    t = Tk()
    @abstractmethod
    def area(self):
        pass
    @abstractmethod
    def perimeter(self):
        pass
    @abstractmethod
    def draw(self):
        pass
class Rectange(Shape):
    """This is the rctangle class"""
    def __init__(self,len,wid):
        self.length=len
        self.width=wid
    def area(self):
        return f"Area :{round(self.length*self.width,2)} m**2"
    def perimeter(self):
        return f"Perimeter :{round(2*(self.length+self.width),2)} m"
    def draw(self):
        """This method will draw the desired shape on the canvas"""
        canvas=Canvas()
        canvas.create_rectangle(self.length,self.width,self.length*2,self.width*2,outline="black",fill="white",width=2)
        canvas.pack()
class Circle(Shape):
    """This is the second class inherited from the shape class"""
    def __init__(self,radius):
        self.radius=radius
    def area(self):
        return f"Area :{round(22/7*(self.radius*self.radius),2)} m**2"
    def perimeter(self):
        return f"Perimeter :{round(2*(22/7*self.radius),2)} m"
    def draw(self):
        """Same this method will show the GUI"""
        canvas=Canvas()
        canvas.create_oval(self.radius,10, self.radius*2, 70, outline="black", fill="white", width=2)
        canvas.pack()
class Square(Rectange):
    def __init__ (self,len,outline,border_size,fill):
        self.length=len
        self.outline=outline
        self.border_size=border_size
        self.colour=fill
    def area(self):
        return f"Area :{round(self.length*self.length,2)}"
    def perimeter(self):
        return f"Perimeter :{round(2*(self.length+self.length),2)} m"
    def draw(self):
        """This method will show the GUI but this time takes the argumentst like colour,size aas a init parameter :)"""
        canvas=Canvas()
        canvas.create_rectangle(self.length,self.length,self.length*2+50,self.length*2+50,outline=self.outline,fill=self.colour,width=self.border_size)
        canvas.pack()
    def __str__(self):
        return f"Area :{round(self.length*self.length,2)}\nOutline :{self.outline}\nBorder_size :{self.border_size}\nColour :{self.colour}"
class Oval(Circle):
    def __init__(self,radius,outline,border_size,fill):
        self.radius=radius
        self.outline=outline
        self.border_size=border_size
        self.fill=fill
    def perimeter(self):
        return f"Perimeter :{round(2*(22/7*self.radius),2)} m"
    def area(self):
        return f"Area :{round(22/7*(self.radius*self.radius),2)} m**2"
    def __str__(self):
        return f"Area :{round(22/7*self.radius,2)}\nOutline :{self.outline}\nBorder_size :{self.border_size}\nFill :{self.fill}"
    def draw(self):
        """same as the square class"""
        """This is called polymorphism where you have multiple inheritance and you have same methods in the calsses but you overight thatt methods to add more functionality -_-"""
        canvas = Canvas()
        canvas.create_rectangle(self.radius,self.radius,80,80,outline=self.outline, fill=self.fill, width=self.border_size)
        canvas.pack()
        Shape.t.mainloop()
def main():
    r=Rectange(50,70)
    print(r.area())
    r.draw()
    c=Circle(40)
    print(c.area())
    c.draw()
    s=Square(30,"black",3,fill="white")
    print(s.area())
    s.draw()
    print(s)
    o=Oval(10,"black",3,fill="white")
    o.draw()
main()
