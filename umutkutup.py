from abc import ABC, abstractmethod

class Kaynak(ABC):
    def __init__(self, baslik, kayit_no):
        self.baslik = baslik
        self.kayit_no = kayit_no

    @property
    def baslik(self):
        return self._baslik

    @baslik.setter
    def baslik(self, deger):
        self._baslik = deger

    @property
    def kayit_no(self):
        return self._kayit_no

    @kayit_no.setter
    def kayit_no(self, deger):
        self._kayit_no = deger

    @abstractmethod
    def __str__(self):
        pass

class Kitap(Kaynak):
    def __init__(self, baslik, kayit_no, sayfa_sayisi, yazar):
        super().__init__(baslik, kayit_no)
        self.sayfa_sayisi = sayfa_sayisi
        self.yazar = yazar

    @property
    def sayfa_sayisi(self):
        return self._sayfa_sayisi

    @sayfa_sayisi.setter
    def sayfa_sayisi(self, deger):
        self._sayfa_sayisi = deger

    @property
    def yazar(self):
        return self._yazar

    @yazar.setter
    def yazar(self, deger):
        self._yazar = deger

    def __str__(self):
        return f"Kitap [Kayit No: {self.kayit_no}] - {self.baslik} | Yazar: {self.yazar} | Sayfa: {self.sayfa_sayisi}"

class Dergi(Kaynak):
    def __init__(self, baslik, kayit_no, konu, baski_sayisi):
        super().__init__(baslik, kayit_no)
        self.konu = konu
        self.baski_sayisi = baski_sayisi

    @property
    def konu(self):
        return self._konu

    @konu.setter
    def konu(self, deger):
        self._konu = deger

    @property
    def baski_sayisi(self):
        return self._baski_sayisi

    @baski_sayisi.setter
    def baski_sayisi(self, deger):
        self._baski_sayisi = deger

    def __str__(self):
        return f"Dergi [Kayit No: {self.kayit_no}] - {self.baslik} | Konu: {self.konu} | Baski Sayisi: {self.baski_sayisi}"

class Islem(ABC):
    @abstractmethod
    def ekle(self, tum_kayitlar):
        pass

    @abstractmethod
    def sil(self):
        pass

    @abstractmethod
    def guncelle(self):
        pass

    @abstractmethod
    def listele(self):
        pass

class KitapIslem(Islem):
    def __init__(self):
        self.kitaplar = []

    def get_kayit_nolar(self):
        return [k.kayit_no for k in self.kitaplar]

    def ekle(self, tum_kayit_nolar):
        print("\n--- Kitap Ekle ---")
        baslik = input("Kitabin basligini girin: ")
        kayit_no = input("Kitabin kayit numarasini girin: ")

        if kayit_no in tum_kayit_nolar:
            print("Hata: Bu kayit numarasi zaten baska bir kaynakta mevcut!")
            return

        yazar = input("Kitabin yazarini girin: ")
        sayfa_sayisi = input("Kitabin sayfa sayisini girin: ")

        yeni_kitap = Kitap(baslik, kayit_no, sayfa_sayisi, yazar)
        self.kitaplar.append(yeni_kitap)
        print("Kitap basariyla eklendi.")
        print(f"Toplam Kitap Sayisi: {len(self.kitaplar)}")

    def sil(self):
        kayit_no = input("Silinecek kitabin kayit numarasini girin: ")
        for kitap in self.kitaplar:
            if kitap.kayit_no == kayit_no:
                self.kitaplar.remove(kitap)
                print("Kitap basariyla silindi.")
                print(f"Kalan Toplam Kitap Sayisi: {len(self.kitaplar)}")
                return
        print("Kayit bulunamadi.")

    def guncelle(self):
        kayit_no = input("Guncellenecek kitabin kayit numarasini girin: ")
        for kitap in self.kitaplar:
            if kitap.kayit_no == kayit_no:
                print("Yeni bilgileri girin (Degistirmek istemiyorsaniz bos birakip Enter'a basin):")
                yeni_baslik = input(f"Yeni Baslik ({kitap.baslik}): ")
                yeni_yazar = input(f"Yeni Yazar ({kitap.yazar}): ")
                yeni_sayfa = input(f"Yeni Sayfa Sayisi ({kitap.sayfa_sayisi}): ")

                if yeni_baslik: kitap.baslik = yeni_baslik
                if yeni_yazar: kitap.yazar = yeni_yazar
                if yeni_sayfa: kitap.sayfa_sayisi = yeni_sayfa
                
                print("Kitap basariyla guncellendi.")
                return
        print("Kayit bulunamadi.")

    def listele(self):
        if not self.kitaplar:
            print("Kayit bulunamadi.")
        else:
            print("\n--- Kitap Listesi ---")
            for kitap in self.kitaplar:
                print(kitap)
            print(f"Toplam Kitap Sayisi: {len(self.kitaplar)}")

class DergiIslem(Islem):
    def __init__(self):
        self.dergiler = []

    def get_kayit_nolar(self):
        return [d.kayit_no for d in self.dergiler]

    def ekle(self, tum_kayit_nolar):
        print("\n--- Dergi Ekle ---")
        baslik = input("Derginin basligini girin: ")
        kayit_no = input("Derginin kayit numarasini girin: ")

        if kayit_no in tum_kayit_nolar:
            print("Hata: Bu kayit numarasi zaten baska bir kaynakta mevcut!")
            return

        konu = input("Derginin konusunu girin: ")
        baski_sayisi = input("Derginin baski sayisini girin: ")

        yeni_dergi = Dergi(baslik, kayit_no, konu, baski_sayisi)
        self.dergiler.append(yeni_dergi)
        print("Dergi basariyla eklendi.")
        print(f"Toplam Dergi Sayisi: {len(self.dergiler)}")

    def sil(self):
        kayit_no = input("Silinecek derginin kayit numarasini girin: ")
        for dergi in self.dergiler:
            if dergi.kayit_no == kayit_no:
                self.dergiler.remove(dergi)
                print("Dergi basariyla silindi.")
                print(f"Kalan Toplam Dergi Sayisi: {len(self.dergiler)}")
                return
        print("Kayit bulunamadi.")

    def guncelle(self):
        kayit_no = input("Guncellenecek derginin kayit numarasini girin: ")
        for dergi in self.dergiler:
            if dergi.kayit_no == kayit_no:
                print("Yeni bilgileri girin (Degistirmek istemiyorsaniz bos birakip Enter'a basin):")
                yeni_baslik = input(f"Yeni Baslik ({dergi.baslik}): ")
                yeni_konu = input(f"Yeni Konu ({dergi.konu}): ")
                yeni_baski = input(f"Yeni Baski Sayisi ({dergi.baski_sayisi}): ")

                if yeni_baslik: dergi.baslik = yeni_baslik
                if yeni_konu: dergi.konu = yeni_konu
                if yeni_baski: dergi.baski_sayisi = yeni_baski
                
                print("Dergi basariyla guncellendi.")
                return
        print("Kayit bulunamadi.")

    def listele(self):
        if not self.dergiler:
            print("Kayit bulunamadi.")
        else:
            print("\n--- Dergi Listesi ---")
            for dergi in self.dergiler:
                print(dergi)
            print(f"Toplam Dergi Sayisi: {len(self.dergiler)}")

class Menu:
    def __init__(self):
        self.kitap_islem = KitapIslem()
        self.dergi_islem = DergiIslem()

    def baslat(self):
        while True:
            print("\n\n--- Kutuphane Yonetim Sistemi ---")
            print("1. Kitap Ekle")
            print("2. Kitap Sil")
            print("3. Kitap Guncelle")
            print("4. Kitaplari Listele")
            print("5. Dergi Ekle")
            print("6. Dergi Sil")
            print("7. Dergi Guncelle")
            print("8. Dergileri Listele")
            print("9. Cikis")

            secim = input("Yapmak istediginiz islemi secin (1-9): ")
            
            tum_kayitlar = self.kitap_islem.get_kayit_nolar() + self.dergi_islem.get_kayit_nolar()

            if secim == '1':
                self.kitap_islem.ekle(tum_kayitlar)
            elif secim == '2':
                self.kitap_islem.sil()
            elif secim == '3':
                self.kitap_islem.guncelle()
            elif secim == '4':
                self.kitap_islem.listele()
            elif secim == '5':
                self.dergi_islem.ekle(tum_kayitlar)
            elif secim == '6':
                self.dergi_islem.sil()
            elif secim == '7':
                self.dergi_islem.guncelle()
            elif secim == '8':
                self.dergi_islem.listele()
            elif secim == '9':
                print("Sistemden cikiliyor...")
                break
            else:
                print("Hatali secim! Lutfen 1-9 arasi bir sayi giriniz.")

if __name__ == "__main__":
    sistem_menusu = Menu()
    sistem_menusu.baslat()
