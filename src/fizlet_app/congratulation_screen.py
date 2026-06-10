import flet as ft
import styles as st
import asyncio


def main(page: ft.Page):
    page.title = "Flashcard Set Creating Screen"
    page.window.height = st.HEIGHT_SCREEN
    page.window.width = st.WIDTH_SCREEN
    page.bgcolor = st.BACKGROUND_COLOR
    page.fonts = st.APP_FONTS
        
    # display number in the screen
    count_down_display = ft.Text(
        "3",
        size= 16,
        color= st.TEXT_COLOR_1,
        italic= True,
        font_family= st.PRIMARY_FONT,
        text_align= ft.TextAlign.CENTER,
    )

    # async mean it will run while the function 
    # without waiting this code run and display the GUI
    async def count_down():
        """counting down from 3 to 0"""
        import mainscreen

        for i in range(3, -1, -1):
            count_down_display.value = str(i)
            await asyncio.sleep(1)
            page.update()
        await asyncio.sleep(0.5)
        page.clean()
        mainscreen.main(page)
        page.update()
        
    
    # create a congratulation layout
    congratulation_layout = ft.Container(
        expand= True,
        alignment= ft.Alignment(0, -0.25),
        content= ft.Column(
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment= ft.CrossAxisAlignment.CENTER,
            controls = [
                ft.Text(
                    "You are Done, Great Job!",
                    size= 80,
                    color= st.TEXT_COLOR_1,
                    font_family= st.PRIMARY_FONT,
                    text_align= ft.TextAlign.CENTER,
                ),
                ft.Text(
                    "...you will be directed back to main screen in...",
                    size= 20,
                    color= st.TEXT_COLOR_1,
                    italic= True,
                    font_family= st.PRIMARY_FONT,
                    text_align= ft.TextAlign.CENTER,
                ),
                count_down_display
            ]
        )   
    )

    # Add it it screen and 
    page.add(congratulation_layout)
    page.window.resizable = False
    page.update()

    # Recall function to count down
    page.run_task(count_down)
    
if __name__ == "__main__":
    ft.run(main)
