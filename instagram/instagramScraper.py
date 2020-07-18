from urllib2 import urlopen
import re
import json
import sys
sys.path.append("models")
from instagramUser import instagramUser

class instagramScraper:
    INSTAGRAM_URL="https://www.instagram.com/"
    userData=instagramUser("", "", "", 0, 0)
    def fetch(self, username):
        link = self.INSTAGRAM_URL + username
        urlStream = urlopen(link)
        urlContent = urlStream.read()

        encapsulatedJsonContentAsString=re.findall("window._sharedData = .*?;</script>", urlContent)
        jsonContentAsString=encapsulatedJsonContentAsString[0].replace("window._sharedData = ", "").replace(";</script>", "")
        jsonContent=json.loads(jsonContentAsString)
        userJsonContent=jsonContent["entry_data"]["ProfilePage"][0]["graphql"]["user"]

        userData=instagramUser(
            username
            , userJsonContent["biography"].encode(sys.stdout.encoding, errors='replace')
            , userJsonContent["business_category_name"]
            , userJsonContent["edge_follow"]["count"]
            , userJsonContent["edge_followed_by"]["count"]
        )

        for node in userJsonContent["edge_owner_to_timeline_media"]["edges"]:
            userData.addPhoto(
                node["node"]["display_url"]
                , node["node"]["edge_liked_by"]["count"]
                , node["node"]["taken_at_timestamp"]
            )
        return userData.__dict__