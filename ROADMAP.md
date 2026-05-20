# Proje Yol Haritası (Roadmap)

Bu dosya, Kütüphane Yönetim Sistemi ödevinin yönergedeki adımlara göre geliştirilme aşamalarını ve tamamlanma durumunu göstermektedir.

## Bölüm 1 - Tasarım
- [x] **1.1 Sınıf Diyagramı:** Sınıflar, özellikler ve metotlar belirlendi. Kalıtım ilişkileri kağıt üzerinde çizilmek üzere planlandı.
- [x] **1.2 Özelliklerin Belirlenmesi:** Kaynak (baslik, kayit_no), Kitap (sayfa_sayisi, yazar) ve Dergi (konu, baski_sayisi) özellikleri tabloya uygun şekilde netleştirildi.
- [x] **1.3 Menü Tasarımı:** 1-4 Kitap işlemleri, 5-8 Dergi işlemleri ve 9 Çıkış olacak şekilde 9 maddeli konsol menüsü tasarlandı.

## Bölüm 2 - Kodlama
- [x] **2.1 Kapsülleme (Zorunlu):** Tüm sınıflardaki özellikler `self._degisken` formatında kapsüllendi, `@property` ve `@deger.setter` ile güvenli erişim sağlandı.
- [x] **2.2 Kalıtım (Zorunlu):** Kitap ve Dergi sınıfları Kaynak sınıfından miras aldı. Üst sınıf bağlantıları `super().__init__()` ile kuruldu.
- [x] **2.3 Soyut Sınıf (Zorunlu):** `abc` modülü sisteme dahil edildi. `Islem` sınıfında `ekle`, `sil`, `guncelle`, `listele` metotları `@abstractmethod` olarak tanımlandı.
- [x] **2.4 Menü Döngüsü (Zorunlu):** Sistem arayüzü `while True` döngüsü içine alınarak sürekli çalışması sağlandı. Kullanıcı seçimleri `if-elif` yapısıyla yönlendirildi.

## Bölüm 3 - Bonus Uygulamaları
- [x] **Kayıt Numarası Kontrolü:** Aynı `kayit_no` ile ikinci bir kitabın veya derginin eklenmesi engellendi.
- [x] **Hata Mesajları:** Listeleme, silme veya güncelleme yaparken ilgili kayıt yoksa "Kayıt bulunamadı." mesajı gösterildi.
- [ ] **Kayıt Sayısı Sayacı:** Ekleme ve listeleme ekranlarının sonuna o anki toplam kitap/dergi sayısını hesaplayıp gösteren `len()` fonksiyonları eklendi.
- [ ] **Formatlı Çıktı:** Sınıfların içine `__str__` metodu yazılarak (override) listeleme ekranında verilerin temiz bir metin halinde yazdırılması sağlandı.

## Teslim Aşaması
- [ ] Kodların değişken adlarında Türkçe karakter kullanılmadan, temel standartlarda yazılması sağlandı.
- [ ] GitHub deposu oluşturularak gerekli kodlar ve dokümantasyon dosyaları eklendi.
- [ ] Tasarım çizimleri ve GitHub linki bir PDF'te birleştirilip Classroom üzerinden teslim edilecek. *(Son adım)*
