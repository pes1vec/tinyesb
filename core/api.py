from __future__ import annotations
import uuid


class Message:
    """
    La classe contiene il payload del dato e le propietà di contesto
    """

    def __init__(self):
        self.headers = {}
        self.body = None


class Exchange:
    """
    La classe Exchange si occupa di trasportare il/i messaggi da un processore al successivo. Il messaggio di output
    di un processore diventa quello di input del successivo.
    """
    in_msg: Message
    out_msg: Message

    def __init__(self):
        self.id = uuid.uuid4()
        self.properties = {}


class Endpoint:
    """
    La classe Endpoint identifica il punto finale di un canale si esso produttocre che consumatore. La classe è
    factory per Exchange, Producer e Consumer (qualora il componente implementi tutti questi aspetti)
    """

    def create_exchange(self) -> Exchange:
        raise NotImplementedError

    def create_producer(self) -> Producer:
        raise NotImplementedError

    def create_consumer(self) -> Consumer:
        raise NotImplementedError


class Processor:
    """
    Il processore consente di implementare logiche di manipolazione, rotazione, divisione, ecc dei messaaggi.
    I processori all'interno di una rotta sono lo stack di trasformazione.
    """

    def process(self, exchange: Exchange):
        raise NotImplementedError


class Producer(Processor):
    """
    Il produttore si occupa di recuperare i dati dal canale utilizzando le informazioni fornite dall'endpoint, creando
    la prima Exchange ed invocando il primo Processor.
    """

    def endpoint(self) -> Endpoint:
        raise NotImplementedError

    def init(self):
        raise NotImplementedError

    def start(self):
        raise NotImplementedError

    def stop(self):
        raise NotImplementedError


class Consumer:
    """
    La classe si occupa di consumare il messaggio dal processore collegato ed inviarlo al canale seguendo le specifiche
    dell'endpoint
    """
    def processor(self) -> Processor:
        raise NotImplementedError


class Component(Endpoint, Consumer, Producer):
    """
    Un componente riunisce tutte le funzionalità di Endpoint, Consumer e Producer registrandosi all'interno del registro
    di contesto, al fine di essere correttamente delegato in base all'uri del canale (lo schema identifica in modo
    univoco il componente)
    """

    def scheme(self) -> str:
        raise NotImplementedError


class Context:
    """
    Il contesto è il contenitore di variabili, registri, stati che si avvicendano nell'esecuzione di una rotta.
    """
    def get_component(self, scheme: str):
        raise NotImplementedError


class Route:
    """
    La rotta si occupa di definire ed eseguire il flusso che l'Exchange deve effetuare per attraversare tutto lo
    stack di Processor
    """

    def context(self) -> Context:
        raise NotImplementedError

    def consumer(self) -> Consumer:
        raise NotImplementedError

    def start(self) -> None:
        raise NotImplementedError
