# Casos de Uso - UniManager

## Objetivo

Este documento descreve os usuários do sistema, suas permissões e as principais decisões funcionais definidas durante o planejamento do UniManager.

# Atores

## Administrador

O administrador possui acesso completo ao sistema.

### Permissões

- Fazer login
- Fazer logout
- Gerenciar alunos
- Gerenciar professores
- Gerenciar cursos
- Gerenciar disciplinas
- Criar turmas
- Matricular alunos
- Visualizar dashboard
- Pesquisar informações
- Gerenciar usuários

## Professor

O professor possui acesso às funcionalidades acadêmicas.

### Permissões

- Fazer login
- Fazer logout
- Visualizar suas disciplinas
- Visualizar alunos matriculados
- Lançar notas
- Registrar frequência
- Consultar desempenho dos alunos

## Aluno

O aluno possui acesso apenas às suas próprias informações.

### Permissões

- Fazer login
- Fazer logout
- Visualizar disciplinas matriculadas
- Consultar notas
- Consultar frequência
- Editar informações do perfil

# Decisões de Projeto

## Sistema de autenticação

O sistema possuirá três tipos de usuários:

- Administrador
- Professor
- Aluno

Cada tipo de usuário terá permissões específicas.

## Cursos

Todo aluno obrigatoriamente estará vinculado a um curso.

Exemplos:

- Ciência da Computação
- Engenharia Civil
- Direito
- Medicina

Cada curso possuirá seu próprio conjunto de disciplinas.

## Disciplinas e Turmas

Inicialmente cada disciplina poderá possuir diferentes turmas.

Essa estrutura poderá ser refinada durante o desenvolvimento do projeto.

## Perfil

Todos os usuários poderão editar:

- Foto
- Nome
- Email
- Senha

## Dashboard

O dashboard será composto por:

- Indicadores (cards)
- Gráficos
- Últimas atividades
- Próximas avaliações
- Estatísticas acadêmicas