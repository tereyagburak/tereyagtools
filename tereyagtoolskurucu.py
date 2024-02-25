import os
import urllib.request
import zipfile




print("TereyagTools Kurucuya Hoş Geldin!")

input("Başlamak İçin Enter'a basın.")
print("TereyagTools || {}\\TereyagTools || konumuna kuruluyor.".format(os.path.expanduser('~')))

print("Klasörler kullanıcı ana dizinine yerleştiriliyor...")
tereyagtools_path = os.path.join(os.path.expanduser('~'), 'TereyagTools')
tereyagtoolscache_path = os.path.join(os.path.expanduser('~'), 'tereyagtoolscache')

os.makedirs(tereyagtools_path, exist_ok=True)
os.makedirs(tereyagtoolscache_path, exist_ok=True)

kapat = input("Uyarı! Devam ederseniz 1MB internet ve disk alanı kullanılacaktır! Devam etmek için Enter tuşuna basın.")


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

# Zip dosyasını silebilirsiniz
os.remove('needlefiles.zip')

print("Dosyalar tereyagtoolscache konumundan TereyagTools konumuna kopyalanıyor...")


os.system("xcopy %USERPROFILE%\\tereyagtoolscache\\TereyagTools %USERPROFILE%\\TereyagTools /s /e /y /c /q")

print("Masaüstüne kısayol kopyalanıyor...")

os.system("xcopy %USERPROFILE%\\tereyagtoolscache\\TereyagTools.lnk %USERPROFILE%\\Desktop /s /e /y /c /q")

print("İşlemler bitti, TereyagTools başarıyla kuruldu.")



kapat = input("Enter'a basıp kapatın!")
