from copy import deepcopy

_NO_SUCCESS_RESPONSE = {'status': False, 'result': {}}

_SUCCESS_RESPONSE = {'status': True}


def success_response():
    return deepcopy(_SUCCESS_RESPONSE)


def no_success_response():
    return deepcopy(_NO_SUCCESS_RESPONSE)
