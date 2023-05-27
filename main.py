from tkinter import StringVar, IntVar, OptionMenu, Button, Tk, Label, Toplevel, Text


class Grupo:
    def __init__(self, num_grupo, inicio, fim):
        self.num_grupo = num_grupo
        self.inicio = inicio
        self.fim = fim


# Criar a lista vazia para armazenar os agendamentos
agendamentos = []

# Criar as variáveis para armazenar os valores selecionados
grupo_selecionado = None
hora_inicio = None
minuto_inicio = None
hora_fim = None
minuto_fim = None


def fechar_janela():
    janela.destroy()


def salvar_e_adicionar():
    global grupo_selecionado, hora_inicio, minuto_inicio, hora_fim, minuto_fim
    # Obter os valores selecionados
    grupo = grupo_selecionado.get()
    inicio = f"{hora_inicio.get()}:{minuto_inicio.get()}"
    fim = f"{hora_fim.get()}:{minuto_fim.get()}"
    # Criar um objeto Grupo com as informações
    novo_grupo = Grupo(grupo, inicio, fim)
    # Adicionar o objeto à lista de agendamentos
    agendamentos.append(novo_grupo)
    # Resetar os valores iniciais
    grupo_selecionado.set(0)
    hora_inicio.set("00")
    minuto_inicio.set("00")
    hora_fim.set("00")
    minuto_fim.set("00")


def salvar_e_gerar():
    global grupo_selecionado, hora_inicio, minuto_inicio, hora_fim, minuto_fim
    # Obter os valores selecionados
    grupo = grupo_selecionado.get()
    inicio = f"{hora_inicio.get()}:{minuto_inicio.get()}"
    fim = f"{hora_fim.get()}:{minuto_fim.get()}"
    # Criar um objeto Grupo com as informações
    novo_grupo = Grupo(grupo, inicio, fim)
    # Adicionar o objeto à lista de agendamentos
    agendamentos.append(novo_grupo)

    # Fechar a janela de agendamento de reuniões
    agenda.destroy()

    # Criar a janela para exibir a tabela
    tabela = Tk()
    tabela.title("Tabela de Agendamentos")
    tabela.geometry("450x600")
    screen_width = tabela.winfo_screenwidth()
    screen_height = tabela.winfo_screenheight()
    window_width = 450
    window_height = 600
    x = (screen_width // 2) - (window_width // 2)
    y = (screen_height // 2) - (window_height // 2)
    tabela.geometry(f"{window_width}x{window_height}+{x}+{y}")
    tabela.resizable(False, False)
    # Criar um widget Text para exibir a tabela
    text_box = Text(tabela, height=40, width=60)
    text_box.pack()

    # Exibir os agendamentos na tabela
    for agendamento in agendamentos:
        texto = f"Grupo {agendamento.num_grupo} - Reunião agendada de {agendamento.inicio} até {agendamento.fim}\n"
        text_box.insert("end", texto)

    # Desabilitar a edição no widget Text
    text_box.config(state="disabled")

    # Iniciar o loop principal da janela
    tabela.mainloop()


def agendar_horarios():
    global grupo_selecionado, hora_inicio, minuto_inicio, hora_fim, minuto_fim
    # Criar a janela principal
    janela.destroy()
    global agenda
    agenda = Tk()
    agenda.title("Exemplo de Agendamento")
    agenda.geometry("800x600")
    screen_width = agenda.winfo_screenwidth()
    screen_height = agenda.winfo_screenheight()
    window_width = 800
    window_height = 600
    x = (screen_width // 2) - (window_width // 2)
    y = (screen_height // 2) - (window_height // 2)
    agenda.geometry(f"{window_width}x{window_height}+{x}+{y}")
    agenda.resizable(False, False)

    # Criar as variáveis para armazenar os valores selecionados
    grupo_selecionado = IntVar(agenda)
    hora_inicio = StringVar(agenda)
    minuto_inicio = StringVar(agenda)
    hora_fim = StringVar(agenda)
    minuto_fim = StringVar(agenda)

    # Definir os valores iniciais
    grupo_selecionado.set(0)
    hora_inicio.set("00")
    minuto_inicio.set("00")
    hora_fim.set("00")
    minuto_fim.set("00")

    # Criar as listas de opções
    grupos = [i for i in range(26)]
    horas = [str(i) for i in range(8, 18)]
    minutos = [str(i).zfill(2) for i in range(0, 61, 5)]

    # Criar os widgets de dropdown menu
    label_grupo = Label(agenda, text="Grupo:")
    label_grupo.grid(row=0, column=0, padx=5, pady=5)
    menu_grupo = OptionMenu(agenda, grupo_selecionado, *grupos)
    menu_grupo.grid(row=0, column=1, padx=5, pady=5)

    label_inicio = Label(agenda, text="Início:")
    label_inicio.grid(row=0, column=2, padx=5, pady=5)
    menu_hora_inicio = OptionMenu(agenda, hora_inicio, *horas)
    menu_hora_inicio.grid(row=0, column=3, padx=5, pady=5)
    menu_minuto_inicio = OptionMenu(agenda, minuto_inicio, *minutos)
    menu_minuto_inicio.grid(row=0, column=4, padx=5, pady=5)

    label_termino = Label(agenda, text="Término:")
    label_termino.grid(row=0, column=5, padx=5, pady=5)
    menu_hora_fim = OptionMenu(agenda, hora_fim, *horas)
    menu_hora_fim.grid(row=0, column=6, padx=5, pady=5)
    menu_minuto_fim = OptionMenu(agenda, minuto_fim, *minutos)
    menu_minuto_fim.grid(row=0, column=7, padx=5, pady=5)

    botao_salvar_e_adicionar = Button(agenda, text="Salvar e adicionar mais um agendamento", command=salvar_e_adicionar)
    botao_salvar_e_adicionar.grid(row=1, column=0, columnspan=4, padx=70, pady=0)

    botao_salvar_e_gerar = Button(agenda, text="Salvar e gerar tabela", command=salvar_e_gerar)
    botao_salvar_e_gerar.grid(row=1, column=4, columnspan=4, padx=0, pady=450)

    # Iniciar o loop principal da janela
    agenda.mainloop()


# Criar a janela
janela = Tk()
janela.title("Minha Tela")
janela.geometry("800x600")
screen_width = janela.winfo_screenwidth()
screen_height = janela.winfo_screenheight()
window_width = 800
window_height = 600
x = (screen_width // 2) - (window_width // 2)
y = (screen_height // 2) - (window_height // 2)
janela.geometry(f"{window_width}x{window_height}+{x}+{y}")
janela.resizable(False, False)
# Criar os botões
fonte = ("Comic Sans MS", 18)
botao_agendar = Button(janela, text="Agendar Horários", font=fonte, command=agendar_horarios, width=25, height=3)
botao_fechar = Button(janela, text="Fechar", font=fonte, command=fechar_janela, width=25, height=3)

# Posicionar os botões no centro
botao_agendar.place(relx=0.5, rely=0.35, anchor="center")
botao_fechar.place(relx=0.5, rely=0.65, anchor="center")

# Iniciar o loop principal da janela
janela.mainloop()
