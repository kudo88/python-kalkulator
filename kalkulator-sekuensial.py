import os
import platform

bersih = 'cls' if platform.system() == 'Windows' else 'clear'

cmd = ('+','-','*','/','=','M+','M-','MR','MC',None,'','RESET')
memori = 0
hasil = 0.0
isi,tampil = '',''
opr = None
selesai = False

def reset():
    memori = 0
    hasil = 0.0
    isi,tampil = '',''
    opr = None
    selesai = False

def isfloat(value):
  try:
    float(value)
    return True
  except ValueError:
    return False

def hitung(par_isi):
    global opr, tampil, hasil, memori
    if opr == '+':
        hasil += par_isi
        tampil += ' + '+str(par_isi)
    elif opr == '-':
        hasil -= par_isi
        tampil += ' - '+str(par_isi)
    elif opr == '*':
        hasil *= par_isi
        tampil += ' * '+str(par_isi)
    elif opr == '/':
        hasil /= par_isi
        tampil += ' / '+str(par_isi) 
    elif opr == 'M+':
        memori += par_isi
    elif opr == 'M-':
        memori -= par_isi

def parse(par_isi):
    global opr, tampil, hasil
    if isfloat(par_isi):
        if opr == None:
            hasil = float(par_isi)
            tampil += f' {par_isi}'
        else:
            hitung(float(par_isi))
    else:
        opr = par_isi
            

while not selesai:
    print('Kalkulator sederhana')
    isi = isi.upper()
    if isi == 'MR':
        print(f'Isi memori > {memori}')
    elif isi == 'MC':
        memori = 0
        print(f'Isi memori sudah dibersihkan')
    if (not isfloat(isi)) and (not isi in cmd):
        print('Masukkan angka / perintah dengan benar.')
    if isi == 'RESET':
        reset
        print('Berhasil reset')
    isi = input('input angka / perintah > ')
    parse(isi)
    if isi == '=':
        print(f'Hasil Kalkulasi > {tampil} = {hasil}')
        selesai = True
    else:
        os.system(bersih)
