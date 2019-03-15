# -*- coding: utf-8 -*-
"""
Created on Fri Apr 20 08:58:30 2018
@author: MFF
"""
tut=""
hexx=["0","1","2","3","4","5","6","7","8","9","A","B","C","D","E","F","a","b","c","d","e","f"]
while True:
    kontrol=True
    giris = input("Renk Kodu: "+ tut) 
    n=len(tut+giris)    
    if n <= 6:
        for i in range(len(giris)): 
            if giris[i] in hexx:
                kontrol=True
                tut+=giris[i]
            else:
                kontrol=False
                break
        if n == 6:
            if kontrol==True:
                break
    else:
        print("6 haneli giriniz.") 
print("\nRenk Kodunuz:",tut)
bekle=input("")
