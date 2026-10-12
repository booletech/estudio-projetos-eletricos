# LibreCAD: guia de estudo

Referência local: 2.2.1.5 ([release L07](https://github.com/LibreCAD/LibreCAD/releases/tag/v2.2.1.5)).
Este guia sintetiza conceitos; a prática atual ainda está limitada ao que consta
em `../VERIFICACAO-001.md`.

## Modelo, unidades e folha

Desenhar em tamanho real, 1:1, na unidade escolhida. O tamanho na folha é
definido na impressão. Unidade padrão da aplicação e preferência de um desenho
são configurações distintas. Modelos DXF podem guardar camadas, configurações
e carimbo para iniciar outros desenhos. [L01 — preparação](https://docs.librecad.org/en/2.2.0_a/guides/dwg-setup.html).

## Geometria e precisão

Entidades incluem linhas, círculos e textos. Coordenadas cartesianas usam X,Y;
as relativas usam `@`, como `@100,0`. A entrada polar combina distância e ângulo.
Cor, espessura e tipo de linha são atributos gráficos; camadas organizam entidades
e seus atributos. [L02 — fundamentos](https://docs.librecad.org/en/latest/ref/fundamentals.html).

Snaps auxiliam a seleção precisa de posições na geometria. Para estudar
extremidades, centros e interseções, verificar os modos disponíveis na interface
e medir o resultado, em vez de confiar no aspecto visual.
[L04 — snapping](https://docs.librecad.org/en/latest/ref/snaps.html).

## Blocos e biblioteca

Blocos reúnem geometria reutilizável com referência de inserção, escala e
rotação. Reutilizar um bloco pela lista mantém suas instâncias relacionadas;
repetir importações da biblioteca pode gerar definições independentes. A camada
0 tem função especial na composição de blocos; isso não significa colocar toda
a planta nessa camada. Explodir um bloco remove essa organização.
[L03 — blocos](https://docs.librecad.org/en/latest/guides/blocks.html).

## Impressão e PDF

A prévia permite verificar papel, orientação, margens, posição e escala. Ajustar
à folha ajuda a enquadrar o desenho, mas a escala escolhida deve ser conferida
quando a entrega exige escala específica. Carimbo e textos também precisam
permanecer legíveis. [L05 — impressão](https://docs.librecad.org/en/latest/guides/completion.html).

O manual estável documenta `dxf2pdf`; `-a` ajusta e centraliza, `-p` define
papel e `-s` define escala. Exemplo documental, **não executado nesta pesquisa**:

```text
librecad dxf2pdf -a -p 420x297 -o planta-002.pdf planta-001.dxf
```

Esse exemplo não garante escala normativa ou resolução do teste anterior.
[L06 — console](https://docs.librecad.org/en/2.2.0_a/guides/console-tool.html).

## Aplicação sugerida ao nosso trabalho

Como convenção interna inicial, separar arquitetura, pontos, circuitos/rotas,
quadros, textos e cotas. A biblioteca de símbolos deverá ser revisada antes
de servir a projetos reais. Um símbolo CAD e uma etiqueta não executam cálculo.

Perguntas para a futura prática: como o desenho preserva unidade ao reabrir?
Como controlar atributos de blocos? Qual escala e folha produzem texto legível?
O que aparece no PDF? A abertura em outro CAD preserva os elementos usados?
Essas respostas devem receber evidência própria e revisão humana.
