class Bunny:

    def __init__(self, name, color):
        self.name = name
        self.color = color
    
    def hop(self, dir):
        # if (dir != "l") or (dir != "r") or (dir != "f") or (dir != "b"):
        #     print("Please enter one of the following: (l)eft, (r)ight, (f)orward, or (b)ackward")
        
        match dir:
            case 'l':
                print(self.name, "hopped left!")
            case 'r':
                print(self.name, "hopped right!")
            case 'f':
                print(self.name, "hopped forward!")
            case 'b':
                print(self.name, "hopped backward!")
            case _:
                print(self.name, "hopped nowhere...")
        


def main():
    foo = Bunny("Foofoo", "white and brown")

    print(foo.name, "is", foo.color)
    foo.hop('f')
    foo.hop('f')
    foo.hop('r')
    foo.hop('l')
    foo.hop('b')

main()