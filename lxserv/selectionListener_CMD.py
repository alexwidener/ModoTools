#!/usr/bin/python
"""
Creating a Selection Listener in Modo.
"""
__author__ = "Alex Widener"
__date__ = "June 10, 2015"
__status__ = "Production"
__version__ = "1.0"
__email__ = "alexwidener#google"

import lx
import lxu.object
import lxu.command
import lxifc


class AwSelListener(lxifc.SelectionListener):
    running = False
    existing = None

    def __init__(self):
        if AwSelListener.existing is None:
            self.listenerService = lx.service.Listener()
            self.listenerService.AddListener(self)
            AwSelListener.existing = self
            self.mesh = ''

    @staticmethod
    def Stop():
        AwSelListener.running = False
        print('My Selection Listener is now stopped')

    @staticmethod
    def Start():
        AwSelListener.running = True
        print('My Selection Listener is now running')

    def Status():
        # Tells you whether it's running or not
        return AwSelListener.running

    def selevent_Add(self, type, subtType):
        if AwSelListener.running:
            scn_srv = lx.service.Scene()
            typename = scn_srv.ItemTypeName(subtType)
            if typename == 'mesh':
                print('I have selected a mesh')
                # the rest of your code

    # Various other methods
    def selevent_Current(self, type):
        pass

    def selevent_Remove(self, type, subtType):
        pass

    def selevent_Time(self, time):
        pass

    def selevent_TimeRange(self, type):
        pass

"""
Turns your listener on or off - you would pass the command
toggle.selListener(below)
to something to turn the event on or off. For example, in a kit that I built,
I turned it on whenever Modo started up, and when I dropped in presets, I made
sure to turn it off, because it would interfere(how I built it would). It all
depends what you're needing out of it.
"""


class AwToggleSelectionListener(lxu.command.BasicCommand):
    def basic_Execute(self, msg, flags):
        if AwSelListener.Status() is True:
            AwSelListener.Stop()
        else:
            AwSelListener.Start()

lx.bless(AwToggleSelectionListener, "toggle.selListener")
