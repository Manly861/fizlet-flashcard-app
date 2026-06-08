import flet as ft
import styles
from mainscreen import main as show_main_screen

def main(page: ft.Page):
    page.title = "Flascard App"
    page.window.height = 600
    page.window.width = 500
    page.bgcolor = styles.BACKGROUND_COLOR


    def get_start(e):
        """moving user to the main screen"""
        page.clean()
        show_main_screen(page)

    # fonts dont work
    page.fonts = {
        "Time_New_Roman" : "fonts/Times.ttf"
    }
    
    fizlet_name_display = ft.Container(
        content = ft.Text(
                "Fizlet",
                size = 80,
                color = styles.TEXT_COLOR_1,
                italic =  True,
                font_family = "Time_New_Roman",
                weight= ft.FontWeight.BOLD,
            ),
        alignment= ft.Alignment(0, -0.25),
    )

    start_button = ft.Container(
        content = ft.FilledButton(
            "Start", 
            color= styles.TEXT_START_BUTTON_COLOR,
            bgcolor = styles.START_BUTTON_COLOR, 
            style=ft.ButtonStyle(
                text_style= ft.TextStyle(
                    size = 36,
                    font_family= "Time_New_Roman",
                    italic= True,
                ),
                shape= ft.RoundedRectangleBorder(radius=10)
            ),
            width= 167, 
            height= 91,
            on_click=get_start,
        ),
        alignment= ft.Alignment(0, 0),
    )

    main_layout = ft.Container(
        content= ft.Column(
            controls= [
                fizlet_name_display,
                start_button,
            ],
            alignment= ft.MainAxisAlignment.CENTER,
            horizontal_alignment= ft.CrossAxisAlignment.CENTER,
        ),
        alignment= ft.Alignment.CENTER,
        expand= True,
    )

    page.add(main_layout)
 
    page.window.resizable = False
    page.update()

if __name__ == "__main__":
    ft.run(main, assets_dir="assets")
