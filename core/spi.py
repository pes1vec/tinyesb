from core.api import Exchange, Message, Consumer, Producer, Processor, Component, Route, Context

class DefaultConsumer(Consumer):
    exc: Exchange = None
    prc: Processor = None

    def __init__(self, prc: Processor):
        self.prc = prc

    def processor(self) -> Processor:
        return self.prc

    def create_exchange(self) -> Exchange:
        self.exc = Exchange()
        self.exc.in_msg = Message()
        return self.exc


class DefaultContext(Context):
    registry = None

    def __init__(self):
        self.registry = {
            'COMPONENTS': {}
        }

    @staticmethod
    def instance(cls):
        if not cls.CONTEXT:
            cls.CONTEXT = DefaultContext()
        return cls.CONTEXT

    def register_component(self, component: Component):
        self.registry['COMPONENTS'][component.scheme()] = component

    def get_component(self, scheme: str):
        component = self.registry['COMPONENTS'][scheme]
        if not component:
            raise Exception(f'Component for scheme \'{scheme}\' not found')
        return component


class DefaultRoute(Route):
    context: Context

    def __init__(self, context: Context):
        self.context = context

    def context(self) -> Context:
        return self.context

    def consumer(self) -> Consumer:
        pass

