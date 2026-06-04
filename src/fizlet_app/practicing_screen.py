import flet as ft
import styles as st

def main(page: ft.Page):
    page.title = "Flashcard-set Creating Screen"
    page.window.height = st.HEIGHT_SCREEN
    page.window.width = st.WIDTH_SCREEN
    page.bgcolor = st.BACKGROUND_COLOR


    page.window.resizable = False
    page.update()

if __name__ == "__main__":
    ft.app(target=main)