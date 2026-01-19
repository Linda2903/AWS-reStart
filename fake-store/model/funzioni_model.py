def product_model(product: dict[str, any])->dict[str, any]:
    return {
        "id": product["id"], 
        "title": product["title"],
        "description": product["description"],
        "price": product["price"],
        "category": product["category"]
    }

def lista_model(lista_completa : list[dict[str, any]] ) -> list[dict[str, any]]:
    return [{"id": product["id"],"title": product["title"]} for product in lista_completa]