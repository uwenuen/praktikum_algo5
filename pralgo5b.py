# -*- coding: utf-8 -*-
"""
Created on Thu Oct 19 19:57:04 2023

@author: Gwen Alaina Marela
"""
print("SELAMAT DATANG DI ZOO ZOO")

pembayaran = 0
pengunjung = 0

while True:
    umur = input('tolong masukkan umur anda: ')
    pengunjung += 1
    if(umur == ''):
        break;
    try:
        umur = int(umur) 
         
        if umur <= 2:
            bayar = 0
        elif 3 <= umur <= 12:
            bayar = 10  
        elif 13 <= umur <= 64:
            bayar = 23  
        else:
            bayar = 15 
        pembayaran += bayar
        pengunjung += 1
        
        print(f"Umur: {umur} tahun, total harga: ${bayar:.2f}")
        
    except ValueError:
        print("Masukkan tidak valid.")
    
print(f"Jumlah Pengunjung: {pengunjung}")
print(f"Total Pembayaran: ${pembayaran:.2f}")
        