from django.shortcuts import render
from django.views.generic.base import TemplateView , RedirectView
# Create your views here.

class SaiNaikRedirectView(RedirectView):
    url='https://www.geekyshows.com' 


class SaiRedirectView(RedirectView):
    pattern_name = 'Sai1'
    permanent = True
    query_string = True

    def get_redirect_url(self , *args , **kwargs):
        print(kwargs)
        kwargs['pk'] = 16
        return super().get_redirect_url(*args , **kwargs)
