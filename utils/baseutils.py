class BaseUtils(object):
    def __int__(self):
        self.code=1000
        self.data=None
        self.error=None

    @property
    def dict(self):
        return self.__dict__