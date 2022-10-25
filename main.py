'''
    * Aplikasi Gempa Terkini
    * MODULARISASI DENGAN FUNCTION
'''


def ekstrasi_data():
    '''
    Tanggal: 25 Oktober 2022
    Waktu: 08:11:23 WIB
    Magnitudo: 4.4
    Kedalaman: 10 km
    Lokasi: 9.02 LS - 117.00 BT
    Pusat Gempa: Pusat gempa berada di darat 33 km Tenggara Sumbawa Barat
    Diraasakan: Dirasakan (Skala MMI): III Sumbawa Barat
    :return:
    '''
    result = dict()
    result['tanggal'] = '25 Oktober 2022'
    result['waktu'] = '08:11:23 WIB'
    result['magnitudo'] = 4.4
    result['lokasi'] = {'ls': 1.48, 'bt': 131.01}
    result['pusat'] = 'Pusat gempa berada di darat 33 km Tenggara Sumbawa Barat'
    result['dirasakan'] = 'Dirasakan (Skala MMI): III Sumbawa Barat'

    return result


def tampilkan_data(result):
    print('Gempa berdasarkan BMKG')
    print(f"Tanggal {result['tanggal']}")
    print(f"Waktu {result['waktu']}")
    print(f"Magnitudo {result['magnitudo']}")
    print(f"Lokasi:  LS:{result['lokasi']['ls']}, BT:{result['lokasi']['bt']}")
    print(f"Pusat {result['pusat']}")
    print(f"Dirasakan {result['dirasakan']}")


if __name__ == '__main__':
    print("Tampilkan data")
    result = ekstrasi_data()
    tampilkan_data(result)
