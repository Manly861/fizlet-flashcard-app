import flet as ft

# Set intital value, such as color, widht and height
background_color = "#110078"
text_color = "#ffffff"
start_button_color = "#e3913b"
other_button_color = "#4f00f8"
box_color = "#362a7f"
text_fonts = {

}

def main(page: ft.Page):
    page.title = "Flascard App"
    page.horizontal_alignment = ft.MainAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    page.window.height = 600
    page.window.width = 500
    page.bgcolor = background_color
    page.fonts = {
        "Time_New_Roman" : "fonts/Times"
    }

    fizlet_name_display = ft.Text(
                    "Fizlet",
                    size = 80,
                    color = text_color,
                    italic =  True,
                    font_family = "Time_New_Roman",
                    weight= ft.FontWeight.BOLD,
    )
    page.add(fizlet_name_display)
    page.window.resizable = False
    page.update()

ft.app(main)
