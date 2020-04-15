from aiohttp.protocol.httpVersion import BaseRequest

class card_http_request():
    """card requests defines all requests that have to do with delivering cards to a client, they produce a card_request per given round, which in this case it can be more abstractly represented as a card delivery"""
    pass

class preflop_card_request(card_http_request):
    pass


class flop_card_request(card_http_request):
    pass


class turn_card_request(card_http_request):
    pass

class river_card_request(card_http_request):
    pass

class showdown_card_request(card_http_request):
    pass
