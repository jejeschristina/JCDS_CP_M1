# Capstone Project Module 1
# Yellow Pages (Daftar Kontak Telepon)

# import regex untuk mengecek input
import re

# Daftar Kontak awal
daftarKontak = [
    {'Nama' : 'Yayasan Pusaka Abadi',
        'Sektor' : 'Pendidikan',
        'Alamat' : 'Jl. V No. 28 Penjaringan',
        'Telepon' : '0216601644'},
    {'Nama' : 'RS Duta Harapan Indah',
        'Sektor' : 'Kesehatan',
        'Alamat' : 'Jl. Teluk Gong Raya No 12',
        'Telepon' : '02166676188'},
    {'Nama' : 'GOR Tanjung Duren',
        'Sektor' : 'Olahraga',
        'Alamat' : 'Jl. Tj. Duren Barat IV No 10',
        'Telepon' : '08157776855'},
    {'Nama' : 'RS Hasan Sadikin Bandung',
        'Sektor' : 'Kesehatan',
        'Alamat' : 'Jl. Pasteur No. 38',
        'Telepon' : '0222034953'},
    {'Nama' : 'Bank BCA KCP Kemang',
        'Sektor' : 'Keuangan',
        'Alamat' : 'Jl. Kemang Selatan V No 60',
        'Telepon' : '1500888'},
    {'Nama' : 'Bank OCBC NISP Bandung',
        'Sektor' : 'Keuangan',
        'Alamat' : 'Jl. Dr. Setiabudi No 148',
        'Telepon' : '0222033480'},
    ]

# Mengambil key pada dictionary dalam daftar kontak
key_daftarKontak = list(daftarKontak[0].keys())

# # FUNGSI TEMPLATE TABEL
# Template tabel untuk menampilkan semua daftar kontak dengan nomor baris
def default_contact():
    print('-' * 100)
    print(' ' * 45 + 'DAFTAR KONTAK')
    print('-' * 100)
    print(' NO.BARIS | {}{}\t| {} \t| {}{}\t| {}'.format(key_daftarKontak[0].upper(), (26-len(str(key_daftarKontak[0])))*' ', key_daftarKontak[1].upper(), key_daftarKontak[2].upper(), (29-len(str(key_daftarKontak[2])))*' ', key_daftarKontak[3].upper()))
    for i in range(len(daftarKontak)):
        print('{}.{}|{}{}\t|{} \t|{}{}\t|{}'.format(i+1,(9-len(str(i)))*' ', daftarKontak[i][key_daftarKontak[0]], (27-len(str(daftarKontak[i][key_daftarKontak[0]])))*' ',daftarKontak[i][key_daftarKontak[1]], daftarKontak[i][key_daftarKontak[2]], (30-len(str(daftarKontak[i][key_daftarKontak[2]])))*' ', daftarKontak[i][key_daftarKontak[3]]))

# Template tabel untuk menampilkan sebagian atau semua daftar kontak tanpa nomor baris
def showList(listData):
    print('-' * 95)
    print(' ' * 41 + 'DAFTAR KONTAK')
    print('-' * 95)
    print(' {}{}\t| {} \t| {}{}\t| {}'.format(key_daftarKontak[0].upper(), (26-len(str(key_daftarKontak[0])))*' ', key_daftarKontak[1].upper(), key_daftarKontak[2].upper(), (29-len(str(key_daftarKontak[2])))*' ', key_daftarKontak[3].upper()))
    for i in range(len(listData)):
        print('{}{}\t|{}\t|{}{}\t|{}'.format(listData[i][key_daftarKontak[0]], (27-len(str(listData[i][key_daftarKontak[0]])))*' ', listData[i][key_daftarKontak[1]], listData[i][key_daftarKontak[2]], (30-len(str(listData[i][key_daftarKontak[2]])))*' ', listData[i][key_daftarKontak[3]]))
 
# Template tabel untuk menampilkan data sebelum dilakukan update
def showListUpdate(listData, x, NewData):
    print('-' * 95)
    print(' ' * 41 + 'DAFTAR KONTAK')
    print('-' * 95)
    print(' {}{}\t| {} \t| {}{}\t| {}'.format(key_daftarKontak[0].upper(), (26-len(str(key_daftarKontak[0])))*' ', key_daftarKontak[1].upper(), key_daftarKontak[2].upper(), (29-len(str(key_daftarKontak[2])))*' ', key_daftarKontak[3].upper()))
    if x == 1:
        for i in range(len(listData)):
            print('{}{}\t|{}\t|{}{}\t|{}'.format(NewData, (27-len(str(NewData)))*' ', listData[i][key_daftarKontak[1]], listData[i][key_daftarKontak[2]], (30-len(str(listData[i][key_daftarKontak[2]])))*' ', listData[i][key_daftarKontak[3]]))
    if x == 2:
        for i in range(len(listData)):
            print('{}{}\t|{}\t|{}{}\t|{}'.format(listData[i][key_daftarKontak[0]], (27-len(str(listData[i][key_daftarKontak[0]])))*' ', NewData, listData[i][key_daftarKontak[2]], (30-len(str(listData[i][key_daftarKontak[2]])))*' ', listData[i][key_daftarKontak[3]]))
    if x == 3:
        for i in range(len(listData)):
            print('{}{}\t|{}\t|{}{}\t|{}'.format(listData[i][key_daftarKontak[0]], (27-len(str(listData[i][key_daftarKontak[0]])))*' ', listData[i][key_daftarKontak[1]], NewData, (30-len(str(NewData)))*' ', listData[i][key_daftarKontak[3]]))
    if x == 4:
        for i in range(len(listData)):
            print('{}{}\t|{}\t|{}{}\t|{}'.format(listData[i][key_daftarKontak[0]], (27-len(str(listData[i][key_daftarKontak[0]])))*' ', listData[i][key_daftarKontak[1]], listData[i][key_daftarKontak[2]], (30-len(str(listData[i][key_daftarKontak[2]])))*' ', NewData))


# # FUNGSI UNTUK FILTER DAFTAR KONTAK
# Filter kontak berdasarkan sektor
def searchList_bySector(inputSektor):
    searchListBySector = (list(filter(lambda data: data['Sektor'] == inputSektor , daftarKontak)))
    return searchListBySector

# Filter kontak berdasarkan nama kontak
def searchList_byName(inputNama):
    search_byName = []
    index_search_byName = []
    for i in range(len(daftarKontak)):
        if inputNama.lower() in daftarKontak[i]['Nama'].lower():
            search_byName.append(daftarKontak[i])
            index_search_byName.append(i)
        else:
            continue
    return search_byName, index_search_byName


# #FUNGSI TAMBAHAN
# Mengubah list daftar kontak menjadi dictionary dengan key = nama kontak tanpa spasi dan lowercase
def daftar_kontak_dict():
    key = []
    daftarKontakDict = {}
    for i in range(len(daftarKontak)):
        key.append(daftarKontak[i]['Nama'].replace(' ','').lower())
        daftarKontakDict[key[i]] = daftarKontak[i]
    return(daftarKontakDict)

# Fungsi tambahan yang dipanggil apabila daftar kontak kosong (tidak ada data)
def no_data():
    noData = input('''
    TIDAK ADA DATA

    1. Tambahkan Kontak Baru
    2. Keluar Dari Program (Exit)
    Silahkan masukkan angka perintah yang ingin dijalankan : ''')
    if noData == '1':
        add_contact()
    else:
        quit()


# # FUNGSI UTAMA
# FUNGSI UTAMA UNTUK MENAMPILKAN DAFTAR KONTAK
def view_contact():
    if len(daftarKontak) == 0:
        no_data()
    else:
        viewMenu = input('''
        ========== View Contact Menu ==========

        1. Tampilkan Kontak Berdasarkan Sektor
        2. Tampilkan Semua Kontak
        3. Cari Kontak Berdasarkan Nama
        4. Kembali ke Menu utama
        Silahkan masukkan angka menu yang ingin dijalankan : ''')
        
        if viewMenu == '1':
            sector = list(set(daftarKontak[i]['Sektor'] for i in range(len(daftarKontak))))
            print('\n======= Daftar Sektor =======')
            for i in range(len(sector)):
                print(f'{i+1}. {sector[i]}')
            print(f'{len(sector)+1}. Kembali ke Menu Sebelumnya')
            while True:
                viewSectorMenu = input('Masukkan angka sektor yang ingin ditampilkan : ')
                if not re.match('^[\d]*$', viewSectorMenu):
                    print('\nInput salah! Input hanya boleh berupa angka.')
                elif int(viewSectorMenu) not in range(1, len(sector)+2):
                    print('\nTidak ada data!')
                else:
                    break
            viewSectorMenu = int(viewSectorMenu)
            if viewSectorMenu == len(sector)+1:
                view_contact()
            else:
                showList(searchList_bySector(sector[viewSectorMenu - 1]))
                view_contact()

        elif viewMenu == '2':
            default_contact()
            view_contact()
        elif viewMenu == '3':
            FindContactName = input('Masukkan nama kontak yang ingin di cari : ')
            if searchList_byName(FindContactName)[0] == []:
                print('\nData tidak ditemukan!')
                view_contact()
            else:
                showList(searchList_byName(FindContactName)[0])
                view_contact()
        elif viewMenu == '4':
            menu()
        else:
            print('\nMenu tidak ditemukan')
            view_contact()


# Subfungsi tambah kontak
def contact_exist():
    contactExist = input('''
    1. Tambah Kontak Lain
    2. Kembali ke Menu Utama
    Silahkan masukkan angka perintah yang ingin dijalankan : ''')
    if contactExist == '1':
        add_contact()
    else:
        menu()

# FUNGSI UTAMA TAMBAH KONTAK
def add_contact():
    default_contact()
    while True:
        inputNama = input('Masukkan Nama Kontak Baru: ')
        if inputNama.replace(' ','').lower() in list(daftar_kontak_dict().keys()):
            print('\nNama kontak sudah ada!')
        else:
            break
    inputSektor = input('Masukkan Sektor : ').capitalize()
    inputAlamat = input('Masukkan Alamat : ')
    while True:
        inputTelepon = input('Masukkan No Telepon (hanya boleh angka) : ')
        if not re.match('^[\d]*$', inputTelepon):
            print('\nInput salah! Input nomor telepon hanya boleh berupa angka.')
        else:
            break
    daftarKontakBaru = [{
        'Nama' : inputNama,
        'Sektor' : inputSektor,
        'Alamat' : inputAlamat,
        'Telepon' : inputTelepon
        }]
    showList(daftarKontakBaru)
    save = input('Simpan Data? [Y/N] : ').lower()
    if save != 'y':
        print('\nBatal menambahkan kontak!')
        contact_exist()
    else:
        daftarKontak.extend(daftarKontakBaru)
        default_contact()
        print('\nData kontak berhasil tersimpan!')
        contact_exist()


# Subfungsi Update Kontak
def contact_for_update():
    contactForUpdate = input('''
    1. Ubah Kontak Lain
    2. Kembali ke Menu Utama
    Silahkan masukkan angka perintah yang ingin dijalankan : ''')
    if contactForUpdate == '1':
        update_contact()
    else:
        menu()

# Subfungsi Update Kontak sesuai Kategori
def update_contact_category(indeks, Kategori, NewData):
    inputUpdateKategori = input('Apakah data yang diupdate sudah benar? [Y/N] : ').lower()
    if inputUpdateKategori == 'y':
        if Kategori == 'Sektor':
            daftarKontak[indeks][Kategori] = NewData.capitalize()
        else:
            daftarKontak[indeks][Kategori] = NewData
        print('\nData sudah diperbarui!')
    else:
        print('\nData tidak terupdate!')

# FUNGSI UTAMA UPDATE KONTAK
def update_contact():
    if len(daftarKontak) == 0:
        no_data()
    else:
        default_contact()
        updateContactMenu = input('''
        1. Update Kontak Berdasarkan No. Baris
        2. Update Kontak Berdasarkan Nama
        3. Kembali ke Menu Utama
        Silahkan masukkan angka perintah yang ingin dijalankan : ''')
        if updateContactMenu == '1':
            while True:
                updateContactByNum = input('Masukkan no. baris yang ingin di update: ')
                if not re.match('^[\d]*$', updateContactByNum):
                    print('\nInput salah! Input hanya boleh berupa angka.\n')
                else:
                    break
            updateContactByNum = int(updateContactByNum)
            if updateContactByNum not in range(1,len(daftarKontak)+1):
                print('\nData tidak tersedia!')
                contact_for_update()
            else:
                print('\nDAFTAR KONTAK YANG AKAN DIUPDATE : ')
                contactUpdate = [daftarKontak[updateContactByNum-1]]
                showList(contactUpdate)
                while True:    
                    updateMenu = input('''
                ======= UPDATE INFORMASI KONTAK =======
                Kategori:
                1. Nama
                2. Sektor
                3. Alamat
                4. Telepon
                Masukkan angka kategori yang ingin diubah : ''')
                    if not re.match('^[\d]*$', updateMenu):
                        print('\nInput salah! Input hanya boleh berupa angka.')
                    elif int(updateMenu) not in range(1, len(key_daftarKontak)+1):
                        print('\nMenu tidak ditemukan!')
                    else:
                        break
                updateMenu = int(updateMenu)
                updateData = input('Masukkan data baru : ')
                if updateMenu == 1:
                    while updateData.replace(' ','').lower() in daftar_kontak_dict().keys():
                        print('\nNama kontak sudah ada!')
                        updateData = input('Masukkan data baru : ')
                elif updateMenu == 4:
                    while not re.match('^[\d]*$', updateData):
                        print('\nInput salah! Input nomor telepon hanya boleh berupa angka.')
                        updateData = input('Masukkan data baru : ')
                showListUpdate(contactUpdate, updateMenu, updateData)
                update_contact_category(updateContactByNum - 1, key_daftarKontak[updateMenu - 1], updateData)
                contact_for_update()
            
        elif updateContactMenu == '2':
            updateContactByName = input('Masukkan nama kontak yang ingin di update : ')
            updContact = searchList_byName(updateContactByName)
            if updContact[0] == []:
                print('\nKontak yang ingin diubah tidak tersedia!')
                contact_for_update()
            else:
                print('\nSEMUA DAFTAR KONTAK YANG INGIN DIUPDATE :')
                showList(updContact[0])
                inputUpdate = input('Update data berikut? [Y/N] : ').lower()
                if inputUpdate != 'y':
                    print('\nKontak gagal diupdate')
                    contact_for_update()
                else:
                    for i in range(len(updContact[1])):
                        print('\nDAFTAR KONTAK YANG AKAN DIUPDATE : ')
                        contactUpdate = [updContact[0][i]]
                        showList(contactUpdate)
                        while True:    
                            updateMenu = input('''
                ======= UPDATE INFORMASI KONTAK =======
                Kategori:
                1. Nama
                2. Sektor
                3. Alamat
                4. Telepon
                Masukkan angka kategori yang ingin diubah : ''')
                            if not re.match('^[\d]*$', updateMenu):
                                print('\nInput salah! Input hanya boleh berupa angka.')
                            elif int(updateMenu) not in range(1, len(key_daftarKontak)+1):
                                print('\nMenu tidak ditemukan!')
                            else:
                                break
                        updateMenu = int(updateMenu)
                        updateData = input('Masukkan data baru : ')
                        if updateMenu == 1:
                            while updateData.replace(' ','').lower() in daftar_kontak_dict().keys():
                                print('\nNama kontak sudah ada!')
                                updateData = input('Masukkan data baru : ')
                        showListUpdate(contactUpdate, updateMenu, updateData)
                        update_contact_category(updContact[1][i], key_daftarKontak[updateMenu - 1], updateData)
                    contact_for_update()
        else:
            menu()


# Subfungsi Hapus Kontak
def contact_not_exist():
    contactNotExist = input('''
    1. Hapus Kontak Lain
    2. Kembali ke Menu Utama
    Silahkan masukkan angka perintah yang ingin dijalankan : ''')
    if contactNotExist == '1':
        delete_contact()
    else:
        menu()

# FUNGSI UTAMA HAPUS KONTAK
def delete_contact():
    if len(daftarKontak) == 0:
        no_data()
    else:
        default_contact()
        deleteContactMenu = input('''
        1. Hapus Kontak Berdasarkan No. Baris
        2. Hapus Kontak Berdasarkan Nama
        3. Kembali ke Menu Utama
        Silahkan masukkan angka perintah yang ingin dijalankan : ''')
        if deleteContactMenu == '1':
            while True:
                deleteContactByNum = input('Masukkan no. baris yang ingin di hapus : ')
                if not re.match('^[\d]*$', deleteContactByNum):
                    print('\nInput salah! Input hanya boleh berupa angka.')
                else:
                    break
            deleteContactByNum = int(deleteContactByNum)
            if deleteContactByNum not in range(1,len(daftarKontak)+1):
                print('\nData tidak tersedia!')
                contact_not_exist()
            else:
                showList([daftarKontak[deleteContactByNum-1]])
                cek = input('Apakah anda yakin ingin menghapus kontak? [Y/N] : ').lower()
                if cek != 'y':
                    print('\nKontak gagal terhapus!')
                    contact_not_exist()
                else:
                    del daftarKontak[deleteContactByNum-1]
                    print('\nKontak berhasil terhapus!')
                    contact_not_exist()

        elif deleteContactMenu == '2':
            deleteContactByName = input('Masukkan nama kontak yang ingin di hapus : ')
            delContact = searchList_byName(deleteContactByName)
            if delContact[0] == []:
                print('\nKontak tidak ditemukan!')
                contact_not_exist()
            else:
                showList(delContact[0])
                cek = input('Apakah anda yakin ingin menghapus kontak? [Y/N] : ').lower()
                if cek != 'y':
                    print('\nKontak gagal terhapus!')
                    contact_not_exist()
                else:
                    for i in reversed(range(len(delContact[1]))):
                        del daftarKontak[delContact[1][i]]
                    print('\nKontak berhasil terhapus!')
                    contact_not_exist()

        else:
            menu()


# Fungsi Menu Utama
def menu():
    while True:
        mainMenu = input('''
        SELAMAT DATANG DI MENU UTAMA DAFTAR KONTAK TELEPON!

        1. Tampilkan Daftar Kontak (View Contact)
        2. Tambah Kontak Baru (Add Contact)
        3. Perbarui Kontak (Update Contact)
        4. Hapus Kontak (Delete Contact)
        0. Keluar dari Program (Exit)
        
        Silahkan masukkan angka menu yang ingin dijalankan : ''')

        if mainMenu == '1':
            view_contact()
        elif mainMenu == '2':
            add_contact()
        elif mainMenu == '3':
            update_contact()
        elif mainMenu == '4':
            delete_contact()
        elif mainMenu == '0':
            quit()
        else:
            print("Menu tidak ditemukan")

menu()