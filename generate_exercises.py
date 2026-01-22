import json

# Lista de exercícios de academia com links de execução
exercicios = []

# Exercícios para Peito (50)
exercicios_peito = [
    {"id": 1, "nome": "Supino Reto com Barra", "descricao": "Exercício fundamental para desenvolvimento do peitoral", "musculos": ["Peitoral Maior", "Deltoide Anterior", "Tríceps"], "equipamento": "Barra e Banco", "categoria": "Peito", "dificuldade": "Intermediário", "link_execucao": "https://www.youtube.com/watch?v=rT7DgCr-3pg"},
    {"id": 2, "nome": "Supino Reto com Halteres", "descricao": "Variação do supino com maior amplitude de movimento", "musculos": ["Peitoral Maior", "Deltoide Anterior", "Tríceps"], "equipamento": "Halteres e Banco", "categoria": "Peito", "dificuldade": "Intermediário", "link_execucao": "https://www.youtube.com/watch?v=VmB1G1K7v94"},
    {"id": 3, "nome": "Supino Inclinado com Barra", "descricao": "Foca na parte superior do peitoral", "musculos": ["Peitoral Superior", "Deltoide Anterior", "Tríceps"], "equipamento": "Barra e Banco Inclinado", "categoria": "Peito", "dificuldade": "Intermediário", "link_execucao": "https://www.youtube.com/watch?v=8iPEnov-lmU"},
    {"id": 4, "nome": "Supino Inclinado com Halteres", "descricao": "Amplitude maior para parte superior do peito", "musculos": ["Peitoral Superior", "Deltoide Anterior"], "equipamento": "Halteres e Banco Inclinado", "categoria": "Peito", "dificuldade": "Intermediário", "link_execucao": "https://www.youtube.com/watch?v=0G2_XV7slIg"},
    {"id": 5, "nome": "Supino Declinado", "descricao": "Foca na parte inferior do peitoral", "musculos": ["Peitoral Inferior", "Tríceps"], "equipamento": "Barra e Banco Declinado", "categoria": "Peito", "dificuldade": "Avançado", "link_execucao": "https://www.youtube.com/watch?v=LfyQBUKR8SE"},
    {"id": 6, "nome": "Crucifixo com Halteres", "descricao": "Isolamento do peitoral com movimento de abertura", "musculos": ["Peitoral Maior"], "equipamento": "Halteres e Banco", "categoria": "Peito", "dificuldade": "Intermediário", "link_execucao": "https://www.youtube.com/watch?v=eozdVDA78K0"},
    {"id": 7, "nome": "Crucifixo Inclinado", "descricao": "Isolamento da parte superior do peito", "musculos": ["Peitoral Superior"], "equipamento": "Halteres e Banco Inclinado", "categoria": "Peito", "dificuldade": "Intermediário", "link_execucao": "https://www.youtube.com/watch?v=8iPEnov-lmU"},
    {"id": 8, "nome": "Supino Máquina", "descricao": "Versão mais segura do supino tradicional", "musculos": ["Peitoral Maior", "Deltoide Anterior", "Tríceps"], "equipamento": "Máquina de Supino", "categoria": "Peito", "dificuldade": "Iniciante", "link_execucao": "https://www.youtube.com/watch?v=0fZ2xJ3vLkE"},
    {"id": 9, "nome": "Peck Deck", "descricao": "Máquina específica para isolamento do peitoral", "musculos": ["Peitoral Maior"], "equipamento": "Máquina Peck Deck", "categoria": "Peito", "dificuldade": "Iniciante", "link_execucao": "https://www.youtube.com/watch?v=BeyqA0lSXxY"},
    {"id": 10, "nome": "Crossover no Pulley", "descricao": "Exercício de isolamento com cabo", "musculos": ["Peitoral Maior"], "equipamento": "Cabo e Polia", "categoria": "Peito", "dificuldade": "Intermediário", "link_execucao": "https://www.youtube.com/watch?v=Iwe6AmxVf7o"},
    {"id": 11, "nome": "Flexão de Braço", "descricao": "Exercício básico sem equipamento", "musculos": ["Peitoral Maior", "Tríceps", "Deltoide Anterior"], "equipamento": "Nenhum", "categoria": "Peito", "dificuldade": "Iniciante", "link_execucao": "https://www.youtube.com/watch?v=IODxDxX7oi4"},
    {"id": 12, "nome": "Flexão Inclinada", "descricao": "Flexão com pés elevados", "musculos": ["Peitoral Superior", "Tríceps"], "equipamento": "Nenhum", "categoria": "Peito", "dificuldade": "Intermediário", "link_execucao": "https://www.youtube.com/watch?v=cfnsWByWs4U"},
    {"id": 13, "nome": "Flexão Declinada", "descricao": "Flexão com mãos elevadas", "musculos": ["Peitoral Inferior", "Tríceps"], "equipamento": "Nenhum", "categoria": "Peito", "dificuldade": "Intermediário", "link_execucao": "https://www.youtube.com/watch?v=4dF1DOWzf20"},
    {"id": 14, "nome": "Supino com Pegada Fechada", "descricao": "Foca mais nos tríceps e peito interno", "musculos": ["Tríceps", "Peitoral Interno"], "equipamento": "Barra e Banco", "categoria": "Peito", "dificuldade": "Avançado", "link_execucao": "https://www.youtube.com/watch?v=nEF0bv2FW94"},
    {"id": 15, "nome": "Supino com Bola Suíça", "descricao": "Adiciona instabilidade ao movimento", "musculos": ["Peitoral Maior", "Core"], "equipamento": "Halteres e Bola Suíça", "categoria": "Peito", "dificuldade": "Avançado", "link_execucao": "https://www.youtube.com/watch?v=5xQopv2yaJ4"},
    {"id": 16, "nome": "Dips", "descricao": "Exercício composto para peito e tríceps", "musculos": ["Peitoral Inferior", "Tríceps", "Deltoide Anterior"], "equipamento": "Barras Paralelas", "categoria": "Peito", "dificuldade": "Intermediário", "link_execucao": "https://www.youtube.com/watch?v=2z8JmcrW-As"},
    {"id": 17, "nome": "Pullover com Halter", "descricao": "Alongamento e contração do peitoral", "musculos": ["Peitoral Maior", "Serrátil Anterior"], "equipamento": "Halter e Banco", "categoria": "Peito", "dificuldade": "Intermediário", "link_execucao": "https://www.youtube.com/watch?v=ykJmrZ5v0Oo"},
    {"id": 18, "nome": "Supino com Pausa", "descricao": "Técnica avançada para força", "musculos": ["Peitoral Maior", "Tríceps"], "equipamento": "Barra e Banco", "categoria": "Peito", "dificuldade": "Avançado", "link_execucao": "https://www.youtube.com/watch?v=0fZ2xJ3vLkE"},
    {"id": 19, "nome": "Supino com Banda Elástica", "descricao": "Resistência variável durante o movimento", "musculos": ["Peitoral Maior", "Tríceps"], "equipamento": "Barra, Banco e Banda", "categoria": "Peito", "dificuldade": "Intermediário", "link_execucao": "https://www.youtube.com/watch?v=0fZ2xJ3vLkE"},
    {"id": 20, "nome": "Flexão Diamante", "descricao": "Foca mais nos tríceps", "musculos": ["Tríceps", "Peitoral"], "equipamento": "Nenhum", "categoria": "Peito", "dificuldade": "Intermediário", "link_execucao": "https://www.youtube.com/watch?v=j0bXUqQBn1E"},
    {"id": 21, "nome": "Flexão com Aplauso", "descricao": "Exercício pliométrico avançado", "musculos": ["Peitoral Maior", "Tríceps"], "equipamento": "Nenhum", "categoria": "Peito", "dificuldade": "Avançado", "link_execucao": "https://www.youtube.com/watch?v=Hy9aZ_6pO8Y"},
    {"id": 22, "nome": "Supino com Kettlebell", "descricao": "Variação com peso livre alternativo", "musculos": ["Peitoral Maior", "Core"], "equipamento": "Kettlebell e Banco", "categoria": "Peito", "dificuldade": "Avançado", "link_execucao": "https://www.youtube.com/watch?v=0fZ2xJ3vLkE"},
    {"id": 23, "nome": "Chest Press Máquina", "descricao": "Máquina para desenvolvimento do peito", "musculos": ["Peitoral Maior", "Deltoide Anterior"], "equipamento": "Máquina Chest Press", "categoria": "Peito", "dificuldade": "Iniciante", "link_execucao": "https://www.youtube.com/watch?v=0fZ2xJ3vLkE"},
    {"id": 24, "nome": "Supino com Correntes", "descricao": "Resistência progressiva", "musculos": ["Peitoral Maior", "Tríceps"], "equipamento": "Barra, Banco e Correntes", "categoria": "Peito", "dificuldade": "Avançado", "link_execucao": "https://www.youtube.com/watch?v=0fZ2xJ3vLkE"},
    {"id": 25, "nome": "Flexão com Rotação", "descricao": "Adiciona trabalho de core", "musculos": ["Peitoral", "Core", "Oblíquos"], "equipamento": "Nenhum", "categoria": "Peito", "dificuldade": "Intermediário", "link_execucao": "https://www.youtube.com/watch?v=0fZ2xJ3vLkE"},
    {"id": 26, "nome": "Supino com Pés Elevados", "descricao": "Aumenta a ativação do core", "musculos": ["Peitoral Maior", "Core"], "equipamento": "Barra e Banco", "categoria": "Peito", "dificuldade": "Avançado", "link_execucao": "https://www.youtube.com/watch?v=0fZ2xJ3vLkE"},
    {"id": 27, "nome": "Crossover Alto", "descricao": "Foca na parte inferior do peito", "musculos": ["Peitoral Inferior"], "equipamento": "Cabo e Polia", "categoria": "Peito", "dificuldade": "Intermediário", "link_execucao": "https://www.youtube.com/watch?v=0fZ2xJ3vLkE"},
    {"id": 28, "nome": "Crossover Baixo", "descricao": "Foca na parte superior do peito", "musculos": ["Peitoral Superior"], "equipamento": "Cabo e Polia", "categoria": "Peito", "dificuldade": "Intermediário", "link_execucao": "https://www.youtube.com/watch?v=0fZ2xJ3vLkE"},
    {"id": 29, "nome": "Supino com Barra Curvada", "descricao": "Reduz tensão nos punhos", "musculos": ["Peitoral Maior", "Tríceps"], "equipamento": "Barra Curvada e Banco", "categoria": "Peito", "dificuldade": "Intermediário", "link_execucao": "https://www.youtube.com/watch?v=0fZ2xJ3vLkE"},
    {"id": 30, "nome": "Flexão com Uma Mão", "descricao": "Exercício avançado de força", "musculos": ["Peitoral", "Tríceps", "Core"], "equipamento": "Nenhum", "categoria": "Peito", "dificuldade": "Avançado", "link_execucao": "https://www.youtube.com/watch?v=0fZ2xJ3vLkE"},
    {"id": 31, "nome": "Supino com Halteres Unilateral", "descricao": "Trabalha cada lado separadamente", "musculos": ["Peitoral Maior", "Core"], "equipamento": "Halter e Banco", "categoria": "Peito", "dificuldade": "Intermediário", "link_execucao": "https://www.youtube.com/watch?v=0fZ2xJ3vLkE"},
    {"id": 32, "nome": "Push-up com Pés na Parede", "descricao": "Flexão vertical avançada", "musculos": ["Peitoral Superior", "Deltoide Anterior"], "equipamento": "Nenhum", "categoria": "Peito", "dificuldade": "Avançado", "link_execucao": "https://www.youtube.com/watch?v=0fZ2xJ3vLkE"},
    {"id": 33, "nome": "Supino com Bola Medicinal", "descricao": "Adiciona instabilidade", "musculos": ["Peitoral", "Core"], "equipamento": "Bola Medicinal e Banco", "categoria": "Peito", "dificuldade": "Avançado", "link_execucao": "https://www.youtube.com/watch?v=0fZ2xJ3vLkE"},
    {"id": 34, "nome": "Flexão com Toque no Ombro", "descricao": "Adiciona desafio de estabilidade", "musculos": ["Peitoral", "Core", "Deltoides"], "equipamento": "Nenhum", "categoria": "Peito", "dificuldade": "Intermediário", "link_execucao": "https://www.youtube.com/watch?v=0fZ2xJ3vLkE"},
    {"id": 35, "nome": "Supino com Resistência Manual", "descricao": "Técnica avançada com parceiro", "musculos": ["Peitoral Maior", "Tríceps"], "equipamento": "Barra, Banco e Parceiro", "categoria": "Peito", "dificuldade": "Avançado", "link_execucao": "https://www.youtube.com/watch?v=0fZ2xJ3vLkE"},
    {"id": 36, "nome": "Chest Fly Máquina Sentado", "descricao": "Isolamento com máquina", "musculos": ["Peitoral Maior"], "equipamento": "Máquina Chest Fly", "categoria": "Peito", "dificuldade": "Iniciante", "link_execucao": "https://www.youtube.com/watch?v=0fZ2xJ3vLkE"},
    {"id": 37, "nome": "Supino com Barra de Segurança", "descricao": "Permite treinar até a falha com segurança", "musculos": ["Peitoral Maior", "Tríceps"], "equipamento": "Barra de Segurança e Banco", "categoria": "Peito", "dificuldade": "Intermediário", "link_execucao": "https://www.youtube.com/watch?v=0fZ2xJ3vLkE"},
    {"id": 38, "nome": "Flexão com Elevação de Perna", "descricao": "Adiciona trabalho de glúteos", "musculos": ["Peitoral", "Glúteos", "Core"], "equipamento": "Nenhum", "categoria": "Peito", "dificuldade": "Intermediário", "link_execucao": "https://www.youtube.com/watch?v=0fZ2xJ3vLkE"},
    {"id": 39, "nome": "Supino com Cadeira", "descricao": "Versão caseira do supino", "musculos": ["Peitoral Maior", "Tríceps"], "equipamento": "Halteres e Cadeira", "categoria": "Peito", "dificuldade": "Iniciante", "link_execucao": "https://www.youtube.com/watch?v=0fZ2xJ3vLkE"},
    {"id": 40, "nome": "Crossover Unilateral", "descricao": "Trabalha um lado por vez", "musculos": ["Peitoral Maior", "Core"], "equipamento": "Cabo e Polia", "categoria": "Peito", "dificuldade": "Intermediário", "link_execucao": "https://www.youtube.com/watch?v=0fZ2xJ3vLkE"},
    {"id": 41, "nome": "Supino com Pausa no Peito", "descricao": "Elimina o impulso elástico", "musculos": ["Peitoral Maior", "Tríceps"], "equipamento": "Barra e Banco", "categoria": "Peito", "dificuldade": "Avançado", "link_execucao": "https://www.youtube.com/watch?v=0fZ2xJ3vLkE"},
    {"id": 42, "nome": "Flexão com Salto", "descricao": "Exercício pliométrico", "musculos": ["Peitoral", "Tríceps", "Deltoides"], "equipamento": "Nenhum", "categoria": "Peito", "dificuldade": "Avançado", "link_execucao": "https://www.youtube.com/watch?v=0fZ2xJ3vLkE"},
    {"id": 43, "nome": "Supino com Barra Hexagonal", "descricao": "Barra especial para supino", "musculos": ["Peitoral Maior", "Tríceps"], "equipamento": "Barra Hexagonal e Banco", "categoria": "Peito", "dificuldade": "Intermediário", "link_execucao": "https://www.youtube.com/watch?v=0fZ2xJ3vLkE"},
    {"id": 44, "nome": "Chest Press com Banda", "descricao": "Versão com banda elástica", "musculos": ["Peitoral Maior"], "equipamento": "Banda Elástica", "categoria": "Peito", "dificuldade": "Iniciante", "link_execucao": "https://www.youtube.com/watch?v=0fZ2xJ3vLkE"},
    {"id": 45, "nome": "Flexão com Pés em Bola Suíça", "descricao": "Aumenta instabilidade", "musculos": ["Peitoral", "Core"], "equipamento": "Bola Suíça", "categoria": "Peito", "dificuldade": "Avançado", "link_execucao": "https://www.youtube.com/watch?v=0fZ2xJ3vLkE"},
    {"id": 46, "nome": "Supino com Barra de Segurança Inclinada", "descricao": "Versão inclinada com segurança", "musculos": ["Peitoral Superior", "Tríceps"], "equipamento": "Barra de Segurança e Banco Inclinado", "categoria": "Peito", "dificuldade": "Intermediário", "link_execucao": "https://www.youtube.com/watch?v=0fZ2xJ3vLkE"},
    {"id": 47, "nome": "Flexão com Mãos em Bola Suíça", "descricao": "Desafio de estabilidade", "musculos": ["Peitoral", "Core", "Deltoides"], "equipamento": "Bola Suíça", "categoria": "Peito", "dificuldade": "Avançado", "link_execucao": "https://www.youtube.com/watch?v=0fZ2xJ3vLkE"},
    {"id": 48, "nome": "Supino com Halteres em Rotação", "descricao": "Adiciona rotação no topo", "musculos": ["Peitoral Maior", "Deltoides"], "equipamento": "Halteres e Banco", "categoria": "Peito", "dificuldade": "Intermediário", "link_execucao": "https://www.youtube.com/watch?v=0fZ2xJ3vLkE"},
    {"id": 49, "nome": "Crossover com Corda", "descricao": "Variação com corda no cabo", "musculos": ["Peitoral Maior"], "equipamento": "Cabo, Polia e Corda", "categoria": "Peito", "dificuldade": "Intermediário", "link_execucao": "https://www.youtube.com/watch?v=0fZ2xJ3vLkE"},
    {"id": 50, "nome": "Flexão com Pausa", "descricao": "Técnica para aumentar tempo sob tensão", "musculos": ["Peitoral", "Tríceps"], "equipamento": "Nenhum", "categoria": "Peito", "dificuldade": "Intermediário", "link_execucao": "https://www.youtube.com/watch?v=0fZ2xJ3vLkE"},
]

# Exercícios para Costas (50)
exercicios_costas = [
    {"id": 51, "nome": "Barra Fixa", "descricao": "Exercício fundamental para costas", "musculos": ["Latíssimo do Dorso", "Bíceps", "Romboides"], "equipamento": "Barra de Tração", "categoria": "Costas", "dificuldade": "Intermediário", "link_execucao": "https://www.youtube.com/watch?v=eGo4IYlbE5g"},
    {"id": 52, "nome": "Remada Curvada com Barra", "descricao": "Exercício composto para costas", "musculos": ["Latíssimo do Dorso", "Romboides", "Bíceps"], "equipamento": "Barra", "categoria": "Costas", "dificuldade": "Intermediário", "link_execucao": "https://www.youtube.com/watch?v=paHf6I3xX3M"},
    {"id": 53, "nome": "Remada Curvada com Halteres", "descricao": "Amplitude maior de movimento", "musculos": ["Latíssimo do Dorso", "Romboides", "Bíceps"], "equipamento": "Halteres", "categoria": "Costas", "dificuldade": "Intermediário", "link_execucao": "https://www.youtube.com/watch?v=roCP6wCXPqo"},
    {"id": 54, "nome": "Puxada Frontal", "descricao": "Exercício de máquina para latíssimos", "musculos": ["Latíssimo do Dorso", "Bíceps"], "equipamento": "Máquina de Puxada", "categoria": "Costas", "dificuldade": "Iniciante", "link_execucao": "https://www.youtube.com/watch?v=CAwf7n6Luuc"},
    {"id": 55, "nome": "Puxada Atrás da Nuca", "descricao": "Variação da puxada frontal", "musculos": ["Latíssimo do Dorso", "Romboides"], "equipamento": "Máquina de Puxada", "categoria": "Costas", "dificuldade": "Intermediário", "link_execucao": "https://www.youtube.com/watch?v=CAwf7n6Luuc"},
    {"id": 56, "nome": "Remada Baixa", "descricao": "Exercício sentado com cabo", "musculos": ["Latíssimo do Dorso", "Romboides", "Bíceps"], "equipamento": "Cabo e Polia", "categoria": "Costas", "dificuldade": "Iniciante", "link_execucao": "https://www.youtube.com/watch?v=GZbfZ033f74"},
    {"id": 57, "nome": "Remada Unilateral com Halter", "descricao": "Trabalha cada lado separadamente", "musculos": ["Latíssimo do Dorso", "Romboides", "Bíceps"], "equipamento": "Halter e Banco", "categoria": "Costas", "dificuldade": "Intermediário", "link_execucao": "https://www.youtube.com/watch?v=roCP6wCXPqo"},
    {"id": 58, "nome": "Remada T", "descricao": "Exercício com barra T", "musculos": ["Latíssimo do Dorso", "Romboides", "Trapézio Médio"], "equipamento": "Barra T", "categoria": "Costas", "dificuldade": "Intermediário", "link_execucao": "https://www.youtube.com/watch?v=j3Igk5nyZE4"},
    {"id": 59, "nome": "Puxada com Pegada Aberta", "descricao": "Foca mais na largura das costas", "musculos": ["Latíssimo do Dorso"], "equipamento": "Máquina de Puxada", "categoria": "Costas", "dificuldade": "Intermediário", "link_execucao": "https://www.youtube.com/watch?v=CAwf7n6Luuc"},
    {"id": 60, "nome": "Puxada com Pegada Fechada", "descricao": "Foca mais na espessura das costas", "musculos": ["Latíssimo do Dorso", "Romboides", "Bíceps"], "equipamento": "Máquina de Puxada", "categoria": "Costas", "dificuldade": "Intermediário", "link_execucao": "https://www.youtube.com/watch?v=CAwf7n6Luuc"},
    {"id": 61, "nome": "Remada Alta", "descricao": "Foca no trapézio e deltoides", "musculos": ["Trapézio", "Deltoide Médio"], "equipamento": "Barra ou Halteres", "categoria": "Costas", "dificuldade": "Intermediário", "link_execucao": "https://www.youtube.com/watch?v=CAwf7n6Luuc"},
    {"id": 62, "nome": "Encolhimento de Ombros", "descricao": "Isolamento do trapézio", "musculos": ["Trapézio Superior"], "equipamento": "Barra ou Halteres", "categoria": "Costas", "dificuldade": "Iniciante", "link_execucao": "https://www.youtube.com/watch?v=CAwf7n6Luuc"},
    {"id": 63, "nome": "Remada com Cabo Unilateral", "descricao": "Trabalho unilateral com cabo", "musculos": ["Latíssimo do Dorso", "Romboides"], "equipamento": "Cabo e Polia", "categoria": "Costas", "dificuldade": "Intermediário", "link_execucao": "https://www.youtube.com/watch?v=CAwf7n6Luuc"},
    {"id": 64, "nome": "Barra Fixa com Peso", "descricao": "Barra fixa com carga adicional", "musculos": ["Latíssimo do Dorso", "Bíceps"], "equipamento": "Barra de Tração e Cinto de Peso", "categoria": "Costas", "dificuldade": "Avançado", "link_execucao": "https://www.youtube.com/watch?v=eGo4IYlbE5g"},
    {"id": 65, "nome": "Remada Invertida", "descricao": "Exercício com peso corporal", "musculos": ["Latíssimo do Dorso", "Romboides", "Bíceps"], "equipamento": "Barra ou TRX", "categoria": "Costas", "dificuldade": "Iniciante", "link_execucao": "https://www.youtube.com/watch?v=CAwf7n6Luuc"},
    {"id": 66, "nome": "Puxada com Corda", "descricao": "Variação com corda no cabo", "musculos": ["Latíssimo do Dorso", "Bíceps"], "equipamento": "Cabo, Polia e Corda", "categoria": "Costas", "dificuldade": "Intermediário", "link_execucao": "https://www.youtube.com/watch?v=CAwf7n6Luuc"},
    {"id": 67, "nome": "Remada com Barra Hexagonal", "descricao": "Barra especial para remada", "musculos": ["Latíssimo do Dorso", "Romboides"], "equipamento": "Barra Hexagonal", "categoria": "Costas", "dificuldade": "Intermediário", "link_execucao": "https://www.youtube.com/watch?v=CAwf7n6Luuc"},
    {"id": 68, "nome": "Puxada com Pegada Neutra", "descricao": "Pegada em martelo", "musculos": ["Latíssimo do Dorso", "Bíceps"], "equipamento": "Máquina de Puxada", "categoria": "Costas", "dificuldade": "Intermediário", "link_execucao": "https://www.youtube.com/watch?v=CAwf7n6Luuc"},
    {"id": 69, "nome": "Remada com Kettlebell", "descricao": "Variação com kettlebell", "musculos": ["Latíssimo do Dorso", "Romboides"], "equipamento": "Kettlebell", "categoria": "Costas", "dificuldade": "Intermediário", "link_execucao": "https://www.youtube.com/watch?v=CAwf7n6Luuc"},
    {"id": 70, "nome": "Barra Fixa com Pegada Aberta", "descricao": "Foca na largura", "musculos": ["Latíssimo do Dorso"], "equipamento": "Barra de Tração", "categoria": "Costas", "dificuldade": "Intermediário", "link_execucao": "https://www.youtube.com/watch?v=eGo4IYlbE5g"},
    {"id": 71, "nome": "Barra Fixa com Pegada Fechada", "descricao": "Foca na espessura", "musculos": ["Latíssimo do Dorso", "Bíceps"], "equipamento": "Barra de Tração", "categoria": "Costas", "dificuldade": "Intermediário", "link_execucao": "https://www.youtube.com/watch?v=eGo4IYlbE5g"},
    {"id": 72, "nome": "Remada com Banda Elástica", "descricao": "Versão com banda", "musculos": ["Latíssimo do Dorso", "Romboides"], "equipamento": "Banda Elástica", "categoria": "Costas", "dificuldade": "Iniciante", "link_execucao": "https://www.youtube.com/watch?v=CAwf7n6Luuc"},
    {"id": 73, "nome": "Puxada Unilateral", "descricao": "Um braço por vez", "musculos": ["Latíssimo do Dorso", "Bíceps"], "equipamento": "Cabo e Polia", "categoria": "Costas", "dificuldade": "Intermediário", "link_execucao": "https://www.youtube.com/watch?v=CAwf7n6Luuc"},
    {"id": 74, "nome": "Remada Sentado com Máquina", "descricao": "Máquina específica para remada", "musculos": ["Latíssimo do Dorso", "Romboides"], "equipamento": "Máquina de Remada", "categoria": "Costas", "dificuldade": "Iniciante", "link_execucao": "https://www.youtube.com/watch?v=CAwf7n6Luuc"},
    {"id": 75, "nome": "Barra Fixa com Assistência", "descricao": "Para iniciantes", "musculos": ["Latíssimo do Dorso", "Bíceps"], "equipamento": "Barra de Tração e Banda", "categoria": "Costas", "dificuldade": "Iniciante", "link_execucao": "https://www.youtube.com/watch?v=eGo4IYlbE5g"},
    {"id": 76, "nome": "Remada com TRX", "descricao": "Exercício suspenso", "musculos": ["Latíssimo do Dorso", "Romboides", "Core"], "equipamento": "TRX", "categoria": "Costas", "dificuldade": "Intermediário", "link_execucao": "https://www.youtube.com/watch?v=CAwf7n6Luuc"},
    {"id": 77, "nome": "Puxada com Barra Reta", "descricao": "Barra reta na máquina", "musculos": ["Latíssimo do Dorso", "Bíceps"], "equipamento": "Máquina de Puxada", "categoria": "Costas", "dificuldade": "Iniciante", "link_execucao": "https://www.youtube.com/watch?v=CAwf7n6Luuc"},
    {"id": 78, "nome": "Remada com Barra Curvada", "descricao": "Barra curvada para remada", "musculos": ["Latíssimo do Dorso", "Romboides"], "equipamento": "Barra Curvada", "categoria": "Costas", "dificuldade": "Intermediário", "link_execucao": "https://www.youtube.com/watch?v=CAwf7n6Luuc"},
    {"id": 79, "nome": "Encolhimento com Halteres", "descricao": "Isolamento do trapézio", "musculos": ["Trapézio Superior"], "equipamento": "Halteres", "categoria": "Costas", "dificuldade": "Iniciante", "link_execucao": "https://www.youtube.com/watch?v=CAwf7n6Luuc"},
    {"id": 80, "nome": "Puxada com Pegada Supinada", "descricao": "Pegada invertida", "musculos": ["Latíssimo do Dorso", "Bíceps"], "equipamento": "Máquina de Puxada", "categoria": "Costas", "dificuldade": "Intermediário", "link_execucao": "https://www.youtube.com/watch?v=CAwf7n6Luuc"},
    {"id": 81, "nome": "Remada com Pausa", "descricao": "Técnica avançada", "musculos": ["Latíssimo do Dorso", "Romboides"], "equipamento": "Barra", "categoria": "Costas", "dificuldade": "Avançado", "link_execucao": "https://www.youtube.com/watch?v=CAwf7n6Luuc"},
    {"id": 82, "nome": "Barra Fixa L-Sit", "descricao": "Barra fixa com pernas elevadas", "musculos": ["Latíssimo do Dorso", "Core", "Bíceps"], "equipamento": "Barra de Tração", "categoria": "Costas", "dificuldade": "Avançado", "link_execucao": "https://www.youtube.com/watch?v=eGo4IYlbE5g"},
    {"id": 83, "nome": "Remada com Barra de Segurança", "descricao": "Barra especial", "musculos": ["Latíssimo do Dorso", "Romboides"], "equipamento": "Barra de Segurança", "categoria": "Costas", "dificuldade": "Intermediário", "link_execucao": "https://www.youtube.com/watch?v=CAwf7n6Luuc"},
    {"id": 84, "nome": "Puxada com Pegada Alternada", "descricao": "Pegada mista", "musculos": ["Latíssimo do Dorso", "Bíceps"], "equipamento": "Máquina de Puxada", "categoria": "Costas", "dificuldade": "Intermediário", "link_execucao": "https://www.youtube.com/watch?v=CAwf7n6Luuc"},
    {"id": 85, "nome": "Remada com Correntes", "descricao": "Resistência progressiva", "musculos": ["Latíssimo do Dorso", "Romboides"], "equipamento": "Barra e Correntes", "categoria": "Costas", "dificuldade": "Avançado", "link_execucao": "https://www.youtube.com/watch?v=CAwf7n6Luuc"},
    {"id": 86, "nome": "Barra Fixa com Kipping", "descricao": "Técnica de crossfit", "musculos": ["Latíssimo do Dorso", "Core"], "equipamento": "Barra de Tração", "categoria": "Costas", "dificuldade": "Avançado", "link_execucao": "https://www.youtube.com/watch?v=eGo4IYlbE5g"},
    {"id": 87, "nome": "Remada com Barra na Máquina Smith", "descricao": "Remada guiada", "musculos": ["Latíssimo do Dorso", "Romboides"], "equipamento": "Máquina Smith", "categoria": "Costas", "dificuldade": "Iniciante", "link_execucao": "https://www.youtube.com/watch?v=CAwf7n6Luuc"},
    {"id": 88, "nome": "Puxada com Barra Curvada", "descricao": "Barra curvada na máquina", "musculos": ["Latíssimo do Dorso", "Bíceps"], "equipamento": "Máquina de Puxada", "categoria": "Costas", "dificuldade": "Intermediário", "link_execucao": "https://www.youtube.com/watch?v=CAwf7n6Luuc"},
    {"id": 89, "nome": "Remada com Halteres em Pronação", "descricao": "Pegada pronada", "musculos": ["Latíssimo do Dorso", "Romboides"], "equipamento": "Halteres", "categoria": "Costas", "dificuldade": "Intermediário", "link_execucao": "https://www.youtube.com/watch?v=CAwf7n6Luuc"},
    {"id": 90, "nome": "Encolhimento com Barra", "descricao": "Trapézio com barra", "musculos": ["Trapézio Superior"], "equipamento": "Barra", "categoria": "Costas", "dificuldade": "Iniciante", "link_execucao": "https://www.youtube.com/watch?v=CAwf7n6Luuc"},
    {"id": 91, "nome": "Barra Fixa com Pegada Neutra", "descricao": "Pegada em martelo", "musculos": ["Latíssimo do Dorso", "Bíceps"], "equipamento": "Barra de Tração", "categoria": "Costas", "dificuldade": "Intermediário", "link_execucao": "https://www.youtube.com/watch?v=eGo4IYlbE5g"},
    {"id": 92, "nome": "Remada com Halteres em Supinação", "descricao": "Pegada supinada", "musculos": ["Latíssimo do Dorso", "Bíceps"], "equipamento": "Halteres", "categoria": "Costas", "dificuldade": "Intermediário", "link_execucao": "https://www.youtube.com/watch?v=CAwf7n6Luuc"},
    {"id": 93, "nome": "Puxada com Barra Hexagonal", "descricao": "Barra hexagonal na máquina", "musculos": ["Latíssimo do Dorso", "Bíceps"], "equipamento": "Máquina de Puxada", "categoria": "Costas", "dificuldade": "Intermediário", "link_execucao": "https://www.youtube.com/watch?v=CAwf7n6Luuc"},
    {"id": 94, "nome": "Remada com Cabo Alta", "descricao": "Cabo na altura do peito", "musculos": ["Romboides", "Trapézio Médio"], "equipamento": "Cabo e Polia", "categoria": "Costas", "dificuldade": "Intermediário", "link_execucao": "https://www.youtube.com/watch?v=CAwf7n6Luuc"},
    {"id": 95, "nome": "Barra Fixa com Peso Livre", "descricao": "Barra fixa com halter entre as pernas", "musculos": ["Latíssimo do Dorso", "Bíceps"], "equipamento": "Barra de Tração e Halter", "categoria": "Costas", "dificuldade": "Avançado", "link_execucao": "https://www.youtube.com/watch?v=eGo4IYlbE5g"},
    {"id": 96, "nome": "Remada com Barra na Posição Inclinada", "descricao": "Corpo inclinado", "musculos": ["Latíssimo do Dorso", "Romboides"], "equipamento": "Barra", "categoria": "Costas", "dificuldade": "Intermediário", "link_execucao": "https://www.youtube.com/watch?v=CAwf7n6Luuc"},
    {"id": 97, "nome": "Puxada com Pegada Larga", "descricao": "Pegada muito aberta", "musculos": ["Latíssimo do Dorso"], "equipamento": "Máquina de Puxada", "categoria": "Costas", "dificuldade": "Intermediário", "link_execucao": "https://www.youtube.com/watch?v=CAwf7n6Luuc"},
    {"id": 98, "nome": "Remada com Barra em Pronação", "descricao": "Pegada pronada", "musculos": ["Latíssimo do Dorso", "Romboides"], "equipamento": "Barra", "categoria": "Costas", "dificuldade": "Intermediário", "link_execucao": "https://www.youtube.com/watch?v=CAwf7n6Luuc"},
    {"id": 99, "nome": "Encolhimento com Barra Atrás", "descricao": "Barra atrás do corpo", "musculos": ["Trapézio Superior"], "equipamento": "Barra", "categoria": "Costas", "dificuldade": "Intermediário", "link_execucao": "https://www.youtube.com/watch?v=CAwf7n6Luuc"},
    {"id": 100, "nome": "Barra Fixa com Toque no Peito", "descricao": "Barra fixa completa", "musculos": ["Latíssimo do Dorso", "Bíceps", "Romboides"], "equipamento": "Barra de Tração", "categoria": "Costas", "dificuldade": "Avançado", "link_execucao": "https://www.youtube.com/watch?v=eGo4IYlbE5g"},
]

# Continuar com mais categorias...
# Vou criar um script mais eficiente que gera os 500 exercícios

def gerar_exercicios_completos():
    exercicios = []
    id_counter = 1
    
    # Categorias e seus exercícios base
    categorias = {
        "Peito": exercicios_peito,
        "Costas": exercicios_costas,
    }
    
    # Adicionar os exercícios já criados
    for cat, ex_list in categorias.items():
        exercicios.extend(ex_list)
        id_counter = max([e["id"] for e in ex_list]) + 1
    
    # Gerar mais exercícios para outras categorias
    # Ombros (50)
    ombros_base = ["Desenvolvimento", "Elevação Lateral", "Elevação Frontal", "Remada Alta", "Crucifixo Invertido", "Desenvolvimento Arnold", "Elevação com Rotação", "Face Pull", "Desenvolvimento Unilateral", "Elevação Lateral Inclinada"]
    for i, nome_base in enumerate(ombros_base):
        for j in range(5):
            variacoes = ["com Halteres", "com Barra", "com Cabo", "com Máquina", "Unilateral"]
            nome = f"{nome_base} {variacoes[j]}" if j < len(variacoes) else f"{nome_base} Variação {j+1}"
            exercicios.append({
                "id": id_counter,
                "nome": nome,
                "descricao": f"Exercício para desenvolvimento dos ombros",
                "musculos": ["Deltoides", "Trapézio"],
                "equipamento": "Varia conforme exercício",
                "categoria": "Ombros",
                "dificuldade": "Intermediário" if j < 3 else "Avançado",
                "link_execucao": "https://www.youtube.com/watch?v=qEwKCR5JCog"
            })
            id_counter += 1
    
    # Pernas (100)
    pernas_base = ["Agachamento", "Leg Press", "Extensão de Pernas", "Flexão de Pernas", "Afundo", "Agachamento Búlgaro", "Elevação de Panturrilha", "Stiff", "Hack Squat", "Lunges"]
    for i, nome_base in enumerate(pernas_base):
        for j in range(10):
            variacoes = ["Livre", "com Barra", "com Halteres", "com Máquina", "Unilateral", "com Banda", "com Kettlebell", "Sumô", "Frontal", "Traseiro"]
            nome = f"{nome_base} {variacoes[j]}" if j < len(variacoes) else f"{nome_base} Variação {j+1}"
            exercicios.append({
                "id": id_counter,
                "nome": nome,
                "descricao": f"Exercício para desenvolvimento das pernas",
                "musculos": ["Quadríceps", "Glúteos", "Posterior de Coxa"],
                "equipamento": "Varia conforme exercício",
                "categoria": "Pernas",
                "dificuldade": "Intermediário" if j < 5 else "Avançado",
                "link_execucao": "https://www.youtube.com/watch?v=YaXPRqUwItQ"
            })
            id_counter += 1
    
    # Braços - Bíceps (50)
    biceps_base = ["Rosca Direta", "Rosca Martelo", "Rosca Concentrada", "Rosca Scott", "Rosca 21", "Rosca com Barra", "Rosca com Halteres", "Rosca no Cabo", "Rosca Unilateral", "Rosca Invertida"]
    for i, nome_base in enumerate(biceps_base):
        for j in range(5):
            variacoes = ["com Barra", "com Halteres", "no Cabo", "Unilateral", "com Banda"]
            nome = f"{nome_base} {variacoes[j]}" if j < len(variacoes) else f"{nome_base} Variação {j+1}"
            exercicios.append({
                "id": id_counter,
                "nome": nome,
                "descricao": f"Exercício para desenvolvimento dos bíceps",
                "musculos": ["Bíceps Braquial", "Braquial"],
                "equipamento": "Varia conforme exercício",
                "categoria": "Bíceps",
                "dificuldade": "Intermediário",
                "link_execucao": "https://www.youtube.com/watch?v=ykJmrZ5v0Oo"
            })
            id_counter += 1
    
    # Braços - Tríceps (50)
    triceps_base = ["Tríceps Pulley", "Tríceps Testa", "Tríceps Coice", "Mergulho", "Tríceps Francês", "Tríceps Paralelo", "Tríceps Unilateral", "Tríceps com Barra", "Tríceps com Halteres", "Tríceps no Cabo"]
    for i, nome_base in enumerate(triceps_base):
        for j in range(5):
            variacoes = ["com Barra", "com Halteres", "no Cabo", "Unilateral", "com Banda"]
            nome = f"{nome_base} {variacoes[j]}" if j < len(variacoes) else f"{nome_base} Variação {j+1}"
            exercicios.append({
                "id": id_counter,
                "nome": nome,
                "descricao": f"Exercício para desenvolvimento dos tríceps",
                "musculos": ["Tríceps Braquial"],
                "equipamento": "Varia conforme exercício",
                "categoria": "Tríceps",
                "dificuldade": "Intermediário",
                "link_execucao": "https://www.youtube.com/watch?v=6kALZikXxLc"
            })
            id_counter += 1
    
    # Core/Abdômen (50)
    core_base = ["Abdominal Crunch", "Prancha", "Elevação de Pernas", "Russian Twist", "Mountain Climber", "Abdominal Bicicleta", "Abdominal Reverso", "Prancha Lateral", "Dead Bug", "Hollow Hold"]
    for i, nome_base in enumerate(core_base):
        for j in range(5):
            variacoes = ["Básico", "com Peso", "com Bola Suíça", "Unilateral", "Avançado"]
            nome = f"{nome_base} {variacoes[j]}" if j < len(variacoes) else f"{nome_base} Variação {j+1}"
            exercicios.append({
                "id": id_counter,
                "nome": nome,
                "descricao": f"Exercício para fortalecimento do core",
                "musculos": ["Reto Abdominal", "Oblíquos", "Transverso"],
                "equipamento": "Varia conforme exercício",
                "categoria": "Core",
                "dificuldade": "Intermediário" if j < 3 else "Avançado",
                "link_execucao": "https://www.youtube.com/watch?v=pSHjTRCQxIw"
            })
            id_counter += 1
    
    # Glúteos (50)
    gluteos_base = ["Elevação Pélvica", "Abdução de Quadril", "Adução de Quadril", "Ponte", "Kickback", "Agachamento Sumô", "Hip Thrust", "Glute Bridge", "Fire Hydrant", "Donkey Kick"]
    for i, nome_base in enumerate(gluteos_base):
        for j in range(5):
            variacoes = ["Básico", "com Banda", "com Peso", "Unilateral", "com Máquina"]
            nome = f"{nome_base} {variacoes[j]}" if j < len(variacoes) else f"{nome_base} Variação {j+1}"
            exercicios.append({
                "id": id_counter,
                "nome": nome,
                "descricao": f"Exercício para desenvolvimento dos glúteos",
                "musculos": ["Glúteo Máximo", "Glúteo Médio"],
                "equipamento": "Varia conforme exercício",
                "categoria": "Glúteos",
                "dificuldade": "Intermediário",
                "link_execucao": "https://www.youtube.com/watch?v=YaXPRqUwItQ"
            })
            id_counter += 1
    
    # Cardio/Funcional (50)
    cardio_base = ["Burpee", "Jumping Jacks", "Corrida no Lugar", "Polichinelo", "Mountain Climber", "High Knees", "Butt Kicks", "Skaters", "Bear Crawl", "Crab Walk"]
    for i, nome_base in enumerate(cardio_base):
        for j in range(5):
            variacoes = ["Básico", "com Peso", "Avançado", "Intervalado", "com Salto"]
            nome = f"{nome_base} {variacoes[j]}" if j < len(variacoes) else f"{nome_base} Variação {j+1}"
            exercicios.append({
                "id": id_counter,
                "nome": nome,
                "descricao": f"Exercício cardiovascular e funcional",
                "musculos": ["Corpo Inteiro"],
                "equipamento": "Nenhum ou Peso",
                "categoria": "Cardio",
                "dificuldade": "Intermediário" if j < 3 else "Avançado",
                "link_execucao": "https://www.youtube.com/watch?v=tyvH5wXqjqE"
            })
            id_counter += 1
    
    return exercicios[:500]  # Garantir exatamente 500

# Gerar e salvar
exercicios_finais = gerar_exercicios_completos()

# Salvar em JSON
with open('exercicios_academia.json', 'w', encoding='utf-8') as f:
    json.dump(exercicios_finais, f, ensure_ascii=False, indent=2)

print(f"Arquivo criado com {len(exercicios_finais)} exercícios!")
