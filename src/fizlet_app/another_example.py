import flet as ft
import math

def main(page: ft.Page):
    page.title = "Quizlet Flashcard Style"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.bgcolor = ft.Colors.GREY_100  # Nền xám nhạt để nổi bật thẻ giống Quizlet

    # Trạng thái theo dõi: True = Mặt trước, False = Mặt sau
    is_front = True

    # 1. THIẾT KẾ MẶT TRƯỚC (Câu hỏi)
    front_card = ft.Container(
        content=ft.Text(
            "What is Python?", 
            size=26, 
            weight=ft.FontWeight.W_600, 
            color=ft.Colors.BLACK87
        ),
        width=450,
        height=280,
        bgcolor=ft.Colors.WHITE,
        border_radius=16,
        alignment=ft.Alignment.CENTER,
        # Đổ bóng nhẹ chuẩn giao diện Quizlet
        shadow=ft.BoxShadow(spread_radius=1, blur_radius=15, color=ft.Colors.with_opacity(0.1, ft.Colors.BLACK)),
        # Hiệu ứng xoay và mờ dần
        animate_rotation=ft.Animation(500, ft.AnimationCurve.EASE_OUT_BACK),
        animate_opacity=ft.Animation(200, ft.AnimationCurve.EASE_IN_OUT),
        rotate=ft.Rotate(angle=0, alignment=ft.Alignment.CENTER),
        opacity=1.0,
    )

    # 2. THIẾT KẾ MẶT SAU (Câu trả lời)
    back_card = ft.Container(
        content=ft.Text(
            "A high-level, programming language.", 
            size=22, 
            color=ft.Colors.BLUE_900,
            text_align=ft.TextAlign.CENTER
        ),
        width=450,
        height=280,
        bgcolor=ft.Colors.WHITE,
        border_radius=16,
        alignment=ft.Alignment.CENTER,
        shadow=ft.BoxShadow(spread_radius=1, blur_radius=15, color=ft.Colors.with_opacity(0.1, ft.Colors.BLACK)),
        animate_rotation=ft.Animation(500, ft.AnimationCurve.EASE_OUT_BACK),
        animate_opacity=ft.Animation(200, ft.AnimationCurve.EASE_IN_OUT),
        # Mặt sau mặc định ban đầu đã lật sẵn 180 độ (math.pi) và ẩn đi
        rotate=ft.Rotate(angle=math.pi, alignment=ft.Alignment.CENTER,
),
        opacity=0.0,
        # Lật ngược hình học mặt sau lại để khi xoay ra trước chữ ĐỌC XUÔI 100% không bị hiệu ứng gương
        
    )

    # 3. Hàm xử lý Lật Thẻ kiểu Quizlet
    def flip_card(e):
        nonlocal is_front
        if is_front:
            # Mặt trước xoay ra sau (180 độ) và ẩn đi
            front_card.rotate.angle = math.pi
            front_card.opacity = 0.0
            
            # Mặt sau xoay về trước (360 độ để tiếp diễn vòng quay) và hiện lên
            back_card.rotate.angle = math.pi * 2
            back_card.opacity = 1.0
        else:
            # Quay ngược lại trạng thái ban đầu
            front_card.rotate.angle = 0
            front_card.opacity = 1.0
            
            back_card.rotate.angle = math.pi
            back_card.opacity = 0.0

        is_front = not is_front
        page.update()

    # 4. Giao diện chính: Dùng Stack để xếp đè 2 mặt lên nhau
    flashcard_stack = ft.Stack(
        controls=[back_card, front_card], # Thằng nào nằm sau viết trước
        width=450,
        height=280,
    )

    page.add(
        ft.Text("QUIZLET FLASHCARD", size=14, weight=ft.FontWeight.BOLD, color=ft.Colors.GREY_500),
        ft.Container(height=10),
        ft.GestureDetector(
            on_tap=flip_card,
            content=flashcard_stack,
            mouse_cursor=ft.MouseCursor.CLICK
        ),
        ft.Container(height=15),
        ft.Text("Bấm vào thẻ để xem đáp án", size=14, color=ft.Colors.GREY_600)
    )

ft.app(target=main)
