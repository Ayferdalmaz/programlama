#1.SORU
def kar():
    x=int(input("finansman geliri giriniz:"))
    y=int(input("pazar geliri giriniz:"))
    z=int(input("kira geliri giriniz:"))
    toplamGelir=x+y+z
    print("toplam gelir")
    k=int(input("ücret giriniz:"))
    l=int(input("finansman giderlerini giriniz:"))
    m=int(input("pazar gideri giriniz:"))
    n=int(input("muhasebe gideri giriniz:"))
    o=int(input("kira gideri giriniz:"))
    toplamGider=k+l+m+n
    print("toplam gider")
    kar=toplamGelir-toplamGider
    if kar>1000:
        print("işletme kar etmiştir.")
    elif kar==0:
        print("işletme başabaş noktasında.")
    else:
        print("işletme zarar etmiştir.")
    return kar




#2.SORU
def oee():
    x=int(input("planlanmış üretim süresini giriniz:"))
    y=int(input("plansız duruş giriniz:"))
    kullanılabilirlikOranı=(x-y)/x
    print("kullanılanilirlik oranı")
    z=int(input("standart çevrim zamanı giriniz:"))
    t=int(input("üretim miktarı giriniz:"))
    performans=(z*t)/(x-y)
    print("performans")
    k=int(input("sağlam ürün miktarı:"))
    l=int(input("toplam ürün miktarı:"))
    kalite=k/l
    print("kalite")
    oee=(kullanılabilirlikOranı*kalite*performans)/100
    return oee




#3.SORU
def adambasiCiro():
    calisan=25
    x=int(input("satış miktarı giriniz:"))
    y=int(input("birim satış fiyatı giriniz:"))
    ciro=x*y
    print("ciro")
    adambasiCiro=ciro/calisan
    return adambasiCiro

    


