import flet as ft

def main(page: ft.Page):
    page.title = "Colegio Marista Santa Marta 2026"
    page.bgcolor = "#82b1ff"
    page.padding = 20
    page.scroll = ft.ScrollMode.AUTO
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    dados_escola = {
        "11":  {"sala": "Sala 01", "entrada": "07:00", "saida": "12:00", "portao": "A", "lanche": "09:30"},
        "12":  {"sala": "Sala 02", "entrada": "08:00", "saida": "08:45", "portao": "Principal", "lanche": "10:00"},
        "13":  {"sala": "Sala 03", "entrada": "07:00", "saida": "12:00", "portao": "A", "lanche": "09:30"},
        "14":  {"sala": "Sala 04", "entrada": "07:00", "saida": "12:00", "portao": "A", "lanche": "09:30"},
        "111": {"sala": "Sala 05", "entrada": "07:00", "saida": "12:00", "portao": "A", "lanche": "09:30"},
        "112": {"sala": "Sala 06", "entrada": "07:00", "saida": "12:00", "portao": "A", "lanche": "09:30"},
        "113": {"sala": "Sala 07", "entrada": "07:00", "saida": "12:00", "portao": "A", "lanche": "09:30"},
        "114": {"sala": "Sala 08", "entrada": "07:00", "saida": "12:00", "portao": "A", "lanche": "09:30"},
        "115": {"sala": "Sala 09", "entrada": "07:00", "saida": "12:00", "portao": "A", "lanche": "09:30"},
        "121": {"sala": "Sala 10", "entrada": "07:00", "saida": "12:00", "portao": "A", "lanche": "09:30"},
        "122": {"sala": "Sala 11", "entrada": "07:30", "saida": "11:45", "portao": "Lateral", "lanche": "09:15"},
        "123": {"sala": "Sala 12", "entrada": "07:00", "saida": "12:00", "portao": "A", "lanche": "09:30"},
        "124": {"sala": "Sala 13", "entrada": "07:00", "saida": "12:00", "portao": "A", "lanche": "09:30"},
        "125": {"sala": "Sala 14", "entrada": "07:00", "saida": "12:00", "portao": "A", "lanche": "09:30"},
        "131": {"sala": "Sala 15", "entrada": "07:00", "saida": "12:00", "portao": "A", "lanche": "09:30"},
        "132": {"sala": "Sala 16", "entrada": "07:00", "saida": "12:00", "portao": "A", "lanche": "09:30"},
        "133": {"sala": "Sala 17", "entrada": "07:00", "saida": "12:00", "portao": "A", "lanche": "09:30"},
        "134": {"sala": "Sala 18", "entrada": "07:00", "saida": "12:00", "portao": "A", "lanche": "09:30"},
        "135": {"sala": "Sala 19", "entrada": "07:00", "saida": "12:00", "portao": "A", "lanche": "09:30"},
        "141": {"sala": "Sala 20", "entrada": "07:00", "saida": "12:00", "portao": "A", "lanche": "09:30"},
        "142": {"sala": "Sala 21", "entrada": "07:00", "saida": "12:00", "portao": "A", "lanche": "09:30"},
        "143": {"sala": "Sala 22", "entrada": "07:00", "saida": "12:00", "portao": "A", "lanche": "09:30"},
        "144": {"sala": "Sala 23", "entrada": "07:00", "saida": "12:00", "portao": "A", "lanche": "09:30"},
        "145": {"sala": "Sala 24", "entrada": "07:00", "saida": "12:00", "portao": "A", "lanche": "09:30"},
        "151": {"sala": "Sala 25", "entrada": "07:00", "saida": "12:00", "portao": "A", "lanche": "09:30"},
        "152": {"sala": "Sala 26", "entrada": "07:00", "saida": "12:00", "portao": "A", "lanche": "09:30"},
        "153": {"sala": "Sala 27", "entrada": "07:00", "saida": "12:00", "portao": "A", "lanche": "09:30"},
        "154": {"sala": "Sala 28", "entrada": "07:00", "saida": "12:00", "portao": "A", "lanche": "09:30"},
        "161": {"sala": "Sala 29", "entrada": "07:00", "saida": "12:00", "portao": "A", "lanche": "09:30"},
        "162": {"sala": "Sala 30", "entrada": "07:00", "saida": "12:00", "portao": "A", "lanche": "09:30"},
        "163": {"sala": "Sala 31", "entrada": "07:00", "saida": "12:00", "portao": "A", "lanche": "09:30"},
        "171": {"sala": "Sala 32", "entrada": "07:00", "saida": "12:00", "portao": "A", "lanche": "09:30"},
        "172": {"sala": "Sala 33", "entrada": "07:00", "saida": "12:00", "portao": "A", "lanche": "09:30"},
        "173": {"sala": "Sala 34", "entrada": "07:00", "saida": "12:00", "portao": "A", "lanche": "09:30"},
        "181": {"sala": "Sala 35", "entrada": "07:00", "saida": "12:00", "portao": "A", "lanche": "09:30"},
        "182": {"sala": "Sala 36", "entrada": "07:00", "saida": "12:00", "portao": "A", "lanche": "09:30"},
        "183": {"sala": "Sala 37", "entrada": "07:00", "saida": "12:00", "portao": "A", "lanche": "09:30"},
        "191": {"sala": "Sala 38", "entrada": "07:00", "saida": "12:00", "portao": "A", "lanche": "09:30"},
        "192": {"sala": "Sala 39", "entrada": "07:00", "saida": "12:00", "portao": "A", "lanche": "09:30"},
        "193": {"sala": "Sala 40", "entrada": "07:00", "saida": "12:00", "portao": "A", "lanche": "09:30"},
    }

    def mostrar_detalhes(turma_nome):
        info = dados_escola.get(turma_nome, {
            "sala": "N/A", "entrada": "07:00", "saida": "12:00", "portao": "A", "lanche": "09:30"
        })
        page.controls.clear()
        page.add(
            ft.Container(
                bgcolor="white",
                padding=30,
                border_radius=20,
                content=ft.Column([
                    ft.Text("TURMA " + turma_nome, size=30, weight="bold", color="blue"),
                    ft.Divider(),
                    ft.Text("Sala: " + info["sala"], size=20, color="black"),
                    ft.Text("Entrada: " + info["entrada"], size=20, color="black"),
                    ft.Text("Saida: " + info["saida"], size=20, color="black"),
                    ft.Text("Portao: " + info["portao"], size=20, color="black"),
                    ft.Text("Lanche: " + info["lanche"], size=20, color="black"),
                    ft.Divider(),
                    ft.ElevatedButton(
                        content=ft.Text("VOLTAR"),
                        on_click=lambda _: montar_inicial()
                    )
                ], horizontal_alignment=ft.CrossAxisAlignment.CENTER)
            )
        )
        page.update()

    def estilo_botao(texto, cor_fundo="lightgrey"):
        return ft.Container(
            content=ft.Text(texto, color="black", weight="bold", size=14),
            alignment=ft.alignment.Alignment(0, 0),
            width=65,
            height=65,
            bgcolor=cor_fundo,
            border_radius=5,
            border=ft.border.all(1, "black54"),
            on_click=lambda _: mostrar_detalhes(texto)
        )

    def montar_inicial():
        page.controls.clear()
        topo = ft.Row([
            ft.Text("MARISTAS 2026", size=25, weight="bold", color="white"),
        ], alignment=ft.MainAxisAlignment.CENTER)
        l1  = ft.Row([estilo_botao("11", "#9ea7c1"), estilo_botao("12"), estilo_botao("13"), estilo_botao("14")], alignment=ft.MainAxisAlignment.CENTER)
        l2  = ft.Row([estilo_botao("111"), estilo_botao("112"), estilo_botao("113"), estilo_botao("114"), estilo_botao("115")], alignment=ft.MainAxisAlignment.CENTER)
        l3  = ft.Row([estilo_botao("121"), estilo_botao("122", "yellow"), estilo_botao("123"), estilo_botao("124", "yellow"), estilo_botao("125")], alignment=ft.MainAxisAlignment.CENTER)
        l4  = ft.Row([estilo_botao("131"), estilo_botao("132"), estilo_botao("133"), estilo_botao("134", "#9ea7c1"), estilo_botao("135")], alignment=ft.MainAxisAlignment.CENTER)
        l5  = ft.Row([estilo_botao("141"), estilo_botao("142"), estilo_botao("143"), estilo_botao("144"), estilo_botao("145")], alignment=ft.MainAxisAlignment.CENTER)
        l6  = ft.Row([estilo_botao("151"), estilo_botao("152"), estilo_botao("153"), estilo_botao("154")], alignment=ft.MainAxisAlignment.CENTER)
        l7  = ft.Row([estilo_botao("161"), estilo_botao("162"), estilo_botao("163")], alignment=ft.MainAxisAlignment.CENTER)
        l8  = ft.Row([estilo_botao("171"), estilo_botao("172"), estilo_botao("173")], alignment=ft.MainAxisAlignment.CENTER)
        l9  = ft.Row([estilo_botao("181"), estilo_botao("182"), estilo_botao("183")], alignment=ft.MainAxisAlignment.CENTER)
        l10 = ft.Row([estilo_botao("191"), estilo_botao("192"), estilo_botao("193")], alignment=ft.MainAxisAlignment.CENTER)
        page.add(topo, ft.Column([l1, l2, l3, l4, l5, l6, l7, l8, l9, l10], spacing=10))
        page.update()

    montar_inicial()

ft.app(target=main, view=ft.AppView.WEB_BROWSER, host="0.0.0.0", port=8080)
