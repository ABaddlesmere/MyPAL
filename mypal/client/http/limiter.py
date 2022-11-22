import time
class Limiter:
    '''
    A class to handle rate limiting for the router
    '''
    def __init__(self, limit: int = 10) -> None:
        self.__max = limit
        self.__history = []

    def lockCheck(self):
        current_time = time.time()
        print(f"self.__history is {self.__history}")
        if len(self.__history) < self.__max:
            self.__history.append(current_time)
            print(f"passed")
            return False
        else:
            if (current_time-min(self.__history)) <= 1:
                print(f"failed, time diff is {current_time-min(self.__history)}")
                return True
            else:
                self.__history = []
                self.__history.append(current_time)
                print(f"history reset | passed")
                return False

    def unlockCheck(self):
        if (time.time()-max(self.__history)) >= 60:
            self.__history = []
            return True
        else:
            return False

    def checkFrom403(self):
        '''
        If last 5 are all within 1s, assume MAL is rate limiting us!
        Otherwise, they are protecting from possible DOS
        '''
        violators = 0
        current_time = time.time()
        for i in range(-1, -len(self.__history), -1):
            if current_time-self.__history[:i] <= 1:
                violators += 1
        return violators >= 5