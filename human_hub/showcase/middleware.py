



class ChatLocaleMiddleware(object):

    def process_request(self, request):
        if request.path in ['/jsi18n/']:
            return None
        match = SHOPPER_CHAT_PATH.match(request.path)
        if match is not None:
            appid = match.groups()[0]
            try:
                store = Store.objects.get(appid=appid)
            except Store.DoesNotExist:
                return HttpResponse(status=404)
            customizations = get_customizations(store)
            request.session['django_language'] = customizations['language']
            request.store = store
            request.customizations = customizations
        else:
            request.session['django_language'] = settings.LANGUAGE_CODE