import flet as ft
import index as i


def main(page: ft.Page):
    pageWidth = 720
    pageHeight = 1000
    page.title = "Assistente de Tarefas"
    page.theme_mode = "LIGHT"
    page.padding = 0
    page.window.width = pageWidth
    page.window.height = pageHeight

    page.update()


    def submitButtomClick(e):

        global nome, descricao, prazo
        global clicks

        if clicks == 0:

            if len(entryTasks.value) <= 3:

                print("Tamanho inválido, digite mais")

            elif entryTasks.value == "/dev delete all":
                i.deleteTask(999)

                taskList.controls.clear()
                page.update()

            elif entryTasks.value[0:10] in "/dev delete":

                dele = entryTasks.value.split()
                deleNumId = int(dele[2])

                i.deleteTask(deleNumId)

                taskList.controls.remove(taskList.controls[deleNumId-1])
                page.update()

            else:

                nome = entryTasks.value

                
                clicks += 1
                taskText.value = "Digite o a descrição da tarefa:"
                page.update()


        elif clicks == 1:
            descricao = entryTasks.value

            taskText.value = "Deslize para definar o prazo para realizar a tarefa:"
            page.update()

            entryTasks.visible = False
            entryPrazo.visible = True

            clicks += 1

        elif clicks == 2:

            taskText.value = "Digite o nome da tarefa: "
            page.update()

            prazo = entryPrazo.value

            i.addTask(name=nome, desc=descricao, pr=round(prazo))

            # Mostra na tela as informações adicionadas (nome/descrição)

            iconText = [ft.Icon(name=ft.Icons.KEYBOARD_ARROW_RIGHT, color="#9EA68F"), ft.Text(value=f"{descricao}", size=15, font_family="Verdana", color="#9EA68F")]

            iconTextRow = ft.Row(spacing=10, expand=1, controls=iconText)

            columnItems = [ft.Text(value=f"{nome}", size=18, font_family="Verdana", color="#525936"),
                iconTextRow]

            column = ft.Column(controls=columnItems, spacing=5, expand=1)

            taskList.controls.append(ft.Container(column))

            # Notifica o usuário 

            i.notificacao(titulo=f"Task: {nome} adicionada com sucesso!", mensagem="Não deixe de fazer a sua tarefa, isso pode acabar atrasando a sua vida depois.")

            entryTasks.visible = True
            entryPrazo.visible = False
            clicks = 0



        entryTasks.value = ""
        
        page.update()


    tittle = ft.Container(
        ft.Text("Assistente de Tarefas", size=18, weight="Bold", text_align="CENTER", width=pageWidth, color="WHITE"),
        bgcolor= "#525936",
        padding=10
    )

    #submitBottom = ft.Container(
    #    content= ft.Button(">", color="WHITE", bgcolor="#6A7348", width= 50, height=50, on_click=submitButtomClick, data=0)
    #)

    submitBottomWidth = 125
    textDefaultColor = "#6A7348"
    smoothGreen = "#9EA68F"

    entryTasks = ft.TextField(hint_text="Digite aqui", width=pageWidth - submitBottomWidth, border_color="#6A7348", selection_color="#6A7348", color="BLACK", value="", min_lines=3)

    entryPrazo = ft.Slider(min=1, max=90, divisions=90, label="{value} Min.", thumb_color=textDefaultColor, overlay_color=smoothGreen, active_color=textDefaultColor, inactive_color=smoothGreen, secondary_active_color=smoothGreen, visible=False)

    submitBottom = ft.Container(
        content= ft.TextButton("Submit", icon="send", on_click=submitButtomClick, width=100),
        bgcolor= "#6A7348",
        border_radius= 20,
        theme=ft.Theme(color_scheme=ft.ColorScheme(primary=ft.Colors.WHITE))
    )

    typingSubmitList = [entryTasks, submitBottom]

    typingSubmit = ft.Row(spacing=5, width=pageWidth, controls= typingSubmitList)

    #tasks = ft.Container(
    #    content= ft.Text("Task 1", size=15, width=400, text_align="CENTER")
    #)

    taskList = ft.ListView(expand=1, spacing=0, padding=5, width=pageWidth)

    taskText = ft.Text(value="Digite o nome da tarefa: ", size=15, color="BLACK")

    for n, d in zip(i.nome(), i.desc()):
        #taskList.controls.append(ft.Text(value=f"{n}", size=18, font_family="Verdana", color="#525936"))

        iconText = [ft.Icon(name=ft.Icons.KEYBOARD_ARROW_RIGHT, color="#9EA68F"), ft.Text(value=f"{d}", size=15, font_family="Verdana", color="#9EA68F")]

        iconTextRow = ft.Row(spacing=10, expand=1, controls=iconText)

        columnItems = [ft.Text(value=f"{n}", size=18, font_family="Verdana", color="#525936"),
            iconTextRow]

        column = ft.Column(controls=columnItems, spacing=5, expand=1)

        taskList.controls.append(ft.Container(column))


    page.add(tittle, taskList, taskText, typingSubmit, entryPrazo)

clicks = 0
ft.app(port=8550 ,target=main)