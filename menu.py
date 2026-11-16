# menu.py - RF3: Publicar el menú diario y semanal

menu_diario = {
    "entrada": "Sopa de quinua",
    "segundo": "Lomo saltado",
    "postre": "Gelatina",
    "bebida": "Chicha morada",
}


def publicar_menu_diario():
    print("MENÚ DEL DÍA")
    for plato, descripcion in menu_diario.items():
        print(f"- {plato.capitalize()}: {descripcion}")


if __name__ == "__main__":
    publicar_menu_diario()
