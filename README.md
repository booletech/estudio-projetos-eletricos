# Estúdio de projetos elétricos

Projetos elétricos residenciais e industriais com LibreCAD e QElectroTech,
bibliotecas, modelos, scripts e instruções de apoio para agentes.

## Estado inicial

A primeira amostra é uma residência esquemática de 8 × 6 m (48 m²), com sala,
quarto, cozinha, área de serviço e banheiro. A planta contém cinco pontos de
iluminação, oito tomadas genéricas, cinco interruptores e o quadro QD-01.
O estudo de quadro organiza quatro circuitos conceituais.

- [Planta editável no LibreCAD](exemplos/residencial-001/planta-residencial-001.dxf)
- [Diagrama editável no QElectroTech](exemplos/residencial-001/quadro-residencial-001.qet)
- [Manifesto de preservação](exemplos/residencial-001/manifesto-001.json)
- [Verificações e limitações](docs/VERIFICACAO-001.md)
- [Próximos trabalhos](docs/PENDENCIAS.md)

**Rascunhos didáticos: não liberados para execução, orçamento final ou entrega
como projeto técnico aprovado.** Potências, bitolas, proteções, DR/DPS,
aterramento, trajetos executivos e revisão técnica estão pendentes.

## Organização

A fase atual é aprendizado, com prática do cômodo simples autorizada. Comece pela
[base de estudo dos programas](docs/pesquisa/README.md) e pelos
[sete perfis de agentes](agentes/README.md). As instruções foram versionadas;
não há serviço autônomo, orquestrador ou modelo treinado instalado.

## Primeiro cômodo em 3D

Exercício criado e reaberto no FreeCAD 1.1.4: área interna de 4 × 3 m (12 m²),
pé-direito de 2,70 m, piso, quatro paredes, porta e janela. Duas paredes estão
transparentes na vista inicial para mostrar o interior. São objetos Part
editáveis, sem classificação BIM/IFC ou projeto elétrico.

- [Modelo FCStd, imagem e macro](exemplos/comodo-3d-001/README.md)
- [Verificações e aprendizado](docs/FREECAD-COMODO-001.md)

O [estudo elétrico do cômodo](exemplos/comodo-eletrico-001/README.md) acrescenta
L1 (uma lâmpada), S1 (um interruptor) e T1–T4 (quatro tomadas ilustrativas).
Há modelo FreeCAD, planta DXF aberta no LibreCAD, imagens e lista de pontos.
Trajetos conceituais e cores gráficas não especificam condutores ou circuitos.

`exemplos/` guarda material sintético. `projetos/` recebe somente material
expressamente autorizado e sem dados pessoais. `agentes/` guarda instruções
versionadas. `scripts/` guarda ferramentas locais. `docs/` registra decisões,
verificações e pendências. `local/`, `tools/` e `.venv/` ficam fora do Git.

## Ferramentas

- LibreCAD 2.2.1.5: https://librecad.org/
- QElectroTech 0.100: https://qelectrotech.org/
- FreeCAD 1.1.4: https://www.freecad.org/

O [guia FreeCAD/BIM](docs/pesquisa/FREECAD-001.md) e o
[plano da casa em 3D](docs/pesquisa/CASA-3D-PLANO-001.md) preparam a próxima
prática. Para abrir a cópia local desta máquina, usar
[o lançador portátil](scripts/abrir-freecad-001.cmd). Em outra máquina, baixar
o pacote oficial e adaptar sua localização; o executável não acompanha o Git.

Nesta máquina, as cópias locais estão em `../tools/`, dentro do diretório de
trabalho original. Os programas e seus instaladores não são distribuídos por
este repositório. Consulte [o registro de ferramentas](docs/FERRAMENTAS.md).

Para verificar a cópia inicial, execute a partir desta pasta:

```powershell
& '..\.venv\Scripts\python.exe' '.\scripts\verificar_exemplos.py'
```

Em outra máquina, use um Python isolado em `.venv`; a verificação usa somente
a biblioteca padrão. Ela verifica integridade e estrutura, sem certificação
elétrica ou validação visual integral.

## Atualizações

A rotina diária verifica alterações autorizadas, executa as verificações
aplicáveis e envia um commit descritivo quando houver mudança real. Não cria
commits vazios. Seu agendamento é configurado no Codex, fora do repositório.
As regras estão em [AGENTS.md](AGENTS.md) e [no fluxo de versionamento](docs/VERSIONAMENTO.md).

## Direitos

O símbolo de disjuntor incorporado ao QET é da biblioteca do QElectroTech;
os créditos e a informação de licença permanecem no arquivo. O uso desses
elementos dentro de diagramas é permitido pela licença da coleção:
https://github.com/qelectrotech/qelectrotech-elements/blob/main/ELEMENTS.LICENSE
Nenhuma licença geral sobre projetos de clientes é concedida automaticamente.
