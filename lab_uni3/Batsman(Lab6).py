import random
class Batsman:
    def __init__(self,name,country,list_of_scores=None):
        self._name=name
        self._country=country
        """This method is used because list are mutable and global so can hold the same previous data even if you empty it or call it again through some pther instance object
        this metod is used to create list when none(no parameter is given) othehrwise associates that parameter to the attribute as a list"""
        if list_of_scores==None:
            self.scores=[]
        else:
            self.scores=list_of_scores
        self.total_score=0
        self.avg=0
        self.max=0
        self.total_fifties=0
        self.total_hundreds=0
        self.random_matches()
        self.__random_scores()
        self.calc_Total()
        self.calc_Average()
        self.find_max_score()
        self.count50s()
        self.count100s()
    def random_matches(self,matches=0):
        """This function will creates random matches when no scores are given"""
        self.x = random.randint(1, 10)
        self.matches = matches
        if  len(self.scores)==0:
            self.matches=(self.x)
        else:
            self.matches=(len(self.scores))
    def __random_scores(self):
        """This function will creates random scores when no matches are given"""
        if len(self.scores)==0:
            for i in range(self.x):
                i = random.randint(1, 10)
                y=0
                if i<=6:
                    y = random.randint(1, 180)
                if i>6 and i<=9:
                    y=random.randint(1,350)
                if i==10:
                    y = random.randint(180, 500)
                self.scores.append(y)
    def calc_Total(self):
        self.total_score=0
        for i in self.scores:
            self.total_score+=i
    def calc_Average(self):
        self.calc_Total()
        self.avg=round(self.total_score/self.matches,2)
    def find_max_score(self):
        self.max=0
        for i in self.scores:
            if i>self.max:
                self.max=i
    def count50s(self):
        for i in self.scores:
            if i>=50 and i<100:
                self.total_fifties+=1
    def count100s(self):
        for i in self.scores:
            if i>=100:
                self.total_hundreds+=1
    def __str__(self):
        return f"Player Name: {self._name}  Player Country: {self._country}\nNo of Matches: {self.matches}\nTotal Score: {self.total_score}\nAverage :{self.avg}\nMax Score: {self.max}\nTotal Fifties: {self.total_fifties}\nTotal Hundreds: {self.total_hundreds}"

"""This is the task two of the lab"""
r=Batsman("Babar Azam","Pakistan")
print(r)
v1=Batsman(name="Ms .Dhoni",country="India")
print(v1)
a=Batsman(name="Abdullah shafique",country="Paksitan",list_of_scores=[117,66,63,7,11])
print(a)
a=Batsman(name="David Warner",country="Australia",list_of_scores=[7,54,109,33,49,3])
print(a)
b=Batsman(name="Shaid afridi",country="Pakistan")
print(b)