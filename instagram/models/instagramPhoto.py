from datetime import datetime

class  instagramPhoto:
    def __init__(self, _url, _numberOfLike, _takenAtEpoch):
        ts=int(_takenAtEpoch)
        self.__dict__["url"]=_url
        self.__dict__["numberOfLike"]=_numberOfLike
        self.__dict__["takenAt"]=datetime.utcfromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
        self.__dict__["takenAtEpoch"]=_takenAtEpoch