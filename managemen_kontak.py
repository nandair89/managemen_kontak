"Program managemen kontak"

def melihat_kontak():
    # melihat semua kontak
    if kontak:
        for num, item in enumerate(kontak, start=1):
            print(f'\n{num}. {item["nama"]} ({item["HP"]}, {item["Email"]})')
    else:
        print("Kontak masih kosong!")
        return 1

def menambah_kontak():
    # menambah kontak
    nama = input("Masukan nama kontak baru: ")
    HP = input("Masukan nomor HP baru: ")
    Email = input("Masukan email baru: ")
    kontak_baru = {'nama': nama, 'HP': HP, 'Email': Email}
    kontak.append(kontak_baru)
    print("Kontak baru berhasil ditambahkan")

def menghapus_kontak():
    # menghapus kontak
    if melihat_kontak() == 1:
        return
    else:
        i_hapus = int(input("Masukan nomor kontak yang akan dihapus: "))
        del kontak[i_hapus - 1]
        print("Kontak yang dimasksud sudah dihapus!")

kontak1 = {'nama': "Ain", 'HP': '02939847', 'Email': 'ain@python.com'}
kontak2 = {'nama': "Aine", 'HP': '03439847', 'Email': 'aine@python.com'}
kontak = [kontak1,kontak2]

while True:
    print("\nMenu Kontak")
    print("1. Melihat Semua Kontak")
    print("2. Menambahkan Kontak Baru")
    print("3. Menghapus Kontak")
    print("4. Keluar dari Menu Kontak")

    pilihan = input("Masukan pilihan menu kontak(1,2,3, atau 4) : ")

    if pilihan == '1':
        melihat_kontak()

    elif pilihan == '2':
        menambah_kontak()

    elif pilihan == '3':
        menghapus_kontak()

    elif pilihan == '4':
        #keluar dari menu kontak
        print("Keluar dari Menu Kontak!")
        break
    else:
        print("Anda memasukan pilhan yang salah!")