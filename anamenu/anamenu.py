#print("\033[1;32;40m")
#print(")
import hesaplamalar.hesapmakinesi
import oyunlar.oyun
import hesaplamalar.nothesabi
import çizimler.çizim.şekiller
print ('Hoş geldin')

def anamenu():
    print("╔═══════════════════════════╗")
    print("║     VEKTOREL DERS         ║")
    print("║                           ║")
    print("║  1-Hesap makinesi         ║") 
    print("║  2-Oyunlar                ║")
    print("║  3-Çizimler               ║")
    print("║  4-Sağlık                 ║")
    print("║  5-Not hesabi             ║")
    print("║  6-...                    ║")
    print("║  ç-çıkış                  ║")
    print("║                           ║")
    print("║    Seçiminiz nedir?       ║")
    print("╚═══════════════════════════╝")                           
    secim = input()
    if secim =="1" :
        hesaplamalar.hesapmakinesi.hmmmenu()
        anamenu()
    if secim=="2" :
        oyunlar.oyun.oyunmenu()
        anamenu()
    
    if secim== "3" :
        çizimler.çizim.şekiller()
        anamenu()
   
    if secim == "5" :
        hesaplamalar.nothesabi.harfnotu()
        anamenu()
        
    if secim == "ç" or secim=="Ç": exit()
    else:
        print("Seçim sadece 1,2,3,4,5,ç olabilir.")
        anamenu()

anamenu()
