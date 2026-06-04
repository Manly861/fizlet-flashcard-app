import flet as ft
import styles as st

def main(page: ft.Page):
    page.title = "Flascard Set Creating Screen"
    page.window.height = st.HEIGHT_SCREEN
    page.window.width = st.WIDTH_SCREEN
    page.bgcolor = st.BACKGROUND_COLOR

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
        )
    )
    
    # Create a term_input bar that ask users for value of the term
    term_input = ft.Container(
        ft.TextField(
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
        )
    )

    # Create a definition_input bar that ask users for value of the definition
    definition_input = ft.Container(
        ft.TextField(
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
        )
    )

    # Create an add button that add a new term_input and definition_input bar
    add_button = ft.Container(
        content = ft.ElevatedButton(
            content= ft.Text(
                 "Add",
                size = 20,
                color= st.TEXT_COLOR_1,                
                weight= ft.FontWeight.BOLD,    
            ),
            bgcolor= st.PLUS_BUTTON_COLOR,
            style = ft.ButtonStyle(
                shape= ft.RoundedRectangleBorder(radius=8),
                padding=ft.Padding.symmetric(horizontal=13, vertical=6),
            ),
        ),
        alignment= ft.Alignment.BOTTOM_CENTER
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
            ),
            bgcolor= st.PLUS_BUTTON_COLOR,
            style = ft.ButtonStyle(
                shape= ft.RoundedRectangleBorder(radius=8),
                padding=ft.Padding.symmetric(horizontal=12, vertical=5),
            ),
        ),
        alignment= ft.Alignment.BOTTOM_CENTER
    )
    


    page.add(add_button)
    page.add(done_button)
    page.window.resizable = False
    page.update()

if __name__ == "__main__":
    ft.run(main)