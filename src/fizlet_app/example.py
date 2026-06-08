import flet as ft
import math

def main(page: ft.Page):
    page.title = "Quizlet Vertical Flashcard"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.bgcolor = ft.Colors.GREY_100

    is_front = True

    # 1. THIẾT KẾ MẶT TRƯỚC (Lật dọc ban đầu ở góc 0)
    front_card = ft.Container(
        content=ft.Text("What is Python?", size=26, weight=ft.FontWeight.W_600, color=ft.Colors.BLACK87),
        width=450,
        height=280,
        bgcolor=ft.Colors.WHITE,
        border_radius=16,
        alignment=ft.alignment.center, # Sửa lại thành viết thường
        shadow=ft.BoxShadow(spread_radius=1, blur_radius=15, color=ft.Colors.with_opacity(0.1, ft.Colors.BLACK)),
        animate_transform=ft.Animation(500, ft.AnimationCurve.EASE_OUT_BACK),
        animate_opacity=ft.Animation(200, ft.AnimationCurve.EASE_IN_OUT),
        # ĐỔI THÀNH ft.transform.Matrix4 Ở ĐÂY
        transform=ft.transform.Matrix4.identity(),
        opacity=1.0,
    )

    # 2. THIẾT KẾ MẶT SAU (Lật dọc úp sẵn 180 độ theo trục X)
    back_card = ft.Container(
        content=ft.Text("A high-level, programming language.", size=22, color=ft.Colors.BLUE_900, text_align=ft.TextAlign.CENTER),
        width=450,
        height=280,
        bgcolor=ft.Colors.WHITE,
        border_radius=16,
        alignment=ft.alignment.center, # Sửa lại thành viết thường
        shadow=ft.BoxShadow(spread_radius=1, blur_radius=15, color=ft.Colors.with_opacity(0.1, ft.Colors.BLACK)),
        animate_transform=ft.Animation(500, ft.AnimationCurve.EASE_OUT_BACK),
        animate_opacity=ft.Animation(200, ft.AnimationCurve.EASE_IN_OUT),
        # ĐỔI THÀNH ft.transform.Matrix4 Ở ĐÂY
        transform=ft.transform.Matrix4.identity().rotation_x(math.pi),
        scale=ft.Scale(scale_y=-1), 
        opacity=0.0,
    )

    # 3. Hàm xử lý LẠT DỌC THẺ
    def flip_card(e):
        nonlocal is_front
        if is_front:
            # Sửa lại thành ft.transform.Matrix4
            front_card.transform = ft.transform.Matrix4.identity().rotation_x(math.pi)
            front_card.opacity = 0.0
            
            back_card.transform = ft.transform.Matrix4.identity().rotation_x(math.pi * 2)
            back_card.opacity = 1.0
        else:
            front_card.transform = ft.transform.Matrix4.identity()
            front_card.opacity = 1.0
            
            back_card.transform = ft.transform.Matrix4.identity().rotation_x(math.pi)
            back_card.opacity = 0.0

        is_front = not is_front
        page.update()

    # 4. Giao diện Stack xếp đè 2 mặt
    flashcard_stack = ft.Stack(
        controls=[back_card, front_card],
        width=450,
        height=280,
    )

    page.add(
        ft.Text("QUIZLET VERTICAL FLIP", size=14, weight=ft.FontWeight.BOLD, color=ft.Colors.GREY_500),
        ft.Container(height=10),
        ft.GestureDetector(
            on_tap=flip_card,
            content=flashcard_stack,
            mouse_cursor=ft.MouseCursor.CLICK
        ),
        ft.Container(height=15),
        ft.Text("Bấm vào thẻ để lật dọc xem đáp án", size=14, color=ft.Colors.GREY_600)
    )

ft.app(target=main)
