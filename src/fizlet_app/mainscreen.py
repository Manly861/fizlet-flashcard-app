import flet as ft
import styles as st
import time
import controller, practicing_screen
from flascard_set_creating_screen import main as show_set_creating_screen
from practicing_screen import main as direct_user_to_practice_screen


def main(page: ft.Page):
    def is_set_clicked(e):
        print("CLICKED")
        text_control = e.control.content.controls[1]
        name_set_chosen = text_control.value + ".json"
        print(f"It is {name_set_chosen}")
        time.sleep(0.5)
        page.clean()
        direct_user_to_practice_screen(page, on_go_back=main, set_chosen=name_set_chosen)
        page.update()

    def direct_user(e):
        """direct users to set-creating screen"""
        page.clean()
        time.sleep(0.5)
        show_set_creating_screen(page, on_go_back=main)
    
    def retreive_and_return_name_of_the_set():
        """retreiving saved data and display in this screen"""
        created_set_list = controller.get_flashcard_set_list()
        name_of_sets_list = []
        for item in created_set_list:
            name_set = ""
            for index in item.name:
                if index == ".":
                    break
                else:
                    name_set += index
            name_of_sets_list.append(name_set)
        return name_of_sets_list

    page.title = "Main Screen"
    page.window.height = st.HEIGHT_SCREEN
    page.window.width = st.WIDTH_SCREEN
    page.bgcolor = st.BACKGROUND_COLOR
    page.fonts = st.APP_FONTS
    
    def retreive_and_return_name_of_the_set():
        """retreiving saved data and display in this screen"""
        created_set_list = controller.get_flashcard_set_list()
        name_of_sets_list = []
        for item in created_set_list:
            name_set = ""
            for index in item.name:
                if index == ".":
                    break
                else:
                    name_set += index
            name_of_sets_list.append(name_set)
        return name_of_sets_list
    
    # Recall function to create a list of flashcard sets' name
    flashcard_set_name_list = retreive_and_return_name_of_the_set()

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
    
    # Create folders that appear in the main screen 
    # and user can interact with
    flascard_set_list = []
    for set_index in range(len(flashcard_set_name_list)):
        flashcard_folder = ft.Container(
            padding= ft.Padding.only(left= 25, bottom=15),
            content = ft.Column( 
                controls =[
                    ft.Button(
                        content= " ",
                        bgcolor= st.BOX_COLOR,
                        style= ft.ButtonStyle(
                            shape= ft.RoundedRectangleBorder(radius=5)),
                        width = 200,
                        height= 130,
                        disabled= True,
                    ),
                    ft.Text(
                        flashcard_set_name_list[set_index],
                        size= 16,
                        font_family= st.PRIMARY_FONT,
                        italic= True,
                        color= st.TEXT_COLOR_1,
                        width= 200,
                        text_align= ft.TextAlign.CENTER,  
                    ),
                ]
            ),
            on_click=is_set_clicked,
        )
        flascard_set_list.append(flashcard_folder)    

    # Create a plus button
    plus_button = ft.Container(
        expand= True,
        padding= ft.Padding.only(bottom=5),
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

    # Put all those varible into a layout
    main_layout = ft.Container(
        expand= True,
        content= ft.Column(
            scroll= ft.ScrollMode.AUTO,
            controls= [
                name_app_display,
                ft.Row(
                    controls=flascard_set_list,  
                    wrap= True,
                    expand=True,
                    alignment= ft.Alignment.CENTER,
                ),
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

