import tkinter as tk
from tkinter import ttk
import threading
import time


class AnimatedApp:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Animasi dan Transisi dengan ttk")
        self.root.geometry("800x650")
        self.root.configure(bg="#1a1a1a")

        # Animation variables
        self.animation_running = False
        self.progress_value = 0
        self.fade_alpha = 1.0

        self._setup_styles()
        self._buat_interface()

    def _setup_styles(self):
        self.style = ttk.Style()

        # Dark theme styles
        self.style.configure("Dark.TFrame", background="#2d2d2d", relief="flat")
        self.style.configure(
            "Dark.TLabel",
            background="#2d2d2d",
            foreground="#ffffff",
            font=("Arial", 11),
        )
        self.style.configure(
            "Title.TLabel",
            background="#2d2d2d",
            foreground="#00ff88",
            font=("Arial", 15, "bold"),
        )
        self.style.configure(
            "Animated.TButton",
            background="#00ff88",
            foreground="#1a1a1a",
            borderwidth=0,
            focuscolor="none",
            padding=(15, 6),
            font=("Arial", 10, "bold"),
        )
        self.style.map(
            "Animated.TButton",
            background=[("active", "#00cc6a"), ("pressed", "#009954")],
        )

    def _buat_interface(self):
        # Main container
        self.main_frame = ttk.Frame(self.root, style="Dark.TFrame")
        self.main_frame.pack(fill="both", expand=True, padx=20, pady=10)

        # Header
        self.header_frame = ttk.Frame(self.main_frame, style="Dark.TFrame")
        self.header_frame.pack(fill="x", pady=(0, 10))
        self.title_label = ttk.Label(
            self.header_frame, text="🎬 Animation Demo", style="Title.TLabel"
        )
        self.title_label.pack()

        # Progress animation section
        self.progress_frame = ttk.LabelFrame(
            self.main_frame, text="Progress Animation", padding="10"
        )
        self.progress_frame.pack(fill="x", pady=(0, 10))

        ttk.Label(
            self.progress_frame, text="Animated Progress Bar:", style="Dark.TLabel"
        ).pack(anchor="w", pady=(0, 5))
        self.progress_bar = ttk.Progressbar(
            self.progress_frame, mode="determinate", length=400, style="TProgressbar"
        )
        self.progress_bar.pack(fill="x", pady=(0, 10))

        progress_controls = ttk.Frame(self.progress_frame, style="Dark.TFrame")
        progress_controls.pack(fill="x")
        ttk.Button(
            progress_controls,
            text="Start Animation",
            style="Animated.TButton",
            command=self.start_progress_animation,
        ).pack(side="left", padx=(0, 10))
        ttk.Button(
            progress_controls,
            text="Stop Animation",
            style="Animated.TButton",
            command=self.stop_animation,
        ).pack(side="left", padx=(0, 10))
        ttk.Button(
            progress_controls,
            text="Reset",
            style="Animated.TButton",
            command=self.reset_progress,
        ).pack(side="left")

        # Sliding panel animation
        self.slide_frame = ttk.LabelFrame(
            self.main_frame, text="Sliding Panel", padding="10"
        )
        self.slide_frame.pack(fill="x", pady=(0, 10))

        self.slide_container = ttk.Frame(
            self.slide_frame, style="Dark.TFrame", height=95
        )
        self.slide_container.pack(fill="x", pady=(0, 10))
        self.slide_container.pack_propagate(False)

        self.sliding_panel = ttk.Frame(self.slide_container, style="Dark.TFrame")
        self.sliding_panel.place(x=-300, y=0, width=320, height=95)

        panel_content = ttk.Frame(self.sliding_panel, style="Dark.TFrame")
        panel_content.pack(fill="both", expand=True, padx=15, pady=10)
        ttk.Label(
            panel_content, text="🎯 Sliding Panel Content", style="Title.TLabel"
        ).pack()
        ttk.Label(
            panel_content,
            text="Panel ini dapat slide masuk dan keluar",
            style="Dark.TLabel",
        ).pack(pady=(5, 0))

        slide_controls = ttk.Frame(self.slide_frame, style="Dark.TFrame")
        slide_controls.pack(fill="x")
        ttk.Button(
            slide_controls,
            text="Slide In",
            style="Animated.TButton",
            command=self.slide_in,
        ).pack(side="left", padx=(0, 10))
        ttk.Button(
            slide_controls,
            text="Slide Out",
            style="Animated.TButton",
            command=self.slide_out,
        ).pack(side="left")

        # Fade animation section
        self.fade_frame = ttk.LabelFrame(
            self.main_frame, text="Fade Animation", padding="10"
        )
        self.fade_frame.pack(fill="both", expand=True)

        self.fade_content = ttk.Frame(self.fade_frame, style="Dark.TFrame")
        self.fade_content.pack(fill="both", expand=True, pady=(0, 10))
        ttk.Label(self.fade_content, text="✨ Fade Content", style="Title.TLabel").pack(
            pady=(8, 4)
        )
        ttk.Label(
            self.fade_content,
            text="Content ini dapat fade in/out dengan smooth transition",
            style="Dark.TLabel",
        ).pack()

        fade_controls = ttk.Frame(self.fade_frame, style="Dark.TFrame")
        fade_controls.pack(fill="x")
        ttk.Button(
            fade_controls,
            text="Fade Out",
            style="Animated.TButton",
            command=self.fade_out,
        ).pack(side="left", padx=(0, 10))
        ttk.Button(
            fade_controls,
            text="Fade In",
            style="Animated.TButton",
            command=self.fade_in,
        ).pack(side="left")

    # Animation methods
    def start_progress_animation(self):
        if not self.animation_running:
            self.animation_running = True
            threading.Thread(target=self._animate_progress, daemon=True).start()

    def _animate_progress(self):
        while self.animation_running and self.progress_value < 100:
            self.progress_value += 1
            self.progress_bar["value"] = self.progress_value
            time.sleep(0.05)
        if self.progress_value >= 100:
            self.animation_running = False

    def stop_animation(self):
        self.animation_running = False

    def reset_progress(self):
        self.animation_running = False
        self.progress_value = 0
        self.progress_bar["value"] = 0

    def slide_in(self):
        threading.Thread(target=self._animate_slide_in, daemon=True).start()

    def _animate_slide_in(self):
        start_x = -300
        end_x = 0
        steps = 30
        for i in range(steps + 1):
            current_x = start_x + (end_x - start_x) * (i / steps)
            self.sliding_panel.place(x=current_x, y=0, width=320, height=95)
            time.sleep(0.02)

    def slide_out(self):
        threading.Thread(target=self._animate_slide_out, daemon=True).start()

    def _animate_slide_out(self):
        start_x = 0
        end_x = -300
        steps = 30
        for i in range(steps + 1):
            current_x = start_x + (end_x - start_x) * (i / steps)
            self.sliding_panel.place(x=current_x, y=0, width=320, height=95)
            time.sleep(0.02)

    def fade_out(self):
        threading.Thread(target=self._animate_fade_out, daemon=True).start()

    def _animate_fade_out(self):
        steps = 20
        for i in range(steps + 1):
            alpha = 1.0 - (i / steps)
            if alpha < 0.5:
                for child in self.fade_content.winfo_children():
                    if hasattr(child, "configure"):
                        child.configure(state="disabled")
            time.sleep(0.05)
        self.fade_content.pack_forget()

    def fade_in(self):
        self.fade_content.pack(fill="both", expand=True, pady=(0, 10))
        threading.Thread(target=self._animate_fade_in, daemon=True).start()

    def _animate_fade_in(self):
        steps = 20
        for i in range(steps + 1):
            alpha = i / steps
            if alpha > 0.5:
                for child in self.fade_content.winfo_children():
                    if hasattr(child, "configure"):
                        try:
                            child.configure(state="normal")
                        except Exception:
                            pass
            time.sleep(0.05)

    def run(self):
        self.root.mainloop()


if __name__ == "__main__":
    app = AnimatedApp()
    app.run()
