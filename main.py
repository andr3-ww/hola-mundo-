import flet as ft

def main(page: ft.Page):
    page.title = "Hola Mundo con Flet"
    page.add(ft.Text("¡Hola Mundo!", size=30, color="blue"))

ft.app(target=main)
