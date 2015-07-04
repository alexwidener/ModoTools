__author__ = "Alex Widener"
__date__ = "July 3, 2015"

import traceback
import lx


def openDialog(setupType=None, title=None, umsg=None, fileFormat=None,
               fileUName=None, ext=None, save_ext=None, resultGetString=None):
    """
    Generic dialog I created so that I could call the same function and pass
    in a variable amount of arguments and it would always behave as directed.
    Also works faster than the standard Modo dialog.

    This works much better than having a bunch of window calls all over your
    code. It's more reliable as well because it'll allow you to figure out
    more quickly if you're doing something wrong with it.

    ExecuteArgString(-1) = Call with parent arguments.

    :param setupType: what type of window to be.
    :param title: The title of the window.
    :param umsg: The user message to display if it is a dialog that calls for
         one. If not, skip.
    :param fileFormat: If there is a file format, it needs to be a file browser
         not a dir browser.
    :param fileUName: userFileName
    :param ext: File extension, can be custom.
    :param save_ext: File extension, can be custom.
    :param resultGetString: if True, returns the result as a string(filename)
        or returns a list of objects.
    :return: returns the result of whatever the user chose.
    This is either a string or a list of objects, depending on the input of
    resultGetString
    """

    # Call a command service and tell it what kind of dialog you want.
    comSvc = lx.service.Command()
    comSvc.ExecuteArgString(-1, lx.symbol.iCTAG_NULL, 'dialog.setup {%s}' %
                                                        setupType)

    # if there is a file format, this converts the dialog to a file browser
    # and not a directory browser.

    if fileFormat is not None:
        comSvc.ExecuteArgString(-1,
                                lx.symbol.iCTAG_NULL,
                                'dialog.fileTypeCustom {0} {1} {2} {3}'.format(fileFormat, fileUName, ext, save_ext))

    if umsg is not None:
        comSvc.ExecuteArgString(-1, lx.symbol.iCTAG_NULL, 'dialog.msg {%s}' % umsg)

    comSvc.ExecuteArgString(-1, lx.symbol.iCTAG_NULL, 'dialog.title {%s}' % title)

    try:
        comSvc.ExecuteArgString(-1, lx.symbol.iCTAG_NULL, 'dialog.open')
        result = comSvc.Spawn(lx.symbol.iCTAG_NULL, 'dialog.result')
        result = comSvc.Query(result, 0)

        if result.Count() > 0:
            if resultGetString:
                return result.GetString(0)
            return result

    except RuntimeError as e:
        print('RuntimeError : %s' % e)
    except ValueError as e:
        print('ValueError : %s' % e)
    except:
        print(traceback.format_exc())
