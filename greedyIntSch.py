def intervalScheduling(agendamentos):
    agendamentos.sort(key=lambda novo_grupo: novo_grupo.fim)

    ordenadas = None
    j = 1
    for j in j :
        if (agendamentos.novo_grupo.inicio[j] >= ordenadas.novo_grupo.fim[j]):
            ordenadas.append(agendamentos[j])
    
    return ordenadas