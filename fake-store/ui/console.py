def print_prodotto(product: dict[str,any]) -> None:
    print("*"*30)
    print("PRODOTTO")
    print("*"*30)
    print(f"ID: {product["id"]}")
    print(f"Titolo: {product["title"]}")
    print(f"Prezzo: {product["price"]}")
    print(f"Descrizione: {product["description"]}")
    print(f"Categoria: {product["category"]["name"]}")
    

def mostra_lista(lista_intestazione: list[dict[str, any]]) -> None:
    print("Ecco la lista dei prodotti disponibili: ")
    for i in lista_intestazione: 
        print(f"{i["id"]} - {i["title"]}")