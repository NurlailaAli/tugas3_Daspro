# Data Dictionary dengan Username & Password Mahasiswa
data_mahasiswa = {
    'Azizi': 'JKT4801',
    'Shani': 'JKT4802',
    'Gracia': 'JKT4803',
    'Christy': 'JKT4804',
    'Chika': 'JKT4805',
    'Marsha': 'JKT49806',
    'Adel': 'JKT4807',
    'Olla': 'JKT4808',
    'Oniel': 'JKT4809',
    'Kathrina': 'JKT48010'
}

# Aplikasi Sistem Login
def login(username, password):
    if username in data_mahasiswa and data_mahasiswa[username] == password:
        return f"Selamat datang, {username}!"
    else:
        return "Data yang dimasukkan salah."

# Contoh penggunaan aplikasi login
input_username = input("Masukkan username: ")
input_password = input("Masukkan password: ")

hasil_login = login(input_username, input_password)
print(hasil_login)