#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
from google.appengine.ext import webapp
from google.appengine.ext.webapp import util
from app.handlers.characterlist import CharacterList
from app.handlers.charactermake import CharacterMake
from app.handlers.characteredit import CharacterEdit
from app.handlers.admin import registClass
from google.appengine.ext.webapp import template

class MainHandler(webapp.RequestHandler):
    def get(self):
        self.response.out.write('Hello world!')


def main():
    webapp.template.register_template_library('app.templatetags.parasiteweb')
    application = webapp.WSGIApplication([('/', CharacterList),
    									  ('/charactermake', CharacterMake),
    									  ('/characteredit', CharacterEdit),
    									  ('/admin/registClass', registClass)],
                                         debug=True)
    util.run_wsgi_app(application)


if __name__ == '__main__':
    main()
