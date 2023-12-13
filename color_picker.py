import tkinter as tk
from tkinter import ttk

import colorsys

class ColorPickerApp:
    def __init__(self, window):
        self.master = window #finestra principale

        self.rect = tk.Canvas(window, width=200, height=100) #crea un rettangolo, tk.Canvs --> crea area disegnabile
        self.rect.pack(pady=10) #top padding

        self.rgb_frame = ttk.Frame(window) #crea un'immagine RGB
        self.rgb_frame.pack(pady=10)

        self.rgb_sliders = self.create_sliders(self.rgb_frame, "RGB", 0, 255) #chiama la funzione create_sliders per creare gli slider RGB

        self.update_color()

    def create_sliders(self, parent, color_space, min_val, max_val): #crea gli slider

        sliders = [] #lista degli slider

        for i, channel in enumerate(color_space):

            label = ttk.Label(parent, text=f"{channel}:") #crea un'etichettà per ogni slider
            label.grid(row=i, column=0, padx=5)

            slider_var = tk.DoubleVar() #crea una variabile per ogni slider
            slider = ttk.Scale(parent, from_=min_val, to=max_val, orient=tk.HORIZONTAL, length=200, variable=slider_var, command=self.update_color)
            slider.grid(row=i, column=1, padx=5)

            sliders.append(slider_var) #aggiunge la variabile alla lista degli slider

        return sliders

    def update_color(self, event=None): #aggiorna il colore del rettangolo

        #crea una lista con i valori degli slider
        rgb_values = []
        for slider in self.rgb_sliders:
            rgb_values.append(int(slider.get()))

        #Conversione dei tre canali RGB da decimale ad esadecimale
        hex_color = "#"
        for i in rgb_values:
            hex_color += f"{i:02X}" #aggiunge alla stringa il valore esadecimale di ogni canale RGB (con due cifre) 

        self.rect.configure(bg=hex_color) #aggiorna il colore del rettangolo

        self.master.title(str(hex_color)) #aggiorna il titolo della finestra con il codide esadecimale del colore

root = tk.Tk() #crea la finestra
app = ColorPickerApp(root) #crea un'istanza di ColorPickerApp
root.mainloop() #aggiorna continuamente la finestra
