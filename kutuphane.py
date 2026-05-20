from abc import ABC, abstractmethod

class Kaynak:
    def __init__(self, baslik, kayitNo):
        self._baslik = baslik
        self._kayitNo = kayitNo

    @property
    def baslik(self):
        return self._baslik

    @baslik.setter
    def baslik(self, value):
        self._baslik = value

    @property
    def kayitNo(self):
        return self._kayitNo

    @kayitNo.setter
    def kayitNo(self, value):
        self._kayitNo = value

class Kitap(Kaynak):
    def __init__(self, baslik, kayitNo, yazar, sayfa_sayisi):
        super().__init__(baslik, kayitNo)
        self._yazar = yazar
        self._sayfa_sayisi = sayfa_sayisi

    @property
    def yazar(self):
        return self._yazar

    @yazar.setter
    def yazar(self, value):
        self._yazar = value

    @property
    def sayfa_sayisi(self):
        return self._sayfa_sayisi

    @sayfa_sayisi.setter
    def sayfa_sayisi(self, value):
        self._sayfa_sayisi = value

    def __str__(self):
        return f"Kayıt No: {self.kayitNo} | Kitap: {self.baslik} | Yazar: {self.yazar} | Sayfa: {self.sayfa_sayisi}"

class Dergi(Kaynak):
    def __init__(self, baslik, kayitNo, yayin_donemi, sayi_no):
        super().__init__(baslik, kayitNo)
        self._yayin_donemi = yayin_donemi
        self._sayi_no = sayi_no

    @property
    def yayin_donemi(self):
        return self._yayin_donemi

    @yayin_donemi.setter
    def yayin_donemi(self, value):
        self._yayin_donemi = value

    @property
    def sayi_no(self):
        return self._sayi_no

    @sayi_no.setter
    def sayi_no(self, value):
        self._sayi_no = value

    def __str__(self):
        return f"Kayıt No: {self.kayitNo} | Dergi: {self.baslik} | Dönem: {self.yayin_donemi} | Sayı: {self.sayi_no}"

class IslemSistemi(ABC):
    @abstractmethod
    def ekle(self):
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

class KutuphaneYonetimi(IslemSistemi):
    def __init__(self):
        self.kitaplar = []
        self.dergiler = []

    def _kayit_kontrol(self, kayitNo):
        for k in self.kitaplar + self.dergiler:
            if k.kayitNo == kayitNo:
                return True
        return False

    def _birebir_ayni_mi(self, tur, baslik, yazar_veya_donem, sayfa_veya_sayi):
        if tur == "kitap":
            for k in self.kitaplar:
                if k.baslik == baslik and k.yazar == yazar_veya_donem and k.sayfa_sayisi == sayfa_veya_sayi:
                    return True
        elif tur == "dergi":
            for d in self.dergiler:
                if d.baslik == baslik and d.yayin_donemi == yazar_veya_donem and d.sayi_no == sayfa_veya_sayi:
                    return True
        return False

    def ekle(self, tur):
        kayitNo = input("Kayıt No: ")
        if self._kayit_kontrol(kayitNo):
            print("Bu kayıt numarası zaten mevcut! Ekleme başarısız.")
            return

        baslik = input("Başlık: ")
        if tur == "kitap":
            yazar = input("Yazar: ")
            sayfa = input("Sayfa Sayısı: ")
            if self._birebir_ayni_mi("kitap", baslik, yazar, sayfa):
                print("Bu kitap zaten eklendi!")
                return
            self.kitaplar.append(Kitap(baslik, kayitNo, yazar, sayfa))
            print("Kitabınız başarıyla eklendi.")
        elif tur == "dergi":
            donem = input("Yayın Dönemi (Aylık/Haftalık): ")
            sayi = input("Sayı No: ")
            if self._birebir_ayni_mi("dergi", baslik, donem, sayi):
                print("Bu dergi zaten eklendi!")
                return
            self.dergiler.append(Dergi(baslik, kayitNo, donem, sayi))
            print("Derginiz başarıyla eklendi.")

    def sil(self, tur):
        kayitNo = input("Silinecek Kaynak Kayıt No: ")
        liste = self.kitaplar if tur == "kitap" else self.dergiler
        for k in list(liste):
            if k.kayitNo == kayitNo:
                liste.remove(k)
                nesne_turu = "Kitap" if tur == "kitap" else "Dergi"
                print(f"{nesne_turu} başarıyla silindi.")
                return
        print("Kayıt bulunamadı.")

    def guncelle(self, tur):
        kayitNo = input("Güncellenecek Kaynak Kayıt No: ")
        liste = self.kitaplar if tur == "kitap" else self.dergiler
        for k in liste:
            if k.kayitNo == kayitNo:
                k.baslik = input(f"Yeni Başlık ({k.baslik}): ")
                if tur == "kitap":
                    k.yazar = input(f"Yeni Yazar ({k.yazar}): ")
                    k.sayfa_sayisi = input(f"Yeni Sayfa Sayısı ({k.sayfa_sayisi}): ")
                    print("Kitap bilgileri başarıyla güncellendi.")
                elif tur == "dergi":
                    k.yayin_donemi = input(f"Yeni Yayın Dönemi ({k.yayin_donemi}): ")
                    k.sayi_no = input(f"Yeni Sayı No ({k.sayi_no}): ")
                    print("Dergi bilgileri başarıyla güncellendi.")
                return
        print("Kayıt bulunamadı.")

    def listele(self, tur):
        liste = self.kitaplar if tur == "kitap" else self.dergiler
        if not liste:
            print("Kayıt bulunamadı.")
            return
        for k in liste:
            print(k)

    def kitap_sayisi(self):
        return len(self.kitaplar)

    def dergi_sayisi(self):
        return len(self.dergiler)

    def toplam_kayit_sayisi(self):
        print(f"Toplam Kitap Sayısı: {self.kitap_sayisi()}")
        print(f"Toplam Dergi Sayısı: {self.dergi_sayisi()}")

sistem = KutuphaneYonetimi()

while True:
    print("\n--- MENÜ ---")
    print("1- Kitap Ekle")
    print("2- Kitap Sil")
    print("3- Kitap Güncelle")
    print("4- Kitap Listele")
    print("5- Dergi Ekle")
    print("6- Dergi Sil")
    print("7- Dergi Güncelle")
    print("8- Dergi Listele")
    print("9- Toplam Kayıt Sayısı")
    print("10- Çıkış")
    
    secim = input("Seçiminiz (1-10): ")
    
    if secim == "1":
        sistem.ekle("kitap")
    elif secim == "2":
        sistem.sil("kitap")
    elif secim == "3":
        sistem.guncelle("kitap")
    elif secim == "4":
        sistem.listele("kitap")
    elif secim == "5":
        sistem.ekle("dergi")
    elif secim == "6":
        sistem.sil("dergi")
    elif secim == "7":
        sistem.guncelle("dergi")
    elif secim == "8":
        sistem.listele("dergi")
    elif secim == "9":
        sistem.toplam_kayit_sayisi()
    elif secim == "10":
        break
    else:
        print("Geçersiz seçim.")