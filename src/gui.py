import tkinter as tk
import time

from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

def createGui(bme280):
    
    fenster = tk.Tk()
    fenster.title("BME280 live measurement")
    fenster.geometry("1000x700")

    titel = tk.Label(
        fenster,
        text="BME280 live measurement",
        font=("Arial", 24)
    )

    titel.pack(pady=10)

    werte_frame = tk.Frame(fenster)
    werte_frame.pack(pady=5)


    temperatur_label = tk.Label(
        werte_frame,
        text="Temperatur: -- °C",
        font=("Arial", 16)
    )
    temperatur_label.grid(row=0, column=0, padx=20)


    druck_label = tk.Label(
        werte_frame,
        text="Luftdruck: -- hPa",
        font=("Arial", 16)
    )
    druck_label.grid(row=0, column=1, padx=20)


    feuchte_label = tk.Label(
        werte_frame,
        text="Luftfeuchtigkeit: -- %",
        font=("Arial", 16)
    )
    feuchte_label.grid(row=0, column=2, padx=20)

    startzeit = time.time()

    zeiten = []
    temperaturen = []
    druecke = []
    feuchten = []

    # Graph

    figur = Figure(figsize=(9, 5), dpi=100)

    ax = figur.add_subplot(111)

    ax.set_title("BME280 Messwerte")
    ax.set_xlabel("Zeit seit Programmstart (Sekunden)")
    ax.set_ylabel("Messwert")

    ax.grid(True)

    temperatur_linie, = ax.plot(
        [],
        [],
        label="Temperatur (°C)"
    )

    druck_linie, = ax.plot(
        [],
        [],
        label="Luftdruck (hPa)"
    )

    feuchte_linie, = ax.plot(
        [],
        [],
        label="Luftfeuchtigkeit (%)"
    )

    ax.legend()


    canvas = FigureCanvasTkAgg(
        figur,
        master=fenster
    )

    canvas.draw()

    canvas.get_tk_widget().pack(
        fill=tk.BOTH,
        expand=True,
        padx=20,
        pady=10
    )