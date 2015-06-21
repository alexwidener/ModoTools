"""
This creates a command that unlocks all masks in a scene.
This goes in an lxserv folder that Modo can reach:
~/Library/Application Support/Luxology/Scripts/lxserv/unlockAllGroupMasks_CMD.py

So it will go through the current scene and unlock everything that is a mask.
Just type into the command line (case sensitive):
unlock.GroupMasks

I wrote this to teach somebody how to start working with the Modo API. 
Maybe it will help someone else.
"""

__author__ = "Alex Widener"
__date__ = "June 10, 2015"
__status__ = "Production"
__version__ = "1.0"
__email__ = "alexwidener#google"


import lx
import lxu.command


class UnlockAllGroupMasksCMD(lxu.command.BasicCommand):
    def __init__(self):
        # inherit the command classes to override
        lxu.command.BasicCommand.__init__(self)
    
    def basic_SetFlags(self, index, flags):
        # Make it undoable
        return lx.symbol.fCMD_UNDO

    def basic_Enable(self, msg):
        # return it as always enabled
        return True

    def basic_Execute(self, msg, flags):
        # curScn:
        # gets the current scene & it's contents. Is CURRENT, not persistent.
        # ask me if you need help explaining that.
        #
        # scnSvc:
        # Gets a scene service. Allows you to operate on the scene.
        #
        # comSvc:
        # Gets a command Service. Allows you to do specific things with commands
        # which calling lx.eval won't
        #
        # selSvc:
        # Allows you to operate on selections
        #
        # selSvc.Drop
        # Drop anything that is currently selected.
        #
        # nMasks:
        # Return a list of masks in the scene as python objects, not as strings
        #
        # ForLoop:
        # UniqueName is only available on objects - returns the string of the
        # item's name. NOT the internal ID, that's different.
        # add = add to selection. We have a clean selection, and want to select
        # all masks.
        #
        # comSvc.ExecuteArgString:
        # Allows you to call a command.
        # This is similar to lx.eval, but allows you to edit extra stuff.
        # -1 = call with parent arguments. This is what would be edited most.
        # iCTAG_NULL = ?? I've never known.
        # last is the command.
        #
        # last selSvc:
        # drop anything that is selected (all the masks) after unlocking them.
        curScn = lxu.select.SceneSelection().current()
        scnSvc = lx.service.Scene()
        comSvc = lx.service.Command()
        selSvc = lx.service.Selection()
        
        selSvc.Drop(selSvc.LookupType(lx.symbol.sSELTYP_ITEM))                

        nMasks = curScn.ItemList(scnSvc.ItemTypeLookup(lx.symbol.sITYPE_MASK))
        for mask in nMasks:
            lxu.select.ItemSelection().select(mask.UniqueName(), add=True)

        comSvc.ExecuteArgString(-1, lx.symbol.iCTAG_NULL, 'shader.unlock')
        selSvc.Drop(selSvc.LookupType(lx.symbol.sSELTYP_ITEM))            
        
    def cmd_Interact(self):
        pass
    
lx.bless(UnlockAllGroupMasksCMD, 'unlock.GroupMasks')
