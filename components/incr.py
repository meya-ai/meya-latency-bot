# -*- coding: utf-8 -*-
from meya import Component


class Incr(Component):

    def start(self):
        scope = self.properties.get('scope') or "flow"
        db = {
            'flow': self.db.flow,
            'user': self.db.user,
            'bot': self.db.bot
        }[scope]
        key = self.properties['key']
        value = int(float(db.get(key) or 0))
        db.set(key, value + 1)
        return self.respond(action="next")
