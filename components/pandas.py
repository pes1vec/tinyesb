from core.api import Message, Exchange, Endpoint, Consumer, Producer
from pandas import DataFrame


class DataFrameComponent(Endpoint):
    df: DataFrame

    def __init__(self, df: DataFrame):
        self.df = df

    def create_exchange(self) -> Exchange:
        exc: Exchange = super().create_exchange()
        exc.in_msg.body = self.df
        return exc

    def create_producer(self) -> Producer:
        pass

    def create_consumer(self) -> Consumer:
        pass

