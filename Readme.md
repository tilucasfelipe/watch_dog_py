# Algoritmo Wathdogs criado para analisar em tempo real todas as alterações realizadas no diretório do projeto.
__________________________________________________________________________
#### O algoritmo conta com os módulos:
- socket
- os
- sys
- logging
- time
- FileSystemEventHandler
- LoggingEventHandler
- Observer

#### Melhorias previstas para as próximas versões:
- Configurar os diretórios desejados para análise via arquivo de configuração.
- Tratar as modificações por tipo, informando os dados do arquivo antes e após a alteração.
- Enviar um email caso haja alteração no diretório - Será parametrizado via arquivo de configuração
- Gerar backup de arquivos de texto, PDF, imagens e/ou planilhas antes da alteração.