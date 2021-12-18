# #%%
# class MojaKlasa:
#     def wyswietl(x):
#         return 'Witaj Świecie'

# x = MojaKlasa()
# print(x.wyswietl())


#     def wyswietl(x):
#         return 'Witaj swiecie'


# x = MojaKlasa()
# print(x.wyswietl())
#%%
class Prostopadloscian:
    def __init__(self):
        self.podstawa_a = 0
        self.podstawa_b = 0
        self.wysokosc_h = 0

    def Objetosc(self):
        return self.podstawa_a * self.podstawa_b * self.wysokosc_h

wtc=Prostopadloscian()
wtc.podstawa_a=100
wtc.podstawa_b=200
wtc.wysokosc_h=400
print(wtc.Objetosc())


#%%

class Prostopadloscian:
    def __init__(self):
        self.podstawa_a=0
        self.podstawa_b=0
        self.wysokosc_h=0

    def Objetosc(self):
        return self.podstawa_h * self.podstawa_a * self.podstawa_b

wtc=Prostopadloscian()
wtc.podstawa_a = 100
wtc.podstawa_b = 200
wtc.wysokosc_h = 400
print(wtc.Objetosc())


# %%
class szopa:
    def __init__(self):
        self.podstawa_a= bok_a
        self.podstawa_b= bok_b
        self.wysokosc_h= wys_h

    def Pomaluj(self):
        return 2*(self.podstawa_a + self.podstawa_b) * self.wysokosc_h

szopa1 = szopa(2,3,4)


# %%
class Szopa:
    def __init__(self, bok_a, bok_b, wys_h):
        self.podstawa_a = bok_a
        self.podstawa_b = bok_b
        self.wysokosc_h = wys_h

    def Pomaluj(self):
        return 2*(self.podstawa_a + self.podstawa_b) * self.wysokosc_h


szopa1 = Szopa(2, 3, 5)
print(szopa1.Pomaluj())
szopa2 = Szopa(5, 1, 2)
print(szopa2.Pomaluj())
# %%

class koty:
    def __init__(self,imie,kolor,masc,dl,):
        self.name = imie
        self.kolor_oczu = kolor
        self.kolor_sersci = masc 
        self.dlugosc = 0
        self.wiek = 0
        self.waga = 0
    def 

    
