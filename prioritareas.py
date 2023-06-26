import heapq
import os
import csv
import datetime
import tkinter as tk
from tkinter import ttk, messagebox
from tkcalendar import Calendar
from PIL import ImageTk, Image
import tkinter.font as tkfont

class Tarea:
    def __init__(self, descripcion, fecha, prioridad, tiempo_estimado):
        self.descripcion = descripcion
        self.fecha = fecha
        self.prioridad = prioridad
        self.tiempo_estimado = tiempo_estimado

# Directorios para acceder a los archivos necesarios
carpeta_principal = os.path.dirname(__file__)
carpeta_imagenes = os.path.join(carpeta_principal, "icons")



    

def abrirSesion():
    Usuario = usuario.get()
    Clave = contrasena.get()
    with open("database/Usuario_Clave.csv", newline='') as archivo:
        lector_csv = csv.reader(archivo, delimiter=',')
        for row in lector_csv:
            x = ' '.join(row)
            lista_comparacion = x.split(";")
            if Usuario == lista_comparacion[0] and Clave == lista_comparacion[1]:  
                ventana_login.withdraw() 
                ventana_principal = tk.Toplevel(ventana_login)
                ventana_principal.title("Prioritareas - Inicio: "+ Usuario)
                ventana_principal.iconbitmap(os.path.join(carpeta_imagenes, "logo.ico"))


                # Configurar la fuente principal en la ventana principal
                ventana_principal.option_add("*Font", fuente_personalizada)


                # Configurar el color de fondo de la ventana
                ventana_principal.configure(bg="#cb2b23")  # Fondo rojo #cb2b23

                # Agregar espaciado alrededor de los elementos
                espaciado = 10

                # Lista de tareas
                tareas = []

                # Crear objeto de estilo
                estilo = ttk.Style()
                # Cargar estilos
                estilo.configure("Estilo.TButton", foreground="black", background="white")
                estilo.configure("Estilo.TButton", relief="solid")
                estilo.configure("Estilo.TButton", font=("Balsamiq Sans", 12), borderwidth=0, borderradius=15, padding=0)

                # Crear cuadro de texto y etiquetas para agregar tarea
                frame_agregar_tarea = tk.Frame(ventana_principal, background='#cb2b23')
                frame_agregar_tarea.pack(pady=espaciado)


                # Establecer el ancho del borde y el margen
                # borde_ancho = 2
                # margen = 5

                def ver_tareas():
                    if len(tareas) > 0:
                        tareas_ordenadas = sorted(tareas, key=lambda tarea: tarea.prioridad)
                        tarea_info = "\n".join(
                            [
                                f"Nombre: {t.descripcion}\nFecha: {t.fecha}\nPrioridad: {t.prioridad}\nTiempo Estimado (h): {t.tiempo_estimado}\n"
                                for t in tareas_ordenadas
                            ]
                        )
                        messagebox.showinfo("Tareas", tarea_info)
                    else:
                        messagebox.showinfo("Tareas", "No tienes tareas pendientes.")

                def editar_tarea():
                    tarea_seleccionada = lista_tareas.curselection()
                    if tarea_seleccionada:
                        tarea_index = tarea_seleccionada[0]
                        tarea = tareas[tarea_index]
                        ventana_editar = tk.Toplevel(ventana_principal)
                        ventana_editar.title("Editar Tarea")
                        ventana_editar.iconbitmap(os.path.join(carpeta_imagenes, "logo.ico"))
                        ventana_editar.geometry("400x300")  # Ajusta el tamaño de la ventana a 700x300 píxeles
                        ventana_editar.resizable(False, False)  # Desactiva la capacidad de redimensionar la ventana
                        ventana_editar.configure(bg="#cb2b23")

                        # Crear cuadros de texto y etiquetas para editar tarea
                        frame_editar_tarea = tk.Frame(ventana_editar)
                        frame_editar_tarea.pack(pady=16)

                        label_descripcion = tk.Label(frame_editar_tarea, text="Nombre:")
                        label_descripcion.grid(row=0, column=0)
                        cuadro_descripcion = tk.Entry(frame_editar_tarea)
                        cuadro_descripcion.grid(row=0, column=1)
                        cuadro_descripcion.insert(0, tarea.descripcion)

                        label_fecha = tk.Label(frame_editar_tarea, text="Fecha:")
                        label_fecha.grid(row=1, column=0)
                        cuadro_fecha = tk.Entry(frame_editar_tarea)
                        cuadro_fecha.grid(row=1, column=1)
                        cuadro_fecha.insert(0, tarea.fecha)

                        label_prioridad = tk.Label(frame_editar_tarea, text="Prioridad:")
                        label_prioridad.grid(row=2, column=0)
                        cuadro_prioridad = tk.Entry(frame_editar_tarea)
                        cuadro_prioridad.grid(row=2, column=1)
                        cuadro_prioridad.insert(0, tarea.prioridad)

                        label_tiempo_estimado = tk.Label(frame_editar_tarea, text="Tiempo Estimado (h): ")
                        label_tiempo_estimado.grid(row=3, column=0)
                        cuadro_tiempo_estimado = tk.Entry(frame_editar_tarea)
                        cuadro_tiempo_estimado.grid(row=3, column=1)
                        cuadro_tiempo_estimado.insert(0, tarea.tiempo_estimado)

                        def guardar_cambios():
                            nueva_descripcion = cuadro_descripcion.get()
                            nueva_fecha = cuadro_fecha.get()
                            nueva_prioridad = cuadro_prioridad.get()
                            nuevo_tiempo_estimado = cuadro_tiempo_estimado.get()

                            if nueva_descripcion and nueva_fecha and nueva_prioridad and nuevo_tiempo_estimado:
                                tarea.descripcion = nueva_descripcion
                                tarea.fecha = nueva_fecha
                                tarea.prioridad = nueva_prioridad
                                tarea.tiempo_estimado = nuevo_tiempo_estimado

                                messagebox.showinfo("Editar Tarea", "Los cambios han sido guardados.")
                                ventana_editar.destroy()
                                actualizar_lista_tareas()
                            else:
                                messagebox.showerror("Error", "Por favor, completa todos los campos.")

                        def cancelar():
                            ventana_editar.destroy()

                        # Crear objeto de estilo
                        estilo = ttk.Style()
                        # Cargar estilos
                        estilo.configure("Estilo.TButton", foreground="black", background="white")
                        estilo.configure("Estilo.TButton", relief="solid")

                        # Aplicar los estilos a los botones
                        estilo.configure("Estilo.TButton", font=("Balsamiq Sans", 12), borderwidth=0, borderradius=15, padding=0, margen=0)

                        # Frame para los botones
                        frame_botones = tk.Frame(ventana_editar,background='#cb2b23')
                        frame_botones.pack(pady=12)

                        # Botón Guardar Cambios
                        boton_guardar = ttk.Button(frame_botones, text="Guardar Cambios", command=guardar_cambios, style="Estilo.TButton")
                        boton_guardar.pack(side="left", padx=12)

                        # Botón Cancelar
                        boton_cancelar = ttk.Button(frame_botones, text="Cancelar", command=cancelar, style="Estilo.TButton")
                        boton_cancelar.pack(side="left", padx=12)

                        # Centrar los botones en la ventana
                        ventana_editar.grid_columnconfigure(0, weight=1)

                def eliminar_tarea():
                    tarea_seleccionada = lista_tareas.curselection()
                    if tarea_seleccionada:
                        tarea_index = tarea_seleccionada[0]
                        tarea = tareas[tarea_index]
                        respuesta = messagebox.askyesno("Eliminar Tarea", f"¿Estás seguro de eliminar la tarea: {tarea.descripcion}?")
                        if respuesta:
                            tareas.pop(tarea_index)
                            messagebox.showinfo("Eliminar Tarea", "La tarea ha sido eliminada.")
                            actualizar_lista_tareas()

                def tarea_terminada():
                    if len(tareas) > 0:
                        tarea_terminada = heapq.nlargest(1, tareas, key=lambda tarea: int(tarea.prioridad))[0]
                        tareas.remove(tarea_terminada)
                        messagebox.showinfo("Tarea Terminada", f"La tarea '{tarea_terminada.descripcion}' con prioridad {tarea_terminada.prioridad} ha sido completada.")
                        actualizar_lista_tareas()
                    else:
                        messagebox.showinfo("Tarea Terminada", "No hay tareas para completar.")

                def agregar_tarea():
                    descripcion = cuadro_descripcion.get()
                    fecha = cuadro_fecha.get()
                    prioridad = cuadro_prioridad.get()
                    tiempo_estimado= cuadro_tiempo_estimado.get()
                    if(prioridad is not None and int(prioridad) <= 10 and int(prioridad) >= 1):
                        if descripcion and fecha and prioridad:
                            nueva_tarea = Tarea(descripcion, fecha, prioridad,tiempo_estimado)
                            tareas.append(nueva_tarea)
                            actualizar_lista_tareas()
                            messagebox.showinfo("Agregar Tarea", "La tarea ha sido agregada.")
                            cuadro_descripcion.delete(0, tk.END)
                            cuadro_fecha.delete(0, tk.END)
                            cuadro_prioridad.delete(0, tk.END)
                            cuadro_tiempo_estimado.delete(0, tk.END)
                        else:
                            messagebox.showerror("Error", "Por favor, completa todos los campos.")
                    else:
                        messagebox.showerror("Error", "La prioridad debe estar en un rango entre 1 y 10")

                def actualizar_lista_tareas():
                    lista_tareas.delete(0, tk.END)
                    for tarea in tareas:
                        lista_tareas.insert(tk.END, tarea.descripcion)

                def abrir_ventana_info():
                    tarea_seleccionada = lista_tareas.curselection()
                    if tarea_seleccionada:
                        tarea_index = tarea_seleccionada[0]
                        tarea = tareas[tarea_index]
                        ventana_info = tk.Toplevel(ventana_principal)
                        ventana_info.title("Información de Tarea")
                        ventana_info.iconbitmap(os.path.join(carpeta_imagenes, "logo.ico"))
                        label_descripcion = tk.Label(ventana_info, text="Nombre:")
                        label_descripcion.pack()
                        label_tarea = tk.Label(ventana_info, text=tarea.descripcion)
                        label_tarea.pack()
                        label_fecha = tk.Label(ventana_info, text="Fecha:")
                        label_fecha.pack()
                        label_fecha_tarea = tk.Label(ventana_info, text=tarea.fecha)
                        label_fecha_tarea.pack()
                        label_prioridad = tk.Label(ventana_info, text="Prioridad:")
                        label_prioridad.pack()
                        label_prioridad_tarea = tk.Label(ventana_info, text=tarea.prioridad)
                        label_prioridad_tarea.pack()

                def seleccionar_fecha(event=None):
                        def guardar_fecha():
                            fecha_seleccionada = calendar.selection_get()
                            cuadro_fecha.delete(0, tk.END)
                            cuadro_fecha.insert(0, fecha_seleccionada.strftime("%Y-%m-%d"))
                            ventana_calendar.destroy()

                        ventana_calendar = tk.Toplevel(ventana_principal)
                        ventana_calendar.title("Seleccionar Fecha")
                        ventana_calendar.iconbitmap(os.path.join(carpeta_imagenes, "logo.ico"))
                        calendar = Calendar(ventana_calendar, selectmode="day")
                        calendar.pack(pady=20)
                        boton_guardar_fecha = tk.Button(ventana_calendar, text="Guardar Fecha", command=guardar_fecha)
                        boton_guardar_fecha.pack()

                def cerrar_sesion():
                    ventana_principal.destroy()
                    ventana_login.deiconify()

                label_descripcion = tk.Label(frame_agregar_tarea, text="Nombre:",bg="#cb2b23", fg="#ffffff")
                label_descripcion.grid(row=0, column=0)

                estilo = ttk.Style()
                estilo.configure("Estilo.TEntry", borderwidth=1, padding=0, bordercolor="black")

                # Crear cuadro de texto
                cuadro_descripcion = ttk.Entry(frame_agregar_tarea, style="Estilo.TEntry")
                cuadro_descripcion.grid(row=0, column=1)

                label_fecha = tk.Label(frame_agregar_tarea, text="Fecha:", bg="#cb2b23", fg="#ffffff")
                label_fecha.grid(row=1, column=0)

                cuadro_fecha = ttk.Entry(frame_agregar_tarea, style="Estilo.TEntry")
                cuadro_fecha.grid(row=1, column=1)

                # Cargar la imagen del botón
                imagen_boton = Image.open("icons/dias-del-calendario.png")  # Reemplaza "ruta_de_la_imagen" con la ruta correcta de tu imagen
                imagen_boton = imagen_boton.resize((25, 25), Image.ANTIALIAS)  # Ajusta el tamaño de la imagen según tus preferencias
                imagen_boton = ImageTk.PhotoImage(imagen_boton)

                # Crear el widget Label con la imagen
                boton_seleccionar_fecha = tk.Label(frame_agregar_tarea, image=imagen_boton, bg="#cb2b23", cursor="hand2")
                boton_seleccionar_fecha.grid(row=1, column=2)

                # Asignar el evento de clic al widget Label
                boton_seleccionar_fecha.bind("<Button-1>", seleccionar_fecha)

                label_prioridad = tk.Label(frame_agregar_tarea, text="Prioridad:",bg="#cb2b23", fg="#ffffff")
                label_prioridad.grid(row=2, column=0)
                cuadro_prioridad = ttk.Entry(frame_agregar_tarea, style="Estilo.TEntry")
                cuadro_prioridad.grid(row=2, column=1)

                label_tiempo_estimado = tk.Label(frame_agregar_tarea, text="Tiempo Estimado (h): ",bg="#cb2b23", fg="#ffffff")
                label_tiempo_estimado.grid(row=3, column=0)
                cuadro_tiempo_estimado = ttk.Entry(frame_agregar_tarea, style="Estilo.TEntry")
                cuadro_tiempo_estimado.grid(row=3, column=1)

                boton_agregar = ttk.Button(frame_agregar_tarea, text="Agregar Tarea", command=agregar_tarea, style="Estilo.TButton")
                boton_agregar.grid(row=4, columnspan=3, pady=12)

                # Crear lista de tareas y scrollbar
                frame_lista_tareas = tk.Frame(ventana_principal)
                frame_lista_tareas.pack(pady=espaciado)

                scrollbar_tareas = tk.Scrollbar(frame_lista_tareas)
                scrollbar_tareas.pack(side=tk.RIGHT, fill=tk.Y)

                lista_tareas = tk.Listbox(frame_lista_tareas, yscrollcommand=scrollbar_tareas.set)
                lista_tareas.pack(side=tk.LEFT, fill=tk.BOTH)

                scrollbar_tareas.config(command=lista_tareas.yview)

                # Agregar tareas iniciales
                # tareas.append(Tarea("Tarea con prioridad 5", "2023-06-26", "5",10))
                # tareas.append(Tarea("Tarea con prioridad 10", "2023-06-26", "10",4))
                # tareas.append(Tarea("Tarea con prioridad 3", "2023-06-26", "3",3))

                # Actualizar lista de tareas
                actualizar_lista_tareas()

                # Botones
                frame_botones = tk.Frame(ventana_principal)
                frame_botones.pack(pady=espaciado)

                boton_ver_tareas = tk.Button(frame_botones, text="Ver Tareas", command=ver_tareas)
                boton_ver_tareas.pack(side=tk.LEFT)

                boton_editar_tarea = tk.Button(frame_botones, text="Editar Tarea", command=editar_tarea)
                boton_editar_tarea.pack(side=tk.LEFT)

                boton_eliminar_tarea = tk.Button(frame_botones, text="Eliminar Tarea", command=eliminar_tarea)
                boton_eliminar_tarea.pack(side=tk.LEFT)

                boton_tarea_terminada = tk.Button(frame_botones, text="Tarea Terminada", command=tarea_terminada)
                boton_tarea_terminada.pack(side=tk.LEFT)

                boton_abrir_info = tk.Button(frame_botones, text="Abrir Información", command=abrir_ventana_info)
                boton_abrir_info.pack(side=tk.LEFT)

                boton_abrir_info = tk.Button(frame_botones, text="Cerrar Sesión", command=cerrar_sesion)
                boton_abrir_info.pack(side=tk.LEFT)
                break
            else:
                pass
        if Usuario != lista_comparacion[0] or Clave != lista_comparacion[1]:
            messagebox.showwarning('Error', 'Usuario o contraseña incorrectos')
        else:
            pass

def crearCuenta():
    ventana_login.withdraw()
    ventanaSecundaria = tk.Toplevel(ventana_login)
    ventanaSecundaria.title("Prioritareas - Crear Cuenta")
    ventanaSecundaria.iconbitmap(os.path.join(carpeta_imagenes, "logo.ico"))
    
    tk.Label(ventanaSecundaria, text="Nueva Cuenta", font=fuente_Titulo).grid(row=0,column=0,columnspan=2,padx=80)
    # Campos de texto
    # Usuario
    tk.Label(ventanaSecundaria, text="Usuario", font=fuente_personalizada).grid(row=1,column=0)
    Usuario = tk.Entry(ventanaSecundaria)
    Usuario.grid(row=1,column=1)

    # Contraseña
    tk.Label(ventanaSecundaria, text="Contraseña", font=fuente_personalizada).grid(row=2,column=0)
    Clave = tk.Entry(ventanaSecundaria)
    Clave.grid(row=2,column=1)
    def crearUsuario():
        try:
            try:
                open("database/Usuario_Clave.csv", "r")
                f = open("database/Usuario_Clave.csv", "a+")
                f.write(Usuario.get()+";"+Clave.get()+"\n")
            except:
                f = open("database/Usuario_Clave.csv", "w")
                f.write(Usuario.get()+";"+Clave.get()+"\n")
                f.close()
        except:
            print("El archivo que se intenta abrir no existe, reintente")
        messagebox.showinfo('Confirmación', 'Se ha creado el usuario satisfactoriamente')
        ventanaSecundaria.destroy()
        ventana_login.deiconify()
    # Botones
    Continuar = tk.Button(ventanaSecundaria, text="Continuar", font=fuente_personalizada, command=crearUsuario).grid(row=3,column=0,columnspan=2)

# Crear ventana login
ventana_login = tk.Tk()
ventana_login.title("Prioritareas - Iniciar Sesión")
ventana_login.iconbitmap(os.path.join(carpeta_imagenes, "logo.ico"))

# Cargar la fuente personalizada
fuente_personalizada = tkfont.Font(family="Balsamiq Sans", size=12)  # Reemplaza "NombreFuente" por el nombre de tu fuente
fuente_Titulo = tkfont.Font(family="Balsamiq Sans", size=20)

tk.Label(ventana_login, text="Bienvenid@ a Prioritareas", font=fuente_Titulo).grid(row=0,column=0,columnspan=2)
# Campos de texto
# Usuario
tk.Label(ventana_login, text="Usuario", font=fuente_personalizada).grid(row=1,column=0)
usuario = tk.Entry(ventana_login)
usuario.grid(row=1,column=1)

# Contraseña
tk.Label(ventana_login, text="Contraseña", font=fuente_personalizada).grid(row=2,column=0)
contrasena = tk.Entry(ventana_login)
contrasena.grid(row=2,column=1)

# Botones
continuar = tk.Button(ventana_login, text="Continuar", font=fuente_personalizada, command=abrirSesion).grid(row=3,column=0)
nuevaCuenta = tk.Button(ventana_login, text="Crear Cuenta", font=fuente_personalizada, command=crearCuenta).grid(row=3,column=1)

# Ejecutar la ventana principal
ventana_login.mainloop()