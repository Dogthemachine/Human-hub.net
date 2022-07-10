from django.utils import translation

def force_default_language_middleware(get_response):

    def middleware(request):
        language = translation.get_language_from_request(request)
        translation.activate(language)
        request.LANGUAGE_CODE = translation.get_language()

    return middleware