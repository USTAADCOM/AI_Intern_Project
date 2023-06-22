from flask import Flask, abort, make_response
import streamlit as st
from transformers import OPTForCausalLM, AutoTokenizer
import regex as re

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello, Flask!'
@app.route('/api/completion/<sentence>/', methods=['GET'])
def generate_sentence(sentence):
    model = OPTForCausalLM.from_pretrained('../models/generate_sentence125m')
    tokenizer = AutoTokenizer.from_pretrained('../models/generate_sentence125m')
    inputs = tokenizer(sentence,return_tensors="pt")
    generate_ids = model.generate(inputs.input_ids.to('cpu'), max_length=30)
    output=tokenizer.batch_decode(generate_ids, skip_special_tokens=True, clean_up_tokenization_spaces=False)[0]
    regex=r"[A-Za-z0-9?! ]*"
    final_output=re.search(regex, output)[0]
    return final_output+".", 201

if __name__ == '__main__':
    app.run(debug=True)