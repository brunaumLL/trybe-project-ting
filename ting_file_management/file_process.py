
from ting_file_management.file_management import txt_importer
import sys


def process(path_file, instance):
    for index in range(len(instance)):
        if instance.search(index)["nome_do_arquivo"] == path_file:
            return None
    txt = txt_importer(path_file)
    data = {
            "nome_do_arquivo": path_file,
            "qtd_linhas": len(txt),
            "linhas_do_arquivo": (txt),
        }
    instance.enqueue(data)
    sys.stdout.write(str(data))
    return data


def remove(instance):
    if instance.__len__() == 0:
        return sys.stdout.write('Não há elementos\n')

    path_file = instance.search(0)["nome_do_arquivo"]
    instance.dequeue()

    return sys.stdout.write(f'Arquivo {path_file} removido com sucesso\n')


def file_metadata(instance, position):
    """Aqui irá sua implementação"""
