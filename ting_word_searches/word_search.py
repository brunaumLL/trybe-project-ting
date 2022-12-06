def exists_word(word, instance):
    occurrences = []
    result = []
    for index in range(len(instance)):
        file = instance.search(index)
        lines = file['linhas_do_arquivo']
        for index in range(len(lines)):
            if word.lower() in lines[index].lower():
                occurrences.append({'linha': index + 1})
        
        if len(occurrences) >= 1:
            result.append({
                'palavra': word,
                'arquivo': file['nome_do_arquivo'],
                'ocorrencias': occurrences
            })

    return result


def search_by_word(word, instance):
    """Aqui irá sua implementação"""
