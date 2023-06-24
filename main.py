import heapq
import datetime
import tkinter as tk
from tkinter import ttk
from tkcalendar import Calendar
from PIL import ImageTk, Image
from tkinter import font


class Tarea:
    def __init__(self, descripcion, fecha, prioridad):
        self.descripcion = descripcion
        self.fecha = datetime.datetime.strptime(fecha, "%d/%m/%Y")
        self.prioridad = prioridad

    def __lt__(self, otra):
        return self.fecha < otra.fecha


class ColaPrioridad:
    def __init__(self):
        self._queue = []

    def agregar_tarea(self, tarea):
        heapq.heappush(self._queue, (tarea.prioridad, tarea))

    def siguiente_tarea(self):
        if len(self._queue) == 0:
            return None
        return heapq.heappop(self._queue)[1]

    def eliminar_tarea(self):
        self._queue.sort()  # Ordenar por prioridad
        tarea_eliminar = self._queue.pop()  # Eliminar la tarea de mayor prioridad
        return tarea_eliminar


def agregar_tarea():
    descripcion = entrada_descripcion.get()
    fecha = entrada_fecha.get()
    prioridad = int(combo_prioridad.get())
    tarea = Tarea(descripcion, fecha, prioridad)
    cola.agregar_tarea(tarea)
    entrada_descripcion.delete(0, tk.END)
    entrada_fecha.delete(0, tk.END)
    combo_prioridad.set("")  # Limpiar la selección
    mostrar_tareas()


def eliminar_tarea():
    tarea_eliminar = cola.eliminar_tarea()
    if tarea_eliminar:
        mostrar_tareas()


def mostrar_tareas():
    tareas_pendientes = []
    for _, tarea in cola._queue:
        tareas_pendientes.append(
            "- {} (Fecha: {}, Prioridad: {})".format(
                tarea.descripcion,
                tarea.fecha.strftime("%d/%m/%Y"),
                tarea.prioridad
            )
        )
    texto_tareas.set("\n".join(tareas_pendientes))


cola = ColaPrioridad()

# Crear ventana
ventana = tk.Tk()
ventana.title("Prioritareas")
ventana.configure(bg="#cb2b23")  # Fondo rojo #cb2b23

# Fuente personalizada
fuente_personalizada = font.Font(family="UntitledTTF.ttf", size=12)

# Estilo para los widgets
estilo = ttk.Style()
estilo.configure(
    "Estilo.TLabel",
    background="#cb2b23",
    foreground="black",
    font=fuente_personalizada
)
estilo.configure(
    "Estilo.TButton",
    background="#cb2b23",
    foreground="black",
    font=fuente_personalizada,
    borderwidth=0,
    relief="solid",
    padding=5
)
estilo.configure(
    "Estilo.TCombobox",
    background="white",
    foreground="black",
    font=fuente_personalizada
)

# Crear widgets
etiqueta_descripcion = ttk.Label(
    ventana,
    text="Nombre de la tarea:",
    style="Estilo.TLabel"
)
entrada_descripcion = ttk.Entry(ventana)
etiqueta_fecha = ttk.Label(
    ventana,
    text="Deadline:",
    style="Estilo.TLabel"
)
entrada_fecha = ttk.Entry(ventana)
logo_calendario = ImageTk.PhotoImage(
    Image.open("dias-del-calendario.png").resize((20, 20))
)  # Ajusta el tamaño según tus necesidades
boton_fecha = ttk.Button(ventana, image=logo_calendario, compound="left")
etiqueta_prioridad = ttk.Label(
    ventana,
    text="Prioridad:",
    style="Estilo.TLabel"
)
combo_prioridad = ttk.Combobox(
    ventana,
    values=list(range(1, 11)),
    style="Estilo.TCombobox"
)
boton_agregar = ttk.Button(
    ventana,
    text="Agregar tarea",
    command=agregar_tarea,
    style="Estilo.TButton"
)
boton_cancelar = ttk.Button(
    ventana,
    text="Cancelar",
    style="Estilo.TButton"
)
boton_eliminar = ttk.Button(
    ventana,
    text="Tarea hecha",
    command=eliminar_tarea,
    style="Estilo.TButton"
)
boton_eliminar.grid(row=3, column=2, padx=10, pady=10)
texto_tareas = tk.StringVar()
etiqueta_tareas = ttk.Label(
    ventana,
    text="Tareas pendientes:",
    style="Estilo.TLabel"
)
texto_mostrar_tareas = ttk.Label(
    ventana,
    textvariable=texto_tareas,
    justify=tk.LEFT,
    wraplength=300
)

# Ubicar widgets en la ventana
etiqueta_descripcion.grid(row=0, column=0, padx=10, pady=5)
entrada_descripcion.grid(row=0, column=1, padx=10, pady=5)
etiqueta_fecha.grid(row=1, column=0, padx=10, pady=5)
entrada_fecha.grid(row=1, column=1, padx=10, pady=5)
boton_fecha.grid(row=1, column=2, padx=5, pady=5)
etiqueta_prioridad.grid(row=2, column=0, padx=10, pady=5)
combo_prioridad.grid(row=2, column=1, padx=10, pady=5)
boton_agregar.grid(row=3, column=0, padx=10, pady=10)
boton_cancelar.grid(row=3, column=1, padx=10, pady=10)
etiqueta_tareas.grid(row=4, column=0, columnspan=2, padx=10, pady=5)
texto_mostrar_tareas.grid(row=5, column=0, columnspan=2, padx=10, pady=5)


# Función para abrir el calendario
def abrir_calendario():
    def seleccionar_fecha():
        fecha_seleccionada = cal.selection_get()
        entrada_fecha.delete(0, tk.END)
        entrada_fecha.insert(tk.END, fecha_seleccionada.strftime("%d/%m/%Y"))
        ventana_calendario.destroy()

    ventana_calendario = tk.Toplevel(ventana)
    cal = Calendar(ventana_calendario, selectmode="day")
    cal.pack(pady=10)
    boton_seleccionar = ttk.Button(
        ventana_calendario,
        text="Seleccionar fecha",
        command=seleccionar_fecha
    )
    boton_seleccionar.pack(pady=10)


boton_fecha.configure(command=abrir_calendario)

ventana.mainloop()
