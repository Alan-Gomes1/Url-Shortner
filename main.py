from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk


# Cores
azul = "#0f0ff7"
branco = "#ffffff"
preto = "#3b3b3b"

# janela
window = Tk()
window.title("Calculator")
window.geometry("650x260")
window.config(bg=preto)

estilo = ttk.Style(window)
estilo.theme_use("clam")

# Unidades de Medidas
unidades = {'massa' : [{'kg':1000}, {'hg':100}, {'dag':10}, {'g':1}, {'dg':0.1}, {'cg':0.01}, {'mg':0.001}],
            'comprimento' : [{'km':1000}, {'hm':100}, {'dam':10}, {'m':1}, {'dm':0.1}, {'cm':0.01}, {'mm':0.001}],
            'area' : [{'km²':1000000}, {'hm²':10000}, {'dam²':100}, {'m²':1}, {'dm²':0.01}, {'cm²':0.0001}, {'mm²':0.000001}]}

def menu(arg):
  """ Atribui os valores das unidades de medidas para os botões 'De' e 'Para'
      Exibe o nome da unidade de medida no frame direita """
  unidade_de = []
  unidade_para = []
  unidade_valores = []
  
  for dicio in unidades[arg]:
    for chave, valor in dicio.items():
      unidade_de.append(chave)
      unidade_para.append(chave)
      unidade_valores.append(valor)
      
  botao_de['values'] = unidade_de
  botao_para['values'] = unidade_para
  label_direita['text'] = arg
  
  def conversao():
    """dada duas unidades de medidas, para calcular a conversão de uma unidade maior para outra menor basta multiplicar R N vezes,
    já para conversão de uma unidade menor para uma maior, basta dividir por R N vezes, 
    sendo R a razão entre as grandezas e N a distância entre as medidas """
    
    de = botao_de.get()
    para = botao_para.get()
    
    try:
      numero = float(entry_numero.get())
      if unidade_de.index(de) >= unidade_para.index(para):
        distancia = unidade_de.index(para) - unidade_para.index(de) # Os parâmetros são invertidos pois o cálculo é entre as distâncias dos índices
        if arg == 'massa' or arg == 'comprimento':
          resultado = numero * (10**distancia)
        elif arg == 'area':
          resultado = numero * (100**distancia)
      else:
        distancia = unidade_para.index(de) - unidade_de.index(para)
        if arg == 'massa' or arg == 'comprimento':
          resultado = numero / (10**distancia)
        elif arg == 'area':
          resultado = numero / (100**distancia)
            
      label_resultado['text'] = resultado
    except:
      label_resultado['text'] = "Operação Inválida"


  # Label Inferior do frame Direita
  label_info = Label(frame_direita, text="Digito o número", width=15, height=2, relief="flat", anchor="center", font=("Ivy 14 bold"), padx=3, pady=3, fg=preto, bg=branco)
  label_info.place(x=1, y=100)

  label_resultado = Label(frame_direita, text="", width=14, height=2, relief="groove", anchor="center", font=("Ivy 14 bold"), padx=3, pady=3, fg=preto, bg=branco)
  label_resultado.place(x=5, y=190)
    
  entry_numero = Entry(frame_direita, width=9, font=("Ivi 15 bold"), justify="center", relief="solid")
  entry_numero.place(x=5, y=150)

  botao_calcular = Button(frame_direita, command=conversao, text="Calcular", width=6, height=1, relief="raised", overrelief="ridge", anchor="nw", font=("Ivi 10 bold"), bg=azul, fg=branco, padx=7)
  botao_calcular.place(x=110, y=150)


# Configurações do Frame Cima
frame_cima = Frame(window, width=450, height=50, bg=branco, padx=3, relief="flat")
frame_cima.place(x=2, y=2)

label_cima = Label(frame_cima, text="Calculadora de Unidades de Medidas", height=1, relief="flat", anchor="center", font=("Ivy 15 bold"), fg=preto, bg=branco)
label_cima.place(x=50, y=10)


# Configurações do Frame Baixo
frame_baixo = Frame(window, width=450, height=210, bg=branco, padx=3, relief="flat")
frame_baixo.place(x=2, y=55)

# Botões
img_massa = Image.open('images/balance.png')
img_massa = img_massa.resize((50,50), Image.Resampling.LANCZOS)
img_massa = ImageTk.PhotoImage(img_massa)
massa = Button(frame_baixo, command=lambda: menu('massa'), text="Massa", image=img_massa, compound=LEFT, width=114, height=50, relief="flat", overrelief="solid", anchor="nw", font=("ivy 10 bold"), bg=azul, fg=branco)
massa.grid(row=0, column=0, sticky=NSEW, padx=5, pady=5)

img_tempo = Image.open('images/clock.png')
img_tempo = img_tempo.resize((35,35), Image.Resampling.LANCZOS)
img_tempo = ImageTk.PhotoImage(img_tempo)
tempo = Button(frame_baixo, text="Tempo", image=img_tempo, compound=LEFT, width=112, height=50, relief="flat", overrelief="solid", anchor="w", font=("ivy 10 bold"), bg=azul, fg=branco, padx=10)
tempo.grid(row=0, column=1, sticky=NSEW, padx=5, pady=5)

img_comprimento = Image.open('images/length.png')
img_comprimento = img_comprimento.resize((40,40), Image.Resampling.LANCZOS)
img_comprimento = ImageTk.PhotoImage(img_comprimento)
comprimento = Button(frame_baixo, command=lambda: menu('comprimento'), text="Comprimento", image=img_comprimento, compound=LEFT, width=114, height=50, relief="flat", overrelief="solid", anchor="nw", font=("ivy 10 bold"), bg=azul, fg=branco)
comprimento.grid(row=0, column=2, sticky=NSEW, padx=5, pady=5)

img_area = Image.open('images/area.png')
img_area = img_area.resize((40,40), Image.Resampling.LANCZOS)
img_area = ImageTk.PhotoImage(img_area)
area = Button(frame_baixo, command=lambda: menu('area'), text="Área", image=img_area, compound=LEFT, width=112, height=50, relief="flat", overrelief="solid", anchor="w", font=("ivy 10 bold"), bg=azul, fg=branco, padx=9)
area.grid(row=1, column=0, sticky=NSEW, padx=5, pady=5)

img_quantidade = Image.open('images/copo-medidor.png')
img_quantidade = img_quantidade.resize((40,40), Image.Resampling.LANCZOS)
img_quantidade = ImageTk.PhotoImage(img_quantidade)
quantidade = Button(frame_baixo, text="Quantidade", image=img_quantidade, compound=LEFT, width=114, height=50, relief="flat", overrelief="solid", anchor="nw", font=("ivy 10 bold"), bg=azul, fg=branco, padx=7)
quantidade.grid(row=1, column=1, sticky=NSEW, padx=5, pady=5)

img_velocidade = Image.open('images/fast.png')
img_velocidade = img_velocidade.resize((40,40), Image.Resampling.LANCZOS)
img_velocidade = ImageTk.PhotoImage(img_velocidade)
velocidade = Button(frame_baixo, text="Velocidade", image=img_velocidade, compound=LEFT, width=114, height=50, relief="flat", overrelief="solid", anchor="nw", font=("ivy 10 bold"), bg=azul, fg=branco, padx=7)
velocidade.grid(row=1, column=2, sticky=NSEW, padx=5, pady=5)

img_temperatura = Image.open('images/celsius.png')
img_temperatura = img_temperatura.resize((40,40), Image.Resampling.LANCZOS)
img_temperatura = ImageTk.PhotoImage(img_temperatura)
temperatura = Button(frame_baixo, text="Temperatura", image=img_temperatura, compound=LEFT, width=114, height=50, relief="flat", overrelief="solid", anchor="nw", font=("ivy 10 bold"), bg=azul, fg=branco, padx=3)
temperatura.grid(row=2, column=0, sticky=NSEW, padx=5, pady=5)

img_energia = Image.open('images/energia-eletrica.png')
img_energia = img_energia.resize((40,40), Image.Resampling.LANCZOS)
img_energia = ImageTk.PhotoImage(img_energia)
energia = Button(frame_baixo, text="Energia", image=img_energia, compound=LEFT, width=112, height=50, relief="flat", overrelief="solid", anchor="nw", font=("ivy 10 bold"), bg=azul, fg=branco, padx=10)
energia.grid(row=2, column=1, sticky=NSEW, padx=5, pady=5)

img_pressao = Image.open('images/medidor-eletrico.png')
img_pressao = img_pressao.resize((40,40), Image.Resampling.LANCZOS)
img_pressao = ImageTk.PhotoImage(img_pressao)
pressao = Button(frame_baixo, text="Pressao", image=img_pressao, compound=LEFT, width=114, height=50, relief="flat", overrelief="solid", anchor="nw", font=("ivy 10 bold"), bg=azul, fg=branco, padx=10)
pressao.grid(row=2, column=2, sticky=NSEW, padx=5, pady=5)


# Configurações do Frame Direita
frame_direita = Frame(window, width=210, height=260, bg=branco, padx=3, relief="flat")
frame_direita.place(x=455, y=2)

label_direita = Label(frame_direita, width=15, height=2, relief="groove", anchor="center", font=("Ivy 15 bold"), fg=preto, bg=branco)
label_direita.place(x=1, y=0)

# Botões
label_de = Label(frame_direita, text="De", height=1, relief="groove", anchor="center", font=("Ivy 9 bold"), fg=preto, bg=branco)
label_de.place(x=10, y=70)
botao_de = ttk.Combobox(frame_direita, width=5, justify=('center'), font=('Ivy 8 bold'))
botao_de.place(x=34, y=70)

label_para = Label(frame_direita, text="Para", height=1, relief="groove", anchor="center", font=("Ivy 9 bold"), fg=preto, bg=branco)
label_para.place(x=100, y=70)
botao_para = ttk.Combobox(frame_direita, width=5, justify=('center'), font=('Ivy 8 bold'))
botao_para.place(x=136, y=70)

window.mainloop()