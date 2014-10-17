import requests


def peeep(url):
    payload = {'r_url': "%s" % (url)}
    headers = {'content-type': 'application/x-www-form-urlencoded'}
    r = requests.post(
        "http://www.peeep.us/upload.php", data=payload, headers=headers,
        allow_redirects=False)
    url = r.headers['Location']
    return "http://www.peeep.us%s" % (url)


def internetarchive(url):
    r = requests.get('http://web.archive.org/save/%s' % (url))
    url = r.headers['Content-Location']
    return "http://web.archive.org%s" % (url)


def archivetoday(url):
    payload = {'url': "%s" % (url)}
    r = requests.post("http://archive.today/submit/", data=payload)
    url = r.headers['Refresh']
    return url[6:]
