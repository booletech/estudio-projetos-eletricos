# Preservação de alterações CAD — revisão 003

Em 16/10/2026, o usuário autorizou preservar as alterações locais como novas
revisões numeradas, conferir os arquivos e sincronizar no GitHub. Esta revisão
arquiva dois exemplos sintéticos; não modifica os arquivos já publicados.

## Arquivos e origem

| Revisão preservada | Arquivo em que a alteração foi encontrada | SHA-256 da revisão |
| --- | --- | --- |
| [Planta elétrica 003](../exemplos/comodo-eletrico-001/planta-003/planta-eletrica-003.dxf) | `exemplos/comodo-eletrico-001/planta-002/planta-eletrica-001.dxf` | `9973c87699ce817bbcfd5feccc2fdd3f338e07a31be946ad0721587110426262` |
| [Sala preservada 003](../exemplos/comodo-sala-001/saida-003/sala-mobiliada-preservada-003.FCStd) | `exemplos/comodo-sala-001/saida-001/sala-mobiliada-eletrica-001.FCStd` | `e7436164e356f020bb6379edd168968fbbd25eefb4d0fdc7421c8a647e7fcda5` |

As cópias são idênticas, byte a byte, aos arquivos locais alterados. Cada pasta
contém `manifesto-preservacao-003.json`, com tamanho, hashes e origem. Os caminhos
antigos foram restaurados localmente a partir de cópias cujo SHA-256 corresponde
ao original publicado, após preservar as alterações nas revisões 003 e em
arquivo local separado. Nenhum original publicado foi substituído.

A sala 003 preserva uma alteração da **sala 001**. Não é uma continuação da
revisão arquitetônica `saida-002` e não se deve presumir que incorpora sua mudança
de janela e passagem para a cozinha. As revisões anteriores permanecem disponíveis.

## Diferenças verificadas

- DXF: 116 linhas, 2 círculos e 26 textos em ambas as versões. Coordenadas,
  raios, camadas, conteúdo dos textos e campos de posicionamento, altura,
  rotação e alinhamento comparados coincidem com tolerância de arredondamento
  de seis casas decimais. Cabeçalhos e registros de serialização diferem.
  Essa comparação não cobre todos os atributos gráficos possíveis do DXF.
- FreeCAD: ZIP e XML íntegros; mesmos 134 identificadores de objetos.
  A abertura de leitura no FreeCAD portátil 1.1.4 encontrou 125 formas não
  nulas no original e 124 na revisão. Todas as formas examinadas são válidas
  segundo `Shape.isValid()`.
- Há alteração geométrica no objeto `Arquitetura`: o volume armazenado passou
  de aproximadamente 9,3485 para 5,8655 m³; os limites externos permaneceram
  iguais. O objeto `TrajetosConceituais` permanece na lista de objetos, mas não
  apresenta forma não nula na revisão. Esses resultados foram preservados,
  sem redesenho ou correção automática.
- A soma dos sólidos das formas examinadas passou de 232 para 212. Essa soma
  inclui compostos e não representa uma contagem de elementos construtivos
  únicos. Nos demais objetos examinados não foram detectadas diferenças nas
  métricas e vértices comparados; isso não prova equivalência geométrica integral.

O [relatório geométrico](../exemplos/comodo-sala-001/saida-003/conferencia-geometria-003.json)
registra métricas e vértices em unidades nativas do modelo (mm, mm² e mm³).
Os documentos foram abertos sem recomputar nem salvar.

## Verificações executadas

Com Python isolado:

```text
scripts/verificar_exemplos.py
exemplos/comodo-eletrico-001/verificar-eletrica-001.py
exemplos/comodo-sala-001/verificar-sala-001.py
scripts/verificar_revisoes_preservadas_003.py
```

Todos passaram. A conferência geométrica adicional usou o Python do FreeCAD
portátil. Os arquivos CAD não foram reexportados. A revisão não inclui PDF,
backups automáticos, ambientes, instaladores ou estudos pessoais do terreno/casa.

Não foi realizada revisão gráfica ou técnica integral. Integridade de arquivos
e validade de formas não aprovam dimensionamento elétrico, estrutural ou uso em
obra. `pronto_para_publicar` e `pronto_para_execucao` permanecem falsos; o envio
ao repositório serve para arquivamento do estudo autorizado.
