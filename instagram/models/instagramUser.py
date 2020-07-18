from instagramPhoto import instagramPhoto

class instagramUser:
    def __init__(self, _username, _biography, _business_category_name, _follow_count, _follower_count):
        self.__dict__["username"]=_username
        self.__dict__["biography"]=_biography
        self.__dict__["business_category_name"]=_business_category_name
        self.__dict__["follow_count"]=_follow_count
        self.__dict__["follower_count"]=_follower_count
        self.__dict__["photos"]=[]

    def addPhoto(self, _url, _numberOfLike, _takenAtEpoch):
        photo=instagramPhoto(_url, _numberOfLike, _takenAtEpoch)
        self.__dict__["photos"].append(photo.__dict__)
      
