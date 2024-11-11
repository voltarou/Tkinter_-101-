# Import library tkinter untuk membuat GUI dan messagebox untuk pesan kesalahan
import tkinter as tk
from tkinter import messagebox

# Fungsi untuk memproses hasil prediksi program studi berdasarkan nilai yang dimasukkan
def hasil_prediksi():
    try:
        # Loop untuk memeriksa setiap nilai mata pelajaran yang dimasukkan pengguna
        for i, entry in enumerate(entries):  # enumerate digunakan untuk mendapatkan index nilai
            nilai = int(entry.get())  # Mengambil nilai dari Entry dan mengonversinya menjadi integer
            # Memeriksa apakah nilai berada dalam rentang 0-100
            if not (0 <= nilai <= 100):
                # Jika tidak, maka ValueError akan dilemparkan dengan pesan kesalahan
                raise ValueError(f"Nilai Mata Pelajaran {i+1} harus berupa angka antara 0-100")
        
        # Jika semua nilai valid, tampilkan hasil prediksi program studi
        hasil_label.config(text="Prediksi Prodi: Teknologi Informasi")
    except ValueError as ve:
        # Menampilkan pesan kesalahan jika nilai yang dimasukkan tidak valid
        messagebox.showerror("Error", f"Kesalahan: {ve}")

# Membuat jendela utama aplikasi
root = tk.Tk()
root.title("Aplikasi Prediksi Prodi Pilihan")
root.geometry("500x500")  # Mengatur ukuran jendela

# Label judul aplikasi
judul_label = tk.Label(root, text="Aplikasi Prediksi Prodi Pilihan", font=("Times New Roman", 18,"bold"), fg="blue")
judul_label.grid(row=0, column=0, columnspan=2, pady=10)

# List untuk menyimpan label dan entry nilai mata pelajaran
labels = []
entries = []

# Loop untuk membuat label dan entry untuk masing-masing nilai mata pelajaran
for i in range(1, 11):
    label = tk.Label(root, text=f"Nilai Mata Pelajaran {i}:")  # Membuat label untuk mata pelajaran ke-i
    label.grid(row=i, column=0, padx=10, pady=5, sticky='w')
    entry = tk.Entry(root)  # Membuat entry untuk memasukkan nilai mata pelajaran ke-i
    entry.grid(row=i, column=1, padx=10, pady=5)
    labels.append(label)  # Menyimpan label ke dalam list labels
    entries.append(entry)  # Menyimpan entry ke dalam list entries

# Tombol untuk memproses hasil prediksi
prediksi_button = tk.Button(root, text="Hasil Prediksi", command=hasil_prediksi)
prediksi_button.grid(row=11, column=0, columnspan=2, pady=20)

# Label untuk menampilkan hasil prediksi
hasil_label = tk.Label(root, text="", font=("Times New Roman", 12))
hasil_label.grid(row=12, column=0, columnspan=2, pady=10)

# Menjalankan aplikasi
root.mainloop()
