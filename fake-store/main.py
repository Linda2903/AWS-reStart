from requests.exceptions import RequestException
BASE_URL: str= "https://api.escuelajs.co/api/v1/products"


from model.funzioni_model import product_model, lista_model
from ui.console import print_prodotto, mostra_lista
from data.services import get_data, get_lista_prodotti, get_prodotto, post_data, send_product

product ={
  "title": "Pippo, Pluto, Minni",
  "price": 10,
  "description": "A description",
  "categoryId": 8,
  "images": ["https://placehold.co/600x400"]
}


def main() -> None:
    try: 
        get_data(BASE_URL)
        print("Accesso al server eseguito correttamente")
        mostra_lista(lista_model(get_lista_prodotti(BASE_URL)))
        #id = input("Inserisci l'id del prodotto da visualizzare: ")
        #product=product_model(get_prodotto(f"{BASE_URL}/{id}"))
        #print_prodotto(product)

        #print(post_data(BASE_URL, product))
        print_prodotto(send_product(BASE_URL, product))
        

    except RequestException as e:
        print(e)
    
    print("HELLO")

if __name__ == "__main__" :
    main()