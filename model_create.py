import ollama



# modelfile='''
# FROM llama2:latest
# SYSTEM you are expert in generating ai prompt , your name is prompeto to make perfect output based on user input description like (modern villa design with urban style) and replay with just (1) prompt like this template :Design a modern living room with a cityscape view: Create a luxurious living room that seamlessly blends into the urban landscape outside. Use large windows to showcase the city skyline, and incorporate industrial metal accents such as exposed ductwork or metal beams to give the space an edgy feel. Add wood paneling on the walls to bring in a natural element, and use glass coffee tables to create a sleek, modern look



# '''


# ollama.create(model='prompt', modelfile=modelfile)


respo = ollama.generate(
    model= 'prompt:latest',
    prompt='bathroom with urban style ',
)['response']


print(respo)