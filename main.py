import json

# Öğrenci sistemi için boş bir liste
kayitlar = []

# Ana Menü
def ana_menu():
    print("\n╔════════════════════════════════╗")
    print("║      📝 Ogrenci Bilgi Sistemi  ║")
    print("╠════════════════════════════════╣")
    print("║ 1. 👤 Yeni Ogrenci Kaydi       ║")
    print("║ 2. 📋 Ogrenci Bilgilerini Gor  ║")
    print("║ 3. 📊 Not Istatistikleri       ║")
    print("║ 4. 🚪 Programdan Cikis         ║")
    print("╚════════════════════════════════╝")

# Benzersiz numara kontrolü
def numara_kontrolu(numara):
    for ogrenci in kayitlar:
        if ogrenci["ogr_no"] == numara:
            return True
    return False

# Yeni öğrenci ekleme fonksiyonu
def yeni_kayit():
    print("\n╔══════════════════════════════╗")
    print("║      ➕ Yeni Ogrenci Kaydi    ║")
    print("╚══════════════════════════════╝")
    
    ad = input("🎓 Ogrencinin Adi: ").capitalize()
    soyad = input("🎓 Ogrencinin Soyadi: ").capitalize()
    
    while True:
        try:
            numara = int(input("🔢 Ogrenci Numarasi (3 Haneli): "))
            if 100 <= numara <= 999 and not numara_kontrolu(numara):
                break
            print("⚠️ Hatali giris! Numara benzersiz ve 3 haneli olmali.")
        except ValueError:
            print("⚠️ Lutfen sadece sayi giriniz!")

    notlar = {}
    ders_secildi = False  # En az bir ders zorunluluğu kontrolü
    while True:
        ders_adi = input("📚 Ders adini giriniz (Cikis icin 0 yazin): ").capitalize()
        if ders_adi == "0":
            if ders_secildi:
                break  # En az bir ders seçildiyse çıkış yapılabilir
            else:
                print("⚠️ En az bir ders girisi zorunludur!")
                continue
        elif ders_adi.strip():  # Boş ders adı kontrolü
            while True:
                try:
                    notu = int(input(f"📝 {ders_adi} notunu giriniz (0-100): "))
                    if 0 <= notu <= 100:
                        notlar[ders_adi] = notu
                        ders_secildi = True  # En az bir ders seçildi
                        break
                    else:
                        print("⚠️ Not 0 ile 100 arasinda olmali.")
                except ValueError:
                    print("⚠️ Lutfen sadece sayi giriniz!")
        else:
            print("⚠️ Ders adi bos olamaz!")

    kayitlar.append({"ad": ad, "soyad": soyad, "ogr_no": numara, "notlar": notlar})
    print("✅ Ogrenci basariyla kaydedildi!")

# Öğrencileri listeleme
def listeleme():
    print("\n╔══════════════════════════════╗")
    print("║     📋 Ogrenci Bilgileri     ║")
    print("╚══════════════════════════════╝")
    if not kayitlar:
        print("⚠️ Henuz kayitli ogrenci yok!")
        return
    for ogrenci in kayitlar:
        print(f"🔹 Isim: {ogrenci['ad']} {ogrenci['soyad']}, Numara: {ogrenci['ogr_no']}")
        print("   --- Notlar ---")
        if ogrenci["notlar"]:
            for ders, notu in ogrenci["notlar"].items():
                print(f"      📚 {ders}: {notu}")
        else:
            print("      ⚠️ Henuz not girilmemis.")
        print("  ════════════════════════════")

# Not istatistikleri
def not_analizi():
    print("\n╔══════════════════════════════╗")
    print("║     📊 Not Analizi           ║")
    print("╚══════════════════════════════╝")
    tum_notlar = []
    for ogrenci in kayitlar:
        tum_notlar.extend(ogrenci["notlar"].values())
    if not tum_notlar:
        print("⚠️ Henuz not girisi yapilmamis!")
        return
    
    en_yuksek = max(tum_notlar)
    en_dusuk = min(tum_notlar)
    ortalama = sum(tum_notlar) / len(tum_notlar)
    
    print(f"🏆 En Yuksek Not: {en_yuksek}")
    print(f"📉 En Dusuk Not: {en_dusuk}")
    print(f"📈 Sinif Ortalamasi: {ortalama:.2f}")

# Program akışı
while True:
    ana_menu()
    secim = input("👉 Bir secim yapiniz: ")
    if secim == "1":
        yeni_kayit()
    elif secim == "2":
        listeleme()
    elif secim == "3":
        not_analizi()
    elif secim == "4":
        print("👋 Programdan cikis yapiliyor...")
        break
    else:
        print("⚠️ Hatali secim, tekrar deneyiniz!")
