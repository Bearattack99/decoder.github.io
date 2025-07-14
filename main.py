from flask import Flask, render_template, request

app = Flask(__name__)

# Updated with your specific encoding mapping
ENCODING_MAP = {
    'a': 'a', 'b': 'c', 'c': 'e', 'd': 'f', 'e': 'h',
    'f': 'j', 'g': 'l', 'h': 'm', 'i': 'o', 'j': 'q',
    'k': 's', 'l': 't', 'm': 'v', 'n': 'x', 'o': 'y',
    'p': 'b', 'q': 'd', 'r': 'g', 's': 'i', 't': 'k',
    'u': 'n', 'v': 'p', 'w': 'r', 'x': 'u', 'y': 'w',
    'z': 'z',
    'A': 'A', 'B': 'C', 'C': 'E', 'D': 'F', 'E': 'H',
    'F': 'J', 'G': 'L', 'H': 'M', 'I': 'O', 'J': 'Q',
    'K': 'S', 'L': 'T', 'M': 'V', 'N': 'X', 'O': 'Y',
    'P': 'B', 'Q': 'D', 'R': 'G', 'S': 'I', 'T': 'K',
    'U': 'N', 'V': 'P', 'W': 'R', 'X': 'U', 'Y': 'W',
    'Z': 'Z'
}

# Create decoding map by reversing the encoding map
DECODING_MAP = {v: k for k, v in ENCODING_MAP.items()}

def encode_text(text):
    """Encode the input text using the encoding map"""
    encoded = []
    for char in text:
        if char in ENCODING_MAP:
            encoded.append(ENCODING_MAP[char])
        else:
            encoded.append(char)  # Keep non-alphabetic characters as-is
    return ''.join(encoded)

def decode_text(text):
    """Decode the input text using the decoding map"""
    decoded = []
    for char in text:
        if char in DECODING_MAP:
            decoded.append(DECODING_MAP[char])
        else:
            decoded.append(char)  # Keep non-alphabetic characters as-is
    return ''.join(decoded)

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    action = None
    input_text = ''
    
    if request.method == 'POST':
        action = request.form.get('action')
        input_text = request.form.get('input_text', '')
        
        if action == 'encode':
            result = encode_text(input_text)
        elif action == 'decode':
            result = decode_text(input_text)
    
    return render_template('index.html', 
                         input_text=input_text, 
                         result=result,
                         action=action)

if __name__ == '__main__':
    app.run(debug=True)