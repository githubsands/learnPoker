from aiohttp.protocol.httpVersion import BaseRequest

class round_http_request():
    """chip requests defines all requests that have to do with recieving chips from a player client, they produce a http request per given round.  chip requests alter the write the pot"""
    def __init__(player):
        self.player=player

    def build_request():
        url = player.get_url()
        req = BaseRequest(url)
        return req

class start_round_http_request(round_http_request):
    """start_round_http_request sends a round_http_request to the player_client, it is responsible for rotating the players position"""
    def __init__(player):

# class end_round_http_request(round_http_request):
