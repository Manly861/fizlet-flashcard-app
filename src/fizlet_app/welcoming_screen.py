import flet as ft

# Set intital value, such as color, widht and height
background_color = "#110078"
text_color = "#ffffff"
start_button_color = "#e3913b"
text_start_button_color = "#000000"
other_button_color = "#4f00f8"
box_color = "#362a7f"
text_fonts = {

}

def main(page: ft.Page):
    page.title = "Flascard App"
    page.window.height = 600
    page.window.width = 500
    page.bgcolor = background_color
    page.fonts = {
        "Time_New_Roman" : "fonts/Times"
    }

    fizlet_name_display = ft.Container(
        content = ft.Text(
                "Fizlet",
                size = 80,
                color = text_color,
                italic =  True,
                font_family = "Time_New_Roman",
                weight= ft.FontWeight.BOLD,
            ),
        alignment= ft.Alignment(0, -0.25),
    )

    start_button = ft.Container(
        content = ft.FilledButton(
            "Start", 
            color= text_start_button_color,
            bgcolor = start_button_color, 
            style=ft.ButtonStyle(
                text_style= ft.TextStyle(
                    size = 26,
                    font_family= "Time_New_Roman",
                    italic= True,
                ),
                shape= ft.RoundedRectangleBorder(radius=10)
            ),
            width= 167, 
            height= 91,
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

ft.app(main)
