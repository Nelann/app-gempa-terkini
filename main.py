'''
    * Aplikasi Gempa Terkini
    * MODULARISASI DENGAN FUNCTION
'''
import gempaterkini

if __name__ == '__main__':
    print("Aplikasi Gempa Terkini")
    result = gempaterkini.ekstrasi_data()
    gempaterkini.tampilkan_data(result)
