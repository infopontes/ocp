from area.models.estados import Estados
import csv
import datetime


def run():
    with open('scripts/estados.csv', mode='r') as file:
        reader = csv.reader(file, delimiter=';')
        #next(reader)  # Advance past the header
        Estados.objects.all().delete()
        for coluna in reader:
            estado = Estados(uf=coluna[0], nome=coluna[1], criado_em=datetime.datetime.now(), atualizado_em=datetime.datetime.now())
            estado.save()