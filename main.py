
"""
The main function sets up a graphical user interface for a "pocket prompt generator" application in
Python using the Flet library for creating text and image prompts.

:param page: The `page` parameter is an object that represents the current page being displayed in
the application. It contains various properties and methods that allow you to customize the
appearance and behavior of the page. In the provided code snippet, the `main` function is the entry
point of the application and it takes a
:type page: Page
"""
from flet import *
import os
from strings_.strings import *
from views.text2text_view import *
from views.image2txt_view import *


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
    page.go('/text_prompt')
    page.update()


app(target=main, assets_dir='assets')

