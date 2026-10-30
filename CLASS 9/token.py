class TokenSource:
    def __init__(self, data):
        self._data = data
        self._i = 0
    def has_next(self):        
    # True if another integer is still available
        return self._i < len(self._data)
    def next_token(self):      
    # returns the next integer, then moves forward
        value = self._data[self._i]
        self._i = self._i + 1
        return value































