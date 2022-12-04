class Orchid:
    def __init__(self, color, pora_kwitnienia, gatunek):
        self.krolestwo = "krolestwo_roslin"
        self.pora_kwitnienia = pora_kwitnienia
        self.gatunek = gatunek
        self.color = color


    def jaki_kolor(self):
        return self.color

    def jaka_pora_kwitnienia(self):
        return self.pora_kwitnienia

    def jaki_gatunek(self):
        return self.gatunek

    def jakie_krolestwo(self):
        return self.krolestwo

storczyk_nr_1 = Orchid()