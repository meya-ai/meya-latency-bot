# -*- coding: utf-8 -*-
import math
from meya import Component


class Pi(Component):

    def start(self):
        text = "{}".format(math.pi)
        message = self.create_message(text=text)
        return self.respond(message=message, action="next")
