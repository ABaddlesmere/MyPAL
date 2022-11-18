import asyncio
import aiohttp
from limiter import Limiter
class RateLimitError:
    ...
class ManualLockError:
    ...

class Router:
    def __init__(self, *args, **kwargs) -> None:
        self.limiter = Limiter(kwargs.get("reqpsec", 5))
        self.requests_ps_locker = kwargs.get("reqpseclocker", self.rps+5)
        self.requests = []
        self.locked = False
        self.header = {"X-MAL-CLIENT-ID": kwargs.get("clientID", None)}

        self.clientSession = None

    async def refresh_clientSession(self):
        print(f"Making a new session as the last one was closed: {self.clientSession.closed if self.clientSession is not None else 'clientSession is None'}")
        self.clientSession = aiohttp.ClientSession(headers=self.header)
        await asyncio.sleep(0.1)

    

    async def GET(self, url, params):
        if self.locked:
            if self.limiter.unlockCheck():
                self.locked = False
            else:
                return
        if self.limiter.lockCheck():
            self.locked = True
            return
        
        async with aiohttp.ClientSession(headers=self.header) as session:
            async with session.get(url=f"{url}?{params}") as resp:
                # resp = r
                match resp.status:
                    case 200:
                        ##Successful get
                        print(f"successful get")
                        json = await resp.json()
                    case 400:
                        ##Bad request, i.e. invalid params
                        print(f"[ERROR] There was a problem with the parameters in the URL | {resp.status} ; {resp.method} ; {resp.reason} ; {resp.url}")
                    case 401:
                        ##Unauthorized, i.e. invalid token
                        print(f"[ERROR] Your token is invalid or has expired | {resp.status} ; {resp.method} ; {resp.reason}")
                    case 403:
                        ##Forbidden, i.e. DoS or being ratelimited
                        print(f"[ERROR] MAL has denied access for this endpoint. This could be due to DoS or rate limiting | {resp.status} ; {resp.method} ; {resp.reason} ; {resp.url}")
                    case 404:
                        ##Not found, the thing you search for was not found
                        print(f"[ERROR] MAL did not find anything for this endpoint | {resp.status} ; {resp.method} ; {resp.reason} ; {resp.url}")
                    case 405:
                        ##Method not allowed, i.e. tried to use PUT when you needed to use GET
                        print(f"[ERROR] Wrong method used for this endpoint")
                    case _:
                        ##Some other status code problem
                        print(f"[ERROR] Encountered an unknown status code from MAL | {resp.status} ; {resp.method} ; {resp.reason}")
        return json
