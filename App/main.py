from database import db, Tarefas
from os import system
import datetime as dt
from winotify import Notification, audio

try:
    db.connect()
except:
    pass

db.create_tables([Tarefas])

class App():
    def __init__(self):
        pass

    def menu():
        global listaTasks
        system('cls')

        option = 0

        def listaTasks():

            print("\033[32m", end="")
            print("="*75)
            print("\033[m", end="")

            viewTasks = Tarefas.select()
            
            print(f"ID  |  Tarefa  | Descrição  | Prazo")

            for t in viewTasks:
                if t.check == True:

                    print("\033[32m", end="")
                    print(f"{t.id} | {t.nome} | {t.descricao} | {t.prazo}")
                    print("\033[m", end="")

                else:
                    if t.view == True:
                        print(f"\033[34m{t.id}\033[m | {t.nome} | \033[34m{t.descricao}\033[m | {t.prazo}")              

            print("\033[32m")
            print("="*75)
            print("\033[m")

        listaTasks()

        print("[ 1 ] - Adicionar Task")
        print("[ 2 ] - Marcar Task")
        print("[ 3 ] - Deletar Task")

        while option != 1 or option != 2 or option != 3:
            option = int(input("Digite a opção desejada: "))

            if option == 1:
                App.addTask()
            elif option == 2:
                App.checkTask()
            elif option == 3:
                App.deleteTask()
            else:
                print("Valor inválido, tente novamente!")


    def addTask():
        system('cls')

        hoje = dt.datetime.now()
        data = hoje.date()
        horas = hoje.hour
        minutos = hoje.minute

        horario = f"{horas}:{minutos}"

        print("\033[32mAdicionar Task\033[m")

        nome = input("Digite o nome da Task: ")
        descricao = input("Digite a descrição: ")
        prazo = int(input("Digite o prazo em minutos: "))
        view = True
        check = False
        horas = horario

        Tarefas.create(nome=nome, descricao=descricao, prazo=prazo, view=view, check=check, horario=horas, data=data)

        App.notificacao(titulo="Tarefa adicionada com sucesso!", mensagem="Não deixe de fazer a sua tarefa, isso pode acabar atrasando a sua vida depois.")

        App.menu()

    def checkTask():
        system('cls')

        listaTasks()

        opcao = int(input("Diga qual task deseja marcar pelo ID: "))

        marcarTask = Tarefas.get(Tarefas.id == opcao)
        marcarTask.check = True
        marcarTask.save()
        
        App.notificacao(titulo="Tarefa realizada com sucesso!", mensagem="Parabéns, você concluiu a sua tarefa, estou tão orgulhoso. Agora você está uma passo mais próximo de concluir o seu objetivo.")

        App.menu()

    def deleteTask():
        system('cls')

        listaTasks()

        opcao = int(input("Diga qual task deseja deletar pelo ID: "))

        deletarTask = Tarefas.get(Tarefas.id == opcao)
        deletarTask.view = False
        deletarTask.save()

        App.notificacao(titulo="Tarefa deletada com sucesso!", mensagem="As vezes não conseguimos concluir alguns projetos, isso é normal, apenas continue e se dedique ao máximo.")

        App.menu()

    def notificacao(titulo, mensagem, duracao="short"):
        notif = Notification(app_id="Assistente de Tarefas", title=titulo, msg=mensagem, duration=duracao, icon=r"C:\Users\muril\OneDrive\Documentos\Meus Projetos\Assistente-de-Tarefas\image\check.png")
        notif.set_audio(audio.Mail, loop=False)

        notif.show()


App.menu()

