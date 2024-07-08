import tkinter as tk
from datetime import datetime, timezone, timedelta

# Dicionário com os fusos horários e seus respectivos deslocamentos em relação ao UTC
fusos_horarios = {
    "UTC": 0,
    "UTC+1": 1,
    "UTC+2": 2,
    "UTC+3": 3,
    "UTC+4": 4,
    "UTC+5": 5,
    "UTC+6": 6,
    "UTC+7": 7,
    "UTC+8": 8,
    "UTC+9": 9,
    "UTC+10": 10,
    "UTC+11": 11,
    "UTC+12": 12,
    "UTC-1": -1,
    "UTC-2": -2,
    "UTC-3": -3,
    "UTC-4": -4,
    "UTC-5": -5,
    "UTC-6": -6,
    "UTC-7": -7,
    "UTC-8": -8,
    "UTC-9": -9,
    "UTC-10": -10,
    "UTC-11": -11,
    "UTC-12": -12,
}

class RelogioMundial:
    def __init__(self, root):
        self.root = root
        self.root.title("Relógio Mundial")
        
        self.current_time = tk.Label(self.root, font=('Helvetica', 24, 'bold'))
        self.current_time.pack(pady=20)
        
        self.seletor_fuso = tk.StringVar()
        self.seletor_fuso.set("UTC")  # Fuso horário padrão inicial é UTC
        
        self.fuso_dropdown = tk.OptionMenu(self.root, self.seletor_fuso, *fusos_horarios.keys(), command=self.update_time)
        self.fuso_dropdown.pack(pady=10)
        
        self.update_time()  # Chama a função para exibir o horário inicial
        
    def update_time(self, event=None):
        fuso_selecionado = self.seletor_fuso.get()
        deslocamento = fusos_horarios[fuso_selecionado]
        
        # Obtém a hora atual considerando o deslocamento do fuso horário selecionado
        hora_atual = datetime.utcnow().replace(tzinfo=timezone.utc) + timedelta(hours=deslocamento)
        hora_formatada = hora_atual.strftime('%Y-%m-%d %H:%M:%S %Z%z')
        
        self.current_time.config(text=hora_formatada)
        
        # Atualiza a cada 1 segundo
        self.root.after(1000, self.update_time)

if __name__ == "__main__":
    root = tk.Tk()
    relogio_mundial = RelogioMundial(root)
    root.mainloop()
