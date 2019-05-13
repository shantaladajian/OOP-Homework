class Grade:
    min=0
    max=100

    def __init__(self, mark=-1):
        self.mark=mark
        if(mark==-1):
            self.mark= Grade.askUserInput()
        else:
            self.mark=mark

    @classmethod
    def askUserInput(cls):
        while True:
            x=input("Please insert the grade between 0 and 100")
            if x.isnumeric():
                x=int(x)
                if x>0 and x<100:
                    return x
                else:
                    print("ERROR. please input a number BETWEEN 0 and 100")
            else:
                print("try again. the number between 0 and 100")

    def display(self):
        if (self.isValid()):
            print(self.mark)
        else:
            print("Invalid mark")

    def isValid(self):
        return Grade.min <= self.mark and self.mark<=Grade.max

def main():
    gr1=Grade(85)
    gr1.display()

    gr2=Grade(185)
    gr2.display()

    gr3=Grade()
    gr3.display()

main()