# -*- coding: utf-8 -*-
class Istenilen_Tabana_Donustur():
    def __init__(self, intSayi, doubleTabanDegeri,secimiki):
            self.intSayi = intSayi
            self.doubleTabanDegeri = doubleTabanDegeri
            self.secimiki = secimiki
            
    def IkilikTabanaCevir(self,onlukSayi):
        if(onlukSayi > 1):  
            self.IkilikTabanaCevir(onlukSayi//2)
        print(onlukSayi%2, end='')

    def DortlukTabanaCevir(self,onlukSayi):
        if(onlukSayi > 1):  
            self.DortlukTabanaCevir(onlukSayi//4)
        print(onlukSayi%4, end='')

    def SekizlikTabanaCevir(self,onlukSayi):
        if(onlukSayi > 1):  
            self.SekizlikTabanaCevir(onlukSayi//8)
        print(onlukSayi%8, end='')

    def OnaltılıkTabanaCevir(self,onlukSayi):
        print(hex(onlukSayi))

    def OnlukTabanaCevir(self):
        onlukSayi= 0
        if self.doubleTabanDegeri == "2":
            ust = 0
            sonuc= 0
            for i in reversed(range(len(self.intSayi))):
                ustal = 2**ust
                sonuc= sonuc + int(self.intSayi[i]) * ustal
                ust = ust + 1
            onlukSayi = sonuc

        if self.doubleTabanDegeri == "10":
            onlukSayi = int(self.intSayi)
        if self.doubleTabanDegeri == "4":
            ust = 0
            sonuc= 0
            for i in reversed(range(len(self.intSayi))):
                ustal = 4**ust
                sonuc= sonuc + int(self.intSayi[i]) * ustal
                ust = ust + 1
            onlukSayi = sonuc      

        if self.doubleTabanDegeri == "8":
            ust = 0
            sonuc= 0
            for i in reversed(range(len(self.intSayi))):
                ustal = 8**ust
                sonuc= sonuc + int(self.intSayi[i]) * ustal
                ust = ust + 1
            onlukSayi = sonuc         

        if self.doubleTabanDegeri == "16":
            ust = 0
            sonuc= 0
            for i in reversed(range(len(self.intSayi))):
                ustal = 16**ust
                onaltilik= self.intSayi[i]

                if self.intSayi[i] == "A" or self.intSayi[i] == "a" :
                    onaltilik = 10
                if self.intSayi[i] == "B" or self.intSayi[i] == "b":
                    onaltilik = 11
                if self.intSayi[i] == "C" or self.intSayi[i] == "c":
                    onaltilik = 12
                if self.intSayi[i] == "D" or self.intSayi[i] == "d":
                    onaltilik = 13
                if self.intSayi[i] == "E" or  self.intSayi[i] == "e":
                    onaltilik = 14
                if self.intSayi[i] == "F" or self.intSayi[i] == "f" :
                    onaltilik = 15
                    
                sonuc= sonuc + int(onaltilik) * ustal
                ust = ust + 1
            onlukSayi = sonuc
        
        if secimiki == "2":
            self.IkilikTabanaCevir(onlukSayi)
        if secimiki == "4":
            self.DortlukTabanaCevir(onlukSayi)
        if secimiki == "8":
            self.SekizlikTabanaCevir(onlukSayi)
        if secimiki == "10":
            print(onlukSayi)
        if secimiki == "16":
            self.OnaltılıkTabanaCevir(onlukSayi)
                

print("Lütfen Gerçekleştireceğiniz İşlemler İçin Aşağıdaki Menüyü Kullanınız.\n")
print("2. İki Tabanında Sayı")
print("4. Dört Tabanında Sayı")
print("8. Sekiz Tabanında Sayı")
print("10. On Tabanında Sayı")
print("16. Onaltı Tabanında Sayı\n")

print("İşlem Yaptırmak İstediğiniz Sayının Tabanını Menüden Seçiniz.\n")
print("Sectiğiniz Kodu Giriniz: ")
secim = input()

print("İşlem Yaptırmak İstediğiniz Sayıyı Giriniz: ")
sayi = input()

print("Hangi Tabana Çevirmek İstediğinizi Menüden Seçiniz: \n")
print("Sectiğiniz Kodu Giriniz: ")
secimiki = input()

donustur = Istenilen_Tabana_Donustur(sayi,secim,secimiki)
donustur.OnlukTabanaCevir()
