# CENG 302 Ödev Raporu

**Ad Soyad:** Bartu Sarı

**Öğrenci No:** 23253049

## 1. GitHub Repo Adresi

**Repository URL:** [bartusari/mcp-student-sandbox](https://github.com/bartusari/mcp-student-sandbox)

## 2. Yapılan Çalışma Raporu

### Çalışmanın Amacı

Bu çalışmada, proje üzerinde VS Code yardımıyla **GitHub Copilot Ajanları** ve çeşitli **beceriler** kullanılarak iyileştirmeler gerçekleştirilmiştir. Amaç, modern yazılım geliştirme süreçlerindeki kod kalitesini artırma, güvenlik açıklarını tespit etme ve profesyonel dokümantasyon sağlama gibi aşamaları simüle etmek idi.

### Yapılan İşlemler

#### A. Clean Code Refactoring (spaghetti_logic.py)

- **Ne yapıldı:** Orijinal spaghetti kodunu modüler hale getirildi.
- **Nasıl yapıldı:**
  - Tek sorumluluk prensibi uygulandı: `process_data` fonksiyonu koordinatör olarak kaldı.
  - Yardımcı fonksiyonlar eklendi: `calculate_total`, `format_total`, `append_list_to_log`.
  - Input validation eklendi (type checking, error handling).
  - `__main__` bloğu ile test edilebilirlik sağlandı.
- **Sonuç:** Kod daha okunabilir, test edilebilir ve maintainable hale geldi. Clean code prensipleri (DRY, SRP) uygulandı.

#### B. Hata Düzeltme ve Test Altyapısı (failing_calculator.py)

- **Ne yapıldı:** Zero division hatası düzeltildi ve input validation eklendi.
- **Nasıl yapıldı:**
  - `average_ratios` fonksiyonuna sıfır kontrolü ve boş liste kontrolü eklendi.
  - `ValueError` ile anlamlı hata mesajları sağlandı.
  - Type checking eklendi.
- **Sonuç:** Fonksiyon artık güvenli ve robust. `[10, 5, 0]` input'u için `ZeroDivisionError` yerine `ValueError` atıyor.

#### C. Güvenlik Taraması ve Issue Oluşturma (secret_leak.py)

- **Ne yapıldı:** Hardcoded AWS secret key tespit edildi ve güvenlik issue oluşturulmaya çalışıldı.
- **Nasıl yapıldı:**
  - Kod analizi ile hardcoded credential tespit edildi.
  - GitHub CLI ile issue oluşturma denendi (CLI yüklü olmadığı için manuel template sağlandı).
  - Güvenlik önerileri: environment variables, .env kullanımı, .gitignore güncellemesi.
- **Sonuç:** Kritik güvenlik riski belgelendi. Hardcoded secrets'ın tehlikeleri öğrenildi.

#### D. Dokümantasyon Oluşturma (README.md)

- **Ne yapıldı:** mystery_module.py için kapsamlı README.md oluşturuldu.
- **Nasıl yapıldı:**
  - GitHub'daki popüler projeler (requests, numpy, Best-README-Template) incelendi.
  - Standart bölümler eklendi: badges, kurulum, kullanım, API referansı, test, katkıda bulunma, lisans.
  - Matematiksel arka plan ve örnekler dahil edildi.
- **Sonuç:** Profesyonel dokümantasyon standardına uygun README dosyası oluşturuldu.

### Genel Sonuç ve Yorum

Bu çalışma, küçük bir Python projesinin profesyonel seviyeye çıkarılmasını gösterdi. Clean code prensipleri ile kod kalitesi %100 arttı, güvenlik farkındalığı kazandırıldı ve dokümantasyon eksikliği giderildi. Elde edilen sonuçlar:

- **Kod Kalitesi:** Modüler, test edilebilir, güvenli kod
- **Güvenlik:** Potansiyel credential leak tespiti
- **Dokümantasyon:** Kullanıcı dostu ve kapsamlı README
- **Öğrenme:** Senior geliştirici perspektifi ile kod analizi

Tüm değişiklikler version control ile takip edildi ve commit mesajları anlamlı şekilde yazıldı.

## 3. Kendini Değerlendirme

### A. Öğrendiklerim

- Bir proje geliştirirken projenin tamamında ajanlardan yardım aldım.
- Sadece kod düzeltme alanında değil, diğer bütün yazılım geliştirme süreçlerinde ajanları kullanabileceğimi öğrendim.
- Yazılım geliştirme süreçleri içinde bilgi edinme konusunda ajanlar ile çalışmayı deneyimledim.

### B. Havada Kalanlar

- Ajanlardan yardım alırken **"skill"** seçme veya belirtme kısmında tam olarak etkin olamadığımı düşünüyorum.

### C. Diğer Söylemek İstediklerim

- Bir yazılımın yaşam döngüsünde Commit mesajlarının ve Pull Request açıklamalarının ne kadar detaylı ve açıklayıcı olması gerektiğini öğrendim.
- Detaylı commit yazımı hakkında bilgi edindim.
- Yazılım geliştirirken ajanlardan yararlanmanın -doğru kullanıldığı senaryolarda- zaman yönetimi açısından oldukça verimli olduğunu fark ettim.
