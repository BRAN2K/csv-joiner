# Juntador de Arquivos do Ney

A motivação para criar esse projeto foi por conta de uma necessidade que meu pai tem no trabalho. Basicamente ele precisa realizar a unificação entre dois CSVs a partir de uma chave em comum e gerar um terceiro CSV com o resultado da unificação. Anteriormente eu tinha criado um script simples em python e o ensinei a usá-lo, porém só funcionava no ambiente que configurei para ele. Por isso criei esse projeto, para facilitar a tarefa de unificação dos arquivos.

## Outras línguas

- [Inglês](../README.md)

## Índice

- [Juntador de Arquivos do Ney](#juntador-de-arquivos-do-ney)
  - [Outras línguas](#outras-línguas)
  - [Índice](#índice)
  - [Recursos](#recursos)
  - [Requisitos](#requisitos)
  - [Instalação](#instalação)
  - [Uso](#uso)
  - [Criação de Executável](#criação-de-executável)
    - [Para criar o executável:](#para-criar-o-executável)
  - [Estrutura do Código](#estrutura-do-código)
    - [`main.py`](#mainpy)
    - [`gui.py`](#guipy)
    - [`joiner.py`](#joinerpy)

## Recursos

- Seleção de dois arquivos CSV.
- Identificação automática de colunas comuns entre os arquivos.
- Realização do join com base em uma coluna selecionada.
- Salvamento do resultado em um novo arquivo CSV.

## Requisitos

Certifique-se de ter o Python 3 instalado em sua máquina.

## Instalação

1. Clone este repositório:

   ```bash
   git clone https://github.com/BRAN2K/csv-joiner.git
   cd csv-joiner
   ```

2. Instale as dependências necessárias com o arquivo `requirements.txt`:
   ```bash
   pip install -r requirements.txt
   ```

## Uso

1. Execute o aplicativo diretamente no terminal:

   ```bash
   python src/main.py
   ```

2. Na interface, clique no botão "Selecione o arquivo 1" e escolha o primeiro arquivo CSV.

3. Clique no botão "Selecione o arquivo 2" e escolha o segundo arquivo CSV.

4. Selecione a coluna que será usada para juntar os arquivos no menu suspenso.

5. Clique no botão "Juntar!" e escolha um diretório para salvar o arquivo resultante.

6. O resultado será salvo como `resultado.csv` no diretório escolhido.

## Criação de Executável

Este projeto pode ser transformado em um executável, permitindo que você execute o aplicativo sem a necessidade de compilar o código toda vez. O processo de build foi testado e está disponível apenas para Windows.

### Para criar o executável:

1. Certifique-se de ter o `PyInstaller` instalado. Se não estiver, instale-o com:

   ```bash
   pip install pyinstaller
   ```

2. Navegue até a pasta raiz do projeto.

3. Execute o seguinte comando:

   ```bash
   pyinstaller -F src/main.py --collect-all customtkinter -w
   ```

   - `-F` gera um único arquivo executável.
   - `--collect-all customtkinter` garante que todos os recursos da biblioteca `customtkinter` sejam incluídos.
   - `-w` inicia a aplicação sem abrir uma janela de console.

4. O executável será gerado na pasta `dist`. Você pode executar o arquivo gerado diretamente.

## Estrutura do Código

O código é dividido em quatro arquivos principais:

### `main.py`

- Inicializa a aplicação e define o tema e modo de aparência da interface. A interface gráfica é baseada na biblioteca `customtkinter`.

### `gui.py`

- Contém a classe `CSVJoinerApp`, que define a interface gráfica, widgets (componentes) e a lógica de interação com o usuário.

### `joiner.py`

- Contém a função `join_csv_files`, que executa o merge dos DataFrames do pandas com base na coluna selecionada.
