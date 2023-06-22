# AI_Intern_Project

Project Clone

1)  type git clone https://github.com/USTAADCOM/AI_Intern_Project.git
2)  Download zip file from Google drive
    https://drive.google.com/file/d/17I7F177zLaa0CsqV4yed5-Kbd2iAX3UW/view?usp=drive_link
4)  Extract and copy models and .env folder in your folder clone from git
__________________________________________________________________________________________________________________________________________
Project contain two portions 
1) Text_Geneerator + Remove Image Background with GUI
2) API
__________________________________________________________________________________________________________________________________________
Start Project
1) activate virtual environment
2) python streamlit Homepage.py
It will start the streamlit server which will open in your default broswer
__________________________________________________________________________________________________________________________________________
API Usage
1) activate virtual environment
2) python app.py (run in API folder)
It will start localhost server
3) http://127.0.0.1:5000/api/completion/sentence_of_your_choice/
It will return the response complete sentence with response Code=201
 __________________________________________________________________________________________________________________________________________
 Model Description
 Text Generator model is developed by using the Hugging face transformers library
 -> Here we opt-125m model for text generation
 -> To use others models for better performance opt-350, opt-1.3b, opt-6.7b, opt-30b 
 Just do the following steps
 1) Change model name in text_geneeration_model.py
 2) Give the name to the folder with which you want to save your model on your computer
 3) run this file it will generate the configuration of your model
 4) Change the model folder name in Generate_Text.py
 5) run Generate_Text.py 

