# Ferramentas locais

| Ferramenta | Versão | Arquivo oficial | SHA-256 conferido |
| --- | --- | --- | --- |
| LibreCAD | 2.2.1.5 | LibreCAD-v2.2.1.5-win64-msvc.exe | 738912fea40aca934689444af9c5cd281572417983cc081c204fe6c779f6941d |
| QElectroTech | 0.100, git8590 | qelectrotech-0.100.0+git8590-x86-win64-readytouse.7z | 552402198011f37633ffcff4f9ce561a9abaf22dc14f9cc09ddc231245b16445 |
| FreeCAD | 1.1.4 | FreeCAD_1.1.4-Windows-x86_64-py311.7z | 4828741fc91ee37fafcdb97a1abacb18b04ba451ac4372d9ff7a7349b36f4d6d |

Fontes:
- https://github.com/LibreCAD/LibreCAD/releases/tag/v2.2.1.5
- https://github.com/qelectrotech/qelectrotech-source-mirror/releases/tag/0.100
- https://github.com/FreeCAD/FreeCAD/releases/tag/1.1.4

LibreCAD: extraído do instalador oficial para uma pasta local, sem executar
instalação global. QElectroTech: pacote portátil oficial. Ambos abriram nesta
máquina. Os executáveis, configurações e bibliotecas completas ficam fora do Git.

FreeCAD: pacote portátil oficial, com perfil de configuração dentro de `../tools`
quando aberto pelo lançador deste repositório. A verificação e seus limites
estão em [FREECAD-INSTALACAO-001.md](FREECAD-INSTALACAO-001.md).
