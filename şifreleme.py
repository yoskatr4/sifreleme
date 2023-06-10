from cryptography.fernet import Fernet
import os

def anahtar_olustur():
    anahtar = Fernet.generate_key()
    with open("anahtar.key", "wb") as dosya:
        dosya.write(anahtar)

def anahtar_yukle():
    with open("anahtar.key", "rb") as dosya:
        anahtar = dosya.read()
    return anahtar

def dosya_sifrele(dosya_adi, anahtar):
    fernet = Fernet(anahtar)
    with open(dosya_adi, 'rb') as dosya:
        veri = dosya.read()
    sifreli_veri = fernet.encrypt(veri)
    with open(dosya_adi, 'wb') as dosya:
        dosya.write(sifreli_veri)

def dosya_sifresini_ac(dosya_adi, anahtar):
    fernet = Fernet(anahtar)
    with open(dosya_adi, 'rb') as dosya:
        sifreli_veri = dosya.read()
    cozulmus_veri = fernet.decrypt(sifreli_veri)
    with open(dosya_adi, 'wb') as dosya:
        dosya.write(cozulmus_veri)

# Kullanıcıdan şifrelemek veya şifresini açmak istediği dosyanın adını ve yolu alalım
dosya_yolu = input("Dosyanın adını ve yolunu girin: ")

# Kullanıcıdan yapmak istediği işlemi alalım (şifreleme veya şifresini açma)
islem = input("İşlemi seçin (sifrele / ac): ")

if islem == "sifrele":
    # Anahtar oluştur
    anahtar_olustur()
    # Anahtarı yükle
    anahtar = anahtar_yukle()
    # Dosyayı şifrele
    dosya_sifrele(dosya_yolu, anahtar)
    print("Dosya başarıyla şifrelendi.")

elif islem == "ac":
    # Anahtarı yükle
    anahtar = anahtar_yukle()
    # Dosyanın şifresini aç
    dosya_sifresini_ac(dosya_yolu, anahtar)
    print("Dosya başarıyla çözüldü.")

else:
    print("Geçersiz işlem seçildi.")

