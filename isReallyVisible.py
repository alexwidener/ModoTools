#!/usr/bin/python

"""
Function that truthfully tells you if an item is visible or not.
If you were to use sICHAN_LOCATOR_VISIBLE, it would only tell you that the
object in question was visible if it's parent was also visible.

I wanted to know if an object's visibility was on whether or not the parent
was visible.
"""


__author__ = "Alex Widener"
__date__ = "June 10, 2015"
__status__ = "Production"
__version__ = "1.0"
__email__ = "alexwidener#google"

import lx
import lxu.select


def isVisible():
    scn_svc = lx.service.Scene()
    curScn = lxu.select.SceneSelection().current()
    chan = curScn.Channels(None, 0.0)
    chanRead = lx.object.ChannelRead(chan)

    nMesh = curScn.ItemList(scn_svc.ItemTypeLookup(lx.symbol.sITYPE_MESH))
    for mesh in nMesh:
        hVisible = lx.symbol.sICHAN_LOCATOR_HVISIBLE
        h = chanRead.Integer(mesh, mesh.ChannelLookup(hVisible))
        print('{0} is {1}').format(mesh.UniqueName(), h)
