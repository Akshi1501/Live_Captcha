def auth_middleware(get_response):
    # One-time configuration and initialization.

    def middleware(request):
     
        print('middleware')
        response = get_response(request)
        return response

    return middleware