# Python Code Analyzer

A Python application that analyzes Python code and visualizes its structure through lexical analysis and parsing.

## Features

- Lexical Analysis: Tokenizes Python code into its basic components
- Syntax Analysis: Parses the code into an Abstract Syntax Tree (AST)
- Visualization: Displays the parse tree in a graphical format
- Interactive GUI: User-friendly interface for code input and analysis

## Installation

1. Create a virtual environment:
```bash
python -m venv venv
```

2. Activate the virtual environment:
- Windows:
```bash
.\venv\Scripts\activate
```
- Unix/MacOS:
```bash
source venv/bin/activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

1. Run the application:
```bash
python main.py
```

2. Enter Python code in the input area
3. Click "Analyze" to see the tokens and AST
4. View the parse tree visualization

## Project Structure

- `main.py`: Main application entry point and GUI
- `lexer_engine.py`: Lexical analyzer implementation
- `parser_engine.py`: Parser implementation
- `tree_visualizer.py`: Parse tree visualization

## Requirements

- Python 3.8 or higher
- Tkinter (usually comes with Python)
- Dependencies listed in requirements.txt 
