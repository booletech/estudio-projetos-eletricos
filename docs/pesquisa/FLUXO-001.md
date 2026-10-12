# Organização proposta para o aprendizado

Este documento é uma síntese nossa, baseada nos dois guias de software; não é
procedimento executivo, norma ou integração implementada.

| Trabalho | LibreCAD | QElectroTech | Evidência adicional necessária |
| --- | --- | --- | --- |
| Planta e localização | Geometria, pontos, cotas e camadas | Referência documental | Dimensões, levantamento e revisão |
| Quadro/circuitos | Localização e etiquetas | Diagrama e identificações | Dados elétricos e dimensionamento |
| Painel industrial | Localização/layout quando aplicável | Potência e comando | Requisitos, fabricantes e revisão |
| Lista de componentes | Dados desenhados conforme convenção | Relatórios de metadados | Conferência de itens e quantidades |
| Entrega | Folha, escala e saída gráfica | Folios e relatórios | Visualização integral e aprovação |

## Vinculação entre documentos

Proposta: manter uma tabela de correspondência com identificadores de quadro,
circuito/equipamento, arquivo e revisão. Comparar manualmente antes de entrega.
Não há sincronizador DXF/QET implementado neste repositório.

## Questões residenciais para futura coleta

Qual arquitetura é válida? Quais dimensões foram verificadas? Quais dados de
alimentação e cargas são conhecidos? Quais condições de instalação e requisitos
locais se aplicam? Quem revisará cálculos e desenhos? Sem respostas, registrar
pendências e limitar-se a exemplos didáticos.

## Questões industriais para futura coleta

O escopo é distribuição, painel ou comando? Quais máquinas/interfaces e dados
de rede são conhecidos? Existe descrição funcional aprovada? Quais documentos
de fabricante e condições de instalação existem? Quais análises de proteção
e segurança são necessárias? Nenhuma solução deve ser presumida pela estética
do diagrama.

## Separação das revisões

Revisão documental: fonte, versão, arquivo e metadados. Revisão gráfica:
legibilidade, escala, conexão representada e saída integral. Revisão elétrica:
critérios, cálculos e adequação. Aprovação final: decisão humana registrada.
Passar uma delas não implica passar as outras. A pesquisa atual cobre conceitos
de software e mantém as demais etapas pendentes.
