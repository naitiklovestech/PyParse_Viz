import ply.yacc as yacc
from lexer_engine import tokens

# Global flag to switch between parse tree and AST
build_ast = False

# Grammar rules
def p_program(p):
    '''program : statements'''
    p[0] = p[1] if build_ast else ('program', p[1])

def p_statements(p):
    '''statements : statement
                  | statements statement'''
    if len(p) == 2:
        p[0] = p[1]
    else:
        p[0] = ('STATEMENTS', p[1], p[2])

def p_statement(p):
    '''statement : assignment
                 | if_statement
                 | while_statement
                 | for_statement
                 | function_def
                 | return_statement
                 | expression
                 | NEWLINE'''
    p[0] = p[1] if p[1] != '\n' else None

def p_assignment(p):
    'assignment : NAME EQUALS expression'
    p[0] = ('ASSIGN', p[1], p[3]) if build_ast else ('assignment', p[1], '=', p[3])

def p_if_statement(p):
    '''if_statement : IF expression COLON NEWLINE statements
                    | IF expression COLON NEWLINE statements ELSE COLON NEWLINE statements'''
    if build_ast:
        if len(p) == 6:
            p[0] = ('IF', p[2], p[5])
        else:
            p[0] = ('IF-ELSE', p[2], p[5], p[9])
    else:
        if len(p) == 6:
            p[0] = ('if_statement', 'if', p[2], ':', p[5])
        else:
            p[0] = ('if_else_statement', 'if', p[2], ':', p[5], 'else', ':', p[9])

def p_while_statement(p):
    'while_statement : WHILE expression COLON NEWLINE statements'
    p[0] = ('WHILE', p[2], p[5]) if build_ast else ('while_statement', 'while', p[2], ':', p[5])

def p_for_statement(p):
    'for_statement : FOR NAME IN expression COLON NEWLINE statements'
    p[0] = ('FOR', p[2], p[4], p[7]) if build_ast else ('for_statement', 'for', p[2], 'in', p[4], ':', p[7])

def p_function_def(p):
    'function_def : DEF NAME LPAREN parameters RPAREN COLON NEWLINE statements'
    p[0] = ('FUNCTION', p[2], p[4], p[8]) if build_ast else ('function_def', 'def', p[2], '(', p[4], ')', ':', p[8])

def p_parameters(p):
    '''parameters : empty
                  | parameter_list'''
    p[0] = p[1]

def p_parameter_list(p):
    '''parameter_list : NAME
                      | parameter_list COMMA NAME'''
    if len(p) == 2:
        p[0] = p[1]
    else:
        p[0] = ('PARAMS', p[1], p[3])

def p_return_statement(p):
    'return_statement : RETURN expression'
    p[0] = ('RETURN', p[2]) if build_ast else ('return_statement', 'return', p[2])

def p_expression(p):
    '''expression : term
                  | expression PLUS term
                  | expression MINUS term
                  | expression AND term
                  | expression OR term'''
    if len(p) == 2:
        p[0] = p[1] if build_ast else ('expression', p[1])
    else:
        p[0] = (p[2], p[1], p[3]) if build_ast else ('expression', p[1], p[2], p[3])

def p_term(p):
    '''term : factor
            | term TIMES factor
            | term DIVIDE factor
            | term EQ factor
            | term NE factor
            | term LT factor
            | term GT factor
            | term LE factor
            | term GE factor'''
    if len(p) == 2:
        p[0] = p[1] if build_ast else ('term', p[1])
    else:
        p[0] = (p[2], p[1], p[3]) if build_ast else ('term', p[1], p[2], p[3])

def p_factor(p):
    '''factor : NUMBER
              | STRING
              | NAME
              | TRUE
              | FALSE
              | NONE
              | NOT factor
              | LPAREN expression RPAREN
              | NAME LPAREN arguments RPAREN'''
    if len(p) == 2:
        p[0] = p[1]
    elif len(p) == 3:
        p[0] = ('NOT', p[2]) if build_ast else ('not_expr', 'not', p[2])
    elif len(p) == 4:
        p[0] = p[2]
    else:
        p[0] = ('CALL', p[1], p[3]) if build_ast else ('function_call', p[1], '(', p[3], ')')

def p_arguments(p):
    '''arguments : empty
                 | argument_list'''
    p[0] = p[1]

def p_argument_list(p):
    '''argument_list : expression
                     | argument_list COMMA expression'''
    if len(p) == 2:
        p[0] = p[1]
    else:
        p[0] = ('ARGS', p[1], p[3])

def p_empty(p):
    'empty :'
    p[0] = []

def p_error(p):
    if p:
        print(f"Syntax error at '{p.value}' (line {p.lineno})")
    else:
        print("Syntax error at EOF")

parser = yacc.yacc()

def generate_parse_tree(code):
    global build_ast
    build_ast = False
    try:
        return parser.parse(code, tracking=True)
    except Exception as e:
        print(f"Error generating parse tree: {str(e)}")
        return None

def generate_ast(code):
    global build_ast
    build_ast = True
    try:
        return parser.parse(code, tracking=False)
    except Exception as e:
        print(f"Error generating AST: {str(e)}")
        return None

def parse_code(code, return_parse_tree=False):
    global build_ast
    build_ast = not return_parse_tree
    try:
        return parser.parse(code, tracking=True)
    except Exception as e:
        print(f"Error parsing code: {str(e)}")
        return None
