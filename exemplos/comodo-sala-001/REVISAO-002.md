# Revisão 002 — janela atrás do sofá e acesso à cozinha

Pedido do usuário executado em 12/10/2026, mantendo a sala de 5 × 4 m e os móveis.

- Janela transferida da parede posterior para a parede atrás do sofá, centralizada
  no encosto. Vão de 1200 × 1000 mm, peitoril a 1100 mm, entre X=2950 e X=4150 mm.
- A antiga abertura, entre X=1500 e X=2700 mm na parede posterior, foi estendida
  até o piso: passagem aberta para a cozinha de 1200 × 2100 mm, sem folha de porta.
- Medidas e solução de passagem são hipóteses adotadas para este modelo sintético.
  A cozinha além da passagem ainda não está modelada.

## Arquivos desta revisão

- [Modelo FreeCAD](saida-002/sala-janela-cozinha-002.FCStd)
- [Vista 3D](saida-002/sala-janela-cozinha-002.png)
- [Planta DXF](planta-002/planta-eletrica-001.dxf)
- [Planta PNG](planta-002/planta-eletrica-001.png) e [SVG](planta-002/planta-eletrica-001.svg)
- [Manifesto 3D](saida-002/manifesto-aberturas-002.json)
- [Manifesto da planta](planta-002/manifesto-planta-001.json)

O nome interno dos arquivos da planta permanece 001; a pasta `planta-002`
identifica a nova revisão. As saídas anteriores continuam preservadas.

## Verificações realizadas

O FreeCAD salvou e reabriu o modelo. A macro conferiu 114 sólidos válidos,
volumes das paredes recortadas, ausência de parede nos dois vãos, esquadrias
na nova posição, peitoril acima do encosto e posições elétricas preservadas.
Os cilindros que representam os trajetos não intersectam os volumes das aberturas.
A vista 3D e a imagem da planta foram inspecionadas. A planta tem 148 linhas,
três círculos e 32 textos. Não houve abertura desta revisão no LibreCAD.

A fonte é `saida-001/sala-mobiliada-eletrica-001.FCStd`, copiada e preservada
com SHA-256 `59231ea6ec8429fafdd44334205c576b80cb8a382d1e8dca9e5acc8bedead33a`.
Hashes e tamanhos dos arquivos novos foram conferidos contra os manifestos.
O estudo elétrico continua conceitual, com dimensionamento e revisão humana
pendentes. `pronto_para_execucao` e `pronto_para_publicar` continuam falsos.

Para reproduzir: executar `alterar-aberturas-002.FCMacro` no FreeCAD com Ctrl+F6;
novas pastas de saída são numeradas automaticamente. Executar
`gerar-planta-sala-002.py` com o Python isolado e Pillow para gerar a planta.
Arquivos salvos localmente; esta revisão não foi enviada ao GitHub.
