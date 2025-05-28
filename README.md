# Python Code Analyzer 🐍

A powerful Python application that analyzes Python code and visualizes its structure through lexical analysis and parsing. This tool helps developers understand code structure and identify potential issues through interactive visualization.

## ✨ Features

### Core Analysis
- **Lexical Analysis**: Tokenizes Python code into its basic components
- **Syntax Analysis**: Parses the code into an Abstract Syntax Tree (AST)
- **Visualization**: Displays the parse tree in a graphical format
- **Interactive GUI**: User-friendly interface for code input and analysis

### New Features
- **Code Metrics**: Calculate and display code complexity metrics
- **Error Detection**: Identify common syntax errors and code smells
- **Export Options**: Export analysis results to various formats (PDF, JSON)
- **Theme Support**: Light and dark mode for better viewing experience
- **Real-time Analysis**: Get instant feedback as you type
- **Code Suggestions**: Receive improvement suggestions based on analysis

## 📸 Screenshots

### Main Interface
![Main Interface](screenshots/main_interface.png)
*The main application window with code input and analysis panels*

### Parse Tree Visualization
![Parse Tree](screenshots/parse_tree.png)
*Interactive visualization of the code's parse tree*

### Analysis Results
![Analysis Results](screenshots/analysis_results.png)
*Detailed analysis results and metrics display*

## 🚀 Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/python-code-analyzer.git
cd python-code-analyzer
```

2. Create a virtual environment:
```bash
python -m venv venv
```

3. Activate the virtual environment:
- Windows:
```bash
.\venv\Scripts\activate
```
- Unix/MacOS:
```bash
source venv/bin/activate
```

4. Install dependencies:
```bash
pip install -r requirements.txt
```

## 💻 Usage

1. Run the application:
```bash
python main.py
```

2. Enter Python code in the input area
3. Click "Analyze" to see the tokens and AST
4. View the parse tree visualization
5. Explore additional features in the toolbar

## 📁 Project Structure

```
python-code-analyzer/
├── main.py              # Main application entry point and GUI
├── lexer_engine.py      # Lexical analyzer implementation
├── parser_engine.py     # Parser implementation
├── tree_visualizer.py   # Parse tree visualization
├── metrics.py           # Code metrics calculation
├── error_detector.py    # Error detection module
└── utils/              # Utility functions and helpers
```

## 📋 Requirements

- Python 3.8 or higher
- Tkinter (usually comes with Python)
- Dependencies listed in requirements.txt

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- Thanks to all contributors who have helped shape this project
- Inspired by various code analysis tools and visualization libraries 
