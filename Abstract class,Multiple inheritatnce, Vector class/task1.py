
class Vector:
    def __init__(self,list):
        self.tupe=list
    def __str__(self):
        j=0
        v=""
        for i in self.tupe:
            if i >=0:
                v+=f"+{i}X{j}"
            else:
                v += f"{i}X{j}"
            j+=1
        return f'The Vector :{v.lstrip("+")}'
    def __getitem__(self, index):
        """These both dunder methods are for the indexing"""
        return self.tupe[index]
    def __setitem__(self, index, value):
        self.tupe[index]=value
    def magnitude(self):
        mag=0
        for i in self.tupe:
            mag+=i**2
        mag=round(mag**0.5,2)
        return f"magnitude :{mag}"
    def dot_product(self,other):
        """This is the method for the dot product of the vector"""
        if len(self.tupe)> len(other.tupe) or len(self.tupe) < len(other.tupe):
            return "dot product is not possible"
        dot=0
        for i in range(len(self.tupe)):
            dot+=self.tupe[i]*other.tupe[i]
        return f"Va.Vb :{dot}"
    def scalar_multiplication(self,c):
        c1=len(self.tupe)
        for i in range(c1):
            self.tupe[i]=(self.tupe[i] * c)
        return self.__str__()
    def negative_of_vector(self):
        """This method will negate a vector"""
        c1 = len(self.tupe)
        for i in range(c1):
            self.tupe[i] = (self.tupe[i] * -1)
        return self.__str__()
    def __add__(self, other):
        """This method will add two vectors"""
        if len(self.tupe) > len(other.tupe) or len(self.tupe) < len(other.tupe):
            return "Addition is not possible"
        c1 = len(self.tupe)
        for i in range(c1):
            self.tupe[i] = (self.tupe[i] +other.tupe[i])
        return self.__str__()
    def __sub__(self, other):
        """This method will subtract the two vectors"""
        if len(self.tupe) > len(other.tupe) or len(self.tupe) < len(other.tupe):
            return "Subtraction is not possible"
        c1 = len(self.tupe)
        for i in range(c1):
            self.tupe[i] = (self.tupe[i] - other.tupe[i])
        return self.__str__()
def main():
    """These are the multiple test cases for the vector class"""
    v=Vector([1,2,3])
    print(v.magnitude())
    print(v.negative_of_vector())
    print(v.scalar_multiplication(3))
    print(v.magnitude())
    d=Vector([1,4,5])
    print(v+d)
    print(v.dot_product(d))
    print(v-d)
    print(v.magnitude())
    print(d.magnitude())
main()