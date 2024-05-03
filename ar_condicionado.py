# consumo_hora = 15.7
# horas = float(input('Quantas horas por dia: '))
# dias = float(input('Quantos dias: '))
# tarifa = 1.11625
# consumo_total = (consumo_hora * horas * tarifa) / 30 * dias

# print(f'O consumo total é de {consumo_total:.2f} reais')

# import customtkinter as ctk

# def calcular_consumo():
#     consumo_hora = 15.7
#     horas = float(entry_horas.get())
#     dias = float(entry_dias.get())
#     tarifa = 1.11625
#     consumo_total = (consumo_hora * horas * tarifa) / 30 * dias
#     label_resultado.configure(text=f'O consumo total é de {consumo_total:.2f} reais')

# # Criando a janela principal
# root = ctk.CTk()
# root.title("Calculadora de Consumo")

# # Criando os widgets
# label_horas = ctk.CTkLabel(root, text="Quantas horas por dia:")
# label_horas.grid(row=0, column=0, padx=10, pady=5, sticky="w")
# entry_horas = ctk.CTkEntry(root)
# entry_horas.grid(row=0, column=1, padx=10, pady=5)

# label_dias = ctk.CTkLabel(root, text="Quantos dias:")
# label_dias.grid(row=1, column=0, padx=10, pady=5, sticky="w")
# entry_dias = ctk.CTkEntry(root)
# entry_dias.grid(row=1, column=1, padx=10, pady=5)

# button_calcular = ctk.CTkButton(root, text="Calcular", command=calcular_consumo)
# button_calcular.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

# label_resultado = ctk.CTkLabel(root, text="")
# label_resultado.grid(row=3, column=0, columnspan=2, padx=10, pady=5)

# # Rodando o loop principal
# root.mainloop()

import streamlit as st

def calcular_consumo():
    consumo_hora = 15.7
    horas = int(entry_horas)
    dias = int(entry_dias)
    tarifa = 1.11625
    consumo_total = (consumo_hora * horas * tarifa) / 30 * dias
    st.write(f'O consumo total é de {consumo_total:.2f} reais')

# Criando os elementos de interface
st.title("Calculadora de Consumo")

horas = st.number_input("Quantas horas por dia:")
dias = st.number_input("Quantos dias:")

# Capturando os valores inseridos pelo usuário
entry_horas = horas
entry_dias = dias

# Botão para calcular o consumo
if st.button("Calcular"):
    calcular_consumo()



