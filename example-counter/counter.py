# "explicit is better than implicit" Python
import flet as ft

def main(page: ft.Page):
    page.title = "Example Counter"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    text_number = ft.TextField(value="0", text_align=ft.TextAlign.RIGHT, width=100)
    
    def max_click(event):
        text_number.value = str(int(text_number.value) + 1)
        page.update()
        
    def minus_click(event):
        text_number.value = str(int(text_number.value) - 1)
        page.update()
        
    page.add(
        ft. Row(
            [
                ft.IconButton(ft.icons.REMOVE, on_click=minus_click),
                text_number,
                ft.IconButton(ft.icons.ADD, on_click=max_click)
            ],
            alignment=ft.MainAxisAlignment.CENTER
        )
    )
ft.app(target=main)