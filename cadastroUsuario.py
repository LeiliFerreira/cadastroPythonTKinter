from tkinter import*
import webbrowser

janela = Tk()
janela.title("Cadastro de Clientes")
janela.geometry("330x260+730+100")

def pesquisar_cep():
    url = ("https://achacep.com.br/")
    webbrowser.open(url)
    
def cadastro():
    nome_cliente = nome.get()
    email_cliente = email.get()
    cidade_cliente = cidade.get()
    endereco_cliente = endereco.get()
    cep_usuario = cep.get()
    contato_cliente = contato.get()
    senha_cliente = senha.get()

    print("\033[1;33mCadastro realizado com sucesso!\033[m")
    print("-------------------------------")
    print("\033[1;30mCliente:\033[m",nome.get())
    print("-------------------------------")
    print("\033[1;30mEmail:\033[m", email.get())
    print("-------------------------------")
    print("\033[1;30mCidade:\033[m",cidade.get())
    print("-------------------------------")
    print("\033[1;30mEndereço:\033[m", endereco.get())
    print("-------------------------------")
    print("\033[1;30mContato:\033[m", contato.get())
    print("-------------------------------")
    print("\033[1;30mSenha:\033[m ********....")

#Nome Cliente
label = Label(janela, text="Nome completo: ",font=("arial",10))
label.grid(column=0, row=0, padx=5, pady=5)

nome = Entry(janela, width=25)
nome.grid(column=1, row=0, padx=5, pady=5)

#Email
label1 = Label(janela, text="Email: ",font=("arial",10))
label1.grid(column=0, row=1, padx=5, pady=5)

email = Entry(janela, width=25)
email.grid(column=1, row=1, padx=5, pady=5)

#Endereço
label2 = Label(janela, text="Cidade: ", font=("arial",10))
label2.grid(column=0, row=2, padx=5, pady=5)

cidade = Entry(janela, width=25)
cidade.grid(column=1, row=2, padx=5, pady=5)

#Cidade
label3 = Label(janela, text="Endereço:",font=("arial",10))
label3.grid(column=0, row=3, padx=5, pady=5)

endereco = Entry(janela, width=25)
endereco.grid(column=1, row=3, padx=5, pady=5)

#CEP
label4 = Label(janela, text="CEP:", font=("arial",10))
label4.grid(column=0, row=4, padx=5, pady=5)

cep = Entry(janela, width=25)
cep.grid(column=1, row=4, padx=5, pady=5)

#Contato
label5 = Label(janela, text="Contato:", font=("arial",10))
label5.grid(column=0, row=5, padx=5, pady=5)

contato = Entry(janela, width=25)
contato.grid(column=1, row=5, padx=5, pady=5)

#Senha
label6 = Label(janela, text="Criar senha:", font=("arial",10))
label6.grid(column=0, row=6, padx=5, pady=5)

senha = Entry(janela, width=25)
senha.grid(column=1, row=6, padx=5, pady=5)

#Botão Cadastrar
botao = Button(janela, text="Cadastrar", width=10, border=2, command=cadastro)
botao['background']='#FFFF00'
botao.grid(column=1, row=7)

#Botão Pesquisar Cep
botao2 = Button(janela, text="?", width=5, border=2, command=pesquisar_cep)
botao2['background']="#C0C0C0"
botao2.grid(column=3, row=4)

janela.mainloop()