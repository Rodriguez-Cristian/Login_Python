from tkinter import *
from tkinter import messagebox
import ttkbootstrap as tb
import sqlite3 #conector de base de datos https://pypi.org/project/db-sqlite3/
import hashlib #libreria para encrimpar contraseña https://pypi.org/project/micropython-hashlib3/

"""
https://sqlitebrowser.org/ 
De esta pagina pueden bajar SqLite
"""
class Ventana(tb.Window): # esta es de ttkbostrap x eso es windows
    def __init__(self):#método se llama automáticamente cuando se crea un nuevo objeto de esta clase.
        super().__init__()#herencia de clases en Python.
        self.ventana_login()#ventana inicial
    
    #---Ventanas que voy a usar---
    
    #centra las ventanas
    def centrar_ventana(self,ventana,ancho,alto):
        #obtener las dimensiones de la pantalla
        pantalla_ancho = self.winfo_screenwidth()
        pantalla_alto = self.winfo_screenheight()
        
        #calcular las coordenadas para centrar ventana
        x = (pantalla_ancho - ancho) // 2
        y = (pantalla_alto - alto) // 2
        
        #establecer las coordenadas de la ventana
        ventana.geometry(f"{ancho}x{alto}+{x}+{y}") 
        #pongo el icono en las ventanas 
        ventana.iconbitmap("login.ico")
    #ventana de login
    def ventana_login(self):
        def ver_clave():
        # Función para alternar la visibilidad de la clave
            if self.ent_clave.cget("show") == "*":
                # Si la clave se está mostrando, ocultarla con asteriscos
               self.ent_clave.config(show="")
            else:
                # Si la clave está oculta con asteriscos, mostrarla como texto normal
               self.ent_clave.config(show="*")
        #configuro la columna de la grilla
        self.grid_columnconfigure(1,weight=1)
        #armo la pantalla
        self.frame_login=Frame(master=self)
        self.frame_login.grid(row=0,column=1,sticky=NSEW)
        
        lblframe_login=tb.LabelFrame(master=self.frame_login,text='Acceso')
        lblframe_login.pack(padx=10,pady=35)
        
        #coloco una imagen en este caso la de goku =)
        imagen = PhotoImage(file="Goku.png")  # Cambia la ruta por la ubicación de tu imagen
        imagen = imagen.subsample(3)  # Redimensiona la imagen 
        lbl_imagen = Label(lblframe_login, image=imagen)#lbl de tipo imagen
        lbl_imagen.image = imagen  # Para evitar que la imagen se elimine por el recolector de basura
        lbl_imagen.pack()#lo empaqueto
        
        lblframe_titulo=tb.Label(master=lblframe_login,text='Goku Sesion',font=('Calibri',18,'bold'))
        lblframe_titulo.pack(padx=10,pady=35)
        
        #campo para ingresar el usuario
        self.ent_usuario= tb.Entry(master=lblframe_login,width=40,justify=CENTER)
        self.ent_usuario.pack(padx=10,pady=10)
        #campo para ingresar la clave
        self.ent_clave= tb.Entry(master=lblframe_login,width=40,justify=CENTER)
        self.ent_clave.pack(padx=10,pady=10)
        self.ent_clave.config(show='*')#para que no se vea la clave
        self.ent_clave.bind('<Return>', self.logueo_usuarios)#para que luego de la clave funcione el enter
        #boton para mostrar clave
        btn_mostrar_clave = tb.Button(master=lblframe_login, text='👀',bootstyle='light', command=ver_clave)
        btn_mostrar_clave.pack()
        #boton de acceso
        btn_acceso= tb.Button(master=lblframe_login,width=38,text='Ingresar',bootstyle = 'success',command=self.logueo_usuarios)
        btn_acceso.pack(padx=10,pady=10)
        #boton para registrarse
        btn_registrarse= tb.Button(master=lblframe_login,width=38,text='Registrarse',bootstyle = 'info',command=self.ventana_nuevo_usuario)
        btn_registrarse.pack(padx=10,pady=10)
        #coloco el focus en el usuario
        self.ent_usuario.focus()    
    #ventana de nuevo usuario
    def ventana_nuevo_usuario(self):
        def mostrar_clave():
        # Función para alternar la visibilidad de la clave
            if  self.ent_clave_nuevo_usuario.cget("show") == "*":
                # Si la clave se está mostrando, ocultarla con asteriscos
                self.ent_clave_nuevo_usuario.config(show="")
            else:
                # Si la clave está oculta con asteriscos, mostrarla como texto normal
                self.ent_clave_nuevo_usuario.config(show="*")
                 
        #Toplevel pone la ventana por encima del usuario
        self.frame_nuevo_usuario=Toplevel(master=self)
        self.frame_nuevo_usuario.title('Nuevo Usuario')
        self.centrar_ventana(self.frame_nuevo_usuario,550,380)
        self.frame_nuevo_usuario.grab_set() #es para que no se pueda realizar ninguna accion hasta que no se cierre la ventana
        
        #CAMPOS DE NUEVOS DATOS
        
        lblframe_nuevo_usuario = tb.LabelFrame(master=self.frame_nuevo_usuario,text='Nuevo Usuario')
        lblframe_nuevo_usuario.pack(padx=15,pady=35)     
        #campos de codigo  
        lbl_codigo_nuevo_usuario = Label(master=lblframe_nuevo_usuario,text='Codigo')
        lbl_codigo_nuevo_usuario.grid(row=0,column=0,padx=10,pady=10)
        self.ent_codigo_nuevo_usuario = tb.Entry(master=lblframe_nuevo_usuario,width=40)
        self.ent_codigo_nuevo_usuario.grid(row=0,column=1,padx=10,pady=10)
        #campos de nombre
        lbl_nombre_nuevo_usuario = Label(master=lblframe_nuevo_usuario,text='Nombre')
        lbl_nombre_nuevo_usuario.grid(row=1,column=0,padx=10,pady=10)
        self.ent_nombre_nuevo_usuario = tb.Entry(master=lblframe_nuevo_usuario,width=40)
        self.ent_nombre_nuevo_usuario.grid(row=1,column=1,padx=10,pady=10)
        #campos de clave
        lbl_clave_nuevo_usuario = Label(master=lblframe_nuevo_usuario,text='Clave')
        lbl_clave_nuevo_usuario.grid(row=2,column=0,padx=10,pady=10)
        self.ent_clave_nuevo_usuario = tb.Entry(master=lblframe_nuevo_usuario,width=40)
        self.ent_clave_nuevo_usuario.grid(row=2,column=1,padx=10,pady=10)
        self.ent_clave_nuevo_usuario.config(show='*')
        #boton para mostrar la clave
        btn_mostrar_clave = tb.Button(master=lblframe_nuevo_usuario, text='👀',bootstyle='light', command=mostrar_clave)
        btn_mostrar_clave.grid(row=2, column=2, padx=10, pady=10)
        #boton para guardar datos
        btn_guardar_usuario=tb.Button(master=lblframe_nuevo_usuario,text='Guardar',width=38,bootstyle='success',command=self.guardar_usuario)
        btn_guardar_usuario.grid(row=3,column=1,padx=10,pady=10)
        #traigo el correlativo del codigo
        self.correlativo_usuarios()
        #pongo el focus en el nombre del usuario
        self.ent_nombre_nuevo_usuario.focus()
    #ventana de cambio de clave
    def ventana_cambio_de_clave(self, nombre_usuario):
        try:
            def visibilidad_Password():
                if  self.ent_clave_cambiar_contrasenia.cget("show") == "*":
                    self.ent_clave_cambiar_contrasenia.config(show="")
                else:
                    self.ent_clave_cambiar_contrasenia.config(show="*")
                
                if  self.ent_clave_cambiar_contrasenia2.cget("show") == "*":
                    self.ent_clave_cambiar_contrasenia2.config(show="")
                else:
                    self.ent_clave_cambiar_contrasenia2.config(show="*")
                    
            def validar_contrasenias(event=None):
                # Función para validar si las contraseñas son iguales y habilitar/deshabilitar el botón modificar
                clave1 = self.ent_clave_cambiar_contrasenia.get()
                clave2 = self.ent_clave_cambiar_contrasenia2.get()
                if clave1 != '' and clave2 != '':
                    if clave1 == clave2:
                        btn_cambiar_contrasenia.config(state="normal")
                    else:
                        btn_cambiar_contrasenia.config(state="disabled")
                        
            #Toplevel pone la ventana por encima del usuario
            self.frame_cambiar_contrasenia=Toplevel(self)
            self.frame_cambiar_contrasenia.title('Cambiar Contraseña')
            self.centrar_ventana(self.frame_cambiar_contrasenia,550,350)
            self.frame_cambiar_contrasenia.grab_set()#es para que no se pueda realizar nada sin cerrar esta ventana
            
            #Campos de datos
            lblframe_cambiar_contrasenia = tb.LabelFrame(master=self.frame_cambiar_contrasenia,text='Modificar Usuario')
            lblframe_cambiar_contrasenia.pack(padx=15,pady=30)
                      
            lbl_nombre_cambiar_contrasenia = Label(master=lblframe_cambiar_contrasenia,text='Nombre')
            lbl_nombre_cambiar_contrasenia.grid(row=1,column=0,padx=10,pady=10)
            self.ent_nombre_cambiar_contrasenia = tb.Entry(master=lblframe_cambiar_contrasenia,width=40)
            self.ent_nombre_cambiar_contrasenia.insert(0, nombre_usuario)  # Insertar el nombre de usuario
            self.ent_nombre_cambiar_contrasenia.config(state='disabled')
            self.ent_nombre_cambiar_contrasenia.grid(row=1,column=1,padx=10,pady=10)
            
            lbl_clave_cambiar_contrasenia = Label(master=lblframe_cambiar_contrasenia,text='Clave')
            lbl_clave_cambiar_contrasenia.grid(row=2,column=0,padx=10,pady=10)
            self.ent_clave_cambiar_contrasenia = tb.Entry(master=lblframe_cambiar_contrasenia,width=40)
            self.ent_clave_cambiar_contrasenia.grid(row=2,column=1,padx=10,pady=10)
            self.ent_clave_cambiar_contrasenia.config(show='*')
            
            lbl_clave_cambiar_contrasenia2 = Label(master=lblframe_cambiar_contrasenia,text='Repetir Clave')
            lbl_clave_cambiar_contrasenia2.grid(row=3,column=0,padx=10,pady=10)
            self.ent_clave_cambiar_contrasenia2 = tb.Entry(master=lblframe_cambiar_contrasenia,width=40)
            self.ent_clave_cambiar_contrasenia2.grid(row=3,column=1,padx=10,pady=10)
            self.ent_clave_cambiar_contrasenia2.config(show='*')
            btn_mostrar_cambiar_contrasenia2 = tb.Button(master=lblframe_cambiar_contrasenia, text='👀',bootstyle='light"', command=visibilidad_Password)
            btn_mostrar_cambiar_contrasenia2.grid(row=3, column=2, padx=10, pady=10)
                            
            btn_cambiar_contrasenia=tb.Button(master=lblframe_cambiar_contrasenia,text='Cambiar Contraseña',width=38,bootstyle='warning',command=self.modificar_contrasenia)
            btn_cambiar_contrasenia.grid(row=4,column=1,padx=10,pady=10)
            btn_cambiar_contrasenia.config(state="disabled")  # Inicialmente deshabilitado
            
            # Vincular la validación al evento de cambio en los campos de entrada
            self.ent_clave_cambiar_contrasenia2.bind("<KeyRelease>", validar_contrasenias)
            self.ent_clave_cambiar_contrasenia.bind("<KeyRelease>", validar_contrasenias) 
        except Exception as e:
            messagebox.showerror("Ventan Modificar Contraseña", f"Ocurrió un error: {e}")  
    
    #---Acciones---
    #loguearme
    def logueo_usuarios(self,event=None):
        try:
            #Conectar a la base de datos
            mi_conexion=sqlite3.connect('Login.db')#ruta de la bd
            #creamos el cursor
            mi_cursor = mi_conexion.cursor() 
            
            con_usuario = self.ent_usuario.get()
            con_clave = self.encriptar_contrasenia(self.ent_clave.get())
            
            #Paso la consulta
            mi_cursor.execute("SELECT * FROM Usuarios WHERE Nombre=? AND Clave = ?",(con_usuario,con_clave))
            
            self.datos_logueo=mi_cursor.fetchall()
        
            if self.datos_logueo !='':
                for fila in self.datos_logueo:
                    self.codigo_usuario_logueado=fila[0]
                    self.nombre_usuario_logueado = fila[1] #obtengo  el usuario
                    clave_usuario_logueado = fila[2] #obtengo la clave
                    self.cambiar_clave =  fila[3] 
                                       
                #Si ya esta registrado y no es su primera vez que ingresa   
                if (self.nombre_usuario_logueado == self.ent_usuario.get() and
                    clave_usuario_logueado == self.encriptar_contrasenia(self.ent_clave.get()) and
                    self.cambiar_clave == 'NO'):   
                        messagebox.showwarning('Logueo','BIENVENIDO A INGRESADO AL SISTEMA')
                        self.frame_login.destroy()
                        quit()#cierro pero aca va en si la llamada al evento que sea necesario
                else:
                    #es la primera vez que ingresa por lo cual necesita cambiar su contraseña
                    if (self.nombre_usuario_logueado == self.ent_usuario.get() and
                    clave_usuario_logueado == self.encriptar_contrasenia(self.ent_clave.get()) and
                    self.cambiar_clave == 'SI'): 
                        self.ventana_cambio_de_clave(self.nombre_usuario_logueado)    

            #aplicar cambios
            mi_conexion.commit()
            #cerrar la conexion
            mi_conexion.close()
        except Exception as e:
            messagebox.showwarning('Error Logueo','El Usuario o Clave son Incorrectas - ¡Revisar!') 
    #encriptar contraseñas
    def encriptar_contrasenia(self, contraseña):
        # Utilizar hashlib para generar un hash seguro de la contraseña
        hashed_password = hashlib.sha256(contraseña.encode()).hexdigest()
        return hashed_password  
    #modificar la contraseña inicial
    def modificar_contrasenia(self):
        if self.ent_clave_cambiar_contrasenia.get() != self.ent_clave_cambiar_contrasenia2.get():
            messagebox.showerror("Modificar Contraseña", "Las contraseñas no coinciden")
            return
    
        if self.ent_nombre_cambiar_contrasenia.get() == '':
            messagebox.showerror("Modificar Contraseña", "El campo de nombre de usuario no puede estar vacío")
            return
    
        try:
            # Conectar a la base de datos
            mi_conexion = sqlite3.connect('Login.db')  # Ruta de la bd
            # Creamos el cursor
            mi_cursor = mi_conexion.cursor() 
            
            # Construir la tupla de datos a modificar
            clave_encriptada = self.encriptar_contrasenia( self.ent_clave_cambiar_contrasenia.get())
            
            # Ejecutar la consulta de actualización
            
            mi_cursor.execute("UPDATE Usuarios SET Clave=?, CambiarClave = 'NO' WHERE Cod=?",(clave_encriptada, self.codigo_usuario_logueado))
            
            # Aplicar cambios
            mi_conexion.commit()
            
            messagebox.showinfo("Modificar Contraseña", "¡Contraseña modificada correctamente!")
            
            # Cerrar la conexión
            mi_conexion.close()
        except Exception as e:
            messagebox.showerror("Modificar Contraseña", f"Ocurrió un error: {e}")
        #rompo la pantalla para que se cierre    
        self.frame_cambiar_contrasenia.destroy()  
    #un correlativo para los cod (id)
    def correlativo_usuarios(self):   
        try:
            #Conectar a la base de datos
            mi_conexion=sqlite3.connect('Login.db')#ruta de la bd
            #creamos el cursor
            mi_cursor = mi_conexion.cursor() 
            #Consulta
            mi_cursor.execute("SELECT MAX(Cod) FROM Usuarios")
            correlativo_usuarios=mi_cursor.fetchone()
            for datos in correlativo_usuarios:
                if datos == None:
                    self.nuevo_correlativo_usuario = (int(1))
                    self.ent_codigo_nuevo_usuario.config(state=NORMAL)
                    self.ent_codigo_nuevo_usuario.insert(0,self.nuevo_correlativo_usuario)
                    self.ent_codigo_nuevo_usuario.config(state='readonly')
                else:
                    self.nuevo_correlativo_usuario = (int(datos)+1)
                    self.ent_codigo_nuevo_usuario.config(state=NORMAL)
                    self.ent_codigo_nuevo_usuario.insert(0,self.nuevo_correlativo_usuario)
                    self.ent_codigo_nuevo_usuario.config(state='readonly')
            mi_conexion.commit()
            #cerrar la conexion
            mi_conexion.close()
        except Exception as e:
            messagebox.showerror('Correlativo Usuarios',f'¡Ocurrió un Error!{e}')
    #guardado de usuario nuevo
    def guardar_usuario(self):
        
        if (self.ent_codigo_nuevo_usuario.get()==''or self.ent_nombre_nuevo_usuario.get()=='' or self.ent_clave_nuevo_usuario.get() ==''): 
            messagebox.showerror("Guardando Usuarios","Todos los campos deben estar llenos")
            return
        try:
            #Conectar a la base de datos
            mi_conexion=sqlite3.connect('Login.db')#ruta de la bd
            #creamos el cursor
            mi_cursor = mi_conexion.cursor() 
            
            clave_encriptada = self.encriptar_contrasenia(self.ent_clave_nuevo_usuario.get())
            guardar_datos_usuarios = (self.ent_codigo_nuevo_usuario.get(),
                                    self.ent_nombre_nuevo_usuario.get(),
                                    clave_encriptada,
                                    "SI")
            #Paso la consulta
            mi_cursor.execute("INSERT INTO Usuarios VALUES(?,?,?,?)",(guardar_datos_usuarios))
            
            #aplicar cambios
            mi_conexion.commit()
            
            messagebox.showinfo("Guardando Usuarios","¡Registro Guardado Correctamente!")
            self.frame_nuevo_usuario.destroy()
            #cerrar la conexion
            mi_conexion.close()
        except Exception as e:
            messagebox.showerror("Guardando Usuarios",f"Ocurrio un ERROR: {e}")
 
# Estructura y llamado   
def main():
    app=Ventana()
    app.title('Login')#Nombre de ventana
    app.iconbitmap("login.ico")#icono
    tb.Style('darkly')#En la pagina hay varios estilos! https://ttkbootstrap.readthedocs.io/en/latest/themes/light/
    app.mainloop()#loop para que no se cierre

if __name__ == '__main__': #ejecuto el main
    main()