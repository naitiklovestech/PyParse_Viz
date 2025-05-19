import tkinter as tk
from tkinter import ttk, scrolledtext, messagebox
from lexer_engine import tokenize_code
from parser_engine import parse_code
from tree_visualizer import visualize_ast, visualize_parse_tree
import json

class CodeAnalyzerGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Python Code Analyzer")
        self.root.geometry("1200x800")
        
        # Create main container 
        self.main_container = ttk.PanedWindow(root, orient=tk.HORIZONTAL)
        self.main_container.pack(fill=tk.BOTH, expand=True)
        
        # Left panel for code input only
        self.left_panel = ttk.Frame(self.main_container)
        self.main_container.add(self.left_panel, weight=1)
        
        self.code_label = ttk.Label(self.left_panel, text="Enter Python Code:")
        self.code_label.pack(anchor=tk.W, padx=5, pady=5)
        
        self.code_input = scrolledtext.ScrolledText(self.left_panel, wrap=tk.WORD, width=50, height=40)
        self.code_input.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
        
        # Add some sample code
        sample_code = '''def calculate_sum(a, b):
    if a > 0 and b > 0:
        return a + b
    else:
        return 0

result = calculate_sum(5, 3)
print(result)'''
        self.code_input.insert(tk.END, sample_code)

        # Right panel for buttons and result display
        self.right_panel = ttk.Frame(self.main_container)
        self.main_container.add(self.right_panel, weight=1)

        # Buttons
        self.lex_btn = ttk.Button(self.right_panel, text="Lexical Analysis", command=self.show_lexical_analysis)
        self.lex_btn.pack(pady=20, padx=20, fill=tk.X)

        self.parse_btn = ttk.Button(self.right_panel, text="Parse Tree", command=self.show_parse_tree)
        self.parse_btn.pack(pady=20, padx=20, fill=tk.X)

        self.ast_btn = ttk.Button(self.right_panel, text="AST", command=self.show_ast)
        self.ast_btn.pack(pady=20, padx=20, fill=tk.X)

        # Result display area
        self.result_label = ttk.Label(self.right_panel, text="Result:")
        self.result_label.pack(anchor=tk.W, padx=5, pady=(30, 5))
        self.result_text = scrolledtext.ScrolledText(self.right_panel, wrap=tk.WORD, width=50, height=30)
        self.result_text.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)

    def show_lexical_analysis(self):
        code = self.code_input.get("1.0", tk.END)
        self.result_text.delete("1.0", tk.END)
        try:
            tokens = tokenize_code(code)
            self.result_text.insert(tk.END, "Tokens:\n")
            for token in tokens:
                self.result_text.insert(tk.END, self.format_token(token) + "\n")
        except Exception as e:
            self.result_text.insert(tk.END, f"Error: {str(e)}")

    def show_parse_tree(self):
        code = self.code_input.get("1.0", tk.END)
        self.result_text.delete("1.0", tk.END)
        try:
            tree = parse_code(code, return_parse_tree=True)
            if tree:
                self.result_text.insert(tk.END, "Parse Tree (structure):\n")
                self.result_text.insert(tk.END, json.dumps(tree, indent=2))
                visualize_parse_tree(tree)
            else:
                self.result_text.insert(tk.END, "Failed to parse code.")
        except Exception as e:
            self.result_text.insert(tk.END, f"Error: {str(e)}")

    def show_ast(self):
        code = self.code_input.get("1.0", tk.END)
        self.result_text.delete("1.0", tk.END)
        try:
            ast = parse_code(code)
            if ast:
                self.result_text.insert(tk.END, "AST (structure):\n")
                self.result_text.insert(tk.END, json.dumps(ast, indent=2))
                visualize_ast(ast)
            else:
                self.result_text.insert(tk.END, "Failed to parse code.")
        except Exception as e:
            self.result_text.insert(tk.END, f"Error: {str(e)}")

    def format_token(self, token):
        return f"Type: {token['type']:<15} Value: {str(token['value']):<20} Line: {token['line']} Col: {token['column']}"

def main():
    root = tk.Tk()
    app = CodeAnalyzerGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main() 