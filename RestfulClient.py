import requests


def maybe_download():
    images = []

    url = "http://www.giantbomb.com/api/games/" \
          "?api_key=[API_KEY]&filter=platforms:13&format=json&offset=100"  # add your API key

    headers = {
        'User-Agent': 'My User Agent 1.0',
        'From': 'user@domain.com'  # add your email
    }

    r = requests.get(url, headers=headers)

    if r.ok:
        jData = r.json()['results']

        guids = []
        for entry in jData:
            guids.append(entry['guid'])

        for i in range(len(guids)):
            url = 'https://www.giantbomb.com/api/images/' + guids[i] + \
                  '?api_key=[API_KEY]&filter=image_tag:AST%20Screenshots&format=json'
            r = requests.get(url, headers=headers)

            jData = r.json()['results']

            if r.json().get('results'):
                for entry in jData:
                    images.append(entry['small_url'])

    else:
        # If response code is not ok (200), print the resulting http error code with description
        r.raise_for_status()

    return images
