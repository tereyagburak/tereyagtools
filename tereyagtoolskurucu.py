import os
import urllib.request
import zipfile




print("TereyagTools Kurucuya Hoş Geldin! V0.7")

input("Başlamak İçin Enter'a basın.")
print("TereyagTools || {}\\TereyagTools || konumuna kuruluyor.".format(os.path.expanduser('~')))

print("Klasörler kullanıcı ana dizinine yerleştiriliyor...")
tereyagtools_path = os.path.join(os.path.expanduser('~'), 'TereyagTools')
tereyagtoolscache_path = os.path.join(os.path.expanduser('~'), 'tereyagtoolscache')

os.makedirs(tereyagtools_path, exist_ok=True)
os.makedirs(tereyagtoolscache_path, exist_ok=True)

kapat = input("Uyarı! Devam ederseniz 25MB internet ve disk alanı kullanılacaktır! Devam etmek için Enter tuşuna basın.")


print("Zip dosyası indiriliyor...")

# GitHub dosyasının URL'si
url = 'https://github.com/tereyagburak/tereyagtools/raw/main/needlefiles.zip'

# İndirme işlemi
urllib.request.urlretrieve(url, 'needlefiles.zip')

print("Zip çıkartılıyor...")

# Zip dosyasını çıkartma
with zipfile.ZipFile('needlefiles.zip', 'r') as zip_ref:
    zip_ref.extractall(tereyagtoolscache_path)

print("Zip dosyası siliniyor...")

# Zip dosyasını sil
os.remove('needlefiles.zip')

print("Dosyalar tereyagtoolscache konumundan TereyagTools konumuna kopyalanıyor...")


os.system("xcopy %USERPROFILE%\\tereyagtoolscache\\TereyagTools %USERPROFILE%\\TereyagTools /s /e /y /c /q")

print("||||    ----Başlat menüsünde TereyagTools' u bulabilirsiniz.----    ||||")

os.system('xcopy %USERPROFILE%\\tereyagtoolscache\\TereyagTools.lnk "%USERPROFILE%\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs" /s /e /y /c /q')

print("İşlemler bitti, TereyagTools başarıyla kuruldu.")


print("Python gereklidir. Eğer cihazınızda Python yüklü değilse https://www.python.org/downloads/ adresinden indirin.")







kapat = input("Programı kapatmak ve TereyagTools' u açmak için Enter tuşuna basın.")


os.system("cls")

os.system("python %USERPROFILE%\\TereyagTools\\toollauncher.py")
