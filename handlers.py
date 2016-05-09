"""
Handlers for the video server
"""
import json
from os import scandir
from os.path import exists
from tornado.web import RequestHandler


class NavigationHandler(RequestHandler):
    def get(self, path):
        abspath = '/media/samba/0ADE833226CEC7BB/video_server/' + path
        if not exists(abspath):
            self.write('{"found": false}')
            return
        files, dirs = [], []
        append_file, append_dir = files.append, dirs.append
        for entry in scandir(abspath):
            if entry.is_file():
                append_file(entry.name)
            else:
                append_dir(entry.name)
        ret = {
            "files": sorted(files),
            "dirs": sorted(dirs),
            "parent": path.rpartition("/")[0]
        }
        self.write(json.dumps(ret))
