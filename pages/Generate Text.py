import streamlit as st
from transformers import OPTForCausalLM, AutoTokenizer
import regex as re
st.title("Text Generator")

def main():

    #col1, col2 = st.columns(2)
    #with col1:
    input_text=st.text_area( label='Input box',key='input', placeholder="Enter your sentnce" , height=250)

    submit = st.button("Generate")
    if submit:
        if input_text!="": 
            generate_model_func(input_text)
        else:
            st.error("Enter your sentence")
            
def generate_model_func(input_text):
    model = OPTForCausalLM.from_pretrained('./models/generate_sentence125m')
    tokenizer = AutoTokenizer.from_pretrained('./models/generate_sentence125m')
    inputs = tokenizer(input_text, return_tensors="pt")
    generate_ids = model.generate(inputs.input_ids.to('cpu'), max_length=30)
    output=tokenizer.batch_decode(generate_ids, skip_special_tokens=True, clean_up_tokenization_spaces=False)[0]
    regex=r"[A-Za-z0-9?! ]*"
    final_output=re.search(regex, output)[0]
    output_text=st.text_area(label='Output box',key='output_text', placeholder="Your output here", value=final_output+".", height=250)
    

main()