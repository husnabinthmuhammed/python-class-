"""
3.Define a class, which have a class parameter and have a same instance parameter.

Hints:
    Define a instance parameter, need add it in __init__ method
    You can inita object with construct parameter or set the value later

"""

class ins:

    clapara="class parameter"
    def __init__(self,instancepara):
        self.instancepara="iam intance para"
        #self.instancepara=instancepara
        #print(self.instancepara)

    def getpara(self):

        print(self.instancepara)

obj = ins("set the value later")
print(obj.clapara)
obj.getpara()