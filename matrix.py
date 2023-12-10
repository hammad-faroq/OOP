class Matrix:
    def __init__(self,row,cols,list):
        self.rows=row
        self.cols=cols
        self.list=list
        self.matrix=""
        self.new=self.cols
        self.new1=self.rows
        self.new2=self.rows

    @property
    def rows(self):
        return self.__rows
    @rows.setter
    def rows(self,value):
        self.__rows=value
    @property
    def cols(self):
        return self.__cols
    @cols.setter
    def cols(self,value):
        self.__cols=value
    @property
    def list(self):
        return self.__list
    @list.setter
    def list(self,value):
        self.__list=value
        ##problem with the rows whrn changed not adding properly
    # def __add__(self, other):
    #     self.matrix="["
    #     self.new=other.rows
    #     self.new1=self.cols
    #     # print(self.new1)
    #     if len(self.list)>len(other.list):
    #         for i in range(len(self.list)):
    #             # print(i)
    #             if i==other.rows:
    #                 self.matrix += ","
    #                 self.matrix += str(self.list[i])
    #                 self.new +=other.rows
    #                 pass
    #             else:
    #                 if i == self.new1:
    #                     self.matrix += "\n"
    #                     self.new1 += self.cols
    #                 if i< len(other.list):
    #                     if i==0:
    #                         pass
    #                     else:
    #                         self.matrix += ","
    #                     # print(i)
    #                     # print(self.rows)
    #                     if i >self.rows:
    #                         # print(i)
    #                         self.matrix+=str(self.list[i]+other.list[i-1])
    #                     else:
    #                         self.matrix += str(self.list[i] + other.list[i])
    #
    #                 else:
    #                     self.matrix += ","
    #                     self.matrix += str(self.list[i])
    #
    #         self.matrix += "]"
    #         return self.matrix
    def __add__(self, other):
        if len(self.list)==len(other.list):
            self.matrix = "["
            self.new = self.cols
            for i in range(len(self.list)):
                if i==self.new:
                    self.matrix += "\n"
                    self.matrix += str(self.list[i] + other.list[i])
                    self.new += self.cols
                else:
                    if i==0:
                        pass
                    else:
                        self.matrix += ","
                    self.matrix += str(self.list[i] + other.list[i])
            self.matrix += "]"
        else:
            return "Can't add two matrices with different order right now!"
        return self.matrix
    def __sub__(self, other):
        if len(self.list) == len(other.list):
            self.matrix = "["
            self.new = self.cols
            for i in range(len(self.list)):
                if i == self.new:
                    self.matrix += "\n"
                    self.matrix += str(self.list[i] - other.list[i])
                    self.new += self.cols
                else:
                    if i == 0:
                        pass
                    else:
                        self.matrix += ","
                    self.matrix += str(self.list[i] - other.list[i])
            self.matrix += "]"
        else:
            return "Can't subtract two matrices with different order right now!"
        return self.matrix


    def __str__(self):
        self.matrix+="["
        for i in range(len(self.list)):
            if i==self.new:
                self.matrix+="\n"
                self.matrix+=str(self.list[i])
                self.new+=self.cols
            else:
                if i==0:
                    pass
                else:
                    self.matrix += ","
                self.matrix+=str(self.list[i])
        self.matrix+="]"
        return self.matrix
    def __mul__(self, other):
        if len(self.list) == len(other.list):
            self.matrix = "["
            self.new = self.cols
            for i in range(len(self.list)):
                if i == self.new:
                    self.matrix += "\n"
                    self.matrix += str(self.list[i] * other.list[i])
                    self.new += self.cols
                else:
                    if i == 0:
                        pass
                    else:
                        self.matrix += ","
                    self.matrix += str(self.list[i]* other.list[i])
            self.matrix += "]"
        else:
            return "Can't Multiply two matrices with different order right now!"
        return self.matrix
    def transpose(self):
        self.matrix=""
        self.matrix += "["
        for i in range(self.cols):
            if i==self.cols-1:
                self.matrix += str(self.list[i])+","+str(self.list[i+self.cols])
            else:
                self.matrix += str(self.list[i]) + "," + str(self.list[i + self.cols])+"\n"
        self.matrix += "]"
        return self.matrix


m=Matrix(2,4,[1,2,3,4,5,6,7,8])
print(m)
print(m.transpose())



