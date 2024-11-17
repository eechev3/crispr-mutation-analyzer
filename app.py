from flask import Flask, render_template, request, jsonify
from Bio.Seq import Seq

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    data = request.json
    original_sequence = data['sequence']
    mutation_position = data['position']
    mutation_type = data['mutation']
    
    # Simulate CRISPR edit
    edited_sequence = list(original_sequence)
    edited_sequence[mutation_position] = mutation_type
    edited_sequence = ''.join(edited_sequence)
    
    original_seq_obj = Seq(original_sequence)
    edited_seq_obj = Seq(edited_sequence)

    # Return results
    return jsonify({
        'original': original_sequence,
        'edited': edited_sequence,
        'original_protein': str(original_seq_obj.translate()),
        'edited_protein': str(edited_seq_obj.translate())
    })

if __name__ == '__main__':
    app.run(debug=True)
