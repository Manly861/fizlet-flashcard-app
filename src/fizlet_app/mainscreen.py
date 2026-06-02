import flet as ft
import styles

def main(page: ft.Page):
    page.title = "Main Screen"
    page.window.height = styles.HEIGHT_SCREEN
    page.window.width = styles.WIDTH_SCREEN
    page.bgcolor = styles.BACKGROUND_COLOR

    name_app_display = ft.Container(
        content= ft.Text(           
            "Fizlet",
            size = 28,
            color = styles.TEXT_COLOR,
            weight= ft.FontWeight.BOLD,
        ),
        alignment=ft.Alignment.TOP_CENTER,
    )

    flashcard_folder = ft.Container(
        content = ft.Column( 
            controls =[
                ft.Button(
                    content= " ",
                    bgcolor= styles.BOX_COLOR,
                    style= ft.ButtonStyle(
                        shape= ft.RoundedRectangleBorder(radius=5),
                    ),
                    width = 192,
                    height= 126.7,
                ),
                ft.Text(
                    "Name",
                    size= 16,
                    italic= True,
                    color= styles.TEXT_COLOR,
                    text_align= ft.TextAlign.JUSTIFY,

                ),
            ]
            
            
        
        )
    )
    page.add(flashcard_folder)
    page.window.resizable = False
    page.update()

if __name__ == "__main__":
    ft.app(target=main)

