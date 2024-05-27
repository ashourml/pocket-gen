import ollama



modelfile='''
FROM llava:latest
SYSTEM you are expert in generating stable diffusion ai prompt respnse with 1 prompt
'''


ollama.create(model='pocket_llava', modelfile=modelfile)


# respo = ollama.generate(
#     model= 'prompt:latest',
#     prompt='bathroom with urban style ',
# )['response']


# print(respo)