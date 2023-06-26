from area.models.municipios import Municipios
import csv
import datetime


def run():
    with open('scripts/municipios.csv', mode='r', encoding='utf8') as file:
        reader = csv.reader(file, delimiter=';')
        #next(reader)  # Advance past the header
        Municipios.objects.all().delete()
        for coluna in reader:
            municipios = Municipios(codigo=coluna[0], nome=coluna[1], criado_em=datetime.datetime.now(), atualizado_em=datetime.datetime.now(), estado_id_id='PI')
            municipios.save()