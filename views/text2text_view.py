from flet import *
from strings_.strings import *
from Logic.llm_logic import LLM_model
import ollama
import clipboard
class Text_prompt(View):
    def __init__(self , page: Page):
        super().__init__(route= '/text_prompt')
        
        
        self.background_color = background_color
        self.foreground_color = foreground_color 
        self.button_color = buttons_color
        self.span_color = span_color
        self.text_style_content = text_style_content
        self.shadow = shadow
        self.llm = LLM_model(ollama)
        
        self.close_icon = IconButton(
            icon=icons.CLOSE_ROUNDED,
            scale=0.8,
            bgcolor=colors.TRANSPARENT,
            icon_color=colors.WHITE ,
            on_click=lambda x: page.window_close()
        )
        
        
        self.user_input = TextField(
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
                multiline=True,
            )
        self.user_details_field = Container(
            padding=padding.only(left=10),
            border_radius=20,
            width=600,
            height=60,
            content=self.user_input
        )
        
        self.image2prompt_bt = TextButton(
            icon= icons.IMAGE_OUTLINED,
            text= "Image to Text",
            tooltip='Switch to Image to text mode',
            icon_color= colors.WHITE,
            on_click= lambda x : self.Switch_view(),
            style= ButtonStyle(
                color= colors.WHITE
            )
            
        )
        # self.switch_bt = Switch(
        #     label= 'Image2Prompt',
        #     label_position= LabelPosition.LEFT,
        #     active_color= colors.GREEN_200,
        #     inactive_track_color= colors.WHITE,
        #     scale= 0.7,
        #     label_style= TextStyle(
        #         size=17  
        #     ),
        #     tooltip= 'Switch to Text2Prompt mode',
        #     mouse_cursor= MouseCursor.CLICK,
        #     on_change= lambda x : self.Switch_view(),
        # )

        
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
                             self.image2prompt_bt ,
                             VerticalDivider(
                                 thickness=1
                                 ),
                             self.close_icon,
                             
                            ],
                            spacing= 0

                        )
                    ]
                )
            ),
            maximizable=False,

        )


        self.prompt_generated = Text(
                value= 'prompt will appear here ...',
                selectable= True,
                opacity= 0.3
            )
        
        self.copy_icon = IconButton(
                    icon= icons.COPY_ALL_OUTLINED,
                    icon_color=colors.WHITE ,
                    scale= 0.6 ,
                    on_click=lambda x: self.copy_prompt(),
                    visible=False,
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
        padding= padding.all(10),
        content= Column(
            controls=[
                self.prompt_generated,
                self.copy_icon
                
            ],
            scroll=True,
            spacing=0
            ),
        
    )
        self.generate_bt = TextButton(
        text= 'Generate',
        style=ButtonStyle(
            bgcolor= colors.GREEN,
            shadow_color= colors.WHITE12,
            padding= padding.all(10),
            color= colors.WHITE,
        ),
        on_click=lambda x: self.prompt_generate()
    )   
        self.prompt_container = Container(
        bgcolor= colors.with_opacity(0.2,self.span_color),
        width= 600 , 
        height= 150,
        content=Container(
        bgcolor= colors.BLACK12,
        border_radius=20,
        height=30,
        width=600,
        padding= padding.all(5),
        content= Column(
            controls=[
                self.prompt_generated,
                self.copy_icon
                
            ],
            spacing=0,
            scroll=True,
            auto_scroll=True
            ),
    ),
        border_radius= 20,
        padding=padding.all(5)
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
                    Container(
                        height=20),
                    self.user_details_field,
                    self.generate_bt,
                    self.prompt_container, 
                    
                ],
                alignment=MainAxisAlignment.START,
                horizontal_alignment=CrossAxisAlignment.CENTER,  
            ),
              
        )
        
        
        self.progress_gen = ProgressRing(
                    scale= 0.7,
                    color= colors.GREEN_200,
                    bgcolor= colors.TRANSPARENT,
                    stroke_width= 5
                )
        
        
        self.controls=[
            self.pageview
        ]
        
                
        self.copied_prompt_snack_bar = SnackBar(
            content=Row(
                controls=[
                    Icon(
                        icons.CHECK_CIRCLE,
                        
                    ),
                    Text(
                            value='prompt copied to clipboard',
                            color=colors.WHITE
                        )
                ]
            ),
            bgcolor=self.foreground_color,
            width= 50,
            behavior=SnackBarBehavior.FLOATING,
            elevation=10,
            shape=RoundedRectangleBorder(radius=10),
            margin= 20
        )
        
        
    def Switch_view(self):
        self.page.go('/image2txt')
        self.page.update()
        
        print('changed')
        # self.page.go('/image2txt')
        # self.page.update()
        # if not self.mode_switch_bt.value:
        #     self.page.views.append('/text_prompt')
        #     self.mode_switch_bt.tooltip = 'Switch to Image2Prompt mode'
        #     self.mode_switch_bt.label = 'Text2Prompt'
        #     self.mode_switch_bt.update()
        #     self.mode_switch_bt.value = True
        #     self.mode_switch_bt.update()
        #     self.page.update()
        # if self.mode_switch_bt.value:
        #     self.page.views.append('/image2txt')    
        #     self.mode_switch_bt.tooltip = 'Switch to Text2Prompt mode'
        #     self.mode_switch_bt.label = 'Image2Prompt'
        #     self.mode_switch_bt.update()
        #     self.mode_switch_bt.value = False
        #     self.mode_switch_bt.update()
        #     self.page.update()               
    def prompt_generate(self):
        
        self.pageview.content.controls[3]= self.progress_gen
            
        self.pageview.update()

        
        prompt = self.user_input.value
        if prompt != '':
            self.prompt_generated.value = ''
            self.copy_icon.visible = True
            prompt_respo = self.llm.generate(prompt=prompt)
            data = ''
            for i in prompt_respo: 
                data += i['response']
                self.prompt_generated.value += i['response']
                self.copy_icon.data =data
                self.copy_icon.update()
                self.prompt_generated.update()
            print(self.copy_icon.data)
            self.pageview.content.controls[3]= self.generate_bt
            
            self.pageview.update()

            
            
    def copy_prompt(self):
        try:
            clipboard.copy(self.copy_icon.data)
        except :
            print('error')
        self.page.snack_bar = self.copied_prompt_snack_bar
        self.page.snack_bar.open = True
        self.page.update()
        

        