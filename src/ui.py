# ui.py
# Define as funções que criam a interface gráfica e realizam a união dos arquivos CSV
import pandas as pd
import tkinter as tk
from tkinter import filedialog, messagebox

def selecionar_arquivo():
    return filedialog.askopenfilename(filetypes=[("CSV Files", "*.csv")])

def salvar_arquivo():
    return filedialog.asksaveasfilename(defaultextension=".csv", filetypes=[("CSV Files", "*.csv")])

def juntar_arquivos():
    arquivo1 = selecionar_arquivo()
    arquivo2 = selecionar_arquivo()
    
    if not arquivo1 or not arquivo2:
        messagebox.showerror("Erro", "Selecione dois arquivos CSV")
        return
    
    df1 = pd.read_csv(arquivo1, sep='|', encoding='latin-1')
    df2 = pd.read_csv(arquivo2, sep='|', encoding='latin-1')
    df_join = pd.merge(df1, df2, on='Ordem')
    
    output_file = salvar_arquivo()
    if not output_file:
        messagebox.showerror("Erro", "Selecione um arquivo de saída")
        return
    
    df_join.to_csv(output_file, index=False)
    messagebox.showinfo("Sucesso", f"Arquivo salvo em: {output_file}")

def launch_ui():
    # Cria a janela principal
    root = tk.Tk()
    root.title("Juntar Arquivos CSV")
    
    tk.Button(root, text="Juntar Arquivos CSV", command=juntar_arquivos).pack(pady=20)
    
    # Inicia a interface gráfica
    root.mainloop()