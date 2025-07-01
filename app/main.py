import flet as ft

def main(page: ft.Page):
    page.title = "App Flet en Docker"
    page.add(ft.Text("¡Desplegado automáticamente con GitHub Actions!"))

ft.app(target=main, port=8500, view=ft.WEB_BROWSER)
