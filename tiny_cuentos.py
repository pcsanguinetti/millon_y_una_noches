import tracery
from tracery.modifiers import base_english
import ast

with open("tiny_cuentos_grammar.txt") as f:
    grammar = f.read()

rules = ast.literal_eval(grammar)

grammar = tracery.Grammar(rules)
grammar.add_modifiers(base_english)
print(grammar.flatten("#origin#"))