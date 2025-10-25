import os
from flask import Flask, request, jsonify
from io import StringIO
import sys
from lexer import LexerFIA
from parser import ParserFIA
from interpreter import VisiteurInterpretation
from errors import FIAError

app = Flask(__name__)

def executer_code(code):
    old_stdout = sys.stdout
    sys.stdout = captured_output = StringIO()
    try:
        lexer = LexerFIA(code)
        tokens = lexer.tokeniser()
        parser = ParserFIA(tokens)
        ast = parser.analyser()
        interpreter = VisiteurInterpretation()
        interpreter.executer(ast)
        output = captured_output.getvalue()
        return output
    except FIAError as e:
        return str(e)
    except Exception as e:
        return f"Erreur inattendue: {str(e)}"
    finally:
        sys.stdout = old_stdout

@app.route('/execute', methods=['POST'])
def execute():
    code = request.json.get('code', '')
    result = executer_code(code)
    return jsonify({'result': result})

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
