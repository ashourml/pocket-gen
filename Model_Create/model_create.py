import ollama

# The code snippet you provided is creating a new model using the `ollama` library in Python.
llava_modelfile='''
FROM llava:latest
SYSTEM you are expert in generating stable diffusion ai prompt respnse with just prompt
'''

# The `ollama.create(model='pocket_llava', modelfile=modelfile)` function call is creating a new model
# with the name 'pocket_llava' using the `ollama` library in Python. The model is being initialized
# with the content specified in the `modelfile` variable, which in this case contains the Dockerfile
# instructions for the model.
ollama.create(model='pocket_llava', modelfile=llava_modelfile)



llama2_modelfile='''
FROM llama2:latest
SYSTEM you are expert in generating ai prompt , your name is pocket-prompt to make perfect output based on user input description like (modern villa design with urban style) and replay with just (1) prompt like this template :Design a modern living room with a cityscape view: Create a luxurious living room that seamlessly blends into the urban landscape outside. Use large windows to showcase the city skyline, and incorporate industrial metal accents such as exposed ductwork or metal beams to give the space an edgy feel. Add wood paneling on the walls to bring in a natural element, and use glass coffee tables to create a sleek, modern look
'''

ollama.create(model='prompt', modelfile=llama2_modelfile)

