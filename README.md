# Ney's CSV Joiner

The motivation for creating this project came from a need that my father has at work. Basically, he needs to unify two CSVs based on a common key and generate a third CSV with the result of the unification. Previously, I had created a simple Python script and taught him how to use it, but it only worked in the environment I set up for him. That's why I created this project, to facilitate the task of unifying the files.

## Other Languages

- [Portuguese (Brazil)](docs/README.pt-br.md)

## Table of Contents

- [Ney's CSV Joiner](#neys-csv-joiner)
  - [Other Languages](#other-languages)
  - [Table of Contents](#table-of-contents)
  - [Features](#features)
  - [Requirements](#requirements)
  - [Installation](#installation)
  - [Usage](#usage)
  - [Create Executable](#create-executable)
    - [To create the executable:](#to-create-the-executable)
  - [Code Structure](#code-structure)
    - [`main.py`](#mainpy)
    - [`gui.py`](#guipy)
    - [`joiner.py`](#joinerpy)

## Features

- Select two CSV files.
- Automatic identification of common columns between files.
- Perform the join based on a selected column.
- Save the result in a new CSV file.

## Requirements

Make sure you have Python 3 installed on your machine.

## Installation

1. Clone this repository:

   ```bash
   git clone https://github.com/BRAN2K/csv-joiner.git
   cd csv-joiner
   ```

2. Install the required dependencies using the `requirements.txt` file:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. Run the application directly in the terminal:

   ```bash
   python src/main.py
   ```

2. In the interface, click the "Select File 1" button and choose the first CSV file.

3. Click the "Select File 2" button and choose the second CSV file.

4. Select the column that will be used to join the files from the drop-down menu.

5. Click the "Join!" button and choose a directory to save the output file.

6. The result will be saved as `resultado.csv` in the chosen directory.

## Create Executable

This project can be turned into an executable, allowing you to run the application without the need to compile the code every time. The build process has been tested and is available only for Windows.

### To create the executable:

1. Make sure you have `PyInstaller` installed. If not, install it with:

   ```bash
   pip install pyinstaller
   ```

2. Navigate to the root folder of the project.

3. Execute the following command:

   ```bash
   pyinstaller -F src/main.py --collect-all customtkinter -w
   ```

   - `-F` generates a single executable file.
   - `--collect-all customtkinter` ensures that all resources of the `customtkinter` library are included.
   - `-w` starts the application without opening a console window.

4. The executable will be generated in the `dist` folder. You can run the generated file directly.

## Code Structure

The code is divided into three main files:

### `main.py`

- Initializes the application and sets the theme and appearance mode of the interface. The graphical interface is based on the `customtkinter` library.

### `gui.py`

- Contains the `CSVJoinerApp` class, which defines the graphical interface, widgets (components), and the user interaction logic.

### `joiner.py`

- Contains the `join_csv_files` function that performs the merge of pandas DataFrames based on the selected column.
