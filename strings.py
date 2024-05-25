from flet import *

# background_color = '#4E5652'
# foreground_color = '#6E7370'
# secondary_color = '#909590'
# content_color = '#9AB69B'
# filled_color = '#5D8064'


background_color = '#040D12'
foreground_color = '#183D3D'
buttons_color = '#5C8374'
span_color = '#93B1A6'



text_style = TextStyle(
    size=12,
    font_family='sf',
    
    # weight=FontWeight.W_100,
    
)
text_style_content = TextStyle(
    size=12,
    font_family="sf",
    # weight=FontWeight.W_200,
    
)

text_style_header = TextStyle(
    size=12,
    font_family="sfm",
    color=colors.WHITE
)

shadow = BoxShadow(
    spread_radius=1,
    blur_radius=5,
    color=colors.with_opacity(0.1 , colors.WHITE12),
    
)
