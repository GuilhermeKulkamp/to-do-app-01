"""
    TO-DO App created wih flet.
    Some notes:
        1. Tis is a full app => UI + Database function
        2. Slighlty longer video bt with more esplanations
        3. Database is local with sqlite3

"""

# modules
import flet
from flet import *
from datetime import datetime
import sqlite3

# let's create the form class first so we can get some data
class FormContainer(UserControl):
    # at this point, we can pass in a function from the main() so we can expand. minimize the form
    def __init__(self): # __init__(self,func)
        # self.func = func
        super().__init__()

    def build(self):
        return Container(
            width=280, 
            height=80,
            bgcolor='bluegrey500',
            opacity=0, # change later => change this to 0 and reverese when called
            border_radius=40,
            margin=margin.only(left=-20,right=-20),
            animate=animation.Animation(400, 'decelerate'),
            animate_opacity=200,
            padding=padding.only(top=45, bottom=45),
            content=Column(
                horizontal_alignment=CrossAxisAlignment.CENTER,
                controls=[
                    TextField(
                        height=48,
                        width=255,
                        filled=True,
                        text_size=12,
                        border_color='transparent',
                        hint_text='Descrição...',
                        hint_style=TextStyle(size=11, color='black'),
                    ),
                    IconButton(
                        ################# PAREI AQUI ############
                    )
                ]
            )
        )

def main(page: Page):
    page.horizontal_alignment = 'center'
    page.vertical_alignment = 'center'

    # function to show/hide form container
    def CreateToDoTask(e):
        # when we click the ADD iconbutton ...
        if form.height != 200:
            form.height = 200
            form.opacity = 1
            form.update()
        else:
            form.height = 80
            form.opacity = 0
            form.update()


    _main_column_ = Column(
        scroll='hidden',
        expand=True,
        alignment=MainAxisAlignment.START,
        controls=[
            Row(
                alignment=MainAxisAlignment.SPACE_BETWEEN,
                controls=[
                    # some title stuff
                    Text('To-do Items', size=18, weight='bold'),
                    IconButton(
                        icons.ADD_CIRCLE_ROUNDED,
                        icon_size=18,
                        on_click=lambda e: CreateToDoTask(e),
                    )
                   
                    
                ]
            ),
            Divider(height=8, color='white24'),
        ]
    )


    # set up some bg and main container
    # The general willcopy that of a mobile app
    page.add(
        # this is just a bg container
        Container(
            width=1500, 
            height=800, 
            margin=-10, 
            bgcolor='bluegrey900',
            alignment=alignment.center,
            content=Row(
                alignment=MainAxisAlignment.CENTER,
                vertical_alignment=CrossAxisAlignment.CENTER,
                controls=[
                    # Main container
                    Container(
                        width=280, 
                        height=600, 
                        bgcolor='#0f0f0f', 
                        border_radius=40, 
                        border= border.all(0.5, 'white'),
                        padding=padding.only(top=35, left=20, right=20),
                        clip_behavior=ClipBehavior.HARD_EDGE, # clip contents to container
                        content=Column(
                            alignment=MainAxisAlignment.CENTER,
                            expand=True,
                            controls=[
                                # main column here ...
                                _main_column_,
                                # Form class here
                                FormContainer(),
                            ]
                        )
                    )
                ]
            )
        )
    )
    page.update()

    # the form container index is as follows. We can set the long element index as a variable 
    # so it can be called faster and easier.
    form = page.controls[0].content.controls[0].content.controls[1].controls[0]
    # now we can call form shenever we want to do something wwith it ...

if __name__ == '__main__':
    flet.app(target=main)