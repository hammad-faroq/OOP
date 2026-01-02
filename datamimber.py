class Timespan():
    def __init__(self,hours1):
        divide=hours1*60
        hr=int(divide//60)
        mn=int(divide%60)
        self.hours=hr
        self.minutes=mn
    def add_hours(self,hours1):
        self.hours+=hours1
    def add_minutes(self,mints):
        if self.minutes+mints>60:
            hours=(self.minutes+mints)//60
            mints1=(self.minutes+mints)%60
            print(mints)
            self.minutes=mints1
            self.hours+=hours
        else:
            self.minutes+=mints
    def show(self):
        return (f"{self.hours} hours and {self.minutes} minutes.")
    def change(self,time2):
        if self.hours-time2.hours <0:
            if (self.minutes-time2.minutes)<0:
                if self.hours>time2.hours:
                    return (((self.hours - time2.hours) * -1) * 60 + (((self.minutes - time2.minutes)) * -1))*-1
                return ((self.hours-time2.hours)*-1)*60+(((self.minutes-time2.minutes))*-1)
            else:
                if self.hours > time2.hours:
                    return (((self.hours - time2.hours) * -1) * 60 + (((self.minutes - time2.minutes)) * -1)) * -1
                return ((self.hours - time2.hours) * -1) * 60 +(self.minutes - time2.minutes)
        else:
            if (self.minutes-time2.minutes)<0:
                if self.hours > time2.hours:
                    return (((self.hours - time2.hours) * -1) * 60 + (((self.minutes - time2.minutes)) * -1)) * -1
                return ((self.hours-time2.hours)*-1)*60+(((self.minutes-time2.minutes))*-1)
            else:
                if self.hours > time2.hours:
                    return (((self.hours - time2.hours) * -1) * 60 + (((self.minutes - time2.minutes)) * -1)) * -1
                return (self.hours - time2.hours)*60+(self.minutes-time2.minutes)


time=Timespan(2)
# print(time.show())
# time.add_hours(2)
# print(time.show())
time.add_minutes(31)
print(time.show())
time2=Timespan(1,)
print(time2.show())
print(time.change(time2))