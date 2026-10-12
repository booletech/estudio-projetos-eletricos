# Instruções para agentes

## Fase atual: pesquisa e aprendizado

Em 12/10/2026, o usuário determinou reunir informações antes de novos projetos.
Nesta fase, ler a base em `docs/pesquisa/` e usar os perfis de `agentes/` apenas
para pesquisar, explicar, registrar evidências e planejar exercícios. Não
criar/alterar CAD, executar exportações ou realizar dimensionamento nesta fase.
Os perfis são instruções consultáveis, não processos autônomos instalados.
Não declarar treinamento de pesos, certificação ou domínio prático completo.
Só avançar para prática quando o usuário solicitar. A rotina diária continua
sincronizando apenas mudanças autorizadas; não iniciar exercícios por conta própria.

Em 12/10/2026, o usuário também autorizou instalar o FreeCAD portátil,
conferir sua abertura e pesquisar modelagem arquitetônica 3D. Essa verificação
de instalação é permitida; ainda não há pedido para construir a casa.

## Escopo e autorização

Trabalhar neste repositório elétrico. O usuário autorizou sua inicialização e
atualização diária em `booletech/estudio-projetos-eletricos`. Essa autorização
abrange exemplos sintéticos, scripts, documentação e instruções de agentes.
O repositório é público: não enviar materiais pessoais, credenciais, plantas
identificáveis de clientes ou arquivos de terceiros sem autorização específica.
Não usar APIs pagas. Não mudar o sistema nem instalar globalmente sem autorização.

## Preservação

Nunca apagar nem sobrescrever originais CAD. Importar por cópia e registrar
SHA-256; novas revisões devem ter nomes numerados. Não incorporar backups
automáticos `#...`, temporários ou instaladores. Usar Python isolado em `.venv`
(nesta máquina pode-se usar `../.venv`) e ferramentas portáteis em `tools`
(nesta máquina `../tools`).

## Trabalho elétrico

Não inventar cargas, tensão, potências, bitolas, proteções ou conformidade.
Separar desenho, cálculo, verificação estrutural e revisão humana. Manter
`pronto_para_publicar` e `pronto_para_execucao` falsos enquanto a aprovação
técnica/final estiver pendente. Arquivar um rascunho no GitHub não o aprova
para execução. Normas e conteúdo técnico exigem revisão humana.

## GitHub e rotina diária

Ler `docs/VERSIONAMENTO.md`. Revisar cada arquivo e a diferença antes de enviar;
nunca executar `git add .` automaticamente. Não alterar o repositório do
estúdio de vídeo, reescrever histórico, forçar push, resolver conflitos
descartando trabalho, ou sobrescrever mudança remota. Sincronizar somente
quando a preservação dos dois lados estiver garantida. Sem mudanças reais,
não criar commit nem notificar. Comunicar falhas, conflitos e impedimentos.

## Verificação

Executar `scripts/verificar_exemplos.py` após mudanças no exemplo inicial.
Registrar as verificações reais e seus limites. Abertura de XML/DXF e hashes
não comprovam revisão gráfica ou elétrica integral. Não declarar exportação
válida sem conferir o resultado. Não implementar funcionalidades futuras
somente na documentação. Não executar agentes em paralelo sem solicitação.
