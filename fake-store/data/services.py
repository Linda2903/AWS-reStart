from requests import get, Response, post
from requests.exceptions import HTTPError,Timeout,InvalidURL,ConnectionError,RequestException


def get_lista_prodotti(url: str) -> list[dict[str, any]]:
    if url is None:
        raise ValueError("L'url non può essere vuoto")
    try: 
        response: Response =get_data(url)
        data= response.json()

        if not isinstance(data, list):
            raise TypeError(
                f"Risposta inattesa: mi aspettavo una lista, "
                f"ma ho ricevuto {type(data).__name__}"
            )
        return data
    
    except Exception as e:
        raise Exception(f"Problema con la response: {e}")

    
def get_prodotto(url: str) -> dict[str, any] :
    if url is None:
        raise ValueError("L'url non può essere vuoto")
    try: 
        response: Response =get_data(url)
        data = response.json()

        if not isinstance(data, dict):
            raise TypeError(
                f"Risposta inattesa: mi aspettavo una lista, "
                f"ma ho ricevuto {type(data).__name__}"
            )
        return data
    
    except Exception as e:
        raise Exception(f"Problema con la response: {e}")


def get_data(url: str)-> Response:
    if url is None:
        raise ValueError("L'url non può essere vuoto")
    try:
        response =get(url)
        response.raise_for_status() #fa scattare automaticamente un errore Python quando la richiesta non è andata a buon fine.
        return response
    
    except HTTPError as e:
        raise HTTPError(f"Errore di tipo :{e}") from e
    #Errore HTTP

    except Timeout as e:
        raise Timeout(f"Errore:la richiesta è andata in timeout {e}") from e
    #Errore di Timeout

    except InvalidURL as e:
        raise InvalidURL(f"Errore: URL non valido {e}") from e

    except ConnectionError as e:
        raise ConnectionError("Errore: impossibile connettersi al server. {e}") from e

    except RequestException as e:
        raise RequestException("Attenzione! Errore generico {e}") from e


""""
if response is None:
        raise TypeError("response deve essere per forza un oggetto Response, non None")
    """

def post_data(url: str, data: dict) -> Response:
    if url is None:
        raise ValueError("L'url non può essere vuoto")
    try:
        #la funzione data da in output una risposta(Response)
        response= post(url,headers={"Content-Type":"application/json"},json=data)
        response.raise_for_status()
        return response.json()
    
    except HTTPError as e:
        raise HTTPError(f"Errore di tipo :{e}") from e
    #Errore HTTP

    except Timeout as e:
        raise Timeout(f"Errore:la richiesta è andata in timeout {e}") from e
    #Errore di Timeout

    except InvalidURL as e:
        raise InvalidURL(f"Errore: URL non valido {e}") from e

    except ConnectionError as e:
        raise ConnectionError("Errore: impossibile connettersi al server. {e}") from e

    except RequestException as e:
        raise RequestException("Attenzione! Errore generico {e}") from e

def send_product(url: str, data: dict) -> dict[str, any]:
    if url is None:
        raise ValueError("L'url non può essere vuoto")
    if data is None:
        raise ValueError("Data non può essere vuoto")
    if not isinstance(data, dict):
        raise TypeError(
            f"Risposta inattesa, mi aspettavo un dict,"
            f"ma ho ricevuto {type(data.__name__)}"
        )
    try:
        response= post_data(url, data)
        return response

    except Exception as e:
        raise Exception(f"Problema {e}")