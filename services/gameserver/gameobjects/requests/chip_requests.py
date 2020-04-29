from aiohttp.protocol.httpVersion import BaseRequest

class chip_http_request():
    """chip requests defines all requests that have to do with recieving chips from a player client, they produce a http request per given round.  chip requests alter the write the pot"""
    def __init__(player):
        self.player=player

    def build_request():
        url = player.get_url()
        req = BaseRequest(url)
        return req


class small_blind_request(chip_http_requests):
    """small_blind is a chip_requests requests chips of 5"""
    pass

class big_blind(chip_http_requests):
    """big_blind is a chip requests that requests chips of 10"""
    pass

class anty(chip_http_requests):
    """anty is a chip requests that requests chips of 1"""
    pass

class check(chip_http_requests):
    """check is a chip requests that requests chips of 0"""
    pass

class bet(chip_http_requests):
    """check is a chip requests that requests chips of n"""
    pass
