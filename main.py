import flet as ft

class ToDo:
    def __init__(self, page: ft.Page):
        self.page = page
        self.page.bgcolor = ft.colors.BLACK
        self.page.window_width = 400
        self.page.window_height = 500
        #self.page.window_resizable = False
        #self.page.window_always_on_top = True
        self.page.title = 'ToDo App'
        self.main_page()

    def task_container(self):
        return ft.Container(
            height=self.page.height * 0.8,
            content=ft.Column(
                controls= [
                    ft.Checkbox(label='Tarefa 1', value=True),
                ]
            ),
        )

    def main_page(self):
        input_task = ft.TextField(
            hint_text='Digite aqui uma tarefa',
            border_color='white',
            )

        input_bar = ft.Row(
            controls=[
                input_task,
                ft.FloatingActionButton(icon=ft.icons.ADD),
            ]
        )

        tabs = ft.Tabs(
            selected_index=0, # define a tab padrão para seleção
            tabs=[
                ft.Tab(text='Todos'),
                ft.Tab(text='Em andamento'),
                ft.Tab(text='Finalizados'),
            ]
        )

        tasks = self.task_container()

        self.page.add(input_bar,tabs,tasks)
    


ft.app(target=ToDo)