import flet as ft
import styles as st
def main(page: ft.Page):
    page.title = "Flascard Set Creating Screen"
    page.window.height = st.HEIGHT_SCREEN
    page.window.width = st.WIDTH_SCREEN
    page.bgcolor = st.BACKGROUND_COLOR

    # Set initial value for width of the bar
    name_input_bar = st.WIDTH_SCREEN - 25
    term_and_definition_input_bar = (st.WIDTH_SCREEN / 2) - 45


    # Display name of the set at the top of the screen
    name_display = ft.Container(
        ft.Text(
            "Almost Done, Ya hu",
            size = 24,
            color = st.TEXT_COLOR_1,
            weight= ft.FontWeight.BOLD,
        ),
        alignment=ft.Alignment.TOP_CENTER,
    )
    
    # Create a name_input bar that ask users for name of the set
    name_input = ft.Container(
        ft.TextField(
            label= "Name",
            label_style= ft.TextStyle(
                color= st.TEXT_COLOR_1,
                weight= ft.FontWeight.BOLD),
            hint_text= "Enter A Name For This Set",
            hint_style= ft.TextStyle(
                color= st.TEXT_COLOR_2, 
                italic= True),                  
            bgcolor= st.BOX_COLOR,
            border_color= st.BOX_COLOR,
            border_radius= 10,
            width= name_input_bar,
        ),
        alignment= ft.Alignment.CENTER,
    )
    
    # Create a term_input bar that ask users for value of the term
    term_input = ft.TextField(
        label= "Term",
        label_style= ft.TextStyle(
            color= st.TEXT_COLOR_1,
            weight= ft.FontWeight.BOLD),
        hint_text= "Enter The Term.",
        hint_style= ft.TextStyle(
            color= st.TEXT_COLOR_2, 
            italic= True),                  
        bgcolor= st.BOX_COLOR,
        border_color= st.BOX_COLOR,
        width= term_and_definition_input_bar,
    )

    # Create a definition_input bar that ask users for value of the definition
    definition_input = ft.TextField(
        label= "Definition",
        label_style= ft.TextStyle(
            color= st.TEXT_COLOR_1,
            weight= ft.FontWeight.BOLD),
        hint_text= "Enter The Definition.",
        hint_style= ft.TextStyle(
            color= st.TEXT_COLOR_2, 
            italic= True),                  
        bgcolor= st.BOX_COLOR,
        border_color= st.BOX_COLOR,
        width= term_and_definition_input_bar,
    )

    # Create an add button that add a new term_input and definition_input bar
    add_button = ft.Container(
        content = ft.Button(
            content= ft.Text(
                 "Add",
                size = 20,
                color= st.TEXT_COLOR_1,                
                weight= ft.FontWeight.BOLD, 
            ),
            bgcolor= st.PLUS_BUTTON_COLOR,
            style = ft.ButtonStyle(
                shape= ft.RoundedRectangleBorder(radius=8),
                alignment=ft.Alignment.CENTER,
                padding=ft.Padding.symmetric(horizontal=13, vertical=6),
            ),
        ),
        padding= ft.Padding.only(bottom=5),
        alignment= ft.Alignment.BOTTOM_CENTER,
    )

    # Create a done button that user are done with the creating 
    # and want to return to the main screen
    done_button = ft.Container(
        content = ft.FilledButton(
            content= ft.Text(
                "Done",
                size = 12,
                color= st.TEXT_COLOR_1,                
                weight= ft.FontWeight.BOLD,    
                style= ft.TextStyle(ft.TextAlign.CENTER)
            ),
            bgcolor= st.PLUS_BUTTON_COLOR,
            style = ft.ButtonStyle(
                shape= ft.RoundedRectangleBorder(radius=8),
                alignment=ft.Alignment.CENTER,
                padding=ft.Padding.symmetric(horizontal=12, vertical=5),
            ),
            align= ft.Alignment.TOP_RIGHT,
        ),
    )

    # Create a layout that name_display and done_button would lie on the same lie
    name_and_done_button_layout = ft.Container(
        content= ft.Row(
            alignment= ft.MainAxisAlignment.SPACE_BETWEEN,
            controls=[
                ft.Container(width=50), 
                name_display, 
                ft.Container(content=done_button, alignment=ft.Alignment.CENTER_RIGHT),
            ]
        ),
        width=name_input_bar,
    )

    # Create a area that users can scroll up or down 
    # if there are many terms and definitions
    input_area_list = ft.ListView(
        expand= True,
        spacing=10,
        padding=ft.Padding.only(top= 10, bottom= 10, left = 0),
        controls=[
            ft.Row(
                controls =[
                    term_input,
                    ft.VerticalDivider(
                        width =20,
                        thickness = 2,
                        color= st.TEXT_COLOR_2,
                    ),
                    definition_input,
                ],
                height = 50,
                alignment= ft.MainAxisAlignment.CENTER, 
            ),
            
        ],
    )
    
    main_layout = ft.Container(
        expand= True,
        content= ft.Column(
            controls= [
                name_and_done_button_layout,
                name_input,
                input_area_list,
                add_button,
            ],
            horizontal_alignment= ft.CrossAxisAlignment.CENTER,
        )
    )
            

    page.add(main_layout)
    page.window.resizable = False
    page.update()

if __name__ == "__main__":
    ft.run(main)