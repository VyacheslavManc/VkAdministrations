import requests
import json

TOKEN = '3b0d46f4e9a632834b85e6c52fbf6feb6cda689e771432c3601a3bc609b5c396343aaeb1823a099f7b0e9'


# https://oauth.vk.com/authorize?client_id=6236525&display=page&redirect_uri=https://oauth.vk.com/blank.html&scope=friends,groups,messages&response_type=token&v=5.68&state=123456


def write_json(data):
    with open('vk_groups.json', 'w') as file:
        json.dump(data, file, indent=2, sort_keys=True, ensure_ascii=False)


def get_info():
    r = requests.get(
        'https://api.vk.com/method/groups.getInvites',
        params={
            'offset': 1,
            'count': 1000,
            'extended': False,
            'access_token': TOKEN,
        }
    )
    write_json(r.json())


def read_json():
    with open('vk_groups.json', 'r') as file:
        json_string = file
        parsed_string = json.load(json_string)
        for group_id in parsed_string["response"]:
            try:
                id = group_id["gid"]
                requests.get(
                    'https://api.vk.com/method/groups.leave',
                    params={
                        'group_id': id,
                        'access_token': TOKEN
                    }
                )
                print(id)
            except TypeError:
                continue


def main():
    return get_info(), read_json()


if __name__ == '__main__':
    main()
