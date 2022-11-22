import aiohttp
from limiter import Limiter


class Router:
    def __init__(self, **kwargs) -> None:
        self.__limiter: Limiter = Limiter(kwargs.get("reqpsec", 5))
        self.__locked = False
        self.__header = {"X-MAL-CLIENT-ID": kwargs.get("clientID", None)}

    '''
    TODO: Figure out an elegant way to reuse and refresh ClientSession
            Mainly because the ClientSession can closed=True, but have async event loop=False
            We cannot rely on accessing the clientSession event loop directly anymore
            since it is being depricated.

    #     self.clientSession = None

    # async def refresh_clientSession(self):
    #     print(f"Making a new session as the last one was closed: {self.clientSession.closed if self.clientSession is not None else 'clientSession is None'}")
    #     self.clientSession = aiohttp.ClientSession(headers=self.__header)
    #     await asyncio.sleep(0.1)
    '''
    
    @property
    def locked(self):
        return self.__locked

    async def GET(self, url, params):
        if self.__locked:
            if self.__limiter.unlockCheck():
                self.__locked = False
            else:
                return
        if self.__limiter.lockCheck():
            self.__locked = True
            return
        json = {"httpError":"", "httpExtra":"N/A"}
        async with aiohttp.ClientSession(headers=self.__header) as session:
            async with session.get(url=f"{url}?{params}") as resp:
                match resp.status:
                    case 200:
                        ##Successful get
                        print(f"successful get")
                        json = await resp.json()
                    case 400:
                        ##Bad request, i.e. invalid params
                        print(f"[ERROR] There was a problem with the parameters in the URL | {resp.status} ; {resp.method} ; {resp.reason} ; {resp.url}")
                        json['httpError'] = "Recieved 400"
                    case 401:
                        ##Unauthorized, i.e. invalid token
                        print(f"[ERROR] Your token is invalid or has expired | {resp.status} ; {resp.method} ; {resp.reason}")
                        json['httpError'] = "Recieved 401"
                    case 403:
                        ##Forbidden, i.e. DoS or being ratelimited
                        print(f"[ERROR] MAL has denied access for this endpoint. This could be due to DoS or rate limiting | {resp.status} ; {resp.method} ; {resp.reason} ; {resp.url}")
                        json["httpError"] = "Recieved 403"
                        if self.__limiter.checkFrom403():
                            print(f"[ERROR] The denied access is thought to be rate limiting")
                            json["httpExtra"] = "Assuming rate limiting"
                        else:
                            print(f"[ERROR] The denied access is thought NOT to be rate limiting")
                            json["httpExtra"] = "Assuming DoS"
                    case 404:
                        ##Not found, the thing you search for was not found
                        print(f"[ERROR] MAL did not find anything for this endpoint | {resp.status} ; {resp.method} ; {resp.reason} ; {resp.url}")
                        json["httpError"] = "Recieved 404"
                    case 405:
                        ##Method not allowed, i.e. tried to use PUT when you needed to use GET
                        print(f"[ERROR] Wrong method used for this endpoint")
                        json["httpError"] = "Recieved 405"
                    case _:
                        ##Some other status code problem
                        print(f"[ERROR] Encountered an unknown status code from MAL | {resp.status} ; {resp.method} ; {resp.reason}")
                        json["httpError"] = "Recieved unknown status code"
                        json["httpExtra"] = f"{resp.status} ; {resp.reason}"
        return json
