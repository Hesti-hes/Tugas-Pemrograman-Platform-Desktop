import tkinter as tk
from tkinter import messagebox
import datetime


class AplikasiBiodata(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Aplikasi Biodata Mahasiswa")
        self.geometry("750x700")
        self.resizable(True, True)
        self.configure(bg="#f0f2f5")

        self.users_db = {  
            "admin": "123",
            "user1": "password1",
            "mahasiswa": "123456",
            "hesti febriyani(24106050010)": "123456"
        }

        self.current_user = None
        self.frame_aktif = None
        
        self.theme_color = "#0d6efd"
        self.theme_active_color = "#0b5ed7"

        self._buat_tampilan_login()
        self._buat_tampilan_biodata()
        
        self._pindah_ke(self.frame_login)
        self._hapus_menu() # Hapus menu pada saat di halaman login

    # LOGIN VIEW
    def _buat_tampilan_login(self):
        self.frame_login = tk.Frame(self, bg="#f0f2f5")
        
        self.login_wrapper = tk.Frame(self.frame_login, bg="#f0f2f5")
        self.login_wrapper.place(relx=0.5, rely=0.5, anchor=tk.CENTER, width=450)
        
        self.card_login = tk.Frame(self.login_wrapper, bg="white", padx=40, pady=40, highlightthickness=1, highlightbackground="#e9ecef")
        self.card_login.pack(fill=tk.BOTH, expand=True)
        
        tk.Label(self.card_login, text="Selamat Datang", font=("Segoe UI", 22, "bold"), bg="white", fg="#212529").pack(pady=(0, 5))
        tk.Label(self.card_login, text="Silakan masuk ke akun Anda", font=("Segoe UI", 11), bg="white", fg="#6c757d").pack(pady=(0, 30))
        
        # Username
        tk.Label(self.card_login, text="Username", font=("Segoe UI", 10, "bold"), bg="white", fg="#495057").pack(anchor=tk.W, pady=(0, 5))
        self.entry_username = tk.Entry(self.card_login, font=("Segoe UI", 12), bg="#f8f9fa", relief=tk.FLAT, highlightthickness=1, highlightbackground="#ced4da", highlightcolor="#0d6efd")
        self.entry_username.pack(fill=tk.X, ipady=8, padx=1)
        self.err_login_user = tk.Label(self.card_login, text="", font=("Segoe UI", 9), bg="white", fg="#dc3545")
        self.err_login_user.pack(anchor=tk.W)
        
        # Password
        tk.Label(self.card_login, text="Password", font=("Segoe UI", 10, "bold"), bg="white", fg="#495057").pack(anchor=tk.W, pady=(15, 5))
        self.entry_password = tk.Entry(self.card_login, font=("Segoe UI", 12), show="*", bg="#f8f9fa", relief=tk.FLAT, highlightthickness=1, highlightbackground="#ced4da", highlightcolor="#0d6efd")
        self.entry_password.pack(fill=tk.X, ipady=8, padx=1)
        self.err_login_pass = tk.Label(self.card_login, text="", font=("Segoe UI", 9), bg="white", fg="#dc3545")
        self.err_login_pass.pack(anchor=tk.W)
        
        # General Error
        self.err_login_general = tk.Label(self.card_login, text="", font=("Segoe UI", 10), bg="white", fg="#dc3545")
        self.err_login_general.pack(pady=(5, 5))
        
        # Button Login
        self.btn_login = tk.Button(
            self.card_login, text="Masuk", font=("Segoe UI", 12, "bold"),
            bg="#0d6efd", fg="white", activebackground="#0b5ed7", activeforeground="white",
            relief=tk.FLAT, cursor="hand2", command=self._coba_login
        )
        self.btn_login.pack(fill=tk.X, pady=(10, 20), ipady=8)
        
        self.btn_login.bind("<Enter>", lambda e: self.btn_login.config(bg="#0b5ed7"))
        self.btn_login.bind("<Leave>", lambda e: self.btn_login.config(bg="#0d6efd"))
        
        self.entry_username.bind("<Return>", lambda e: self.entry_password.focus_set())
        self.entry_password.bind("<Return>", lambda e: self._coba_login())

    # BIODATA VIEW
    def _buat_tampilan_biodata(self):
        self.frame_biodata = tk.Frame(self, bg="#f0f2f5")
        
        # Header user (Accent color top bar)
        self.header_frame = tk.Frame(self.frame_biodata, bg=self.theme_color, height=70)
        self.header_frame.pack(fill=tk.X)
        self.header_frame.pack_propagate(False)
        
        self.lbl_header_title = tk.Label(self.header_frame, text="Aplikasi Biodata", font=("Segoe UI", 16, "bold"), bg=self.theme_color, fg="white")
        self.lbl_header_title.pack(side=tk.LEFT, padx=30, pady=20)
        
        self.lbl_header_user = tk.Label(self.header_frame, text="", font=("Segoe UI", 12), bg=self.theme_color, fg="white")
        self.lbl_header_user.pack(side=tk.RIGHT, padx=30, pady=22)
        
        # Main content card
        self.card_biodata = tk.Frame(self.frame_biodata, bg="white", padx=30, pady=20, highlightthickness=1, highlightbackground="#e9ecef")
        self.card_biodata.pack(fill=tk.BOTH, expand=True, padx=30, pady=20)
        
        tk.Label(self.card_biodata, text="Form Biodata Mahasiswa", font=("Segoe UI", 18, "bold"), bg="white", fg="#212529").pack(anchor=tk.W, pady=(0, 15))
        
        # Variables
        self.var_nama = tk.StringVar()
        self.var_nim = tk.StringVar()
        self.var_jurusan = tk.StringVar()
        self.var_jk = tk.StringVar(value="Pria")
        self.var_setuju = tk.IntVar()
        
        self.var_nama.trace_add("write", self.validate_form)
        self.var_nim.trace_add("write", self.validate_form)
        self.var_jurusan.trace_add("write", self.validate_form)
        self.var_setuju.trace_add("write", self.validate_form)
        
        self.form_container = tk.Frame(self.card_biodata, bg="white")
        self.form_container.pack(fill=tk.BOTH, expand=True)
        self.form_container.columnconfigure(1, weight=1)
        
        self.entries = {}
        self.errors = {}
        
        self._add_form_row("Nama Lengkap", "nama", self.var_nama, 0)
        self._add_form_row("NIM", "nim", self.var_nim, 1)
        self._add_form_row("Jurusan", "jurusan", self.var_jurusan, 2)
        
        # Alamat
        tk.Label(self.form_container, text="Alamat Lengkap", font=("Segoe UI", 10, "bold"), bg="white", fg="#495057").grid(row=6, column=0, sticky="NW", pady=(8, 2), padx=(0, 20))
        
        alamat_frame = tk.Frame(self.form_container, bg="#f8f9fa", highlightthickness=1, highlightbackground="#ced4da", highlightcolor=self.theme_color)
        alamat_frame.grid(row=6, column=1, sticky="EW", pady=(8, 0))
        
        self.scrollbar_alamat = tk.Scrollbar(alamat_frame)
        self.scrollbar_alamat.pack(side=tk.RIGHT, fill=tk.Y)
        
        self.text_alamat = tk.Text(alamat_frame, height=3, font=("Segoe UI", 11), bg="#f8f9fa", relief=tk.FLAT)
        self.text_alamat.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)
        
        self.text_alamat.config(yscrollcommand=self.scrollbar_alamat.set)
        self.scrollbar_alamat.config(command=self.text_alamat.yview)
        
        self.entries["alamat"] = alamat_frame
        self.errors["alamat"] = tk.Label(self.form_container, text="", font=("Segoe UI", 9), bg="white", fg="#dc3545")
        self.errors["alamat"].grid(row=7, column=1, sticky="W")
        
        self.text_alamat.bind("<KeyRelease>", self.validate_form)
        self.text_alamat.bind("<FocusOut>", lambda e: self.validasi_field(e, self.text_alamat, self.errors["alamat"], "alamat"))

        # Jenis Kelamin
        tk.Label(self.form_container, text="Jenis Kelamin", font=("Segoe UI", 10, "bold"), bg="white", fg="#495057").grid(row=8, column=0, sticky="W", pady=(10, 2))
        jk_frame = tk.Frame(self.form_container, bg="white")
        jk_frame.grid(row=8, column=1, sticky="W", pady=(10, 2))
        tk.Radiobutton(jk_frame, text="Pria", variable=self.var_jk, value="Pria", font=("Segoe UI", 10), bg="white", activebackground="white", cursor="hand2").pack(side=tk.LEFT, padx=(0, 20))
        tk.Radiobutton(jk_frame, text="Wanita", variable=self.var_jk, value="Wanita", font=("Segoe UI", 10), bg="white", activebackground="white", cursor="hand2").pack(side=tk.LEFT)
        
        # Checkbox
        self.check_setuju = tk.Checkbutton(self.form_container, text="Saya menyetujui pengumpulan data ini.", variable=self.var_setuju, font=("Segoe UI", 10), bg="white", activebackground="white", cursor="hand2")
        self.check_setuju.grid(row=9, column=0, columnspan=2, sticky="W", pady=(15, 5))
        
        # Buttons frame
        btn_frame = tk.Frame(self.card_biodata, bg="white")
        btn_frame.pack(fill=tk.X, pady=(15, 0))
        
        self.btn_submit = tk.Button(
            btn_frame, text="Submit Biodata", font=("Segoe UI", 11, "bold"),
            bg=self.theme_color, fg="white", activebackground=self.theme_active_color,
            relief=tk.FLAT, cursor="hand2", command=self.submit_data, state=tk.NORMAL
        )
        self.btn_submit.pack(side=tk.RIGHT, ipady=6, ipadx=20)
        
        self.btn_submit.bind("<Enter>", lambda e: self.btn_submit.config(bg=self.theme_active_color))
        self.btn_submit.bind("<Leave>", lambda e: self.btn_submit.config(bg=self.theme_color))
        
        self.label_hasil = tk.Label(self.card_biodata, text="", font=("Segoe UI", 11), bg="white", fg="#198754", justify=tk.LEFT)
        self.label_hasil.pack(anchor=tk.W, pady=(20, 0))

        # Keyboard shortcuts (Enter to submit)
        self.entries["nama"].bind("<Return>", self.submit_shortcut)
        self.entries["nim"].bind("<Return>", self.submit_shortcut)
        self.entries["jurusan"].bind("<Return>", self.submit_shortcut)

    def _add_form_row(self, label_text, field_name, var, row_idx):
        tk.Label(self.form_container, text=label_text, font=("Segoe UI", 10, "bold"), bg="white", fg="#495057").grid(row=row_idx*2, column=0, sticky="W", pady=(8, 2), padx=(0, 20))
        entry = tk.Entry(self.form_container, font=("Segoe UI", 11), textvariable=var, bg="#f8f9fa", relief=tk.FLAT, highlightthickness=1, highlightbackground="#ced4da", highlightcolor=self.theme_color)
        entry.grid(row=row_idx*2, column=1, sticky="EW", pady=(8, 0), ipady=5)
        
        err_lbl = tk.Label(self.form_container, text="", font=("Segoe UI", 9), bg="white", fg="#dc3545")
        err_lbl.grid(row=row_idx*2+1, column=1, sticky="W")
        
        entry.bind("<FocusOut>", lambda e: self.validasi_field(e, entry, err_lbl, field_name))
        
        self.entries[field_name] = entry
        self.errors[field_name] = err_lbl

    # NAVIGATION & MENU
    def _pindah_ke(self, frame_tujuan):
        if self.frame_aktif is not None:
            self.frame_aktif.pack_forget()
        
        self.frame_aktif = frame_tujuan
        self.frame_aktif.pack(fill=tk.BOTH, expand=True)

        if frame_tujuan == self.frame_login:
            self.after(100, lambda: self.entry_username.focus_set())
        elif frame_tujuan == self.frame_biodata:
            self.after(100, lambda: self.entries["nama"].focus_set())

    def _buat_menu(self):
        self.menu_bar = tk.Menu(self)
        self.config(menu=self.menu_bar)

        self.file_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.file_menu.add_command(label="Simpan Hasil", command=self.simpan_hasil)
        self.file_menu.add_separator()
        self.file_menu.add_command(label="Logout", command=self._logout)
        self.file_menu.add_separator()
        self.file_menu.add_command(label="Keluar", command=self.destroy)

        self.menu_bar.add_cascade(label="File", menu=self.file_menu)

    def _hapus_menu(self):
        empty_menu = tk.Menu(self)
        self.config(menu=empty_menu)

    # VALIDATION & LOGIC
    def _coba_login(self):
        username = self.entry_username.get().strip()
        password = self.entry_password.get()

        # Reset states
        self.err_login_general.config(text="")
        self.err_login_user.config(text="")
        self.err_login_pass.config(text="")
        self.entry_username.config(highlightbackground="#ced4da")
        self.entry_password.config(highlightbackground="#ced4da")

        if not username:
            self.entry_username.config(highlightbackground="#dc3545")
            self.err_login_user.config(text="Username wajib diisi.")
            self.entry_username.focus_set()
            return
            
        if not password:
            self.entry_password.config(highlightbackground="#dc3545")
            self.err_login_pass.config(text="Password wajib diisi.")
            self.entry_password.focus_set()
            return
            
        if len(username) < 3:
            self.entry_username.config(highlightbackground="#dc3545")
            self.err_login_user.config(text="Username minimal 3 karakter.")
            self.entry_username.focus_set()
            return

        if username in self.users_db and self.users_db[username] == password:
            self.current_user = username
            self._ubah_background_user()
            self._reset_form_biodata()
            self._update_title_with_user()
            self._buat_menu()
            self._pindah_ke(self.frame_biodata)
            
            self.entry_username.delete(0, tk.END)
            self.entry_password.delete(0, tk.END)
        else:
            self.entry_username.config(highlightbackground="#dc3545")
            self.entry_password.config(highlightbackground="#dc3545")
            self.err_login_general.config(text="Username atau Password salah.")
            self.entry_password.delete(0, tk.END)
            self.entry_username.focus_set()

    def _logout(self):
        if messagebox.askyesno("Logout", f"Apakah Anda yakin ingin logout dari akun {self.current_user}?"):
            self.current_user = None
            self._update_title_with_user()
            self._hapus_menu()
            
            self.entry_username.delete(0, tk.END)
            self.entry_password.delete(0, tk.END)
            
            self.entry_username.config(highlightbackground="#ced4da")
            self.entry_password.config(highlightbackground="#ced4da")
            self.err_login_general.config(text="")
            self.err_login_user.config(text="")
            self.err_login_pass.config(text="")
            
            self._reset_form_biodata()
            self._pindah_ke(self.frame_login)

    def validate_form(self, *args):
        # Jika field sedang dalam state error (merah), lakukan validasi secara real-time pada setiap ketikan.
        # Jika belum error (baru mengetik awal), kita tidak memunculkan error secara agresif.
        for field in ["nama", "nim", "jurusan"]:
            if self.entries[field].cget("highlightbackground") == "#dc3545":
                self.validasi_field(None, self.entries[field], self.errors[field], field)
                
        if self.entries["alamat"].cget("highlightbackground") == "#dc3545":
            self.validasi_field(None, self.text_alamat, self.errors["alamat"], "alamat")

    def _clear_error(self, widget, err_lbl):
        widget.config(highlightbackground="#ced4da")
        err_lbl.config(text="")

    def _set_error(self, widget, err_lbl, msg):
        widget.config(highlightbackground="#dc3545")
        err_lbl.config(text=msg)

    def validasi_field(self, event, widget, err_lbl, field_name):
        val = widget.get("1.0", tk.END).strip() if field_name == "alamat" else widget.get().strip()
        ui_widget = self.entries[field_name]
            
        if not val:
            self._set_error(ui_widget, err_lbl, f"{field_name.capitalize()} wajib diisi.")
        elif field_name == "nama":
            if not any(c.isalpha() for c in val):
                self._set_error(ui_widget, err_lbl, "Nama harus mengandung huruf.")
            elif not all(c.isalpha() or c.isspace() or c in ".,'-" for c in val):
                self._set_error(ui_widget, err_lbl, "Nama tidak boleh mengandung angka/simbol.")
            else:
                self._clear_error(ui_widget, err_lbl)
        elif field_name == "nim" and (not val.isdigit() or len(val) < 8):
            self._set_error(ui_widget, err_lbl, "Format NIM tidak valid (minimal 8 angka).")
        elif field_name == "jurusan":
            if not any(c.isalpha() for c in val):
                self._set_error(ui_widget, err_lbl, "Jurusan harus mengandung huruf.")
            elif not all(c.isalnum() or c.isspace() or c in ".,'-&()" for c in val):
                self._set_error(ui_widget, err_lbl, "Jurusan tidak boleh mengandung simbol tidak valid.")
            else:
                self._clear_error(ui_widget, err_lbl)
        else:
            self._clear_error(ui_widget, err_lbl)

    def submit_data(self):
        try:
            # Memicu validasi pada semua field agar error state muncul
            self.validasi_field(None, self.entries["nama"], self.errors["nama"], "nama")
            self.validasi_field(None, self.entries["nim"], self.errors["nim"], "nim")
            self.validasi_field(None, self.entries["jurusan"], self.errors["jurusan"], "jurusan")
            self.validasi_field(None, self.text_alamat, self.errors["alamat"], "alamat")
            
            # Ambil nilai terbaru
            nama = self.var_nama.get().strip()
            nim = self.var_nim.get().strip()
            jurusan = self.var_jurusan.get().strip()
            alamat = self.text_alamat.get("1.0", tk.END).strip()
            jk = self.var_jk.get()
            
            # Cek status validasi dari state UI (jika ada yg masih merah berarti tidak valid)
            is_valid = True
            for field in ["nama", "nim", "jurusan", "alamat"]:
                if self.entries[field].cget("highlightbackground") == "#dc3545":
                    is_valid = False
                
            if not is_valid:
                messagebox.showwarning("Input Tidak Valid", "Silakan periksa kembali field yang berwarna merah!")
                return

            if self.var_setuju.get() == 0:
                messagebox.showwarning("Peringatan", "Anda harus menyetujui pengumpulan data!")
                return

            hasil = f"Nama: {nama}\nNIM: {nim}\nJurusan: {jurusan}\nAlamat: {alamat}\nJenis Kelamin: {jk}"
            messagebox.showinfo("Data Tersimpan", hasil)

            self.label_hasil.config(text=f"BIODATA TERSIMPAN:\nDiinput oleh: {self.current_user}\n\n{hasil}", fg=self.theme_color)
        except Exception as e:
            messagebox.showerror("Error", f"Terjadi kesalahan saat memproses data:\n{str(e)}")

    def submit_shortcut(self, event=None):
        if self.btn_submit["state"] == tk.NORMAL:
            self.submit_data()

    def simpan_hasil(self):
        try:
            hasil = self.label_hasil.cget("text")
            if not hasil or "BIODATA TERSIMPAN" not in hasil:
                messagebox.showwarning("Peringatan", "Tidak ada data untuk disimpan. Silakan submit terlebih dahulu.")
                return

            ts = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"biodata_{self.current_user}_{ts}.txt"

            with open(filename, "w", encoding="utf-8") as f:
                f.write(f"Data disimpan oleh: {self.current_user}\n")
                f.write(f"Waktu penyimpanan: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
                f.write("-" * 50 + "\n")
                f.write(hasil)

            messagebox.showinfo("Berhasil", f"Data berhasil disimpan ke file '{filename}'.")
        except PermissionError:
            messagebox.showerror("Error", "Tidak memiliki izin untuk menyimpan file di lokasi ini.")
        except Exception as e:
            messagebox.showerror("Error", f"Terjadi kesalahan:\n{str(e)}")

    def _reset_form_biodata(self):
        self.var_nama.set("")
        self.var_nim.set("")
        self.var_jurusan.set("")
        self.text_alamat.delete("1.0", tk.END)
        self.var_jk.set("Pria")
        self.var_setuju.set(0)
        self.label_hasil.config(text="")
        
        for field in ["nama", "nim", "jurusan", "alamat"]:
            self._clear_error(self.entries[field], self.errors[field])

    def _update_title_with_user(self):
        if self.current_user:
            self.title(f"Aplikasi Biodata Mahasiswa - User: {self.current_user}")
        else:
            self.title("Aplikasi Biodata Mahasiswa")

    def _ubah_background_user(self):
        # Role-based themes
        themes = {
            "admin": {"primary": "#0d6efd", "active": "#0b5ed7"},
            "user1": {"primary": "#198754", "active": "#157347"},
            "mahasiswa": {"primary": "#fd7e14", "active": "#e37012"},
            "hesti febriyani(24106050010)": {"primary": "#d63384", "active": "#b82971"}
        }
        
        theme = themes.get(self.current_user, {"primary": "#0d6efd", "active": "#0b5ed7"})
        self.theme_color = theme["primary"]
        self.theme_active_color = theme["active"]
        
        # Apply theme colors
        self.header_frame.config(bg=self.theme_color)
        self.lbl_header_title.config(bg=self.theme_color)
        self.lbl_header_user.config(bg=self.theme_color, text=f"User: {self.current_user}")
        
        # Update button colors dynamically when theme changes
        self.btn_submit.config(bg=self.theme_color, activebackground=self.theme_active_color)
        self.btn_submit.bind("<Enter>", lambda e: self.btn_submit.config(bg=self.theme_active_color))
        self.btn_submit.bind("<Leave>", lambda e: self.btn_submit.config(bg=self.theme_color))
        
        for entry in self.entries.values():
            entry.config(highlightcolor=self.theme_color)


if __name__ == "__main__":
    app = AplikasiBiodata()
    app.mainloop()