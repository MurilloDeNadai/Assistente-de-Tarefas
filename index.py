from database import db, Tarefas
from os import system
import datetime as dt
from winotify import Notification, audio
import random



try:
    db.connect()
except:
    pass

db.create_tables([Tarefas])


def nome():

    returnTasks = list()

    viewTasks = Tarefas.select()


    for t in viewTasks:
        if t.check == True:
            pass

        else:
            if t.view == True:
                returnTasks.append(t.nome)

    return returnTasks


def desc():

    returnDesc = list()

    viewDesc = Tarefas.select()


    for t in viewDesc:
        if t.check == True:
            pass

        else:
            if t.view == True:
                returnDesc.append(t.descricao)

    return returnDesc


def addTask(name, desc, pr):

    hoje = dt.datetime.now()
    data = hoje.date()
    horas = hoje.hour
    minutos = hoje.minute

    horario = f"{horas}:{minutos}"

    nome = name
    descricao = desc
    prazo = pr
    view = True
    check = False
    horas = horario

    Tarefas.create(nome=nome, descricao=descricao, prazo=prazo, view=view, check=check, horario=horas, data=data)


def checkTask():
    system('cls')

    opcao = int(input("Diga qual task deseja marcar pelo ID: "))

    marcarTask = Tarefas.get(Tarefas.id == opcao)
    marcarTask.check = True
    marcarTask.save()
    
    notificacao(titulo="Tarefa realizada com sucesso!", mensagem="Parabéns, você concluiu a sua tarefa, estou tão orgulhoso. Agora você está uma passo mais próximo de concluir o seu objetivo.")


def deleteTask(inf):

    if inf == 999:
        deletarTask = Tarefas.select()
        for d in deletarTask:
            d.delete_instance()
    else:
        deletarTask = Tarefas.get(Tarefas.id == inf)
        deletarTask.delete_instance()


    #notificacao(titulo="Tarefa deletada com sucesso!", mensagem="As vezes não conseguimos concluir alguns projetos, isso é normal, apenas continue e se dedique ao máximo.")


def notificacao(titulo, mensagem, duracao="short"):
    notif = Notification(app_id="Assistente de Tarefas", title=titulo, msg=mensagem, duration=duracao)
    notif.set_audio(audio.Mail, loop=False)

    notif.show()

