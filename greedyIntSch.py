def intervalScheduling(agendamentos):
    # Ordena os agendamentos por tempo de término
    agendamentos.sort(key=lambda x: x.fim)
    
    solucao = []
   
    for agendamento in agendamentos:
        # Se a solução está vazia ou o agendamento não conflita com o último adicionado
        if not solucao or agendamento.inicio >= solucao[-1].fim:
            solucao.append(agendamento)

    return solucao
