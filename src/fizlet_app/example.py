import flet as ft
import styles as st
import time

def main(page: ft.Page):
    page.title = "Flashcard Set Creating Screen"
    page.window.height = st.HEIGHT_SCREEN
    page.window.width = st.WIDTH_SCREEN
    page.bgcolor = st.BACKGROUND_COLOR
    page.fonts = st.APP_FONTS


    count_down_display = ft.Text(
        "3",
        size= 16,
        color= st.TEXT_COLOR_1,
        italic= True,
        font_family= st.PRIMARY_FONT,
        text_align= ft.TextAlign.CENTER,
    )

    congratulation_layout = ft.Container(
        expand= True,
        alignment= ft.Alignment(0, -0.25),
        content= ft.Column(
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment= ft.CrossAxisAlignment.CENTER,
            controls = [
                ft.Text(
                    "You are Done, Great Job!",
                    size= 80,
                    color= st.TEXT_COLOR_1,
                    font_family= st.PRIMARY_FONT,
                    text_align= ft.TextAlign.CENTER,
                ),
                ft.Text(
                    "...you will be directed back to main screen in...",
                    size= 20,
                    color= st.TEXT_COLOR_1,
                    italic= True,
                    font_family= st.PRIMARY_FONT,
                    text_align= ft.TextAlign.CENTER,
                ),
                count_down_display
            ]
        )   
    )

    page.add(congratulation_layout)
    page.window.resizable = False
    page.update()

    for i in range(3, 0, -1):
        time.sleep(1)
        count_down_display.value = str(i)
        page.update()
ft.run(main)
