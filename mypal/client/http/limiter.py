import time
class Limiter:
    '''
    A class to handle rate limiting for the router
    '''
    def __init__(self, limit: int = 10) -> None:
        self.max = limit
        self.history = []

    def lockCheck(self):
        print(f"self.history is {self.history}")
        if len(self.history) < self.max:
            self.history.append(time.time())
            print(f"passed")
            return False
        else:
            if (time.time()-min(self.history)) <= 1:
                print(f"failed, time diff is {time.time()-min(self.history)}")
                return True
            else:
                self.history = []
                self.history.append(time.time())
                print(f"history reset | passed")
                return False

    def unlockCheck(self):
        if (time.time()-min(self.history)) >= 60:
            self.history = []
            return True
        else:
            return False