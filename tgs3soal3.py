jadwal_dasproif3 = {'senin': 'jam08:00', 'selasa': '10:50', 'rabu': '08:00'}
jadwal_dasproif2 = {'kamis': 'jam08:00', 'jumat': '10:50', 'sabtu': '15:00'}

# Menggabungkan data dari jadwaldasproif2 ke dalam jadwaldasproif3
jadwal_dasproif3.update(jadwal_dasproif2)

# Menampilkan output yang diharapkan
print("Jadwal gabungan =", jadwal_dasproif3)