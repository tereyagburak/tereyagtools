import subprocess

print("Hoşgeldiniz!")

karanlik_sistem = ["C:\\Windows\\regedit.exe", "/s", "%USERPROFILE%\\TereyagTools\\ozellestirme\\akma\\KS.reg"]
aydinlik_sistem = ["C:\\Windows\\regedit.exe", "/s", "%USERPROFILE%\\TereyagTools\\ozellestirme\\akma\\AS.reg"]
karanlik_uyg = ["C:\\Windows\\regedit.exe", "/s", "%USERPROFILE%\\TereyagTools\\ozellestirme\\akma\\KU.reg"]
aydinlik_uyg = ["C:\\Windows\\regedit.exe", "/s", "%USERPROFILE%\\TereyagTools\\ozellestirme\\akma\\AU.reg"]

print(" 1 - Karanlık Modu Sistem Genelinde Aç")
print(" 2 - Aydınlık Modu Sistem Genelinde Aç")
print(" 3 - Karanlık Modu Uygulamaların Genelinde Aç")
print(" 4 - Aydınlık Modu Uygulamaların Genelinde Aç")

eylem = input("Yapmak istediğiniz eylemin numarasını girin: ")

if eylem == "1":
    subprocess.run(karanlik_sistem, shell=True)

elif eylem == "2":
    subprocess.run(aydinlik_sistem, shell=True)

elif eylem == "3":
    subprocess.run(karanlik_uyg, shell=True)

elif eylem == "4":
    subprocess.run(aydinlik_uyg, shell=True)

elif eylem == "31":
    print("ayip")

kapat = input("Enter' a basıp kapatın")
