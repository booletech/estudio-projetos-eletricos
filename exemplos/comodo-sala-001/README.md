# Sala ampliada e mobiliada — estudo 001

Sala sintética com dimensões internas de **5 × 4 m (20 m²)** e altura de 2,70 m.
Criada no FreeCAD 1.1.4 em 12/10/2026 a partir de uma cópia do cômodo anterior.

## Arquivos

- [Modelo editável FreeCAD](saida-001/sala-mobiliada-eletrica-001.FCStd)
- [Vista 3D com trajetos elétricos](saida-001/sala-mobiliada-isometrico-001.png)
- [Vista da decoração](vista-001/sala-decoracao-001.png)
- [Planta DXF para LibreCAD](planta-001/planta-eletrica-001.dxf)
- [Planta em PNG](planta-001/planta-eletrica-001.png) e [SVG](planta-001/planta-eletrica-001.svg)
- [Lista de pontos](planta-001/lista-pontos-001.csv)

## Conteúdo do modelo

Sofá de 2,20 × 1,00 m voltado para a TV, rack, estante lateral, livros,
almofadas, tapete, vasos, planta ornamental e quatro quadros geométricos.
As peças são sólidos simples editáveis, sem imagens ou modelos de terceiros.
A tela da TV tem diagonal de 43 polegadas (1092,2 mm), com proporção ilustrativa
16:9: aproximadamente 952 × 535 mm. A moldura é adicional; não representa um
produto de fabricante específico. As dimensões do mobiliário são hipóteses do exercício.

Uma lâmpada L1, interruptor S1 que controla L1 e quatro tomadas T1–T4 foram
reposicionados para a sala ampliada. T3 fica atrás do rack. D1 e A0 são referências
de distribuição e origem ainda indefinida. Coordenadas, alturas e sete trajetos
estão em [pontos-001.json](pontos-001.json). As alturas de 1100 mm para o interruptor
e 300 mm para tomadas são ilustrativas. Laranja e azul distinguem categorias
gráficas; não identificam condutores. O raio dos cilindros não dimensiona eletrodutos.

## Conferência e limites

A macro salvou e reabriu o FCStd, verificou 114 sólidos válidos, volumes das
paredes com aberturas, posições dos pontos e extremos de sete rotas. As duas
imagens 3D e a prévia 2D foram inspecionadas visualmente. Na vista decorativa,
duas paredes, trajetos e etiquetas foram ocultados apenas em memória; partes
do mobiliário ficam oclusas conforme o ângulo. O FCStd salvo conserva o estudo completo.

O DXF contém 144 linhas, três círculos e 30 textos em seis camadas. Sua geometria
é 1:1 em milímetros; configurar milímetros e escala de impressão no LibreCAD.
A planta mostra projeções simplificadas dos móveis, sem todos os enfeites 3D.
Esta revisão da planta foi conferida em PNG e por estrutura; sua abertura no
LibreCAD ainda não foi verificada nesta etapa.

O verificador local confere hashes, arquivo FCStd/ZIP/XML, pontos CSV/JSON,
extremos de rotas, estrutura DXF, dimensões PNG e leitura SVG. Não valida
dimensionamento nem conformidade elétrica. Alimentação, cargas, circuitos,
condutores, proteções e revisão humana continuam pendentes. Os indicadores
`pronto_para_execucao` e `pronto_para_publicar` permanecem falsos.

## Preservação e reprodução

A fonte `../comodo-3d-001/saida-002/comodo-001.FCStd` foi copiada sem alterações.
SHA-256: `81a0be19aa58bcb56289ed640e3e1360ae255ff5802be3cbbdf37c13a7cfc7d5`.
Os manifestos nas pastas de saída registram hashes e verificações. Originais e
revisões anteriores permanecem preservados.

No FreeCAD, abrir `criar-sala-001.FCMacro` e executar com Ctrl+F6; requer
`mobiliario-001.py`, configuração e fonte nos caminhos relativos existentes.
A macro cria uma nova pasta `saida-NNN`. `mostrar-decoracao-001.FCMacro`
gera uma pasta `vista-NNN` a partir da saída 001, sem salvar mudanças no modelo.

Executar `gerar-planta-sala-001.py` com Python isolado e Pillow para criar nova
`planta-NNN`. Executar `verificar-sala-001.py` com a biblioteca padrão para
conferir especificamente esta revisão 001. Nesta máquina, usar o Python em
`../../../.venv/Scripts/python.exe` a partir desta pasta.

Arquivos preparados localmente. Envio ao GitHub pendente de resolver a regra
mais recente do diretório de trabalho: “Não publicar”.
