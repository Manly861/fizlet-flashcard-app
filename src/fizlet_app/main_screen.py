import flet as ft

# Set intital value, such as color, widht and height
background_color = "#E91919"

def main(page: ft.Page):
    page.title = "Hello World!"
    page.window.height = 500
    page.window.width = 500
    page.window.bgcolor = background_color
    page.add(ft.Text("Hello World! I am Fizlet"))
    page.window.resizable = False
    page.update()

ft.app(main)
