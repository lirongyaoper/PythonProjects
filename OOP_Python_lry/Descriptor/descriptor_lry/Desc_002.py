class Desc(object):
    def __get__(self, instance, owner):
        print("__get__...")
        print("self: \t\t",self)
        print("instance: \t",instance)
        print("owner:  \t",owner)
        print('='*40,"\n")
    def __set__(self, instance, value):
        print("__set__...")
        print("self: \t\t",self)
        print("instance: \t",instance)
        print("value:  \t",value)
        print('=',"\n")

class TestDesc(object):
    x = Desc()

t = TestDesc()
t.x



#https://www.cnblogs.com/FlurryHeart/p/18528815