import tkinter as tk
from tkinter import messagebox, ttk

usuarios = {"admin": "1234"}  # Dicionário para armazenar usuários e senhas
equipamentos = ["Notebook", "Projetor", "Impressora"]
reservas = []

# Cores para o tema
bg_color = "#2C3E50"  # Azul escuro
fg_color = "#ECF0F1"  # Branco gelo
btn_color = "#3498DB"  # Azul vibrante
btn_fg = "#000000"  # Texto preto nos botões

# Estilizando a aplicação
def configurar_estilo():
    style = ttk.Style()
    style.configure("TButton", font=("Arial", 12), background=btn_color, foreground=btn_fg, padding=5)
    style.configure("TLabel", font=("Arial", 12), background=bg_color, foreground=fg_color)
    style.configure("TEntry", font=("Arial", 12))
    style.configure("TCombobox", font=("Arial", 12))

# Tela de Login
def login():
    usuario = entry_usuario.get()
    senha = entry_senha.get()
    if usuario in usuarios and usuarios[usuario] == senha:
        messagebox.showinfo("Sucesso", "Login realizado com sucesso!")
        root.withdraw()
        abrir_main(usuario)  # Passa o nome do usuário logado
    else:
        messagebox.showerror("Erro", "Usuário ou senha incorretos.")

def abrir_cadastro():
    cadastro_window = tk.Toplevel()
    cadastro_window.title("Cadastro de Usuário")
    cadastro_window.geometry("400x300")
    cadastro_window.configure(bg=bg_color)

    ttk.Label(cadastro_window, text="Nome de Usuário:").pack(pady=5)
    entry_nome = ttk.Entry(cadastro_window)
    entry_nome.pack(pady=5)

    ttk.Label(cadastro_window, text="Senha:").pack(pady=5)
    entry_senha = ttk.Entry(cadastro_window, show="*")
    entry_senha.pack(pady=5)

    def cadastrar():
        nome = entry_nome.get()
        senha = entry_senha.get()
        if nome and senha:
            if nome in usuarios:
                messagebox.showerror("Erro", "Usuário já existe!")
            else:
                usuarios[nome] = senha
                messagebox.showinfo("Cadastro", f"Usuário {nome} cadastrado com sucesso!")
                cadastro_window.destroy()
        else:
            messagebox.showwarning("Atenção", "Preencha todos os campos.")

    ttk.Button(cadastro_window, text="Cadastrar", command=cadastrar).pack(pady=10)

# Tela Principal
def abrir_main(usuario_logado):
    main_window = tk.Toplevel()
    main_window.title("Menu Principal")
    main_window.geometry("400x400")
    main_window.configure(bg=bg_color)

    ttk.Label(main_window, text=f"Bem-vindo, {usuario_logado}!", font=("Arial", 14)).pack(pady=10)

    ttk.Button(main_window, text="Lista de Equipamentos", width=30, command=abrir_lista).pack(pady=5)
    ttk.Button(main_window, text="Adicionar Equipamento", width=30, command=abrir_adicionar_equipamento).pack(pady=5)
    ttk.Button(main_window, text="Reservar Equipamento", width=30, command=lambda: abrir_reserva(usuario_logado)).pack(pady=5)
    ttk.Button(main_window, text="Visualizar Reservas", width=30, command=visualizar_reservas).pack(pady=5)

# Tela de Lista de Equipamentos
def abrir_lista():
    lista_window = tk.Toplevel()
    lista_window.title("Lista de Equipamentos")
    lista_window.geometry("400x300")
    lista_window.configure(bg=bg_color)

    ttk.Label(lista_window, text="Equipamentos Disponíveis", font=("Arial", 12)).pack(pady=10)

    for equipamento in equipamentos:
        ttk.Label(lista_window, text=equipamento).pack()

# Tela de Adicionar Equipamento
def abrir_adicionar_equipamento():
    add_window = tk.Toplevel()
    add_window.title("Adicionar Equipamento")
    add_window.geometry("400x200")
    add_window.configure(bg=bg_color)

    ttk.Label(add_window, text="Nome do Novo Equipamento:").pack(pady=5)
    entry_equipamento = ttk.Entry(add_window)
    entry_equipamento.pack(pady=5)

    def adicionar_equipamento():
        novo_equipamento = entry_equipamento.get()
        if novo_equipamento:
            if novo_equipamento in equipamentos:
                messagebox.showwarning("Atenção", "Esse equipamento já está cadastrado.")
            else:
                equipamentos.append(novo_equipamento)
                messagebox.showinfo("Sucesso", f"Equipamento {novo_equipamento} adicionado com sucesso!")
                add_window.destroy()
        else:
            messagebox.showwarning("Atenção", "Preencha o nome do equipamento.")

    ttk.Button(add_window, text="Adicionar", command=adicionar_equipamento).pack(pady=10)

# Tela de Reserva de Equipamento
def abrir_reserva(usuario_logado):
    reserva_window = tk.Toplevel()
    reserva_window.title("Reservar Equipamento")
    reserva_window.geometry("400x250")
    reserva_window.configure(bg=bg_color)

    ttk.Label(reserva_window, text="Selecione o Equipamento:").pack(pady=5)
    
    equipamento_var = tk.StringVar()
    equipamento_combobox = ttk.Combobox(reserva_window, textvariable=equipamento_var, values=equipamentos, state="readonly")
    equipamento_combobox.pack(pady=5)

    def reservar():
        equipamento = equipamento_var.get()
        if equipamento:
            reservas.append((usuario_logado, equipamento))
            messagebox.showinfo("Reserva", f"Reserva feita para {equipamento} por {usuario_logado}.")
            reserva_window.destroy()
        else:
            messagebox.showwarning("Atenção", "Selecione um equipamento.")

    ttk.Button(reserva_window, text="Reservar", command=reservar).pack(pady=10)

# Tela de Visualização de Reservas
def visualizar_reservas():
    reservas_window = tk.Toplevel()
    reservas_window.title("Reservas Realizadas")
    reservas_window.geometry("400x250")
    reservas_window.configure(bg=bg_color)

    ttk.Label(reservas_window, text="Lista de Reservas", font=("Arial", 12)).pack(pady=10)

    if reservas:
        for usuario, equipamento in reservas:
            ttk.Label(reservas_window, text=f"{usuario} reservou {equipamento}").pack()
    else:
        ttk.Label(reservas_window, text="Nenhuma reserva encontrada.").pack()

# Criando a tela de login
root = tk.Tk()
root.title("Login")
root.geometry("350x300")
root.configure(bg=bg_color)

configurar_estilo()

ttk.Label(root, text="Usuário:").pack(pady=5)
entry_usuario = ttk.Entry(root)
entry_usuario.pack(pady=5)

ttk.Label(root, text="Senha:").pack(pady=5)
entry_senha = ttk.Entry(root, show="*")
entry_senha.pack(pady=5)

ttk.Button(root, text="Login", command=login).pack(pady=10)
ttk.Button(root, text="Cadastrar Novo Usuário", command=abrir_cadastro).pack(pady=5)

root.mainloop()

