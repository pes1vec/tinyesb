from __future__ import annotations
from core.spi import DefaultRoute


class Builder:
    route = None

    def __init__(self):
        self.route = DefaultRoute()

    def consume(self, uri:str) -> Builder:
        return self

    def produce(self, uri:str) -> Builder:
        return self

    def build(self) -> Route:
        return self.route


if __name__ == '__main__':
    (Builder().consume("csv:///Users/fabry/Downloads/comuni.csv?encoding=latin-1")
     .produce("csv://Users/fabry/Downloads/output.csv")
     .build()
     .start())
