from tkinter import *

from tkinter import messagebox
from tkinter import ttk
import time
import sqlite3
from tkinter import ttk

conexion = sqlite3.connect('final.db')


def ventanaPrincipal():
    ventana = Tk()
    ventana.config(bg= "#fec5bb")
    ventana.geometry("1200x680")



   # reloj

    labelHora = Label(ventana)
    labelHora.config(bg= "#fec5bb", fg="#264653", font="30")
    labelHora.place(x=1100,y=60)
    def reloj():
        time1 =""
        time2=time.strftime("%H:%M:%S")
        if (time1 != time2):
            labelHora.config(text=time2)
            labelHora.after(500,reloj)
    reloj()

    # frame botones
    botones = Frame(ventana, bg="#d8e2dc", width="250", height="500")
    botones.place(x= 30,y=100)

    # ------------------------------ IMAGEN--------------------------------
    Imagen = PhotoImage(file = "d.png")
    Fondo = Label(ventana, image=Imagen)
    Fondo.place(x=300, y=110)

    # contenedores

    frameInicio = Frame(ventana, bg="#72A1C0", width= 840, height= 500)

    frameVentas = Frame(ventana, bg="#457b9d", width=840, height=500)

    frameStock = Frame(ventana, bg="#219ebc", width=840, height=500)

    # frameClientes = Frame(ventana, bg="#6CACBA", width=840, height=500)
    #
    # frameArticulos = Frame(ventana, bg="#598392", width=840, height=500)
    #
    # frameProveedores = Frame(ventana, bg="#7BACAD", width=840, height=500)

    # funciones

    def inicio():
        frameInicio.place(x=310, y=100)
        frameVentas.place_forget()
        frameStock.place_forget()

    def ventas():
        frameInicio.place_forget()
        frameVentas.place(x=310, y=100)
        frameStock.place_forget()

    def stock():
        frameInicio.place_forget()
        frameVentas.place_forget()
        frameStock.place(x=310, y=100)


    # def clientes():
    #     frameInicio.place_forget()
    #     frameVentas.place_forget()
    #     frameStock.place_forget()
    #     frameClientes.place(x=310, y=100)
    #     frameArticulos.place_forget()
    #     frameProveedores.place_forget()
    #
    # def articulos():
    #     frameInicio.place_forget()
    #     frameVentas.place_forget()
    #     frameStock.place_forget()
    #     frameClientes.place_forget()
    #     frameArticulos.place(x=310, y=100)
    #     frameProveedores.place_forget()
    #
    # def proveedores():
    #     frameInicio.place_forget()
    #     frameVentas.place_forget()
    #     frameStock.place_forget()
    #     frameClientes.place_forget()
    #     frameArticulos.place_forget()
    #     frameProveedores.place(x=310, y=100)

    # botones del frame

    inicio = Button(botones, text="Inicio", width=20, command=inicio)
    # inicio.place(x=50,y=70)

    ventas = Button(botones, text="Ventas", width=20, command=ventas)
    ventas.place(x=50, y=70)

    stock = Button(botones, text="Stock", width=20, command= stock)
    stock.place(x=50, y=140)

    #stock.place(x=50, y=210)

    # clientes = Button(botones, text="Clientes", width=20, command=clientes)
    # clientes.place(x=50, y=280)
    #
    # articulos = Button(botones, text="Articulos", width=20, command=articulos)
    # articulos.place(x=50, y=350)
    #
    # proveedores = Button(botones, text="Proveedores", width=20, command=proveedores)
    # proveedores.place(x=50, y=420)





    #   ------------   V E N T A S   -------------

    # contenedor botones ventas

    contenedorBotonesVentas = Frame(frameVentas, bg="#E24A3E", width="200", height="400")
    contenedorBotonesVentas.place(x=610,y=50)

    # contenedores de ventas

    contenedorNuevaVenta = Frame(frameVentas, width=550, height=400)

    contenedorBuscarVenta = Frame(frameVentas, width=550, height=400)

    contenedorModificarVenta = Frame(frameVentas, width=550, height=400)

    contenedorEliminarrVenta = Frame(frameVentas, width=550, height=400)



    # funciones

    def ventasCrear():
        contenedorNuevaVenta.place(x=30, y=50)
        contenedorBuscarVenta.place_forget()
        contenedorModificarVenta.place_forget()
        contenedorEliminarrVenta.place_forget()


    def ventasBuscar():
        contenedorBuscarVenta.place(x=30, y=50)
        contenedorNuevaVenta.place_forget()
        contenedorModificarVenta.place_forget()
        contenedorEliminarrVenta.place_forget()

    def ventasModificar():
        contenedorModificarVenta.place(x=30, y=50)
        contenedorNuevaVenta.place_forget()
        contenedorBuscarVenta.place_forget()
        contenedorEliminarrVenta.place_forget()
    def ventasEliminar():
        contenedorEliminarrVenta.place.place(x=30, y=50)
        contenedorNuevaVenta.place_forget()
        contenedorBuscarVenta.place_forget()
        contenedorModificarVenta.place_forget()
    # botones de ventas

    crear = Button(contenedorBotonesVentas, text="Nueva Venta", width=20, command=ventasCrear )
    crear.place(x=20, y=50)

    buscar = Button(contenedorBotonesVentas, text="Buscar", width=20, command= ventasBuscar)
    buscar.place(x=20, y=100)

    modificar = Button(contenedorBotonesVentas, text="Modificar", width=20)
    modificar.place(x=20, y=150)

    eliminar = Button(contenedorBotonesVentas, text="Eliminar", width=20)
    eliminar.place(x=20, y=200)

    # label y entry s de ventas



    # Nueva venta

    contenedorAgregarProducto = Frame(contenedorNuevaVenta, width =550, height=270, bg="white")
    contenedorAgregarProducto.place(x=0,y=0)

    contenedorListarProductos = Frame(contenedorNuevaVenta, width=550, height=400, bg="white")



    nuevaVenta = Label(contenedorAgregarProducto, text="Nueva Venta", bg="peachpuff2")
    nuevaVenta.place(x=250, y=20)

    # codigoProducto = Label(contenedorAgregarProducto, text="Código de producto", bg="peachpuff2")
    # codigoProducto.place(x=30, y=70)
    #
    # ecodigoProducto = Entry(contenedorAgregarProducto, width=12)
    # ecodigoProducto.place(x=300, y=70)
    #
    # producto = Label(contenedorAgregarProducto, text="Nombre del producto", bg="peachpuff2")
    # producto.place(x=30, y=110)
    #
    # eproducto = Entry(contenedorAgregarProducto, width=12)
    # eproducto.place(x=300, y=110)
    nombre = ""
    codigo =""
    def buscarProducto():

        tabla= conexion.cursor()
        nombreBuscado=(entryBusquedaVenta.get(),)
        tabla.execute("select * from stock where nombre = ?",nombreBuscado) #codigo nombre cantidad precio
        conexion.commit()
        datosBuscados = tabla.fetchall()
        tabla.close()
        codigoBuscado = Label(contenedorAgregarProducto, text=("Código: "+ str(datosBuscados[0][0])))
        codigoBuscado.place(x=30, y=110)
        stockBuscado = Label(contenedorAgregarProducto, text=("Stock disponible: "+ str(datosBuscados[0][2])))
        stockBuscado.place(x=200, y=110)
        eprecioUnitario.insert(0,datosBuscados[0][3])
        codigo = datosBuscados[0][0]
        nombre = datosBuscados[0][1]




    ventaBuscarPor = Label(contenedorAgregarProducto, text="Nombre del producto:")
    ventaBuscarPor.place(x=30, y=70)

    entryBusquedaVenta = Entry(contenedorAgregarProducto)
    entryBusquedaVenta.place(x=200, y=70)

    precioUnitario = Label(contenedorAgregarProducto, text="Precio Unitario", bg="peachpuff2")
    precioUnitario.place(x=30, y=150)

    eprecioUnitario = Entry(contenedorAgregarProducto, width=12)
    eprecioUnitario.place(x=300, y=150)

    cantidad = Label(contenedorAgregarProducto, text="Cantidad", bg="peachpuff2")
    cantidad.place(x=30, y=190)

    ecantidad = Entry(contenedorAgregarProducto, width=12)
    ecantidad.place(x=300, y=190)

    botonBuscarStock = Button(contenedorAgregarProducto, text="Buscar", command=buscarProducto)
    botonBuscarStock.place(x=420, y=70)

    def total():
        total = float(eprecioUnitario.get()) * float(ecantidad.get())
        etotal.insert(0,total)

    total = Button(contenedorAgregarProducto, text="Total:", bg="peachpuff2", command=total)
    total.place(x=30, y=230)

    etotal = Entry(contenedorAgregarProducto, width=12)
    etotal.place(x=300, y=230)

    listaProductos = []
    listaPreciosUnitarios=[]
    listaCantidad=[]
    listaTotal = []
    listaCarrito = []
    listaUnitaria = []

    def agregar():
        datos = (entryBusquedaVenta.get(), eprecioUnitario.get(), ecantidad.get(), etotal.get())
        tabla = conexion.cursor()
        tabla.execute("INSERT INTO venta VALUES (?,?,?,?)", datos)
        conexion.commit()
        tabla.close()
        messagebox.showinfo("venta", "Agregado Exitosamente")
        listaProductos.append(entryBusquedaVenta.get())
        listaPreciosUnitarios.append(float(eprecioUnitario.get()))
        listaCantidad.append(int(ecantidad.get()))
        listaTotal.append(float(eprecioUnitario.get()) * float((ecantidad.get())))
        listaUnitaria=[entryBusquedaVenta.get(),float(eprecioUnitario.get()),int(ecantidad.get()),(float(eprecioUnitario.get()) * float((ecantidad.get())))]
        listaCarrito.append(listaUnitaria)
        entryBusquedaVenta.delete(0, END)
        eprecioUnitario.delete(0, END)
        eprecioUnitario.delete(0, END)
        ecantidad.delete(0, END)
        etotal.delete(0, END)

    def finalizar(listaProductos=listaProductos, listaCantidad=listaCantidad, listaTotal=listaTotal):

        sumatoria = 0
        for total in listaTotal:
            sumatoria += total
        sumatoriaTupla = (sumatoria,)
        tabla = conexion.cursor()
        tabla.execute("insert into caja values (?)", sumatoriaTupla)
        conexion.commit()
        tabla.close()

        #imprimir ticket!

        with open('ticket.txt', 'w', encoding='utf-8') as f:
            f.writelines("producto     precio      cantidad     subtotal")
            f.write('\n')
            for line in listaCarrito:
                f.writelines(str(line))
                f.write('\n')
            f.write("------------------Total a pagar: $")
            f.write(str(sumatoria))
            f.close()

        contador = 0
        for i in listaProductos:
            tabla= conexion.cursor()
            nomb=(i,)
            print(nomb)
            tabla.execute("select cantidad from stock where nombre = ?",nomb)
            conexion.commit()
            cantidad = tabla.fetchall()[0][0]

            print(cantidad)
            print(listaCantidad[contador])
            cantidad -= listaCantidad[contador]
            print(cantidad)
            datos = [cantidad,nomb[0]]
            print(datos)
            tabla.execute("update stock set cantidad = ? where nombre = ? ",datos)
            conexion.commit()
            tabla.close()
            contador += 1


        listaProductos = []
        listaPreciosUnitarios = []
        listaCantidad = []
        listaTotal = []
        messagebox.showinfo("venta","Venta finalizada")
        eprecioUnitario.delete(0,END)
        ecantidad.delete(0,END)
        etotal.delete(0,END)

    def volver():
        botonVolver.place_forget()
        botonAgregar.place(x=400, y=290)
        botonDetalle.place(x=400, y=325)
        botonEnviar.place(x=400, y=360)
        contenedorListarProductos.place_forget()
        contenedorAgregarProducto.place(x=0,y=0)

    botonVolver = Button(contenedorListarProductos, text="Volver", command=volver)

#--------------------------- DETALLE -------------------------------------------------
    def detalle():
        contenedorListarProductos.place(x=0, y=0)
        botonAgregar.place_forget()
        botonVolver.place(x=480, y=360)
        contenedorAgregarProducto.place_forget()
        botonDetalle.place_forget()
        botonEnviar.place_forget()

        tituloNombre = Label(contenedorListarProductos, text="Producto")
        tituloNombre.place(x=20, y=25)

        listaDetalleNombre = Listbox(contenedorListarProductos, width=22, height=15)
        listaDetalleNombre.place(x=10, y=50)

        for i in listaProductos:
            listaDetalleNombre.insert(0, i)


        tituloPrecioUnitario = Label(contenedorListarProductos, text="Precio Unitario")
        tituloPrecioUnitario.place(x=165, y=25)

        listaDetallePrecioU = Listbox(contenedorListarProductos, width=12, height=15)
        listaDetallePrecioU.place(x=170, y=50)

        for precio in listaPreciosUnitarios:
            listaDetallePrecioU.insert(0, precio)


        tituloCantidad = Label(contenedorListarProductos, text="Cantidad")
        tituloCantidad.place(x=280, y=25)

        listaDetalleCantidad = Listbox(contenedorListarProductos, width=12, height=15)
        listaDetalleCantidad.place(x=270, y=50)

        for cantidad in listaCantidad:
            listaDetalleCantidad.insert(0, cantidad)


        tituloTotal = Label(contenedorListarProductos, text="Total")
        tituloTotal.place(x=390, y=25)

        listaDetalleTotal = Listbox(contenedorListarProductos, width=12, height=15)
        listaDetalleTotal.place(x=370, y=50)

        for tot in listaTotal:
            listaDetalleTotal.insert(0, tot)


        entryTotalDetalle=Entry(contenedorListarProductos, width=12)
        entryTotalDetalle.place(x=372, y=305)

        subtotal = 0
        for valor in listaTotal:
            subtotal += valor
        entryTotalDetalle.insert(0,subtotal)

#   botones

    botonAgregar = Button(contenedorNuevaVenta, text="Agregar", command=agregar)
    botonAgregar.place(x=400, y=290)

    botonDetalle = Button(contenedorNuevaVenta, text="Detalle hasta el momento", command=detalle)
    botonDetalle.place(x=400, y=325)

    botonEnviar = Button(contenedorNuevaVenta, text="Finalizar venta", command=finalizar)
    botonEnviar.place(x=400, y=360)

    # buscar venta
    filtros = ttk.Combobox(contenedorBuscarVenta)
    filtros.place(x=50,y=50)
    values= ["filtro1", "filtro2", "filtro3", "filtro4"]
    filtros["values"] = values

    # ------------------------------------ STOCK ----------------------------------------------------------
    # FRAME: frameStock

    tituloStock = Label(frameStock, text="Consulta de Stock")
    tituloStock.place(x=100,y=70)

    buscarPor = Label(frameStock, text="Buscar por:")
    buscarPor.place(x=150,y=140)

    lista=["Código","Nombre"]
    comboboxBuscar = ttk.Combobox(frameStock)
    comboboxBuscar.place(x=250,y=140)
    comboboxBuscar["values"]=lista

    entryBusqueda = Entry(frameStock)
    entryBusqueda.place(x=420,y=140)

    def buscarStock():
        tabla = conexion.cursor()
        if comboboxBuscar.get() == "Nombre":
            labelNombreStock.config(text="Código")
            nombreBuscar = (entryBusqueda.get(),)
            tabla.execute("select codigo, cantidad from stock where nombre = ?", nombreBuscar)
            conexion.commit()
            datosBuscados = tabla.fetchall()
            tabla.close()
            entryNombreStock.delete(0, END)
            entryNombreStock.insert(0, datosBuscados[0][0])
            entryStock.delete(0, END)
            entryStock.insert(0, datosBuscados[0][1])
        elif comboboxBuscar.get() == "Código":
            labelNombreStock.config(text="Nombre")
            nombreBuscar = (entryBusqueda.get(),)
            tabla.execute("select nombre, cantidad from stock where codigo = ?", nombreBuscar)
            conexion.commit()
            datosBuscados = tabla.fetchall()
            tabla.close()
            entryNombreStock.delete(0, END)
            entryNombreStock.insert(0, datosBuscados[0][0])
            entryStock.delete(0, END)
            entryStock.insert(0, datosBuscados[0][1])
        else:
            messagebox.showwarning("Error", "No existe la opción seleccionada")

    botonBuscarStock = Button(frameStock, text="Buscar", command=buscarStock)
    botonBuscarStock.place(x=560,y=138)

    labelNombreStock = Label(frameStock, text="Nombre")
    labelNombreStock.place(x=220,y=200)
    entryNombreStock = Entry(frameStock)
    entryNombreStock.place(x=300,y=200)


    labelStock = Label(frameStock, text="Stock")
    labelStock.place(x=220, y=250)
    entryStock = Entry(frameStock)
    entryStock.place(x=300, y=250)



    #----------------------------------------------CLIENTES-----------------------------------------------

    # tituloClientes = Label(frameClientes, text="Ingresar cliente")
    # tituloClientes.place(x=150,y=30)
    #
    # clienteNombre = Label(frameClientes, text= "Nombre y apellido")
    # clienteNombre.place(x=20,y=60)
    # entyClienteNombre = Entry(frameClientes)
    # entyClienteNombre.place(x=150, y=60)
    #
    # clienteDNI = Label(frameClientes, text="Nombre y apellido")
    # clienteDNI.place(x=20, y=120)
    # entryClienteDNI = Entry(frameClientes)
    # entryClienteDNI.place(x=150, y=120)
    #
    # clienteDireccion = Label(frameClientes, text="Nombre y apellido")
    # clienteDireccion.place(x=20, y=180)
    # entyClienteDireccion = Entry(frameClientes)
    # entyClienteDireccion.place(x=150, y=180)
    #
    # clienteTelefono = Label(frameClientes, text="Nombre y apellido")
    # clienteTelefono.place(x=20, y=240)
    # entyClienteTelefono = Entry(frameClientes)
    # entyClienteTelefono.place(x=150, y=240)
    #
    # botonGuardarCliente = Button()
    # #botonGuardarCliente.place(x=, y=)

    ventana.mainloop()

# -------------------LOGGIN-----------------------------------

def ventanaLogin():
    login = Tk()
    login.geometry("500x500")

    #cuenta

    labelCuenta = Label(login, text = "Cuenta: ")
    labelCuenta.place(x= 140, y=140)
    cuenta = Entry(login)
    cuenta.place(x=220,y=140)

    # contraseña

    labelContraseña = Label(login, text="Contraseña: ")
    labelContraseña.place(x=140, y=180)
    contraseña = Entry(login)
    contraseña.place(x=220, y=180)

    # validar

    def validar():
        if (cuenta.get()=="cmolina" and contraseña.get()=="lalala15"):
            login.destroy()
            ventanaPrincipal()
        else:
            messagebox.showwarning("Denegado","Los datos ingresados son incorrectos")

    # boton

    botonValidar=Button(login,text="Ingresar", command=validar)
    botonValidar.place(x=170,y=220)

    login.mainloop()

ventanaLogin()
#ventanaPrincipal()