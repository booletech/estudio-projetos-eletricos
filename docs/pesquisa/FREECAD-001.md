# FreeCAD: base de estudo para a casa em 3D

Pesquisa de 12/10/2026; referência: FreeCAD 1.1.4 portátil para Windows x86_64.
[Instalação](../FREECAD-INSTALACAO-001.md) e
[catálogo de fontes](fontes-freecad-001.json). Os resumos são próprios,
baseados na documentação da comunidade FreeCAD. O ramo `main` da documentação
pode evoluir além da versão instalada; conferir detalhes antes da prática.

## Ambiente BIM

O BIM integrado reúne arquitetura, ferramentas Draft e suporte a documentação
2D com TechDraw. Pode usar linhas/esboços para gerar objetos como paredes.
Arch, BIM e Native-IFC foram integrados na série 1.0. A organização pode usar
edifício, níveis e grupos; um modelo deve conservar objetos reconhecíveis.
[F02 — BIM](https://github.com/FreeCAD/FreeCAD-documentation/blob/main/wiki/BIM_Workbench.md).

## Paredes

Uma parede pode partir de linha, polilinha ou esboço. Altura, espessura e
alinhamento em relação à base são parâmetros importantes. Bases em face ou
sólido têm comportamento diferente: nem toda propriedade altera a geometria
da mesma forma. Medir e examinar os encontros depois de editar parâmetros.
[F03 — Wall](https://github.com/FreeCAD/FreeCAD-documentation/blob/main/wiki/Arch_Wall.md).

## Portas e janelas

Window também sustenta portas e oferece tipos predefinidos. O objeto pode ser
associado a uma parede hospedeira e definir um volume para abrir o vão. Não
confundir um símbolo perto da parede com uma abertura efetivamente realizada;
conferir associação, dimensões e recorte.
[F04 — Window](https://github.com/FreeCAD/FreeCAD-documentation/blob/main/wiki/Arch_Window.md).

## Cobertura

Roof cria cobertura inclinada a partir de contorno e mantém parâmetros de
inclinação, beiral e espessura. A documentação orienta contorno fechado e
avisa sobre limitações em formas complexas. Estudar primeiro um caso simples;
a forma visual resultante não substitui cálculo estrutural.
[F05 — Roof](https://github.com/FreeCAD/FreeCAD-documentation/blob/main/wiki/Arch_Roof.md).

## Aproveitar a planta DXF

Há importador C++ e alternativa antiga em Python com dependências próprias.
Suas capacidades diferem: o C++ importa geometria de blocos, mas pode ignorar
textos, cotas e atributos internos. Conferir medida conhecida, orientação e
conteúdo realmente importado; não presumir preservação integral.
[F06 — DXF](https://github.com/FreeCAD/FreeCAD-documentation/blob/main/wiki/Draft_DXF.md).

Nossa proposta: importar uma cópia da arquitetura como referência e modelar
os objetos BIM separadamente. Símbolos/textos elétricos não devem virar paredes
indiscriminadamente. Definir alturas e espessuras ausentes antes de modelar.
Essa importação e a transformação em casa 3D ainda não foram executadas.

## Navegação com touchpad

O estilo **Touchpad** pode ser escolhido na barra de status ou em Edit →
Preferences → Display → Navigation. Nesse estilo, Shift e movimento do ponteiro
deslocam a vista; Alt e movimento rotacionam; Ctrl+Shift e movimento controlam
zoom. PgUp/PgDn também oferecem zoom. O comportamento do driver do notebook
precisa ser conferido localmente.
[F07 — navegação](https://github.com/FreeCAD/FreeCAD-documentation/blob/main/wiki/Mouse_navigation.md).

**V, depois F** enquadra todos os objetos visíveis. Também existe em View →
Standard views → Fit all. O enquadramento não muda medidas.
[F08 — Fit all](https://github.com/FreeCAD/FreeCAD-documentation/blob/main/wiki/Std_ViewFitAll.md).

## Troca e direitos

Preservar o modelo nativo `.FCStd` e revisões. IFC depende de IfcOpenShell e
conferência dos objetos exportados; presença da biblioteca não comprova troca
sem perdas. IFC não foi testado nesta etapa.
[F09 — IFC](https://github.com/FreeCAD/FreeCAD-documentation/blob/main/wiki/Arch_IFC.md).

O uso comercial do FreeCAD é permitido, e os modelos produzidos não herdam
automaticamente a licença do programa. A documentação informa CC BY 3.0;
mantemos crédito à comunidade FreeCAD, links e resumos, sem redistribuir manuais
inteiros. [F11 — licença](https://github.com/FreeCAD/FreeCAD-documentation/blob/main/wiki/License.md).

## Limite da etapa

A pesquisa orienta a próxima prática. Não criou uma casa, validou importações
ou certificou estrutura/instalações. A correspondência entre FCStd, planta DXF
e QET será um controle documental nosso: não há sincronizador automático.
