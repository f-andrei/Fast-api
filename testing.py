import requests
from datetime import datetime

api_url = "http://127.0.0.1:8000"


def get_datetime_str():
    dt_now = datetime.now()
    dt_now = str(dt_now)
    return dt_now

create_task_data = {
    "id": "1231312312431",
    "username": "Andrei123",
    "channel_id": 123432,
    "server_id": "serverid"
}

get_user_id = "1231312312431"

put_discord_user = "updated discord user"

put_discord_channel = "133111"

class User:
    USER_CREATE_USER = "user/create_user"
    USER_GET_USER = "user/get_user"
    USER_UPDATE_DISCORD_USER = "user/update_username"
    USER_UPDATE_PREFERRED_CHANNEL = "user/update_channel_id"

    def __init__(self, api_url):
        self.api_url = api_url


    def create_user(self, user_data: dict):
        url = "{}/{}".format(self.api_url, self.USER_CREATE_USER)
        print(url)
        response = requests.post(url, json=user_data)
        return response.json()
    
    def get_user(self, user_id: str):
        url = "{}/{}/{}".format(self.api_url, self.USER_GET_USER, user_id)
        response = requests.get(url)
        return response.json()
    
    def update_username(self, username: str, user_id: str):
        url = "{}/{}/{}/{}".format(self.api_url, self.USER_UPDATE_DISCORD_USER, user_id, username)
        response = requests.put(url)
        return response.json()
    
    def update_channel_id(self, channel_id: int, user_id: str):
        url = "{}/{}/{}/{}".format(self.api_url, self.USER_UPDATE_PREFERRED_CHANNEL, user_id, channel_id)
        response = requests.put(url)
        return response.json()
    
if __name__ == "__main__":
    user = User(api_url=api_url)

    #response = user.create_user(create_task_data)
    #response = user.get_user(user_id="1231312312431")
    response = user.update_username(username=put_discord_user, user_id=get_user_id)
    #response = user.update_channel_id(channel_id=put_discord_channel, user_id=get_user_id)
    print(response)