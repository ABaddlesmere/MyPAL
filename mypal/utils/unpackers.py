from mypal.models.mypal.enums import UNKNOWN, MISSING

def check_for_null(o) -> bool:
    '''
    Checks if MAL returned a null value
    '''
    return o == [] or o == "" or o == {} or o == None 

def unpack_payload(
    payload: dict,
    field: str,
    req: list,
    returnType: object = None,
    recursive: bool=False
    ) -> object | UNKNOWN | MISSING:
    '''
    Unpacks the specified field from the given payload
    '''
    if field not in req:
        return UNKNOWN()
    temp = payload.get(field, None)
    if check_for_null(temp):
        return MISSING()
    if recursive:
        if returnType is None:
            return temp
        else:
            return [returnType(item) for item in temp]
    if returnType is None:
        return temp
    return returnType(temp)

def unpack_common(
    payload: dict,
    field: str,
    ) -> object | MISSING:
    return payload.get(field, MISSING)