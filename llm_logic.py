import ollama
from io import BytesIO
from flet import *


class LLM_model():
    def __init__(self , llm: ollama ):
        super().__init__()
        
        
        self.model = 'prompt:latest'
        self.llava_model = 'pocket_llava:latest'
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
    
    def Image_describe(self, image , prompt):
        img_bytes =self.read_image(image)
        
        self.describe = ollama.generate(
            model= self.llava_model,
            prompt= f'with details in this photo give me stable diffusion prompt with this details : {prompt}',
            stream=True,
            images=[img_bytes],
            
            
        ) 
        return self.describe
    


    def read_image(self, file_path):
        with open(file_path, "rb") as file:
            image_bytes = file.read()
        return image_bytes







# llm = LLM_model(ollama)
# re = ""
# respo = llm.Image_describe([imgb],'brown leather couch , blue light , 4k details ,realistic')

# for i in respo:
    
#     print(re.join(i['response']) )