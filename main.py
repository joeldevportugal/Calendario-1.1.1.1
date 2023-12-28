import customtkinter
from tkinter import *
import calendar
import threading

# defenir cores -------------------------------------------------------------------------------------------
co0 = '#0000FF' # cor  azul para o background calendario 
co1 = '#FFFFFF' # cor branca para o texto
#----------------------------------------------------------------------------------------------------------

# função -------------------------------------------------------------------------------------------------
def mostrar_calendario():
    ano = int(entrada_ano.get())
    mes = int(entrada_mes.get())

    cal = calendar.monthcalendar(ano, mes)

    # Limpar o frame do calendário antes de exibir um novo
    for widget in frame_calendario.winfo_children():
        widget.destroy()

    # Cabeçalho do calendário
    dias_semana = ['Seg', 'Ter', 'Qua', 'Qui', 'Sex', 'Sáb', 'Dom']
    for col, dia in enumerate(dias_semana):
        label_dia = Label(frame_calendario, text=dia, font=('arial', 17, 'bold'),bg=co0, fg=co1)
        label_dia.grid(row=0, column=col, padx=10, pady=5)

    # Dias do mês
    for row, week in enumerate(cal, start=1):
        for col, day in enumerate(week):
            if day == 0:
                label_dia = Label(frame_calendario, text='', font=('arial', 15),bg=co0)
            else:
                label_dia = Label(frame_calendario, text=str(day), font=('arial', 18),bg=co0,fg=co1)

            label_dia.grid(row=row, column=col, padx=10, pady=5)
#---------------------------------------------------------------------------------------------------------            

# Configuração da janela principal -----------------------------------------------------------------------
janela = customtkinter.CTk()
janela.title('Calendário dev Joel Python')
janela.geometry('400x330+100+100')
janela.resizable(False, False)
janela.config(bg=co0)
janela.iconbitmap(r'C:\Users\HP\Desktop\Programas em python\Calendario\calendario 1.1.1\icon.ico')
#---------------------------------------------------------------------------------------------------------
# Criar entradas de ano e mês ----------------------------------------------------------------------------
Label(janela, text='Ano:', font=('arial', 18),bg=co0, fg=co1).place(x=10, y=10)
entrada_ano = Entry(janela, width=10, font=('arial', 18))
entrada_ano.place(x=68, y=10)

Label(janela, text='Mês:', font=('arial', 18),bg=co0, fg=co1).place(x=205, y=10)
entrada_mes = Spinbox(janela, from_=1, to=12, font=('arial', 18), width=5)
entrada_mes.place(x=265, y=10)
#----------------------------------------------------------------------------------------------------------
# Botão para mostrar o calendário -------------------------------------------------------------------------
btn_mostrar_calendario = customtkinter.CTkButton(janela, text='Mostrar Calendário', bg_color=co0,text_color=co1, command=mostrar_calendario, font=('arial', 18))
btn_mostrar_calendario.place(x=10, y=290)
#----------------------------------------------------------------------------------------------------------
# Frame para o calendário ---------------------------------------------------------------------------------
frame_calendario = Frame(janela, bg=co0)
frame_calendario.place(x=10, y=50)
#----------------------------------------------------------------------------------------------------------
janela.mainloop()
