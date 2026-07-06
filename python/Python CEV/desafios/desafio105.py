
def notas(*notas, sit=False):
    """-> Função para analisar notas e situações de vários alunos.

    Args:
        notas (float): Uma ou mais notas dos alunos (aceita várias notas). 
        sit (bool, optional): Indicando se deve ou não adicionar a situação. Defaults to False.

    Returns:
        dict(): Dicionario com várias informações sobre a situação da turma.
    """
    aluno = {}
    aluno['total'] = len(notas)
    aluno['maior'] = max(notas)
    aluno['menor'] = min(notas)
    aluno['media'] = round(sum(notas) / len(notas), 2)
    if sit == True:
        if aluno['media'] >= 7:
            aluno['situação'] = 'BOA'
        elif 5 <= aluno['media'] < 7:
            aluno['situação'] = 'RAZOÁVEL'
        else:
            aluno['situação'] = 'RUIM'
    return aluno


resp = notas(5.5, 9.5, 10, 6.5, sit=True)
print(resp)

help(notas)
