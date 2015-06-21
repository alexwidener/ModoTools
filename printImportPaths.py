#!/usr/bin/python
"""
Print all import paths to the event log.
"""

import lx


def printImportPaths():
    platform = lx.service.Platform()
    pathCount = platform.ImportPathCount()

    for each in range(pathCount):
        print(platform.ImportPathByIndex(each))
