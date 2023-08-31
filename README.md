# Sistema de Backup Distribuído
Projeto da AB1 da matéria de sistemas distribuídos.

## Pré Requisitos:
1. Implementar backups programados de um conjunto de dados.
2. Prover funcionalidade para restaurar backup.

## Etapas:

1. Foram criados dois `buckets` no google cloud, um para envio de arquivos e outro para armazenamento.
2.  Na criação dos buckets foi ativado a opção de `controle de versões de objetos` para poder se ter a funcionalidade de restaurar o backup de um dado, sendo definido um limite de 3 versões para cada objeto e a exclusão da versão mais antiga a cada 7 dias com intuito de uma melhor utilização da memória
4. Foi desenvolvido um script em python para facilitar o envio dos arquivos para o bucket.
5. Foi criado um `job de transferência` para enviar diariamente os arquivos de um bucket para o outro.
6. É possível restaurar o backup de um arquivo indo em `"Detalhes do objeto" → "Histórico de Versões"`, e escolher a versão desejada.

## Vídeo de Demonstração
Link: https://youtu.be/CRKL7HCKrNQ
