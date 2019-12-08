class Day8():
    def __init__(self):
        self.name = "D8E1"
        with open("tasks/day8/input", "r") as f:
            self.f = f.read();
            self.f = list(map(int, self.f[:-1]))

    def run(self):
        width = 25
        height = 6


        layers = [self.f[i*(width*height):(i+1) * (width*height)] for i in range((len(self.f) + (width*height) - 1) // (width*height))]

        minzero = height * width
        minzeroidx = 0
        for idx, i in enumerate(layers):
            if i.count(0) < minzero:
                minzero = i.count(0)
                minzeroidx = idx
        print(layers[minzeroidx])

        transposed = [list(i) for i in zip(*layers)]

        def top_not_transparent(lst):
            for i in lst:
                if i != 2:
                    return i

        image = []
        for i in transposed:
            image.append(top_not_transparent(i))
        binstr = ''.join([str(i) for i in image])


        def binstr_to_img(string):
            retstr = ""
            for i in string:
                if i == '1':
                    retstr += ' '
                else:
                    retstr += '█'
            return retstr

        for i in range(height):
            print(binstr_to_img(binstr[i*25:(i+1)*25]))

        return layers[minzeroidx].count(1) * layers[minzeroidx].count(2)
