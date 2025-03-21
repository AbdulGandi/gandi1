


daftar_belanja = []

def tambah_item (item):
    daftar_belanja.append(item)
    print(f'"{item}" telah di tambahkan ke daftar belanja.')
def tampilkan_daftar():
    if daftar_belanja:
        print("\nDaptar Belanja:")
        for i, item in enumerate(daftar_belanja, 1):
            print(f"{i}. {item}")
    else:
        print("\nDaftar belanja kosong.")
def hapus_item(index):
    if 0 <= index < len(daftar_belanja):
        item = daftar_belanja.pop(index)
        print(f'"{item}"telah di hapus daftar belanja.')
    else:
        print("index tidak valid")
while True:
    print("\nMenu:")
    print("1. Tambah Item")
    print("2. Lihat Daftar Belanja")
    print("3. hapus item")
    print("4. Keluar")

    pilihan = input("pilihan menu (1-4): ")

    if pilihan == "1":
        item = input("masukan nama item: ")
        tambah_item(item)
    elif pilihan == "2":
        tampilkan_daftar()
    elif pilihan == "3":
        tampilkan_daftar()
        index = int(input("masukan nomor item yang ingin dihapus: ")) - 1
        hapus_item(index)
    elif pilihan == "4":
        print("terima kasih| program selesai.")
        break
    else:
        print("pilihan tidak valid, silakan coba lagi.")
