import requests
import getpass
import json
import sys
import os
import ntpath
import magic
from urllib.parse import urljoin

GITHUB_API = 'https://api.github.com'

mime = magic.Magic(mime=True)


def check_status(res, j):
    if res.status_code >= 400:
        msg = j.get('message', 'UNDEFINED')
        print('ERROR: %s' % msg)
        return 1
    return 0


def upload_asset(path, owner, repo, tag):
    token = os.environ['GITHUB_TOKEN']

    url = urljoin(GITHUB_API,
                  '/'.join(['repos', owner, repo, 'releases', 'tags', tag]))
    res = requests.get(url)

    j = json.loads(res.text)
    if check_status(res, j):
        return
    upload_url = j['upload_url']
    upload_url = upload_url.split('{')[0]

    fname = ntpath.basename(path)
    with open(path) as f:
        contents = f.read()
    content_type = mime.from_file(path)

    headers = {'Content-Type': content_type, 'Authorization': token}
    params = {'name': fname}

    res = requests.post(upload_url, data=contents, auth=(owner, token),
                        headers=headers, params=params)

    j = json.loads(res.text)
    if check_status(res, j):
        return
    print('SUCCESS: %s uploaded' % fname)

if __name__ == '__main__':
    path = sys.argv[1]
    owner = sys.argv[2]
    repo = sys.argv[3]
    tag = sys.argv[4]
    if not os.path.isabs(path):
        path = os.path.join(os.path.dirname(os.path.realpath(__file__)), path)
    upload_asset(path, owner, repo, tag)
