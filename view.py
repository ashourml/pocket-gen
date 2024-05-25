from flet import *
from strings import *

class Text_prompt(View):
    def __init__(self , page: Page):
        super().__init__(route= '/text_prompt')
        
        
        self.background_color = background_color
        self.foreground_color = foreground_color 
        self.button_color = buttons_color
        self.span_color = span_color
        self.text_style_content = text_style_content
        self.shadow = shadow
        
        self.close_icon = IconButton(
            icon=icons.CLOSE_ROUNDED,
            scale=0.8,
            bgcolor=colors.TRANSPARENT,
            icon_color=colors.WHITE ,
            on_click=lambda x: page.window_close()
        )
        
        self.details_field = Container(
            padding=padding.all(10),
            border_radius=25,
            width=600,
            height=60,
            content=TextField(
                width=600,
                height=40,
                border_radius=20,
                bgcolor=colors.with_opacity(0.4,self.foreground_color),
                hint_text='Enter your prompt details ...',
                hint_style=text_style,
                password=False,
                can_reveal_password=False,
                content_padding=padding.all(5),
                border_width=0,
                tooltip='Black OPS',
                cursor_color=colors.WHITE,
                cursor_width=0.3,
                text_style=self.text_style_content,
                multiline=True

            )
        )
        
        self.drag_bar = WindowDragArea(
            content=Container(
                height=40,
                border_radius=20,
                bgcolor=self.foreground_color,
                shadow=self.shadow,
                content=Row(
                    alignment=MainAxisAlignment.SPACE_BETWEEN,
                    controls=[
                        Row(
                            alignment=MainAxisAlignment.START,
                            controls=[
                                Container(
                                    # bgcolor=foreground_color,
                                    # border_radius=30,
                                    content=Image(
                                        src=r'assets\icons\Asset.png',
                                        scale=0.7
                                        
                                    ),
                                    on_click=lambda x: print('logo clicked')

                                ),
                            ],

                        ),
                        Row(
                            alignment=MainAxisAlignment.END,
                            controls=[
                             self.close_icon
                            ],

                        )
                    ]
                )
            ),
            maximizable=False,

        )

        self.prompt_generated = Text(
                value= ' here the prompt that generate independ on the user input',
                max_lines= 10,
                selectable= True,
            )
        
        self.copy_icon = IconButton(
                    icon= icons.COPY_ALL_OUTLINED,
                    icon_color=colors.WHITE ,
                    scale= 0.6 ,
                )
        self.prompt_container_controls = Row(
        alignment=MainAxisAlignment.START,
        controls= [
            self.copy_icon
        ]
    )
        
        self.prompt_txt = Container(
        bgcolor= colors.BLACK12,
        border_radius=20,
        height=30,
        width=600,
        padding= padding.all(5),
        content= Column(
            controls=[
                self.prompt_generated,
                self.prompt_container_controls,
            ]
            ),
    )
        self.generate_bt = TextButton(
        text= 'Generate',
        style=ButtonStyle(
            bgcolor= colors.GREEN,
            shadow_color= colors.WHITE12,
            padding= padding.all(10),
            color= colors.WHITE
        ),
    )   
        self.prompt_container = Container(
        bgcolor= colors.with_opacity(0.2,self.span_color),
        width= 600 , 
        height= 150,
        content=self.prompt_txt,
            
        border_radius= 20,
        padding=padding.all(15)
    )
        
        self.pageview = Container(
            bgcolor=self.background_color , 
            width=900,
            height=400,
            border_radius=30,
            padding= 10,
            content=Column(
                controls=[
                    self.drag_bar,
                    self.details_field,
                    self.generate_bt,
                    self.prompt_container,
                    
                    
                    
                ],
                alignment=MainAxisAlignment.START,
                horizontal_alignment=CrossAxisAlignment.CENTER,  
            ),
            
            
        )
        
        self.controls=[
            self.pageview
        ]