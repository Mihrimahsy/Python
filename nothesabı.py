def harfnotu():
    print("Bu fonksiyon harf notu hesaplar.")
    not1 = int(input("Notun nedir?"))
    if not1 > 100 or not1 < 0 : print ("yanlış giriş '0-100' arası olabilir")
    else :
        if not1 > 90 : print("Notun AA")
        elif not1 > 80 : print("Notun BA")
        elif not1 > 70 : print("Notun BB")
        elif not1 < 50 : print("Kaldın")
        if not1 >70 and not1<90 : print("Notun iyi dostum")
        
    
