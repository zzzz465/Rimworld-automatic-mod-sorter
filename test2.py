class test:
    var1 = str('var1 initial')

    @classmethod
    def setvar1(cls):
        cls.var1 = 'setvar1 called'

    @classmethod
    def printvar1(cls):
        print(cls.var1)

class1 = test()

print(class1.var1)

class1.setvar1()
print(class1.var1)
print(class1.printvar1())
print(class1.var1)
