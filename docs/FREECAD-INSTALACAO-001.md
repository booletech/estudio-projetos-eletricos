# FreeCAD: instalação portátil — registro 001

Data: 12/10/2026. Versão selecionada: 1.1.4 estável, Windows x86_64, Python
embutido py311. Fonte: [release oficial](https://github.com/FreeCAD/FreeCAD/releases/tag/1.1.4).

## Preservação e integridade

Pacote: `FreeCAD_1.1.4-Windows-x86_64-py311.7z`, 418.088.341 bytes.
SHA-256 conferido contra o digest publicado pelo GitHub:
`4828741fc91ee37fafcdb97a1abacb18b04ba451ac4372d9ff7a7349b36f4d6d`.
O arquivo baixado foi preservado em `../tools/downloads/freecad-001/`.

Destino local: `../tools/freecad-1.1.4-001/`. Programas, arquivos de usuário,
temporários e configurações ficam fora do Git. Não houve instalação global,
mudança de PATH persistente ou associação global de arquivos.

## Abertura local

O [lançador](../scripts/abrir-freecad-001.cmd) aponta para o executável na pasta
portátil e direciona configuração/dados/temporários para `../tools/freecad-profile-001/`.
Os parâmetros `--user-cfg`, `--system-cfg` e as variáveis `FREECAD_USER_*`
estão documentados na [configuração oficial](https://github.com/FreeCAD/FreeCAD-documentation/blob/main/wiki/Start_up_and_Configuration.md).
O perfil é local a esta instalação; não acompanha os arquivos enviados ao GitHub.

## Estado da verificação

- Download e hash: concluídos.
- Extração: concluída pelo 7-Zip sem erros; 35.582 arquivos, 3.214 pastas,
  2.307.792.881 bytes descompactados.
- Lançador: executado com sucesso, usando o executável oficial da raiz do pacote.
- Abertura da interface: conferida; janela `FreeCAD 1.1.4`, tela de configuração
  inicial em português e unidade padrão mm/kg/s/graus.
- BIM: arquivo do ambiente incluído no pacote; seu carregamento e uso ainda não testados.
- Navegação Touchpad: pesquisada e documentada; configuração e ensaio pendentes.
- Modelagem de casa, importação DXF, exportação e IFC: não realizados nesta etapa.

As instruções do agente e a pesquisa são materiais de consulta. A construção
e revisão da casa 3D permanecem futuras e dependem da solicitação de prática.
