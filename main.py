import flet as ft
import sqlite3

class ToDo:
    def __init__(self, page: ft.Page):
        self.page = page
        self.page.bgcolor = ft.colors.BLACK
        self.page.window_width = 400
        self.page.window_height = 500
        #self.page.window_resizable = False
        #self.page.window_always_on_top = True
        self.page.title = 'ToDo App'
        self.task = '',
        self.view = 'all'
        self.db_excute('CREATE TABLE IF NOT EXISTS tasks(name, status)')
        self.results= self.db_excute('SELECT * FROM tasks')
        self.main_page()

    
    # conexão com o banco de dados
    def db_excute(self, query, params = []):
        with sqlite3.connect('database.db') as con:
            cur = con.cursor()
            cur.execute(query, params)
            con.commit()
            return cur.fetchall()
    

    # adiciona uma tarefa
    def add_task(self, e, input_task):
        name = self.task
        status = 'incomplete'

        if name:
            self.db_excute(query='INSERT INTO tasks VALUES(?,?)',
                           params=[name,status])
            input_task.value = ''
            self.results= self.db_excute('SELECT * FROM tasks')
            self.update_task_list()

    # atualiza a lista de tarefas
    def update_task_list(self):
        tasks = self.task_container()
        self.page.controls.pop()
        self.page.add(tasks)
        self.page.update()

    # atualiza status da tarefa
    def task_checked(self, e):
        is_checked= e.control.value
        label = e.control.label

        if is_checked:
            self.db_excute('UPDATE tasks SET status = "complete" WHERE name = ?',params=[label])
        else:
            self.db_excute('UPDATE tasks SET status = "incomplete" WHERE name = ?',params=[label])

        self.update_task_list 

    # atualiza as views conforme as abas
    def tabs_changed(self, e):
        if e.control.selected_index == 0:
            self.results = self.db_excute('SELECT * FROM tasks')
            self.view = 'all'
        elif e.control.selected_index == 1:
            self.results = self.db_excute('SELECT * FROM tasks WHERE status = "incomplete"')
            self.view = 'incomplete'            
        elif e.control.selected_index == 2:
            self.results = self.db_excute('SELECT * FROM tasks WHERE status = "complete"')
            self.view = 'complete'    

        self.update_task_list()        


    def task_container(self):
        return ft.Container(
            height=self.page.height * 0.8,
            content=ft.Column(
                controls= [
                    # carrega as tarefas do arquivo
                    ft.Checkbox(label=res[0], 
                                on_change = self.task_checked,
                                value=True if res[1] == 'complete' else False)
                    for res in self.results if res
                ]
            ),
        )
    
    def set_value(self, e):
        self.task = e.control.value

    def main_page(self):
        input_task = ft.TextField(
            hint_text='Digite aqui uma tarefa',
            border_color='white',
            on_change=self.set_value,
            )

        input_bar = ft.Row(
            controls=[
                input_task,
                ft.FloatingActionButton(
                    icon=ft.icons.ADD,
                    on_click=lambda e: self.add_task(e, input_task),
                    ),
            ]
        )

        tabs = ft.Tabs(
            selected_index=0, # define a tab padrão para seleção
            on_change=self.tabs_changed,
            tabs=[
                ft.Tab(text='Todos'),
                ft.Tab(text='Em andamento'),
                ft.Tab(text='Finalizados'),
            ]
        )

        tasks = self.task_container()

        self.page.add(input_bar,tabs,tasks)
    


ft.app(target=ToDo)