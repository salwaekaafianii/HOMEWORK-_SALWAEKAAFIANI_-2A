barang = []

def tampilan():
    print('\nSelamat Datang di Program Manajemen Stok Barang!')
    print('Pilihan :')
    print('1. Tambah data barang')
    print('2. Edit data')
    print('3. Hapus data barang')
    print('4. Cari data')
    print('5. Tampilkan data barang')
    print('6. Tampilkan jumlah data')
    print('7. Keluar')

  

def tambah_data():
    nama = str(input('Masukkan nama barang :'))
    stok = int(input('Masukkan stok barang : '))
    barang_new = {'nama' : nama, 'stok' : stok}
    barang.append(barang_new)
    print('---------- Data berhasil ditambahkan ----------')

def edit_data():
    index = int(input('Edit data index ke = '))
    if index < len(barang):
        nama_barang = str(input('Masukan nama : '))
        stok_baru = int(input('Masukan stok : '))
        barang[index]['nama'] = nama_barang
        barang[index]['stok'] = stok_baru
        print('---------- Data berhasil diubah ----------')
    else:
        print('---------- Index tidak valid ----------')

def hapus_data():
    hapus = int(input('Hapus data index ke : '))
    barang.pop(hapus) 
    print('----------- Data berhasil dihapus ------------')

def cari_data():
    nama_barang = input('Cari nama barang : ')
    print('========== Hasil Pencarian ==========')
    for i in barang:
        if i['nama'] == nama_barang:
            print(' ➤ ', i['nama'], ', Stok : ', i['stok'])
            return
    print('----------- Data tidak ditemukan ------------')

def tampil_data():
    print('========== Toko Elektronik ==========')
    for i in barang:
        print(' ➤ ',i['nama'],', Stok : ',i['stok'])
    if not barang:
        print('----------- Data barang kosong ------------')
        
def tampil_jumlah_data():
    print('Jumlah data barang : ', len(barang), 'barang')