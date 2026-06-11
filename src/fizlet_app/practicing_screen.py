import flet as ft
import styles as st
import controller, congratulation_screen, json

# Create initial value and retrieve data
flash_card_width = 600
flash_card_height = 350
animation_speed = 350

def main(page: ft.Page, on_go_back=None, set_chosen = ""):
    page.title = "Flashcard Set Creating Screen"
    page.window.height = st.HEIGHT_SCREEN
    page.window.width = st.WIDTH_SCREEN
    page.bgcolor = st.BACKGROUND_COLOR
    page.fonts = st.APP_FONTS

    def go_back(e):
        """direct user back to main screen"""
        page.clean()
        if on_go_back:
            on_go_back(page)
        page.update()
    
    def show_side_of_card(e):
        """flip the card when user clicks on it"""
        print("CLICKED")
        term_side.opacity = 0 if term_side.opacity == 1 else 1
        definition_side.opacity = 1 if definition_side.opacity == 0 else 0
        page.update()

    def move_on_to_next_card(e):
        """Move user to the next card"""
        # set initial value of current_index
        print("CLICKED and MOVING ON")
        global current_index
        current_index += 1
        
        try:
            # change the text of term and definition into next data
            print(f"Current card is", {selected_set["vocab_set"][current_index]["term"]})
            term_text_display.value = selected_set["vocab_set"][current_index]["term"]
            definition_text_display.value = selected_set["vocab_set"][current_index]["definition"]
            term_side.opacity = 1.0
            definition_side.opacity = 0.0
            page.update()

            # if they reach the end of the set, 
            # they will be direct back to main screen
        except IndexError:
            page.clean()
            congratulation_screen.main(page)
            page.update()

    def move_back_to_previous_card(e):
        """move user back to the previous card"""
        # set initial value of current_index
        print("CLICKED and MOVING BACK")
        global current_index
        current_index -= 1

        # check if user try to move to index -1
        if current_index == -1:
            current_index = 0

        # change the text of term and definition into previous data
        print(f"Current card is", {selected_set["vocab_set"][current_index]["term"]})
        term_text_display.value = selected_set["vocab_set"][current_index]["term"]
        definition_text_display.value = selected_set["vocab_set"][current_index]["definition"]
        term_side.opacity = 1.0
        definition_side.opacity = 0.0
        page.update()

 
    # retreive the data of chosen flashcard set
    global current_index
    current_index = 0
    selected_set = controller.get_data(str(set_chosen))
    selected_set = json.loads(selected_set)

    # Display name of the set at the top of the screen
    name_display = ft.Container(
        ft.Text(
            selected_set["name"],
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

    # Create a term (front) side of the flashcard for displaying
    term_text_display = ft.Text(
        selected_set["vocab_set"][current_index]["term"],
        color= st.TEXT_COLOR_1,
        size= 50 if len(selected_set["vocab_set"][current_index]["term"]) > 35 else 80,
        weight=ft.FontWeight.BOLD,
        style= ft.TextStyle(ft.TextAlign.CENTER)
    )

    term_side = ft.Container(
        content= ft.Button(
            content= term_text_display,
            bgcolor= st.BOX_COLOR,
            style= ft.ButtonStyle(
                shape= ft.RoundedRectangleBorder(radius=5),
                ),
            width = flash_card_width,
            height= flash_card_height,
            on_click= show_side_of_card,
        ),
        animate_opacity= animation_speed,
        opacity=1.0,
        alignment= ft.Alignment.CENTER,
        padding= ft.Padding.only(top=30,left=20),
    )

    # # Create a definition (back) side of the flashcard for displaying
    definition_text_display = ft.Text(
        selected_set["vocab_set"][current_index]["definition"],
        color= st.TEXT_COLOR_1,
        size= 16 if len(selected_set["vocab_set"][current_index]["term"]) > 35 else 25,
        style= ft.TextStyle(ft.TextAlign.CENTER)
    )

    definition_side = ft.Container(
        content = ft.Button(
            content= definition_text_display,
            bgcolor= st.BOX_COLOR,
            style= ft.ButtonStyle(
                shape= ft.RoundedRectangleBorder(radius=5),
                ),
            width = flash_card_width,
            height= flash_card_height,
            on_click= show_side_of_card,
        ),
        opacity=0.0,
        animate_opacity= animation_speed,
        alignment= ft.Alignment.CENTER,
        padding= ft.Padding.only(top=30,left=20),
    )

    # Create a layout for a flash card
    flashcard_layout = ft.Stack([term_side, definition_side]) # mouse_cursor=ft.MouseCursor.CLICK)
    
    # Create a next button that move user to next flashcard
    next_button = ft.Container(
        expand= True,
        padding= ft.Padding.only(left=20, bottom=35),
        content= ft.Button(
            content= ft.Icon(
                ft.Icons.ARROW_FORWARD, 
                color= st.TEXT_COLOR_1,
                scale= 1.5,
            ),
            disabled= True,
            bgcolor= st.PLUS_BUTTON_COLOR,
            style= ft.ButtonStyle(shape= ft.RoundedRectangleBorder(radius=5)),
        ),
        alignment= ft.Alignment.BOTTOM_CENTER,
        on_click= move_on_to_next_card,
    )

    # Create a next button that move user to next flashcard
    previous_button = ft.Container(
        expand= True,
        padding= ft.Padding.only(left=20, bottom=35),
        content= ft.Button(
            content= ft.Icon(
                ft.Icons.ARROW_BACK, 
                color= st.TEXT_COLOR_1,
                scale= 1.5,
            ),
            disabled= True,
            bgcolor= st.PLUS_BUTTON_COLOR,
            style= ft.ButtonStyle(shape= ft.RoundedRectangleBorder(radius=5)),
        ),
        alignment= ft.Alignment.BOTTOM_CENTER,
        on_click= move_back_to_previous_card,
    )
    
    # create a layout that home button and name will lie in a same line
    name_and_home_button_layout = ft.Container(
        content= ft.Row(
            alignment= ft.MainAxisAlignment.SPACE_BETWEEN,
            controls=[
                ft.Container(content=home_button, alignment=ft.Alignment.CENTER_LEFT),
                name_display, 
                ft.Container(width=50), 
            ]
        ),
        width=st.WIDTH_SCREEN,
    )

    # Put all those varible into a layout
    main_layout = ft.Container(
        expand= True,
        content= ft.Column(
            controls= [
                name_and_home_button_layout,
                flashcard_layout,
                ft.Row([previous_button, next_button])
            ], 
        ), 
    )

    page.add(main_layout)
    page.window.resizable = False
    page.update()

if __name__ == "__main__":
    ft.run(main)