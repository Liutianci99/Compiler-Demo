import re
from re import match
from tokenize import group

Token_patterns = {
    'Pre_Directive': r'#[^\n]*',
    'Keyword':r'\b(int|float|char|double|void|if|else|while|for|do|return|break|continue)\b',
    "Constant":r'\b\d+\b|\'[^\']\'|"[^"]*"',
    'Identifier':r'[a-zA-Z_][a-zA-Z0-9_]*',
    "Operater":r'[+\-*/=<>!&|]',
    "Separator":r'[.;,\(\)\{\}]'
}
Token_regex = {key:re.compile(pattern) for key, pattern in Token_patterns.items()}


def tokenize(lines):
    tokens = []
    line_number = 1
    for line in lines:
        line = line.strip()
        position = 0
        while position < len(line):
            match_found = False
            for token_type, regex in Token_regex.items():
                match = regex.match(line, position)
                if match:
                    token = (token_type, match.group(), line_number)
                    line_number +=1
                    tokens.append(token)
                    position = match.end()
                    match_found = True
                    break
            if not match_found:
                position += 1
    return tokens

with open("code.txt", "r") as file:
    lines = file.readlines()
    tokens = tokenize(lines)
    for token in tokens:
        print(f' {token[1]} 在 {token[2]} 行中是 {token[0]} 类型')




