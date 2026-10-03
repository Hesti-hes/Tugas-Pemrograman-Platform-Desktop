import tkinter as tk
from tkinter import messagebox


# Membuat kelas utama aplikasi
class AplikasiBiodata(tk.Tk):

    def __init__(self):
        super().__init__()

        # Konfigurasi window utama
        self.title("Aplikasi Biodata Mahasiswa")
        self.geometry("600x700")
        self.resizable(True, True)

        # Warna latar belakang
        self.configure(bg="lightblue")

        # Database user sederhana
        self.users_db = {
            "admin": "123",
            "user1": "password1",
            "mahasiswa": "123456",
            "hesti febriyani(24106050010)": "123456"
        }

        # Status login
        self.current_user = None

        # Atribut untuk manajemen frame
        self.frame_aktif = None

        # Buat tampilan
        self._buat_tampilan_login()
        self._buat_tampilan_biodata()

        # Tampilkan frame login di awal
        self._pindah_ke(self.frame_login)

    # Membuat Tampilan Biodata
    def _buat_tampilan_biodata(self):

        # Variabel Kontrol Tkinter
        self.var_nama = tk.StringVar()
        self.var_nim = tk.StringVar()
        self.var_jurusan = tk.StringVar()
        self.var_jk = tk.StringVar(value="Pria")
        self.var_setuju = tk.IntVar()

        # Aktifkan trace untuk validasi real-time
        self.var_nama.trace_add("write", self.validate_form)
        self.var_nim.trace_add("write", self.validate_form)
        self.var_jurusan.trace_add("write", self.validate_form)

        # Frame Biodata
        self.frame_biodata = tk.Frame(
            master=self,
            padx=20,
            pady=20
        )

        self.warna_background_awal = self.frame_biodata.cget("bg")

        self.frame_biodata.columnconfigure(
            1,
            weight=1
        )

        # Judul
        self.label_judul = tk.Label(
            master=self.frame_biodata,
            text="FORM BIODATA MAHASISWA",
            font=("Arial", 16, "bold")
        )

        self.label_judul.grid(
            row=0,
            column=0,
            columnspan=2,
            pady=20
        )

        # Frame khusus untuk input dengan border
        self.frame_input = tk.Frame(
            master=self.frame_biodata,
            relief=tk.GROOVE,
            borderwidth=2,
            padx=10,
            pady=10
        )

        # Input Nama
        self.label_nama = tk.Label(
            master=self.frame_input,
            text="Nama Lengkap:",
            font=("Arial", 12)
        )

        self.label_nama.grid(
            row=0,
            column=0,
            sticky="W",
            pady=2
        )

        self.entry_nama = tk.Entry(
            master=self.frame_input,
            width=30,
            font=("Arial", 12),
            textvariable=self.var_nama
        )

        self.entry_nama.grid(
            row=0,
            column=1,
            pady=2
        )

        # Input NIM
        self.label_nim = tk.Label(
            master=self.frame_input,
            text="NIM:",
            font=("Arial", 12)
        )

        self.label_nim.grid(
            row=1,
            column=0,
            sticky="W",
            pady=2
        )

        self.entry_nim = tk.Entry(
            master=self.frame_input,
            width=30,
            font=("Arial", 12),
            textvariable=self.var_nim
        )

        self.entry_nim.grid(
            row=1,
            column=1,
            pady=2
        )

        # Input Jurusan
        self.label_jurusan = tk.Label(
            master=self.frame_input,
            text="Jurusan:",
            font=("Arial", 12)
        )

        self.label_jurusan.grid(
            row=2,
            column=0,
            sticky="W",
            pady=2
        )

        self.entry_jurusan = tk.Entry(
            master=self.frame_input,
            width=30,
            font=("Arial", 12),
            textvariable=self.var_jurusan
        )

        self.entry_jurusan.grid(
            row=2,
            column=1,
            pady=2
        )

        # Input Alamat
        self.label_alamat = tk.Label(
            master=self.frame_input,
            text="Alamat:",
            font=("Arial", 12)
        )

        self.label_alamat.grid(
            row=3,
            column=0,
            sticky="NW",
            pady=2
        )

        # Frame untuk Text dan Scrollbar
        self.frame_alamat = tk.Frame(
            master=self.frame_input,
            relief=tk.SUNKEN,
            borderwidth=1
        )

        # Scrollbar
        self.scrollbar_alamat = tk.Scrollbar(
            master=self.frame_alamat
        )

        self.scrollbar_alamat.pack(
            side=tk.RIGHT,
            fill=tk.Y
        )

        # Text widget
        self.text_alamat = tk.Text(
            master=self.frame_alamat,
            height=5,
            width=28,
            font=("Arial", 12)
        )

        self.text_alamat.pack(
            side=tk.LEFT,
            fill=tk.BOTH,
            expand=True
        )

        # Hubungkan scrollbar dengan Text
        self.scrollbar_alamat.config(
            command=self.text_alamat.yview
        )

        self.text_alamat.config(
            yscrollcommand=self.scrollbar_alamat.set
        )

        self.frame_alamat.grid(
            row=3,
            column=1,
            pady=2
        )

        # Jenis Kelamin
        self.label_jk = tk.Label(
            master=self.frame_input,
            text="Jenis Kelamin:",
            font=("Arial", 12)
        )

        self.label_jk.grid(
            row=4,
            column=0,
            sticky="W",
            pady=2
        )

        self.frame_jk = tk.Frame(
            master=self.frame_input
        )

        self.frame_jk.grid(
            row=4,
            column=1,
            sticky="W"
        )

        self.radio_pria = tk.Radiobutton(
            master=self.frame_jk,
            text="Pria",
            variable=self.var_jk,
            value="Pria"
        )

        self.radio_pria.pack(
            side=tk.LEFT
        )

        self.radio_wanita = tk.Radiobutton(
            master=self.frame_jk,
            text="Wanita",
            variable=self.var_jk,
            value="Wanita"
        )

        self.radio_wanita.pack(
            side=tk.LEFT
        )

        # Checkbox persetujuan
        self.check_setuju = tk.Checkbutton(
            master=self.frame_input,
            text="Saya menyetujui pengumpulan data ini.",
            variable=self.var_setuju,
            font=("Arial", 10),
            command=self.validate_form
        )

        self.check_setuju.grid(
            row=5,
            column=0,
            columnspan=2,
            pady=10,
            sticky="W"
        )

        self.frame_input.grid(
            row=1,
            column=0,
            columnspan=2,
            sticky="EW"
        )

        # Tombol Submit
        self.btn_submit = tk.Button(
            master=self.frame_biodata,
            text="Submit Biodata",
            font=("Arial", 12, "bold"),
            command=self.submit_data,
            state=tk.DISABLED
        )

        self.btn_submit.grid(
            row=6,
            column=0,
            columnspan=2,
            pady=20,
            sticky="EW"
        )

        # Event hover
        self.btn_submit.bind(
            "<Enter>",
            self.on_enter
        )

        self.btn_submit.bind(
            "<Leave>",
            self.on_leave
        )

        # Keyboard shortcuts
        self.entry_nama.bind(
            "<Return>",
            self.submit_shortcut
        )

        self.entry_nim.bind(
            "<Return>",
            self.submit_shortcut
        )

        self.entry_jurusan.bind(
            "<Return>",
            self.submit_shortcut
        )

        self.text_alamat.bind(
            "<Return>",
            self.submit_shortcut
        )

        # Label hasil
        self.label_hasil = tk.Label(
            master=self.frame_biodata,
            text="",
            font=("Arial", 12, "italic"),
            justify=tk.LEFT
        )

        self.label_hasil.grid(
            row=7,
            column=0,
            columnspan=2,
            sticky="W",
            padx=10
        )

        # Membuat Menu
        self._buat_menu()

    # Membuat Tampilan Login
    def _buat_tampilan_login(self):

        self.frame_login = tk.Frame(
            master=self,
            padx=20,
            pady=100
        )

        # Konfigurasi grid
        self.frame_login.grid_columnconfigure(
            0,
            weight=1
        )

        self.frame_login.grid_columnconfigure(
            1,
            weight=1
        )

        # Judul Login
        tk.Label(
            self.frame_login,
            text="HALAMAN LOGIN",
            font=("Arial", 16, "bold")
        ).grid(
            row=0,
            column=0,
            columnspan=2,
            pady=20
        )

        # Input Username
        tk.Label(
            self.frame_login,
            text="Username:",
            font=("Arial", 12)
        ).grid(
            row=1,
            column=0,
            sticky="W",
            pady=5
        )

        self.entry_username = tk.Entry(
            self.frame_login,
            font=("Arial", 12)
        )

        self.entry_username.grid(
            row=1,
            column=1,
            pady=5,
            sticky="EW"
        )

        # Input Password
        tk.Label(
            self.frame_login,
            text="Password:",
            font=("Arial", 12)
        ).grid(
            row=2,
            column=0,
            sticky="W",
            pady=5
        )

        self.entry_password = tk.Entry(
            self.frame_login,
            font=("Arial", 12),
            show="*"
        )

        self.entry_password.grid(
            row=2,
            column=1,
            pady=5,
            sticky="EW"
        )

        # Tombol Login
        self.btn_login = tk.Button(
            self.frame_login,
            text="Login",
            font=("Arial", 12, "bold"),
            command=self._coba_login
        )

        self.btn_login.grid(
            row=3,
            column=0,
            columnspan=2,
            pady=20,
            sticky="EW"
        )

        # Keyboard shortcuts untuk login
        self.entry_username.bind(
            "<Return>",
            lambda e: self.entry_password.focus_set()
        )

        self.entry_password.bind(
            "<Return>",
            lambda e: self._coba_login()
        )

    # System Navigation
    def _pindah_ke(self, frame_tujuan):
        """Method untuk berpindah antar tampilan"""

        if self.frame_aktif is not None:
            self.frame_aktif.pack_forget()

        self.frame_aktif = frame_tujuan

        self.frame_aktif.pack(
            fill=tk.BOTH,
            expand=True
        )

        # Auto-focus berdasarkan frame yang ditampilkan
        if frame_tujuan == self.frame_login:
            self.after(
                100,
                lambda: self.entry_username.focus_set()
            )

        elif frame_tujuan == self.frame_biodata:
            self.after(
                100,
                lambda: self.entry_nama.focus_set()
            )

    # Method Biodata
    def submit_data(self):

        # Cek checkbox
        if self.var_setuju.get() == 0:
            messagebox.showwarning(
                "Peringatan",
                "Anda harus menyetujui pengumpulan data!"
            )
            return

        # Ambil data dari form
        nama = self.entry_nama.get()
        nim = self.entry_nim.get()
        jurusan = self.entry_jurusan.get()

        alamat = self.text_alamat.get(
            "1.0",
            tk.END
        ).strip()

        jenis_kelamin = self.var_jk.get()

        # Cek field kosong
        if not nama or not nim or not jurusan:
            messagebox.showwarning(
                "Input Kosong",
                "Semua field harus diisi!"
            )
            return

        # Tampilkan hasil
        hasil = (
            f"Nama: {nama}\n"
            f"NIM: {nim}\n"
            f"Jurusan: {jurusan}\n"
            f"Alamat: {alamat}\n"
            f"Jenis Kelamin: {jenis_kelamin}"
        )

        messagebox.showinfo(
            "Data Tersimpan",
            hasil
        )

        # Tampilkan hasil di label
        self.label_hasil.config(
            text=f"BIODATA TERSIMPAN:\n\n{hasil}"
        )

    def validate_form(self, *args):

        nama_valid = self.var_nama.get().strip() != ""
        nim_valid = self.var_nim.get().strip() != ""
        jurusan_valid = self.var_jurusan.get().strip() != ""
        setuju_valid = self.var_setuju.get() == 1

        if (
            nama_valid
            and nim_valid
            and jurusan_valid
            and setuju_valid
        ):
            self.btn_submit.config(
                state=tk.NORMAL
            )
        else:
            self.btn_submit.config(
                state=tk.DISABLED
            )

    def on_enter(self, event):

        if self.btn_submit["state"] == tk.NORMAL:
            self.btn_submit.config(
                bg=self.frame_biodata.cget("bg")
            )

    def on_leave(self, event):

        self.btn_submit.config(
            bg="SystemButtonFace"
        )

    def submit_shortcut(self, event=None):

        if self.btn_submit["state"] == tk.NORMAL:
            self.submit_data()

    # Implementasi Login dan Validasi Input
    def _coba_login(self):
        """Method untuk memproses attempt login"""

        username = self.entry_username.get().strip()
        password = self.entry_password.get()

        # Validasi input kosong
        if not username or not password:
            messagebox.showwarning(
                "Login Gagal",
                "Username dan Password tidak boleh kosong."
            )

            self.entry_username.focus_set()
            return

        # Validasi panjang minimum
        if len(username) < 3:
            messagebox.showwarning(
                "Login Gagal",
                "Username minimal 3 karakter."
            )

            self.entry_username.focus_set()
            return

        # Cek Kredensial
        if username in self.users_db and self.users_db[username] == password:

            # Simpan user yang sedang login
            self.current_user = username

            # Ubah background sesuai user yang berhasil login
            self._ubah_background_user()

            messagebox.showinfo(
                "Login Berhasil",
                f"Selamat Datang, {username}!"
            )

            # Reset form biodata
            self._reset_form_biodata()

            # Update title
            self._update_title_with_user()

            # Pindah ke halaman biodata
            self._pindah_ke(self.frame_biodata)

            # Bersihkan field login setelah berhasil
            self.entry_username.delete(
                0,
                tk.END
            )

            self.entry_password.delete(
                0,
                tk.END
            )

        else:
            messagebox.showerror(
                "Login Gagal",
                "Username atau Password salah."
            )

            # Bersihkan password
            self.entry_password.delete(
                0,
                tk.END
            )

            # Focus kembali ke username
            self.entry_username.focus_set()

    # Helper Method
    def _reset_form_biodata(self):

        self.var_nama.set("")
        self.var_nim.set("")
        self.var_jurusan.set("")

        self.text_alamat.delete(
            "1.0",
            tk.END
        )

        self.var_jk.set("Pria")
        self.var_setuju.set(0)

        self.label_hasil.config(
            text=""
        )

    def _update_title_with_user(self):

        if self.current_user:
            self.title(
                f"Aplikasi Biodata Mahasiswa - User: {self.current_user}"
            )
        else:
            self.title(
                "Aplikasi Biodata Mahasiswa"
            )

    def _ubah_background_user(self):

        warna_user = {
            "admin": "lightblue",
            "user1": "lightgreen",
            "mahasiswa": "lightyellow",
            "hesti febriyani(24106050010)": "lightpink"
        }

        warna_background = warna_user.get(
            self.current_user,
            self.warna_background_awal
        )

        self.frame_biodata.config(
            bg=warna_background
        )

        self._ubah_warna_widget(
            self.frame_biodata,
            warna_background
        )

        self.menu_bar.config(
            bg=warna_background,
            activebackground=warna_background
        )

        self.file_menu.config(
            bg=warna_background,
            activebackground=warna_background
        )

    def _ubah_warna_widget(self, widget, warna_background):

        if isinstance(widget, (tk.Frame, tk.Label, tk.Button)):
            widget.config(
                bg=warna_background
            )

        for child in widget.winfo_children():
            self._ubah_warna_widget(
                child,
                warna_background
            )

    # Logout
    def _logout(self):

        if messagebox.askyesno(
            "Logout",
            f"Apakah {self.current_user} yakin ingin logout?"
        ):

            self.current_user = None

            # Kembalikan background biodata ke warna awal
            self._ubah_background_user()

            # Hapus menu
            self._hapus_menu()

            # Kembalikan title
            self._update_title_with_user()

            # Bersihkan field login
            self.entry_username.delete(
                0,
                tk.END
            )

            self.entry_password.delete(
                0,
                tk.END
            )

            # Reset biodata
            self._reset_form_biodata()

            # Kembali ke halaman login
            self._pindah_ke(
                self.frame_login
            )

            self.entry_username.focus_set()

    # Menu
    def _buat_menu(self):

        self.menu_bar = tk.Menu(
            master=self
        )

        self.config(
            menu=self.menu_bar
        )

        self.file_menu = tk.Menu(
            master=self.menu_bar,
            tearoff=0
        )

        self.file_menu.add_command(
            label="Logout",
            command=self._logout
        )

        self.file_menu.add_separator()

        self.file_menu.add_command(
            label="Keluar",
            command=self.destroy
        )

        self.menu_bar.add_cascade(
            label="File",
            menu=self.file_menu
        )

    def _hapus_menu(self):

        empty_menu = tk.Menu(
            self
        )

        self.config(
            menu=empty_menu
        )


# Menjalankan aplikasi
if __name__ == "__main__":
    app = AplikasiBiodata()
    app.mainloop()