import flet as ft
import styles as st
import time
import controller
from flascard_set_creating_screen import main as show_set_creating_screen

flashcard_set_name = "Name"

def main(page: ft.Page):
    page.title = "Main Screen"
    page.window.height = st.HEIGHT_SCREEN
    page.window.width = st.WIDTH_SCREEN
    page.bgcolor = st.BACKGROUND_COLOR
    page.fonts = st.APP_FONTS

    def direct_user(e):
        page.clean()
        time.sleep(0.5)
        show_set_creating_screen(page, on_go_back=main)
    
    # Create a intial value to display in the screen
    main_screen_list = controller.get_flashcard_set_list()
    print(main_screen_list)
    for item in main_screen_list:
        print(controller.get_data(str(item.name)))

    # Create a value that display name at the top corner
    name_app_display = ft.Container(
        content= ft.Text(           
            "Fizlet",
            size = 28,
            font_family= st.PRIMARY_FONT,
            color = st.TEXT_COLOR_1,
            weight= ft.FontWeight.BOLD,
        ),
        alignment=ft.Alignment.TOP_CENTER,
    )
    
    # Create a folder that appear in the main screen 
    # and user can interact with
    flashcard_folder = ft.Container(
        content = ft.Column( 
            controls =[
                ft.Button(
                    content= " ",
                    bgcolor= st.BOX_COLOR,
                    style= ft.ButtonStyle(
                        shape= ft.RoundedRectangleBorder(radius=5)),
                    width = 192,
                    height= 126.7,
                ),
                ft.Text(
                    flashcard_set_name,
                    size= 16,
                    font_family= st.PRIMARY_FONT,
                    italic= True,
                    color= st.TEXT_COLOR_1,
                    text_align= ft.TextAlign.CENTER,
                    width = 175,
                ),
            ]
        )
    )

    # Create a plus button
    plus_button = ft.Container(
        expand= True,
        content= ft.Button(
            content= ft.Icon(
                ft.Icons.ADD, 
                color= st.TEXT_COLOR_1,
            ),
            bgcolor= st.PLUS_BUTTON_COLOR,
            style= ft.ButtonStyle(shape= ft.CircleBorder()),
            on_click= direct_user,
        ),
        alignment= ft.Alignment.BOTTOM_CENTER
    )

    main_layout = ft.Container(
        expand= True,
        content= ft.Column(
            controls= [
                name_app_display,
                flashcard_folder,
                plus_button,
            ],
            alignment= ft.MainAxisAlignment.SPACE_BETWEEN
        )

    )
    page.add(main_layout)
    page.window.resizable = False
    page.update()

if __name__ == "__main__":
    ft.run(main)

