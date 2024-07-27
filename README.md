## Como Instalar e Executar

### Pré-requisitos

- Python 3.x

### Passos

1. Clone o repositório:

   ```sh
   git clone https://github.com/seu-usuario/CSVJoiner.git
   cd CSVJoiner
   ```

2. Crie e ative um ambiente virtual:

   ```sh
   python -m venv venv
   source venv/bin/activate  # No Windows use: venv\Scripts\activate
   ```

3. Instale as dependências:

   ```sh
   pip setup.py install

   ```

4. Execute a aplicação:
   ```sh
   python src/main.py
   ```

### Gerar o Executável

1. Instale o `pyinstaller`:

   ```sh
   pip install pyinstaller
   ```

2. Gere o executável:
   ```sh
   pyinstaller --onefile --windowed src/main.py
   ```

O executável será criado na pasta `dist`.
