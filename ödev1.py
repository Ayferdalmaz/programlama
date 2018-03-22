satisMiktari=500
birimSatisFiyati=20
ciro=5000
i=0
while(ciro<=500000):
    ciro=(ciro)+satisMiktari*birimSatisFiyati
    satisMiktari=satisMiktari+200
    birimSatisFiyati=birimSatisFiyati+10
    i=i+1
print('500.000 den fazla kar',i,'.ayda tamamlanmıştır')






stokMiktari=10000
alinanUrun=100
satilanUrun=500
fark=alinanUrun-satilanUrun
i=0
while(stokMiktari>0):
    stokMiktari=stokMiktari+fark
    i=i+1
print(i)





toplam=0
while True:
    print("bir sayi giriniz, cıkış icin 0(sıfır)")
    girilen=int(input("sayı:"))
    if(girilen!=0):
        a=girilen%3
        toplam=toplam+a
        print('Toplam',toplam)
    else:
        print('cıkış yapıldı')
        break



calisan=50
yevmiye=90
aylikMesai=0
haftalikMaas=630
aylikMaas=0
while(aylikMesai<=22):
    haftalikMesai=int(input("haftalık mesai:"))
    aylikMesai=haftalikMesai*4
    haftalikMaas=haftalikMaas+(haftalikMesai*yevmiye*0.10)
    aylikMaas=aylikMaas+haftalikMaas*4
    print('aylik maas:',aylikMaas)
else:
    print("aylık mesai 22 saatten fazla olamaz.")




gunlukUretilen=200
gunlukDefoluUrun=0
toplamDefoluUrun=0
i=0
while(gunlukDefoluUrun<=gunlukUretilen*0.20):
    gunlukDefoluUrun=int(input('günlük defolu ürün miktarı:'))
    toplamDefoluUrun=toplamDefoluUrun+gunlukDefoluUrun
    i=i+1
    if(gunlukDefoluUrun>gunlukUretilen*0.20):
        print("defolu ürün sayısı limiti aştı")
        break
    print(i,"günlük","defolu ürün sayısı:",toplamDefoluUrun)











