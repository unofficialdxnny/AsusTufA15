import tkinter as tk
import asusctl

class App(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.label = tk.Label(self, text="ASUS TUF A15 Control Panel")
        self.label.pack()

        self.fan_frame = tk.Frame(self)
        self.fan_frame.pack()
        self.fan_label = tk.Label(self.fan_frame, text="Fan Speed:")
        self.fan_label.pack(side=tk.LEFT)
        self.fan_slider = tk.Scale(self.fan_frame, from_=0, to=100, orient=tk.HORIZONTAL)
        self.fan_slider.pack(side=tk.LEFT)
        self.fan_apply_button = tk.Button(self.fan_frame, text="Apply", command=self.apply_fan_settings)
        self.fan_apply_button.pack(side=tk.LEFT)

        self.kb_frame = tk.Frame(self)
        self.kb_frame.pack()
        self.kb_enabled_var = tk.BooleanVar()
        self.kb_enabled_var.set(False)
        self.kb_enabled_checkbox = tk.Checkbutton(self.kb_frame, text="Keyboard Backlight Enabled", variable=self.kb_enabled_var)
        self.kb_enabled_checkbox.pack()
        self.kb_brightness_label = tk.Label(self.kb_frame, text="Keyboard Brightness:")
        self.kb_brightness_label.pack(side=tk.LEFT)
        self.kb_brightness_slider = tk.Scale(self.kb_frame, from_=0, to=3, orient=tk.HORIZONTAL)
        self.kb_brightness_slider.pack(side=tk.LEFT)
        self.kb_apply_button = tk.Button(self.kb_frame, text="Apply", command=self.apply_kb_settings)
        self.kb_apply_button.pack(side=tk.LEFT)

    def apply_fan_settings(self):
        fan_speed = self.fan_slider.get()
        asusctl.set_fan_speed(fan_speed)

    def apply_kb_settings(self):
        kb_enabled = self.kb_enabled_var.get()
        kb_brightness = self.kb_brightness_slider.get()
        asusctl.set_keyboard_backlight(kb_enabled, kb_brightness)

root = tk.Tk()
app = App(root)
app.mainloop()
