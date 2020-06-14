def nums():
    args = input('input numbers: ')
    return args.split(' ')

#Figure class will find perimetr of all
class Figure: 
    def perimetr(self, sides):
        perim = 0
        if len(sides) > 2:
            for i in sides:
                perim += int(i)
        elif len(sides) == 1:
            perim = int(sides[0]) * 4
        elif len(sides) == 2:
            perim = int(sides[0]) * 2 + int(sides[1]) * 2
        print('Perimetr is', perim)

class Squere(Figure):
    def squere(self, sides):
        self.sides = sides
        sq = 0
        for i in sides:
            sq = int(i) * int(i)
        print('Squere is', sq)

class Triange(Figure):
    def squere(self):
        print('Triange squere')

class Mnogoug:
    def squere(self):
        print('Mnogoug squere')


def main():
    sides = nums()
    if len(sides) == 1:
        s = Squere()
        s.squere(sides)
        s.perimetr(sides)
    elif len(sides) == 3:
        s = Triange()
        s.squere()
        s.perimetr(sides)
    else:
        s = Mnogoug()
        s.squere()
        s.perimetr(sides)

main()