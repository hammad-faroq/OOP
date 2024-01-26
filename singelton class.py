class Singelton:
    is_instance=None
    def __init__(self,name):
        self.name=name
    @staticmethod
    def has_obj(name):
        if Singelton.is_instance==None:
            Singelton.is_instance=Singelton(name=name)
            return Singelton.is_instance
        else:
            print("Object already exist")
s=Singelton.has_obj("Hammad")
s4=Singelton("aHammad")
s1=Singelton.has_obj("Hammads")
s2=Singelton.has_obj("Hammad")

