import flet as ft
import styles

def main(page: ft.Page):
    page.title = "Flashcard-set Creating Screen"
    page.window.height = styles.HEIGHT_SCREEN
    page.window.width = styles.WIDTH_SCREEN
    page.bgcolor = styles.BACKGROUND_COLOR


    page.window.resizable = False
    page.update()

if __name__ == "__main__":
    ft.app(target=main)