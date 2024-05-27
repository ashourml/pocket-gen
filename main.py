import socket
from flet import *
import os
from strings import *
from text_view import *
from image2txt_view import *


def main(page: Page):


    page.title = 'pocket prompt gen'
    page.padding = 10
    page.window_maximizable = False
    page.window_min_width = 900
    page.window_min_height = 415
    page.window_max_width = 900
    page.window_max_height = 415
    page.window_always_on_top = True 
    page.padding = 0
    page.spacing = 0
    page.window_frameless = True
    page.window_bgcolor = colors.TRANSPARENT
    page.bgcolor = colors.TRANSPARENT
    page.theme = Theme(font_family='sf')
    page.auto_scroll = True
    page.fonts = {
        'sf': r"assets\fonts\alfont_com_SFProAR_semibold.ttf",
        'sfm' : r"assets\fonts\SF-Pro-Text-Medium.otf"
    }
    page.theme = Theme(font_family='sf')

    

    
    def router(route) -> None:
        page.views.clear()
        
        if page.route == '/text_prompt':
            text_prom = Text_prompt(page)
            page.views.append(text_prom)
            
        if page.route == '/image2txt':
            image_prom = Image_prompt(page )
            page.views.append(image_prom)
        
                        
        page.update()

                
    page.on_route_change = router
    page.go('/image2txt')
    page.update()


app(target=main, assets_dir='assets')

