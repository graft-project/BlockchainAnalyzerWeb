from urlparse import urljoin


server = 'http://pypi.python.org/'
detail_path = '/pypi/Flask/%s'


class Release(object):

    def __init__(self, version):
        self.version = version

    def to_json(self):
        return dict(version=self.version,
                    detail_url=self.detail_url)

    @property
    def detail_url(self):
        return urljoin(server, detail_path % self.version)


releases = map(Release, [
    '0.1',
])
