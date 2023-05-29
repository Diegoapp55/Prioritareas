import datetime
import tkinter as tk

class Tarea:
    def __init__(self, descripcion, fecha, prioridad):
        self.descripcion = descripcion
        self.fecha = datetime.datetime.strptime(fecha, "%d/%m/%Y %H:%M")
        self.prioridad = prioridad
        self.hecha = False

    def __lt__(self, otra):
        return self.fecha < otra.fecha

class ColaPrioridad:
    def __init__(self):
        self._queue = []

    def agregar_tarea(self, tarea):
        i = 0
        while i < len(self._queue) and tarea.prioridad <= self._queue[i][1].prioridad:
            i += 1
        self._queue.insert(i, (tarea.prioridad, tarea))

    def siguiente_tarea(self):
        if len(self._queue) == 0:
            return None
        tarea = self._queue[0][1]
        if tarea.hecha:
            self._queue.pop(0)
            return self.siguiente_tarea()
        return tarea

cola = ColaPrioridad()

def agregar_tarea():
    descripcion = entrada_descripcion.get()
    fecha = entrada_fecha.get()
    prioridad = int(entrada_prioridad.get())
    tarea = Tarea(descripcion, fecha, prioridad)
    cola.agregar_tarea(tarea)
    entrada_descripcion.delete(0, tk.END)
    entrada_fecha.delete(0, tk.END)
    entrada_prioridad.delete(0, tk.END)
    mostrar_tareas()

def tarea_hecha():
    tarea = cola.siguiente_tarea()
    if tarea is not None:
        tarea.hecha = True
        mostrar_tareas()

def mostrar_tareas():
    tareas_pendientes = []
    for tarea in cola._queue:
        if not tarea[1].hecha:
            tareas_pendientes.append("- {} (Fecha: {}, Prioridad: {})".format(tarea[1].descripcion, tarea[1].fecha.strftime("%d/%m/%Y %H:%M"), tarea[1].prioridad))
    texto_tareas.set("\n".join(tareas_pendientes))

# Crear ventana
ventana = tk.Tk()
ventana.title("Gestor de tareas")

# Crear widgets
etiqueta_descripcion = tk.Label(ventana, text="Nombre:")
etiqueta_descripcion.config(font=("Arial", 12, "bold"), bg="#F2F2F2", fg="black", borderwidth=0, relief="solid")

entrada_descripcion = tk.Entry(ventana)
etiqueta_fecha = tk.Label(ventana, text="Deadline (dd/mm/yyyy hh:mm):")
entrada_fecha = tk.Entry(ventana)
etiqueta_prioridad = tk.Label(ventana, text="Prioridad (1-10):")
entrada_prioridad = tk.Entry(ventana)
boton_agregar = tk.Button(ventana, text="Guardar cambios", command=agregar_tarea)
boton_tarea_hecha = tk.Button(ventana, text="Tarea hecha", command=tarea_hecha)
texto_tareas = tk.StringVar()
etiqueta_tareas = tk.Label(ventana, text="Tareas pendientes:", font=("Arial", 12, "bold"))
texto_mostrar_tareas = tk.Label(ventana, textvariable=texto_tareas, justify=tk.LEFT)

# Ubicar widgets en la ventana
etiqueta_descripcion.grid(row=0, column=0)
entrada_descripcion.grid(row=0, column=1)
etiqueta_fecha.grid(row=1, column=0)
entrada_fecha.grid(row=1, column=1)
etiqueta_prioridad.grid(row=2, column=0,padx=10, pady=10)
entrada_prioridad.grid(row=2, column=1, padx=10, pady=10)
boton_agregar.grid(row=3, column=0, padx=10, pady=10)
boton_tarea_hecha.grid(row=3, column=1, padx=10, pady=10)
etiqueta_tareas.grid(row=4, column=0, padx=10, pady=10)
texto_mostrar_tareas.grid(row=5, column=0, columnspan=2, padx=10, pady=10)

# Iniciar bucle de eventos
ventana.mainloop()
