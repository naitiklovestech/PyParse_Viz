import tkinter as tk
from tkinter import ttk, scrolledtext
from lexer_engine import tokenize_code
from parser_engine import parse_code
from tree_visualizer import save_and_return_image
from PIL import Image, ImageTk
import json

class CodeAnalyzerGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Python Code Analyzer")
        self.root.geometry("1600x900")

        self.main_container = ttk.PanedWindow(root, orient=tk.HORIZONTAL)
        self.main_container.pack(fill=tk.BOTH, expand=True)

        self.left_panel = ttk.Frame(self.main_container)
        self.main_container.add(self.left_panel, weight=1)

        self.code_label = ttk.Label(self.left_panel, text="Enter Python Code:")
        self.code_label.pack(anchor=tk.W, padx=5, pady=5)

        self.code_input = scrolledtext.ScrolledText(self.left_panel, wrap=tk.WORD, width=60, height=40)
        self.code_input.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)

        sample_code = '''def calculate_sum(a, b):
    if a > 0 and b > 0:
        return a + b
    else:
        return 0

result = calculate_sum(5, 3)
print(result)'''
        self.code_input.insert(tk.END, sample_code)

        self.right_panel = ttk.Frame(self.main_container)
        self.main_container.add(self.right_panel, weight=2)

        self.lex_btn = ttk.Button(self.right_panel, text="Lexical Analysis", command=self.show_lexical_analysis)
        self.lex_btn.pack(pady=10, padx=20, fill=tk.X)

        self.parse_btn = ttk.Button(self.right_panel, text="Parse Tree", command=self.show_parse_tree)
        self.parse_btn.pack(pady=10, padx=20, fill=tk.X)

        self.ast_btn = ttk.Button(self.right_panel, text="AST", command=self.show_ast)
        self.ast_btn.pack(pady=10, padx=20, fill=tk.X)

        self.result_label = ttk.Label(self.right_panel, text="Result:")
        self.result_label.pack(anchor=tk.W, padx=5, pady=(30, 5))

        self.result_text = scrolledtext.ScrolledText(self.right_panel, wrap=tk.WORD, width=80, height=20)
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
                image_path = save_and_return_image(tree)
                self.open_image_window(image_path, "Parse Tree")
            else:
                self.result_text.insert(tk.END, "Failed to parse code.")
        except Exception as e:
            self.result_text.insert(tk.END, f"Error: {str(e)}")

    def show_ast(self):
        code = self.code_input.get("1.0", tk.END)
        self.result_text.delete("1.0", tk.END)
        try:
            tree = parse_code(code, return_parse_tree=False)
            if tree:
                self.result_text.insert(tk.END, "AST (structure):\n")
                self.result_text.insert(tk.END, json.dumps(tree, indent=2))
                image_path = save_and_return_image(tree, filename="ast.png")
                self.open_image_window(image_path, "Abstract Syntax Tree")
            else:
                self.result_text.insert(tk.END, "Failed to parse code.")
        except Exception as e:
            self.result_text.insert(tk.END, f"Error: {str(e)}")

    def open_image_window(self, image_path, title):
        try:
            image = Image.open(image_path)
            image = image.resize((1200, 700))  # Resize to fit nicely

            top = tk.Toplevel(self.root)
            top.title(title)

            tk_image = ImageTk.PhotoImage(image)
            label = tk.Label(top, image=tk_image)
            label.image = tk_image  # Prevent garbage collection
            label.pack(padx=10, pady=10)
        except Exception as e:
            self.result_text.insert(tk.END, f"Error displaying image: {str(e)}")

    def format_token(self, token):
        return f"Type: {token['type']:<15} Value: {str(token['value']):<20} Line: {token['line']} Col: {token['column']}"

def main():
    root = tk.Tk()
    app = CodeAnalyzerGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()
