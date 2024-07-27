import os
import customtkinter as ctk
import pandas as pd

from tkinter import filedialog, messagebox
from joiner import join_csv_files

class CSVJoinerApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Juntador de arquivos do Ney")
        self.geometry("450x405")
        self.resizable(False, False)

        # Centralizar a janela
        self.update_idletasks()
        width = self.winfo_width()
        height = self.winfo_height()
        x = (self.winfo_screenwidth() // 2) - (width // 2)
        y = (self.winfo_screenheight() // 2) - (height // 2)
        self.geometry('{}x{}+{}+{}'.format(width, height, x, y))

        self.file1 = None
        self.file2 = None

        self.create_widgets()

    def create_widgets(self):
        small_padding = {'pady': (2, 0)}
        large_padding = {'pady': (20, 0)}

        self.grid_columnconfigure(0, weight=1)

        # Header
        self.header_label = ctk.CTkLabel(self, text="Juntador de arquivos do Ney", font=("Arial", 20, "bold"))
        self.header_label.grid(row=0, column=0, pady=25)

        # Botão Selecionar Arquivo 1
        self.select_file1_btn = ctk.CTkButton(self, text="Selecione o arquivo 1", font=("Arial", 14, "bold"), command=self.select_file1, width=300, height=40, fg_color="#1E90FF", text_color="#FFFFFF")
        self.select_file1_btn.grid(row=1, column=0)

        # Label do Arquivo 1
        self.file1_label = ctk.CTkLabel(self, text="Nenhum arquivo selecionado", font=("Arial", 12))
        self.file1_label.grid(row=2, column=0, **small_padding)

        # Botão Selecionar Arquivo 2
        self.select_file2_btn = ctk.CTkButton(self, text="Selecione o arquivo 2", font=("Arial", 14, "bold"), command=self.select_file2, width=300, height=40, fg_color="#1E90FF", text_color="#FFFFFF")
        self.select_file2_btn.grid(row=3, column=0, **large_padding)

        # Label do Arquivo 2
        self.file2_label = ctk.CTkLabel(self, text="Nenhum arquivo selecionado", font=("Arial", 12))
        self.file2_label.grid(row=4, column=0, **small_padding)

        # Label da Coluna de Join
        self.column_label = ctk.CTkLabel(self, text="Selecione o nome da chave para juntar", font=("Arial", 12))
        self.column_label.grid(row=5, column=0, **large_padding)

        # Menu de Opções para Coluna
        self.column_optionmenu = ctk.CTkOptionMenu(self, values=[""], width=300, height=40, button_color="#1E90FF", button_hover_color="#87CEEB")
        self.column_optionmenu.grid(row=6, column=0, **small_padding)

        # Botão Juntar Arquivos
        self.join_files_btn = ctk.CTkButton(self, text="Juntar!", font=("Arial", 16, "bold"), command=self.join_files, width=450, height=60, fg_color="#1c5996", text_color="#FFFFFF", hover_color="#87CEEB", state="disabled", corner_radius=0)
        self.join_files_btn.grid(row=7, column=0, pady=20)

    def select_file1(self):
        self.file1 = filedialog.askopenfilename(filetypes=[("CSV Files", "*.csv")])
        if self.file1:
            self.file1_label.configure(text=f"Arquivo {os.path.basename(self.file1)} selecionado")
            self.update_common_keys()
            self.check_files_selected()

    def select_file2(self):
        self.file2 = filedialog.askopenfilename(filetypes=[("CSV Files", "*.csv")])
        if self.file2:
            self.file2_label.configure(text=f"Arquivo {os.path.basename(self.file2)} selecionado")
            self.update_common_keys()
            self.check_files_selected()

    def update_common_keys(self):
        if self.file1 and self.file2:
            df1 = pd.read_csv(self.file1, nrows=0)
            df2 = pd.read_csv(self.file2, nrows=0)
            common_keys = list(set(df1.columns).intersection(df2.columns))
            if common_keys:
                self.column_optionmenu.configure(values=common_keys)
                self.column_optionmenu.set(common_keys[0])
            else:
                messagebox.showerror("Erro", "Os arquivos não possuem colunas em comum")

    def check_files_selected(self):
        if self.file1 and self.file2:
            self.join_files_btn.configure(state="normal", fg_color="#1E90FF")
        else:
            self.join_files_btn.configure(state="disabled", fg_color="#1c5996", text_color="#FFFFFF")

    def join_files(self):
        if not self.file1 or not self.file2:
            messagebox.showerror("Erro", "Selecione os dois arquivos CSV")
            return

        join_column = self.column_optionmenu.get()
        if not join_column:
            messagebox.showerror("Erro", "Selecione a coluna para o join")
            return

        df1 = pd.read_csv(self.file1)
        df2 = pd.read_csv(self.file2)

        if join_column not in df1.columns or join_column not in df2.columns:
            messagebox.showerror("Erro", f"A coluna '{join_column}' não existe em um dos arquivos")
            return

        try:
            df_join = join_csv_files(df1, df2, join_column)
        except Exception as e:
            messagebox.showerror("Erro", f"Ocorreu um erro ao juntar os arquivos: {e}")
            return

        output_folder = filedialog.askdirectory()
        if not output_folder:
            messagebox.showerror("Erro", "Selecione uma pasta de saída")
            return

        output_file = os.path.join(output_folder, "resultado.csv")
        df_join.to_csv(output_file, index=False)
        messagebox.showinfo("Sucesso", f"Arquivo salvo em: {output_file}")
