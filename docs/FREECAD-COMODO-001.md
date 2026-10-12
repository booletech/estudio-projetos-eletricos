# FreeCAD: primeiro cômodo — registro 001

Data: 12/10/2026. Pedido: criar um cômodo simples, mostrar e continuar o projeto.
Software utilizado: FreeCAD portátil 1.1.4, ambiente Part.

## Resultado realizado

[Modelo e imagem](../exemplos/comodo-3d-001/README.md): dimensões internas
4000 × 3000 mm, pé-direito 2700 mm, paredes de 150 mm, piso de 100 mm,
porta com vão 900 × 2100 mm e janela com vão 1200 × 1000 mm, peitoril 1000 mm.
Todas essas medidas são hipóteses didáticas, não dados de imóvel real.

Usamos Part::Box para peças editáveis e Part::Cut para os dois vãos. A folha
da porta está rotacionada 90° para dentro. A janela possui caixilho simplificado
e duas peças de vidro. O modelo tem quatro paredes completas e nenhum teto;
duas paredes têm transparência para mostrar o interior na vista isométrica.

## Verificações efetivamente concluídas

- Salvar FCStd e reabrir no próprio FreeCAD; recomputar o documento reaberto.
- Conferir 16 peças visíveis: forma não nula, validade geométrica, volume positivo,
  um sólido por peça e ausência de estado de erro.
- Comparar o volume das paredes cortadas com o volume original menos os vãos.
- Testar pontos dentro dos vãos e em porções remanescentes das duas paredes.
- Exportar PNG nativo de 1400 × 1000 pixels e inspecionar visualmente o resultado.
- Conferir SHA-256 da macro utilizada, FCStd e PNG contra o manifesto.
- Testar a integridade ZIP do FCStd; o Document.xml não contém o caminho local.

## Aprendizado incorporado

O primeiro verificador incluiu grupos de documentos porque eles também expõem
Shape. Sua forma pode reunir vários sólidos; isso não indica defeito em uma
peça. A revisão 002 restringe a checagem por peça a Part::Box e Part::Cut.
A revisão 001 foi preservada e identificada como não funcional.

Na interface desta versão, Ctrl+F6 executa a macro; F6 inicia depuração.
Ao selecionar arquivo em um diálogo nativo do Windows, usar barras invertidas
no caminho absoluto ou apenas o nome quando estiver na pasta correta.

As propriedades das peças são editáveis, mas não há uma planilha vinculando
todas as dimensões. Para regenerar o conjunto, ajustar as constantes da macro
em uma nova revisão. Salvar novas tentativas em pastas numeradas e registrar
erros reais sem alegar sucesso antes de reabrir e conferir as saídas.

## Limitações

Este exercício demonstrou construção de geometria Part e salvamento nativo.
Não demonstra objetos BIM/IFC, vínculos de hospedeiros, importação DXF,
exportação IFC, navegação Touchpad testada, coordenação elétrica, desempenho
de uma casa completa ou conformidade técnica. Portas, vidros e caixilhos são
representações simplificadas. Revisão humana técnica/final permanece pendente;
`pronto_para_publicar` e `pronto_para_execucao` continuam falsos.
