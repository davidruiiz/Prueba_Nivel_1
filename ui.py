import helpers
import database as db
from tkinter import *
from tkinter import ttk
from tkinter.messagebox import askokcancel, WARNING


class CenterWidgetMixin:
    def center(self):
        self.update()
        w = self.winfo_width()
        h = self.winfo_height()
        ws = self.winfo_screenwidth()
        hs = self.winfo_screenheight()
        x = int(ws/2 - w/2)
        y = int(hs/2 - h/2)
        self.geometry(f"{w}x{h}+{x}+{y}")


class CreateVehicleWindow(Toplevel, CenterWidgetMixin):
    def __init__(self, parent):
        super().__init__(parent)
        self.title("Crear vehículo")
        self.build()
        self.center()
        self.transient(parent)
        self.grab_set()

    def build(self):
        frame = Frame(self)
        frame.pack(padx=20, pady=10)

        Label(frame, text="Número de Bastidor (2 ints y 1 upper char)").grid(row=0, column=0)
        Label(frame, text="Color (de 1 a 30 chars)").grid(row=0, column=1)
        Label(frame, text="Ruedas").grid(row=0, column=2)

        bastidor = Entry(frame)
        bastidor.grid(row=1, column=0)
        bastidor.bind("<KeyRelease>", lambda event: self.validate(event, 0))
        color = Entry(frame)
        color.grid(row=1, column=1)
        color.bind("<KeyRelease>", lambda event: self.validate(event, 1))
        ruedas = Entry(frame)
        ruedas.grid(row=1, column=2)
        ruedas.bind("<KeyRelease>", lambda event: self.validate(event, 2))

        frame = Frame(self)
        frame.pack(pady=10)

        crear = Button(frame, text="Crear", command=self.create_vehicle)
        crear.configure(state=DISABLED)
        crear.grid(row=0, column=0)
        Button(frame, text="Cancelar", command=self.close).grid(row=0, column=1)

        self.validaciones = [0, 0, 0]
        self.crear = crear
        self.bastidor = bastidor
        self.color = color
        self.ruedas = ruedas

    def create_vehicle(self):
        self.master.treeview.insert(
            parent='', index='end', iid=self.bastidor.get(),
            values=(self.bastidor.get(), self.color.get(), self.ruedas.get()))
        db.Vehiculos.crear(self.bastidor.get(), self.color.get(), self.ruedas.get())
        self.close()

    def close(self):
        self.destroy()
        self.update()

    def validate(self, event, index):
        valor = event.widget.get()
        valido = helpers.bastidor_valido(valor, db.Vehiculos.lista) if index == 0 \
            else (len(valor) >= 1 and len(valor) <= 30)
        event.widget.configure({"bg": "Green" if valido else "Red"})
        # Cambiar el estado del botón en base a las validaciones
        self.validaciones[index] = valido
        self.crear.config(state=NORMAL if self.validaciones == [1, 1, 1] else DISABLED)


class EditVehicleWindow(Toplevel, CenterWidgetMixin):
    def __init__(self, parent):
        super().__init__(parent)
        self.title("Actualizar vehículo")
        self.build()
        self.center()
        self.transient(parent)
        self.grab_set()

    def build(self):
        frame = Frame(self)
        frame.pack(padx=20, pady=10)

        Label(frame, text="Número de Bastidor").grid(row=0, column=0)
        Label(frame, text="Color (de 1 a 30 chars)").grid(row=0, column=1)
        Label(frame, text="Ruedas").grid(row=0, column=2)

        bastidor = Entry(frame)
        bastidor.grid(row=1, column=0)
        color = Entry(frame)
        color.grid(row=1, column=1)
        color.bind("<KeyRelease>", lambda event: self.validate(event, 0))
        ruedas = Entry(frame)
        ruedas.grid(row=1, column=2)
        ruedas.bind("<KeyRelease>", lambda event: self.validate(event, 1))

        vehiculo = self.master.treeview.focus()
        campos = self.master.treeview.item(vehiculo, 'values')
        bastidor.insert(0, campos[0])
        bastidor.config(state=DISABLED)
        color.insert(0, campos[1])
        ruedas.insert(0, campos[2])

        frame = Frame(self)
        frame.pack(pady=10)

        actualizar = Button(frame, text="Actualizar", command=self.edit_vehicle)
        actualizar.grid(row=0, column=0)
        Button(frame, text="Cancelar", command=self.close).grid(row=0, column=1)

        self.validaciones = [1, 1]
        self.actualizar = actualizar
        self.bastidor = bastidor
        self.color = color
        self.ruedas = ruedas

    def edit_vehicle(self):
        vehiculo = self.master.treeview.focus()
        self.master.treeview.item(vehiculo, values=(
            self.bastidor.get(), self.color.get(), self.ruedas.get()))
        db.Vehiculos.modificar(self.bastidor.get(), self.color.get(), self.ruedas.get())
        self.close()

    def close(self):
        self.destroy()
        self.update()

    def validate(self, event, index):
        valor = event.widget.get()
        valido = (valor.isalpha() and len(valor) >= 2 and len(valor) <= 30)
        event.widget.configure({"bg": "Green" if valido else "Red"})
        # Cambiar el estado del botón en base a las validaciones
        self.validaciones[index] = valido
        self.actualizar.config(state=NORMAL if self.validaciones == [1, 1] else DISABLED)


class MainWindow(Tk, CenterWidgetMixin):
    def __init__(self):
        super().__init__()
        self.title("Gestor de vehículos")
        self.build()
        self.center()

    def build(self):
        frame = Frame(self)
        frame.pack()

        treeview = ttk.Treeview(frame)
        treeview['columns'] = ('Número de Bastidor', 'Color', 'Ruedas')

        treeview.column("#0", width=0, stretch=NO)
        treeview.column("Número de Bastidor", anchor=CENTER)
        treeview.column("Color", anchor=CENTER)
        treeview.column("Ruedas", anchor=CENTER)

        treeview.heading("Número de Bastidor", text="Número de Bastidor", anchor=CENTER)
        treeview.heading("Color", text="Color", anchor=CENTER)
        treeview.heading("Ruedas", text="Ruedas", anchor=CENTER)

        scrollbar = Scrollbar(frame)
        scrollbar.pack(side=RIGHT, fill=Y)
        treeview['yscrollcommand'] = scrollbar.set

        for vehiculo in db.Vehiculos.lista:
            treeview.insert(
                parent='', index='end', iid=vehiculo.bastidor,
                values=(vehiculo.bastidor, vehiculo.color, vehiculo.ruedas))

        treeview.pack()

        frame = Frame(self)
        frame.pack(pady=20)

        Button(frame, text="Crear", command=self.create).grid(row=0, column=0)
        Button(frame, text="Modificar", command=self.edit).grid(row=0, column=1)
        Button(frame, text="Borrar", command=self.delete).grid(row=0, column=2)

        self.treeview = treeview

    def delete(self):
        vehiculo = self.treeview.focus()
        if vehiculo:
            campos = self.treeview.item(vehiculo, "values")
            confirmar = askokcancel(
                title="Confirmar borrado",
                message=f"¿Borrar {campos[1]} {campos[2]}?",
                icon=WARNING)
            if confirmar:
                self.treeview.delete(vehiculo)
                db.Vehiculos.borrar(campos[0])

    def create(self):
        CreateVehicleWindow(self)

    def edit(self):
        if self.treeview.focus():
            EditVehicleWindow(self)


if __name__ == "__main__":
    app = MainWindow()
    app.mainloop()
