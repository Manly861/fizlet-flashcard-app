import flet as ft
import styles as st
import controller
def main(page: ft.Page, on_go_back=None):
    page.title = "Flascard Set Creating Screen"
    page.window.height = st.HEIGHT_SCREEN
    page.window.width = st.WIDTH_SCREEN
    page.bgcolor = st.BACKGROUND_COLOR
    page.fonts = st.APP_FONTS

    def term_and_definition_input_area():
        """create an area for user to enter value of term and definition"""
        term_user_input= term_input_field()
        definition_user_input= definition_input_field()
        term_and_definition_inputs_list.append((term_user_input, definition_user_input))
        return ft.Row(
                controls= [
                    term_user_input,
                    ft.VerticalDivider(
                        width =20,
                        thickness = 2,
                        color= st.TEXT_COLOR_2,
                    ),
                    definition_user_input,
                ],
                height = 50,
                alignment= ft.MainAxisAlignment.CENTER)

    def add_term_and_definition_field(e):
        """add new term and definition input field when being clicked"""
        print("CLICKED")
        input_area_list.controls.append(term_and_definition_input_area())
        page.update()

    def process_user_input(e):
        """process user' inputs after they click done button"""
        vocab_set = []
        for term_input, definition_input in term_and_definition_inputs_list:
            vocab_set.append(
                {
                    "term": str(term_input.value),
                    "definiton": str(definition_input.value)
                }
            )
        flashcard_set = {
            "name": str(name_input.value),
            "vocab_set": vocab_set
        }
        flashcard_set_list.append(flashcard_set)
        for item in flashcard_set_list:
            file_name = item.get("name").strip() + ".json"
            result = controller.store_data(file_name, item)
        print(flashcard_set_list)
        page.clean()
        if on_go_back:
            on_go_back(page)
        page.update()
    
    def term_input_field():
        """Create a term_input field"""
        return ft.TextField(
            label= "Term",
            label_style= ft.TextStyle(
                color= st.TEXT_COLOR_1,
                weight= ft.FontWeight.BOLD,
                font_family= st.PRIMARY_FONT),
            hint_text= "Enter The Term.",
            hint_style= ft.TextStyle(
                color= st.TEXT_COLOR_2, 
                italic= True,
                font_family= st.PRIMARY_FONT),  
            color= st.TEXT_COLOR_2,                  
            bgcolor= st.BOX_COLOR,
            border_color= st.BOX_COLOR,
            width= term_and_definition_input_bar,
        )
    
    def definition_input_field():
        """Create a definition input field"""
        return ft.TextField(
            label= "Definition",
            label_style= ft.TextStyle(
                color= st.TEXT_COLOR_1,
                weight= ft.FontWeight.BOLD,
                font_family= st.PRIMARY_FONT),
            hint_text= "Enter The Definition.",
            hint_style= ft.TextStyle(
                color= st.TEXT_COLOR_2, 
                italic= True,
                font_family= st.PRIMARY_FONT),
            color= st.TEXT_COLOR_2,                    
            bgcolor= st.BOX_COLOR,
            border_color= st.BOX_COLOR,
            width= term_and_definition_input_bar,
        )
        
    # Set initial value for width of the bar
    flashcard_set_list = []
    term_and_definition_inputs_list = []
    name_input_bar = st.WIDTH_SCREEN - 25
    term_and_definition_input_bar = (st.WIDTH_SCREEN / 2) - 45

    # Display name of the set at the top of the screen
    name_display = ft.Container(
        ft.Text(
            " ",
            size = 24,
            color = st.TEXT_COLOR_1,
            font_family= st.PRIMARY_FONT,
            weight= ft.FontWeight.BOLD,
        ),
        alignment=ft.Alignment.TOP_CENTER,
    )
    
    # Create a name_input bar that ask users for name of the set
    name_input = ft.TextField(
        label= "Name",
        label_style= ft.TextStyle(
            color= st.TEXT_COLOR_1,
            weight= ft.FontWeight.BOLD,
            font_family= st.PRIMARY_FONT,),
        hint_text= "Enter A Name For This Set",
        hint_style= ft.TextStyle(
            color= st.TEXT_COLOR_2, 
            italic= True,
            font_family= st.PRIMARY_FONT),        
        color= st.TEXT_COLOR_2,          
        bgcolor= st.BOX_COLOR,
        border_color= st.BOX_COLOR,
        border_radius= 10,
        width= name_input_bar,
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
            on_click=add_term_and_definition_field,
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
                style= ft.TextStyle(ft.TextAlign.CENTER),
                font_family= st.PRIMARY_FONT,
            ),
            bgcolor= st.PLUS_BUTTON_COLOR,
            style = ft.ButtonStyle(
                shape= ft.RoundedRectangleBorder(radius=8),
                alignment=ft.Alignment.CENTER,
                padding=ft.Padding.symmetric(horizontal=12, vertical=5),
            ),
            on_click= process_user_input,
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
            term_and_definition_input_area()
        ],
    )
    
    # Put all those varible into a layout
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