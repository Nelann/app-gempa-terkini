import requests
from bs4 import BeautifulSoup


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
    try:
        content = requests.get("https://www.bmkg.go.id/")
    except Exception:
        return None

    if content.status_code == 200:
        soup = BeautifulSoup(content.text, 'html.parser')

        times = soup.find('span', {'class': 'waktu'})
        times = times.text.split(', ')
        waktu = times[1]
        tanggal = times[0]

        data_content = soup.find('div', {'class': 'col-md-6 col-xs-6 gempabumi-detail no-padding'})
        data_content = data_content.findChildren('li')

        i = 0
        magnitudo = None
        kedalaman = None
        koordinat = None
        lokasi = None
        dirasakan = None

        for res in data_content:
            if i == 1:
                magnitudo = res.text
            elif i == 2:
                kedalaman = res.text
            elif i == 3:
                koordinat = res.text.split(' - ')
                ls = koordinat[0]
                bt = koordinat[1]
            elif i == 4:
                lokasi = res.text
            elif i == 5:
                dirasakan = res.text
            i += 1


        result = {
            'tanggal': tanggal,
            'waktu': waktu,
            'magnitudo': magnitudo,
            'kedalaman': kedalaman,
            'koordinat': {
                'ls': ls,
                'bt': bt,
            },
            'lokasi': lokasi,
            'dirasakan': dirasakan
        }

        return result

    else:
        return None


def tampilkan_data(result):
    if result is None:
        print("Tidak bisa menemukan data terkini")
        return

    print('Gempa berdasarkan BMKG')
    print(f"Tanggal {result['tanggal']}")
    print(f"Waktu {result['waktu']}")
    print(f"Magnitudo {result['magnitudo']}")
    print(f"Kedalaman {result['kedalaman']}")
    print(f"Koordinat LS:{result['koordinat']['ls']} BT:{result['koordinat']['bt']} ")
    print(f"Lokasi:  {result['lokasi']}")
    print(f"Dirasakan {result['dirasakan']}")
