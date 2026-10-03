import tkinter as tk

# Membuat jendela utama
window = tk.Tk()
window.title("Form Biodata Mahasiswa")
window.geometry("500x600")
window.resizable(False, False)
window.configure(bg="lavender") 

# Membuat label judul
label_judul = tk.Label(
    master=window,
    text="FORM BIODATA MAHASISWA",
    font=("Arial", 16, "bold"),
    bg="lavender"
)
label_judul.pack(pady=20)

# Input Nama
label_nama = tk.Label(master=window, text="Nama Lengkap:", bg="lavender")
label_nama.pack()
entry_nama = tk.Entry(master=window, width=50)
entry_nama.pack(pady=5)

# Input NIM
label_nim = tk.Label(master=window, text="NIM:", font=("Arial", 12), bg="lavender")
label_nim.pack(pady=5)
entry_nim = tk.Entry(master=window, width=50)
entry_nim.pack(pady=5)

# Input Jurusan  
label_jurusan = tk.Label(master=window, text="Jurusan:", font=("Arial", 12), bg="lavender")
label_jurusan.pack(pady=5)
entry_jurusan = tk.Entry(master=window, width=50)
entry_jurusan.pack(pady=5)

# Menjalankan event loop
window.mainloop()