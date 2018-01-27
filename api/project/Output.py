def outputTrue(message=None, results=None):
    out = {"fail": False, "success": True, "warningMessage": [], "failMessage": [], "result": True, "message": ""}
    if (message is not None):
        out["message"] = message
    if (results is not None):
        out["result"] = results
    return out


def outputFalse(message=None, results=None):
    out = {"fail": False, "success": True, "warningMessage": [], "failMessage": [], "result": False, "message": ""}
    if (message is not None):
        out["result"] = message
    if (results is not None):
        out["result"] = results
    return out


def outputFailure(failMessage=None, warningMessage=None, results=None, message=None):
    out = {"fail": True, "success": False, "warningMessage": [], "failMessage": [], "result": {}, "message": ""}
    if (failMessage is not None):
        if (failMessage != []):
            out["failMessage"] = failMessage
    if (warningMessage is not None):
        out["warningMessage"] = warningMessage
    if (results is not None):
        out["result"] = results
    if (message is not None):
        out["result"] = message
    return out


def outputSuccess(message=None, results=None, warningMessage=None):
    out = {'fail': False, 'success': True, 'warningMessage': [], 'failMessage': [], 'result': {}, 'message': ""}
    if (message is not None):
        out["message"] = message
    if (results is not None):
        out["result"] = results
    if (warningMessage is not None):
        out["warningMessage"] = warningMessage
    return out
