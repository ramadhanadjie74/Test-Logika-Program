# [5, 7, 7, 9, 10, 4, 5, 10, 6, 5] ◄◄ 3
# [10 20 20 10 10 30 50 10 20] ◄◄ 3
# [6 5 2 3 5 2 2 1 1 5 1 3 3 3 5] ◄◄ 6
# [1 1 3 1 2 1 3 3 3 3] ◄◄ 4

# Kemarin Shopia per[gi ke mall. ◄◄ 4
# Saat meng*ecat tembok, Agung dib_antu oleh Raihan. ◄◄ 5
# Berapa u(mur minimal[ untuk !mengurus ktp? ◄◄ 3
# Masing-masing anak mendap(atkan uang jajan ya=ng be&rbeda. ◄◄ 4

import math

if __name__ == "__main__":
	# ════════════════════════════════════════════════════════════════════════════════
	# Soal 1
	# ────────────────────────────────────────────────────────────────────────────────

	susunan_angka = input('Input susunan angka: ')
	# input dari user, dihilangkan [] di posisi kiri dan kanan, lalu di 'split' di bagian spasi
	arr_susunan_angka = susunan_angka.strip('[]').split()
	arr_angka = []
	for x in arr_susunan_angka:
		# hilangkan koma (,) pada angka dan tambahkan angka ke dalam array angka
		arr_angka.append(x.strip(',').strip())

	dict_angka = {}
	# cek jumlah masing-masing angka, dan masukkan angka pada grup masing-masing
	for angka in arr_angka:
		if angka in dict_angka:
			dict_angka[angka] += 1
		else:
			dict_angka[angka] = 1

	total_pasang = 0
	# loop masing-masing angka, dan hitung jumlah angka yang bisa dibagi 2, dan bulatkan ke bawah untuk mendapatkan jumlah pasang
	for key, value in dict_angka.items():
		jumlah_pasang = math.floor(value / 2)
		total_pasang += jumlah_pasang

	print('Jumlah pasang ► {}'.format(total_pasang))

	# ════════════════════════════════════════════════════════════════════════════════
	# Soal 2
	# ────────────────────────────────────────────────────────────────────────────────

	kalimat = input('Input kalimat: ')
	stop_symbol = ',.?!'
	arr_kata = []
	for kata in kalimat.strip().split():
		# buang tanda - untuk memastikan kata berulang seperti 'masing-masing' agar dianggap sebagai kata yang hanya mempunyai susunan huruf saja
		kata = kata.replace('-', '')
		# hilangkan tanda ,.?! pada bagian kanan kata
		kata = kata.rstrip(stop_symbol)
		# cek apakah kata tersusun dari alphabet saja
		if kata.isalpha():
			arr_kata.append(kata)
	jumlah_kata = len(arr_kata)

	print('Jumlah kata ► {}'.format(jumlah_kata))
