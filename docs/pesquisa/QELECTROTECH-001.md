# QElectroTech: guia de estudo

Referência local: 0.100, git8590 ([release Q08](https://github.com/qelectrotech/qelectrotech-source-mirror/releases/tag/0.100)).
As páginas consultadas nem sempre identificam a mesma versão; confirmar os
detalhes no programa antes de adotar uma sequência como procedimento validado.

## Projeto, folio e elemento

O projeto agrupa folios, elementos, condutores, propriedades e relações,
inclusive entre folhas. Essa estrutura sustenta a organização da documentação.
[Q01 — projeto](https://qelectrotech.github.io/qelectrotech-doc/users/project/what_is.html).

Um elemento contém representação gráfica e informações como identificação,
artigo e fabricante. As famílias têm diferentes possibilidades de vínculo.
Metadados incompletos limitam os relatórios, mesmo que o símbolo apareça correto.
[Q02 — elemento](https://qelectrotech.github.io/qelectrotech-doc/users/element/what_is.html).

## Terminais e condutores

Na criação manual, arrastar de um terminal até outro identificado pelo programa.
Na automática, a ferramenta deve estar habilitada e os terminais alinhados.
O manual descreve aviso de potenciais que não impede necessariamente a criação
da ligação. Logo, a conexão desenhada não comprova correção elétrica.
[Q03 — criação de condutor](https://qelectrotech.github.io/qelectrotech-doc/users/schema/conductor/conductor_creation.html).

## Numeração e referências

A numeração admite padrões com texto, variáveis e sequências. Antes da prática,
definir o padrão e como identificar mudanças; números automáticos não comprovam
bitola, função ou existência física do fio.
[Q04 — numeração](https://qelectrotech.github.io/qelectrotech-doc/users/conductor/properties/conductor_numbering.html).

Elementos mestre podem ter vários escravos vinculados; o mestre concentra a
informação do componente na lista de materiais. O vínculo deve ser conferido
para que contatos/bobinas representem o equipamento pretendido.
[Q05 — referência do mestre](https://qelectrotech.github.io/qelectrotech-doc/users/element/cross_reference/cross_reference_master.html).

## Relatórios e saída

O manual documenta CSV de nomenclatura com escolha de campos e filtros.
Conferir identificações e quantidades; não tratar a lista como orçamento
completo nem assumir inclusão de cabos, comprimentos ou acessórios ausentes.
[Q06 — nomenclatura](https://qelectrotech.github.io/qelectrotech-doc/users/export&print/export_nomenclature.html).

A documentação de PDF orienta selecionar o projeto e os folios de saída, mas
essa página ainda menciona versão 0.7. Ela serve como orientação de estudo;
detalhes de menus e links no PDF de 0.100 continuam a confirmar.
[Q07 — PDF](https://qelectrotech.github.io/qelectrotech-doc/users/export&print/create_pdf.html).

## Aplicação sugerida ao nosso trabalho

Residencial: estudar identificação de circuitos e relação com o quadro.
Industrial: estudar separação de potência/comando, referências e organização
por folhas. São propostas internas, não esquemas já projetados ou aprovados.
Não foi comprovada sincronização automática com LibreCAD ou cálculo completo.

Perguntas de prática futura: todos os condutores do XML carregam? Uma linha
é conexão ou forma gráfica? Vínculos sobrevivem à reabertura? CSV reflete
componentes esperados? PDF inclui todos os folios sem cortes? Não responder
essas questões com uma contagem estrutural apenas.
