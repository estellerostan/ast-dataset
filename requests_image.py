import requests
from io import open as iopen

import RestfulClient


def requests_image(file_url):
    suffix_list = ['jpg', 'gif', 'png', 'tif', 'svg', ]
    file_name = file_url.split('/')[-1]

    headers = {
        'User-Agent': 'My User Agent 1.0',
        'From': 'user@domain.com'  # add your email
    }

    i = requests.get(file_url, headers=headers)
    file_suffix = file_name.split('.')[1]

    if file_suffix in suffix_list and i.ok:
        with iopen('/home/deeplearning/Pictures/' + file_name, 'wb') as file:  # the mode is 'wb' for'write binary
            file.write(i.content)
    else:
        i.raise_for_status()
        return False


if __name__ == '__main__':
    images = RestfulClient.maybe_download()

    for i in range(len(images)):
        requests_image(images[i])
