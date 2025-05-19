import tkinter as tk
from tkinter import ttk, messagebox, PhotoImage
from pyswip import Prolog

class InicioGUI:
    def __init__(self, root, main_app):
        self.root = root
        self.root.title("Bienvenido A Taller Mecánico PROLOG")
        self.main_app = main_app

        self.logo_img = PhotoImage(file="Imagenes/Logo.png").subsample(3, 3)  # Se Ajusta el tamaño con subsample
        logo_label = ttk.Label(root, image=self.logo_img)
        logo_label.pack(pady=10)

        bienvenida_label = ttk.Label(root, text="Bienvenido a tu taller de confianza", font=("Arial", 14))
        bienvenida_label.pack(pady=5)

        marca_label = ttk.Label(root, text="Por favor, ingresa la marca de tu vehículo:")
        marca_label.pack(pady=5)

        self.marca_entry = ttk.Entry(root)
        self.marca_entry.pack(pady=5)

        ingresar_button = ttk.Button(root, text="Ingresar", command=self.iniciar_app)
        ingresar_button.pack(pady=10)

    def iniciar_app(self):
        marca_vehiculo = self.marca_entry.get()
        self.root.destroy()
        self.main_app.root.title(f"Diagnóstico Mecánico - Vehículo: {marca_vehiculo}")
        self.main_app.root.deiconify() # Mostrar la ventana principal

class TallerMecanicoGUI:
    def __init__(self, root):
        self.root = root
        self.root.withdraw() # Ocultar la ventana principal al inicio
        self.prolog = None # Inicializar prolog como None
        self.Imagenes = {
            "fuga_aceite": PhotoImage(file="Imagenes/FugaAceite.png").subsample(2, 2),
            "perdida_compresion": PhotoImage(file="Imagenes/PerdidaCompresion.png").subsample(2, 2),
            "pastillas_desgastadas": PhotoImage(file="Imagenes/ProblemasFrenos.png").subsample(2, 2),
            "pedal_freno_fondo": PhotoImage(file="Imagenes/ProblemasFrenos.png").subsample(2, 2),
            "falla_encendido": PhotoImage(file="Imagenes/SistemaEncendido.png").subsample(2, 2),
            "sobrecalentamiento": PhotoImage(file="Imagenes/SobreCalentamiento.png").subsample(2, 2),
            "ruido_suspension": PhotoImage(file="Imagenes/Suspension.png").subsample(2, 2),
            "rebote_excesivo": PhotoImage(file="Imagenes/Suspension.png").subsample(2, 2)
        }

        try:
            self.prolog = Prolog()
            self.prolog.consult("TallerMecanico.pl")
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo cargar TallerMecanico.pl: {e}")
            root.destroy()
            return

        self.create_widgets()

    def create_widgets(self):
        botones_info = [
            ("Falla de Encendido", "falla_encendido"),
            ("Sobrecalentamiento", "sobrecalentamiento"),
            ("Fuga de Aceite", "fuga_aceite"),
            ("Pérdida de Compresión", "perdida_compresion"),
            ("Problemas de Frenos", "pastillas_desgastadas"),
            ("Suspensión del Vehículo", "ruido_suspension"),
            ("Suspensión de Rebote Excesivo", "rebote_excesivo"),
            ("Pedal de Freno al Fondo", "pedal_freno_fondo")
        ]

        for i, (texto, sintoma) in enumerate(botones_info):
            ttk.Button(self.root, text=texto, command=lambda s=sintoma: self.mostrar_diagnostico(s)).grid(row=i // 2, column=i % 2, padx=10, pady=10, sticky="ew")

        self.resultado_label = ttk.Label(self.root, text="")
        self.resultado_label.grid(row=len(botones_info) // 2 + 1, column=0, columnspan=2, padx=10, pady=10, sticky="ew")

        self.imagen_label = ttk.Label(self.root)
        self.imagen_label.grid(row=len(botones_info) // 2 + 2, column=0, columnspan=2, padx=10, pady=10)

        self.root.grid_columnconfigure(0, weight=1)
        self.root.grid_columnconfigure(1, weight=1)

    def mostrar_diagnostico(self, sintoma):
        if self.prolog:
            resultados = list(self.prolog.query(f"diagnostico({sintoma}, Accion)"))
            if resultados:
                diagnosticos = "\n".join([res["Accion"] for res in resultados])
                self.resultado_label.config(text=f"Diagnostico para {sintoma.replace('_', ' ').capitalize()}:\n{diagnosticos}")
                self.mostrar_imagen(sintoma)
            else:
                self.resultado_label.config(text=f"No se encontraron diagnosticos para {sintoma.replace('_', ' ').capitalize()}.")
                self.imagen_label.config(image=None)
        else:
            messagebox.showerror("Error", "El motor de Prolog no se ha inicializado correctamente.")

    def mostrar_imagen(self, sintoma):
        if sintoma == "fuga_aceite":
            self.imagen_label.config(image=self.Imagenes["fuga_aceite"])
        elif sintoma == "perdida_compresion":
            self.imagen_label.config(image=self.Imagenes["perdida_compresion"])
        elif sintoma == "pastillas_desgastadas":
            self.imagen_label.config(image=self.Imagenes["pastillas_desgastadas"])
        elif sintoma == "pedal_freno_fondo":
            self.imagen_label.config(image=self.Imagenes["pedal_freno_fondo"])
        elif sintoma == "falla_encendido":
            self.imagen_label.config(image=self.Imagenes["falla_encendido"])
        elif sintoma == "sobrecalentamiento":
            self.imagen_label.config(image=self.Imagenes["sobrecalentamiento"])
        elif sintoma == "ruido_suspension":
            self.imagen_label.config(image=self.Imagenes["ruido_suspension"])
        elif sintoma == "rebote_excesivo":
            self.imagen_label.config(image=self.Imagenes["rebote_excesivo"])
        else:
            self.imagen_label.config(image=None)
"""""
if __name__ == "__main__":
    root_inicio = tk.Tk()
    main_app_root = tk.Tk()
    main_app = TallerMecanicoGUI(main_app_root)
    inicio_gui = InicioGUI(root_inicio, main_app)
    main_app_root.withdraw() # Ocultar la ventana principal al inicio
    root_inicio.mainloop()
    # Cuando la ventana de inicio se cierra, se inicia la aplicación principal
    main_app_root.mainloop()""" #Verificar los errores cometidos en el main y comparar con la corrección.

if __name__ == "__main__":
    root = tk.Tk()  # Solo una instancia de Tk
    main_app = TallerMecanicoGUI(root)  # Se oculta internamente en su __init__
    
    inicio_window = tk.Toplevel(root)  # Ventana de inicio
    inicio_gui = InicioGUI(inicio_window, main_app)

    root.mainloop()

    
