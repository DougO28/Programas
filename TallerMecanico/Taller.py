import tkinter as tk
from tkinter import ttk, messagebox, PhotoImage
from pyswip import Prolog

class TallerMecanicoGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Diagnóstico Mecánico")

        try:
            self.prolog = Prolog()
            self.prolog.consult("TallerMecanico.pl")
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo cargar TallerMecanico.pl: {e}")
            root.destroy()
            return

        self.Imagenes = {
            "fuga_aceite": PhotoImage(file="Imagenes/FugaAceite.png").subsample(2, 2), # Ajusta el tamaño si es necesario
            "perdida_compresion": PhotoImage(file="Imagenes/PerdidaCompresion.png").subsample(2, 2),
            "pastillas_desgastadas": PhotoImage(file="Imagenes/ProblemasFrenos.png").subsample(2, 2),
            "pedal_freno_fondo": PhotoImage(file="Imagenes/ProblemasFrenos.png").subsample(2, 2),
            "falla_encendido": PhotoImage(file="Imagenes/SistemaEncendido.png").subsample(2, 2),
            "sobrecalentamiento": PhotoImage(file="Imagenes/SobreCalentamiento.png").subsample(2, 2),
            "ruido_suspension": PhotoImage(file="Imagenes/Suspension.png").subsample(2, 2),
            "rebote_excesivo": PhotoImage(file="Imagenes/SUspension.png").subsample(2, 2)
        }

        self.create_widgets()

    def create_widgets(self):
        # Botones para los diferentes diagnósticos
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

        # Configurar el peso de las columnas para que los botones se expandan
        self.root.grid_columnconfigure(0, weight=1)
        self.root.grid_columnconfigure(1, weight=1)

    def mostrar_diagnostico(self, sintoma):
        resultados = list(self.prolog.query(f"diagnostico({sintoma}, Accion)"))
        if resultados:
            diagnosticos = "\n".join([res["Accion"] for res in resultados])
            self.resultado_label.config(text=f"Diagnostico para {sintoma.replace('_', ' ').capitalize()}:\n{diagnosticos}")
            self.mostrar_imagen(sintoma)
        else:
            self.resultado_label.config(text=f"No se encontraron diagnosticos para {sintoma.replace('_', ' ').capitalize()}.")
            self.imagen_label.config(image=None)

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

if __name__ == "__main__":
    root = tk.Tk()
    app = TallerMecanicoGUI(root)
    root.mainloop()