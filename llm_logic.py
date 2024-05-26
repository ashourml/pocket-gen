import ollama



from flet import *


class LLM_model():
    def __init__(self , llm: ollama ):
        super().__init__()
        
        
        self.model = 'prompt:latest'
        # self.system_msg = 'you are expert in generating ai prompt to make perfect output based on user input description and replay with just 1 prompt '
        # self.template = """Design a modern living room with a cityscape view: Create a luxurious living room that seamlessly blends into 
        # the urban landscape outside. Use large windows to showcase the city skyline, and incorporate industrial metal
        # accents such as exposed ductwork or metal beams to give the space an edgy feel. Add wood paneling on the walls to
        # bring in a natural element, and use glass coffee tables to create a sleek, modern look """
        self.respo = ''
        
        
        
        
    def generate(self, prompt)  -> str:
        self.respo = ollama.generate(
            model=  self.model,
            # system= self.system_msg,
            # template=self.template,
            prompt= prompt,
            stream= True

        )
        return self.respo
    
    
    
    
# llm = LLM_model(ollama)
# re = ""
# respo = llm.generate('modern room with glass , wood , urban design')

# for i in respo:
#     print(re.join(i['response']) )