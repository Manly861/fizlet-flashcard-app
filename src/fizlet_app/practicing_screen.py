import flet as ft
import styles as st
import mainscreen, time
from mainscreen import main as show_main_screen

def main(page: ft.Page):
    page.title = "Flashcard-set Creating Screen"
    page.window.height = st.HEIGHT_SCREEN
    page.window.width = st.WIDTH_SCREEN
    page.bgcolor = st.BACKGROUND_COLOR
    page.fonts = st.APP_FONTS

    def go_back(e):
        page.clean()
        time.sleep(0.5)
        show_main_screen(page)

    # Display name of the set at the top of the screen
    name_display = ft.Container(
        ft.Text(
            mainscreen.flashcard_set_name,
            size = 24,
            font_family= st.PRIMARY_FONT,
            color = st.TEXT_COLOR_1,
            weight= ft.FontWeight.BOLD,
        ),
        alignment=ft.Alignment.TOP_CENTER,
    )

    # Create a home button to help user go back to main screen
    home_button = ft.Container(
        content = ft.TextButton(
            content= ft.Icon(
                ft.Icons.HOME, 
                color= st.TEXT_COLOR_1,
            ),
            on_click=go_back,
            scale=1.5,
        ),
    )

    # Create a flashcard for displaying
    flascard_display = ft.Container(
    )

    # Create a next button


    page.add(home_button)
    page.window.resizable = False
    page.update()

if __name__ == "__main__":
    ft.app(target=main)