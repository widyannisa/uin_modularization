nama = 'Widyaningrum'
program = 'Gerak Lurus'

print(f'Program {program} oleh {nama}')

def hitung_kecepatan(jarak, waktu):
    kecepatan = jarak / waktu
    print(f'Jarak = {jarak / 1000}km ditempuh dalam waktu = {waktu / 60}menit')
    print(f'Sehingga kecepatan = {kecepatan} m/s')
    return kecepatan

# jarak = 10000
# waktu = 5 * 60
kecepatan = hitung_kecepatan (1000, 5 * 60)
kecepatan = hitung_kecepatan (3000, 70 * 60)

def hitung_usaha(gaya, jarak ) :
    usaha = gaya * jarak
    print(f'gaya = {gaya / 10}Newton dengan perpindahan = {jarak / 1}meter')
    print(f'sehingga usaha = {usaha} joule')
    return usaha

#gaya
#jarak
usaha = hitung_usaha(15, 5 * 1)
usaha = hitung_usaha(30, 7 * 1)