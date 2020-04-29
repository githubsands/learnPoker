from aiohttp.protocol.httpVersion import BaseRequest

class chip_http_request():
    """chip requests defines all requests that have to do with sending chips to the gameserver"""
    def __init__(game):
        """game is the location of the gameserver that the player is playing in"""
        self.game=game

    def build_request():
        url = game
        req = BaseRequest(url)
        return req


class small_blind_request(chip_http_requests):
    """small_blind builds a request of 5 chips to the gameserver"""
    pass

class big_blind(chip_http_requests):
    """big_blind builds a request of 10 chips to be sent to the gameserver"""
    pass

class anty(chip_http_requests):
    """bet builds a request of 1 chips to be sent to the game server"""
    pass

class check(chip_http_requests):
    """check builds a request of nil to be sent to the game server"""
    pass

class bet(chip_http_requests):
    """bet builds a request of X chips to be sent to the game server"""
    pass
