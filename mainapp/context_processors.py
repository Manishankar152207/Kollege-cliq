from urllib import request


def auth_check(request):
    if request.session.has_key('user_id') or request.session.has_key('college_id'):
        return {'is_login':True}
    else:
        return {'is_login':False}
    
