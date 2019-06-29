my_answer=[]
yanlis=0
bos=0
dogru=0
key=[]
import time as t
from datetime import datetime as d
while 1:
    start=t.time()
    soru_sayisi=int(input("Test kaç soru?:"))
    for n in range(1,soru_sayisi+1,1):
        cktp=str(n)+". sorunun doğru cevabı:"
        temporary=input(cktp)
        key.append(temporary)
    for x in range(0,100):
        print("\n")
    for n in range(1,len(key)+1,1):
        tmp=str(n)+". soruya verilen cevap = "
        temp=input(tmp)
        my_answer.append(temp)
    for temp_ in range(1,len(key)+1,1):
        if my_answer[temp_-1]==key[temp_-1]:
            print(str(temp_)+". soru doğru")
            dogru+=1
        elif my_answer[temp_-1]=="":
            print(str(temp_)+". soru boş")
            bos+=1
        else:
            yanlis+=1
            print(str(temp_)+". soru hatalı. Doğru cevap",key[temp_-1],"iken sen ",my_answer[temp_-1],"yaptın")
    acc=dogru/soru_sayisi
    out="TEST SONUÇLARI:\nAcc="+str(acc)+"\n"+str(dogru)+" doğru\n"+str(yanlis)+" yanlış\n"+str(bos)+" boş\n\n"        
    print(out)
    xc=input("Uygulamdan çıkmak için \"K\"ya, yeni test içinse başka bir tuşa basınız.")
    if xc.upper()=="K":
        break
    else:
        pass
