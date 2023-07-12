from flask import Flask, render_template, request, jsonify
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.sequence import pad_sequences
import numpy as np
import pickle

app = Flask(__name__)

# Load the trained model
model = load_model('output/seq2seq.h5')

# Load the tokenizers
with open('output/x_tokenizer.pickle', 'rb') as handle:
    x_tokenizer = pickle.load(handle)

with open('output/y_tokenizer.pickle', 'rb') as handle:
    y_tokenizer = pickle.load(handle)

# Define maximum lengths
max_text_len = 100
max_summary_len = 15


def preprocess_text(input_text):
    # Tokenize the input text
    text_seq = x_tokenizer.texts_to_sequences([input_text])
    # Pad the sequences
    text_seq = pad_sequences(text_seq, maxlen=max_text_len, padding='post')
    return text_seq


def decode_sequence(input_seq, summary_length):
    # Generate the summary sequence using the trained model
    e_out, e_h, e_c = model.encoder_model.predict(input_seq)
    target_seq = np.zeros((1, 1))
    target_seq[0, 0] = y_tokenizer.word_index['sostok']
    decoded_seq = ''
    while True:
        output_tokens, h, c = model.decoder_model.predict([target_seq] + [e_out, e_h, e_c])
        sampled_token_index = np.argmax(output_tokens[0, -1, :])
        sampled_token = y_tokenizer.index_word[sampled_token_index]
        if sampled_token == 'eostok' or len(decoded_seq.split()) >= (summary_length - 1):
            break
        decoded_seq += ' ' + sampled_token
        target_seq = np.zeros((1, 1))
        target_seq[0, 0] = sampled_token_index
        e_h, e_c = h, c
    return decoded_seq.strip()


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/compare')
def compare():
    return render_template('compare.html')


@app.route('/summarize', methods=['POST'])
def summarize():
    # Get the input text and summary length from the request
    input_text = request.json.get('input_text')
    summary_length = request.json.get('summary_length')

    if input_text is None or summary_length is None:
        return jsonify({'error': 'Missing input text or summary length'}), 400

    # Preprocess the text
    input_seq = preprocess_text(input_text)

    # Generate the summary
    summary = decode_sequence(input_seq, summary_length)

    # Return the summary as the response
    response = {'summary': summary}
    return jsonify(response)


if __name__ == '__main__':
    app.run(debug=True)
