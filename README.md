#push ederken kaynaklanan bir sorunu düzeltebilmek amaçlı cursor kullanılmıştır.
# Kütüphane Yönetim Sistemi

Bu proje, Nesne Yönelimli Programlama dersi ödevi kapsamında geliştirilmiş basit bir konsol (CLI) uygulamasıdır. Projede Python kullanılmış olup, temel OOP (Nesne Yönelimli Programlama) kavramları pratiğe dökülmüştür.

## Proje Hakkında
Kütüphane yöneticisinin sistemdeki kitapları ve dergileri kolayca takip edebilmesi için tasarlanmıştır. İşlemler menü üzerinden numaralar tuşlanarak yapılır.

**Projede Kullanılan OOP Prensipleri:**
* **Sınıflar (Classes):** Nesnelerin temel yapı taşı olarak kullanıldı.
* **Kalıtım (Inheritance):** Kitap ve Dergi sınıfları, ortak özellikleri barındıran Kaynak sınıfından türetildi.
* **Kapsülleme (Encapsulation):** Özelliklere doğrudan erişim engellenerek `@property` ve `@setter` metotları kullanıldı.
* **Soyut Sınıflar (Abstract Classes):** Ortak işlemler (`ekle`, `sil` vb.) soyut sınıflar üzerinden şablonlandırıldı.

## Özellikler
- Yeni kitap ve dergi ekleme.
- Kayıt numarasına göre sistemden kaynak silme.
- Mevcut kaynakların bilgilerini güncelleme.
- Tüm kütüphane envanterini listeleme.
- *Bonus:* Aynı kayıt numarasına sahip ikinci bir eşyanın eklenmesini engelleme.

## Nasıl Çalıştırılır?
Projeyi kendi bilgisayarınızda çalıştırmak için sisteminizde Python 3.x yüklü olması yeterlidir.

1. Bu projeyi bilgisayarınıza indirin.
2. Terminal veya komut istemcisini açarak kodun bulunduğu klasöre gidin.
3. Aşağıdaki komutu çalıştırarak menüyü başlatın:

```bash
python dosya_adi.py
