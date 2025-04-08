from peewee import *

db = SqliteDatabase('tarefas.db')

class Tarefas(Model):
    nome = CharField()
    descricao = TextField()
    prazo = DecimalField()
    view = BooleanField()
    check = BooleanField()
    horario = CharField()
    data = CharField()


    class Meta:
        database = db
