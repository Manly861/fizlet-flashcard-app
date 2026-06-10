import flet as ft
import styles as st
import controller, time
from mainscreen import main as show_main_screen

def main(page: ft.Page):
    page.title = "Flashcard Set Creating Screen"
    page.window.height = st.HEIGHT_SCREEN
    page.window.width = st.WIDTH_SCREEN
    page.bgcolor = st.BACKGROUND_COLOR
    page.fonts = st.APP_FONTS

    def go_back(e):
        """direct user back to main screen"""
        page.clean()
        time.sleep(0.5)
        show_main_screen(page)
    
    def show_side_of_card(e):
        print("CLICKED")
        front_side.opacity = 0 if front_side.opacity == 1 else 1
        back_side.opacity = 1 if back_side.opacity == 0 else 0
        page.update()

    # Creat initial value
    flash_card_width = 600
    flash_card_height = 350
    animation_speed = 350

    # Display name of the set at the top of the screen
    name_display = ft.Container(
        ft.Text(
            " Name Display ",
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

    # Create a front and back side of the flashcard for displaying
    front_side = ft.Container(
        content= ft.Button(
            content= ft.Text(
                "A",
                color= st.TEXT_COLOR_1,
                size= 100,
                weight=ft.FontWeight.BOLD,
                style= ft.TextStyle(ft.TextAlign.CENTER)
                ),
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
    back_side = ft.Container(
        content = ft.Button(
            content= ft.Text(
                "ABCxyc",
                color= st.TEXT_COLOR_1,
                size= 80,
                style= ft.TextStyle(ft.TextAlign.CENTER)
                ),
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
    
    # Create a next button
    next_button = ft.Container(
        expand= True,
        padding= ft.Padding.only(left=20, bottom=35),
        content= ft.Button(
            content= ft.Icon(
                ft.Icons.FORWARD, 
                color= st.TEXT_COLOR_1,
                scale= 1.5,
            ),
            bgcolor= st.PLUS_BUTTON_COLOR,
            style= ft.ButtonStyle(shape= ft.RoundedRectangleBorder(radius=5)),
        ),
        alignment= ft.Alignment.BOTTOM_CENTER,
    )
    
    #
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
                ft.Stack([front_side, back_side]),
                next_button,
            ], 
        ), 
    )

    page.add(main_layout)
    page.window.resizable = False
    page.update()

if __name__ == "__main__":
    ft.run(main)