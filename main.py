import modul as mod

while True:
    mod.tampilan() 
    pilihan = input('\nMasukkan pilihan : ')

    if pilihan == '1':
        mod.tambah_data()
    elif pilihan == '2':
        mod.edit_data()
    elif pilihan == '3':
        mod.hapus_data()
    elif pilihan == '4':
        mod.cari_data()
    elif pilihan == '5':
        mod.tampil_data()
    elif pilihan == '6':
        mod.tampil_jumlah_data()
    elif pilihan == '7':
        print('Terima kasih.')
        break
    else:
        print('Pilihan tidak valid. Silakan pilih opsi yang benar.')