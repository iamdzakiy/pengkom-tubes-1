#Information
"""
Kelompok 14 - ATM
1. 
2. 
3.
4. 
"""

#Kamus dan Variabel
"""
Data variabel
- Akuns = Bentuk jamak dari akun (kumpulan akun)

Admin variabel
- semua_akuns = 
- 

Nasabah variabel


"""

#Intensi ATM

#Management dan Aturan


import random
import pickle
import os.path
import sys

def semua_akuns():
    if os.path.isfile("Akuns.bat"):            
        read_file=open("Akuns.bat","rb")
        Akuns=pickle.load(read_file)
        read_file.close()
        return Akuns
    else:
        print("Data tidak tersedia")
        return {}

def tampil_akun(Act):
    print("_"*50)
    print("Nama Nasabah:",Act[0])
    print("Nomor Telepon:",Act[1])
    print("Alamat:",Act[2])
    print("Jenis Kelamin:",Act[3])
    print("PIN:",Act[4])
    print("Saldo:",Act[5])
    print("_"*50)

def write_Akuns(Akuns):
    write_file=open("Akuns.bat","wb")
    pickle.dump(Akuns,write_file)
    write_file.close()

def tambah_akun():
    Akuns=semua_akuns()
    nomor_akun=random.randint(10000000,100000000)
    name=input("Masukkan Nama Nasabah: ")
    nomor_telepon=input("Masukkan Nomor Telepon: ")
    alamat=input("Masukkan Alamat: ")
    jenis_kelamin=input("Masukkan Jenis Kelamin: ")
    PIN=random.randint(100000,1000000)
    saldo=0

    Akuns[nomor_akun]=[name,nomor_telepon,alamat,jenis_kelamin,PIN,saldo]

    write_Akuns(Akuns)
    print("Akun berhasil dibuat")
 

def hapus_akun():
    Akuns=semua_akuns()
    nomor_akun=input("Masukkan Nomor Akun:")
    if nomor_akun in Akuns.keys():
        del Akuns[nomor_akun]
        print("Akun sudah dihapus")
        write_Akuns(Akuns)
    else:
        print("Akun tidak tersedia")
        
def ubah_akun():
    Akuns=semua_akuns()
    nomor_akun=input("Masukkan Nomor Akun:")
    if nomor_akun in Akuns.keys():
        tampil_akun(Akuns[nomor_akun])
        print("Apa yang ingin Anda ubah:")
        print("0.Nama Nasabah")
        print("1.Nomor Telepon")
        print("2.Alamat")
        print("3.Jenis Kelamin")
        pilihan=int(input())
        if pilihan>=0 and pilihan<4:
            v=input("Masukkan New Value:")
            if v!="":
                Akuns[nomor_akun][pilihan]=v
                write_Akuns(Akuns)
                print("Akun berhasil diperbaharui")
            else:
                print("Try Again..")
        else:
            print("Salah Pilihan")
    else:
        print("Akun tidak tersedia")

def tampil_semua_akun():
    Akuns=semua_akuns()
    print("$"*50)
    print("Tabel Akun".center(50))
    print("$"*50)
    for akun in Akuns:
        print(akun,Akuns[akun])
        
def cari_akun():
    Akuns=semua_akuns()
    nomor_akun=input("Masukkan Nomor Akun:")
    if nomor_akun in Akuns.keys():
        tampil_akun(Akuns[nomor_akun])
    else:
        print("Akun tidak tersedia")

def admin_menu():
    print("$"*50)
    print("Dashboard Admin".center(50))
    print("$"*50)
    print("1.Tambah Akun")
    print("2.Hapus Akun")
    print("3.Ubah Akun")
    print("4.Tampilkan Semua Akun")
    print("5.Cari Akun")
    print("0.keluar")
    
    pilihan=int(input("Select:"))
    if pilihan==1:tambah_akun()
    elif pilihan==2:hapus_akun()
    elif pilihan==3:ubah_akun()
    elif pilihan==4:tampil_semua_akun()
    elif pilihan==5:cari_akun()
    elif pilihan==0:keluar()

    input("lanjut...")
    admin_menu()

def setor_tunai(no_rekening):
    Akuns=semua_akuns()
    amount=int(input("Masukkan Jumlah Setor Tunai: "))
    Akuns[no_rekening][5]=int(Akuns[no_rekening][5])+amount
    write_Akuns(Akuns)
    print("Uang berhasil disetor")
    

def tarik_tunai(no_rekening):
    Akuns=semua_akuns()
    amount=int(input("Masukkan Jumlah Tarik Tunai: "))
    if(Akuns[no_rekening][5]>amount):
        Akuns[no_rekening][5]=int(Akuns[no_rekening][5])-amount
        print("Tarik tunai berhasil.")
        write_Akuns(Akuns)
    else:
        print("Tidak bisa tarik tunai")

def cek_saldo(no_rekening):
    Akuns=semua_akuns()
    print("Saldo: Rp.",Akuns[no_rekening][5])

def menu_nasabah(no_rekening):
    print("$"*50)
    print("Dashboard Nasabah".center(50))
    print("$"*50)
    print("1.Setor Tunai")
    print("2.Tarik Tunai")
    print("3.Cek Saldo")
    print("0.keluar")
    pilihan=int(input("Select:"))
    if pilihan==1:setor_tunai(no_rekening)
    elif pilihan==2:tarik_tunai(no_rekening)
    elif pilihan==3:cek_saldo(no_rekening)
    elif pilihan==0:keluar()
    input("Lanjut...")
    menu_nasabah(no_rekening)
    
def keluar():
    main_menu()

def batal():
    sys.exit()

def main_menu():
    print("$"*50)
    print("Sistem Bank".center(50))
    print("$"*50)
    print("1.Login Admin\n2.Login Nasabah\n3.Batal")
    pilihan=int(input("Select: "))
    if pilihan==1:
        admin_id=input("Masukkan Admin Id:")
        PIN=input("Masukkan Admin PIN:")
        if admin_id=="Matin" and PIN=="1414141414":
            admin_menu()
        elif admin_id=="Dzakiy" and PIN=="1414141414":
            admin_menu()
        elif admin_id=="Revalina" and PIN=="1414141414":
            admin_menu()
        elif admin_id=="Lenny" and PIN=="1414141414":
            admin_menu()
        else:
            print("id/PIN tidak sesuai")
    elif pilihan==2:
        Akuns=semua_akuns()
        no_rekening=input("Masukkan Nomor Akun:")
        if no_rekening in Akuns.keys():
            PIN=int(input("Masukkan PIN:"))
            if Akuns[no_rekening][4]==PIN:
                menu_nasabah(no_rekening)
            else:
                print("PIN tidak sesuai")
        else:
            print("Akun tidak tersedia")
    elif pilihan==3:
        batal()
    else:
        print("Gagal. Tidak sesuai pilihan")
        main_menu()


main_menu()
