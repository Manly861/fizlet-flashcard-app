import flet as ft
import styles as st

def main(page: ft.Page):
    page.title = "Practicing Screen"
    page.window.height = st.HEIGHT_SCREEN
    page.window.width = st.WIDTH_SCREEN
    page.bgcolor = st.BACKGROUND_COLOR

    # Create a name_input bar that ask users for name of the set
    name_input_display = ft.Container(
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

    # Create a definition_input bar that ask users for value of the definition

    # Create an add button that add a new term_input and definition_input bar

    # Create a done button that user are done with the creating 
    # and want to return to the main screen



    page.add(name_input_display)
    page.window.resizable = False
    page.update()

if __name__ == "__main__":
    ft.run(main)