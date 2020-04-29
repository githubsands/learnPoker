from aiohttp.protocol.httpVersion import BaseRequest

class game_http_request():
    """chip requests defines all requests that have to do with recieving chips from a player client, they produce a http request per given round.  chip requests alter the write the pot"""
    def __init__(players):
        self.player=player

    def build_request():
        requests = ()
        for player in players:
            url = player.get_url()
            req = BaseRequest(url)
            requests.append(req)

        return req

# this needs to be a async requests
class start_round_http_request():
    pass

class end_round_http_request():
    pass

