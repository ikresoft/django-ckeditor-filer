from django import http
from django.core import urlresolvers 
from models import ThumbnailOption
import json

def url_reverse(request): 
    if request.method in ('GET', 'POST'): 
        data = getattr(request, request.method) 
        url_name = data.get('url_name') 
        try: 
            path = urlresolvers.reverse(url_name, args=data.getlist('args')) 
            (view_func, args, kwargs) = urlresolvers.resolve(path)
            return http.HttpResponse(path, content_type="text/plain")
            #return view_func(request, *args, **kwargs)
        except urlresolvers.NoReverseMatch: 
            return http.HttpResponse("Greska", content_type="text/plain")
    return http.HttpResponseNotAllowed(('GET', 'POST'))


from easy_thumbnails.files import get_thumbnailer
from filer.models.imagemodels import Image

def url_image(request, image_id, thumb_options=None, width=None, height=None):
    image = Image.objects.get(pk=image_id)
    url = image.url
    thumbnail_options = {}
    if thumb_options is not None:
        thumbnail_options = ThumbnailOption.objects.get(pk=thumb_options).as_dict
    
    if width is not None or height is not None:
        width = int(width)
        height = int(height)

        size = (width, height)
        thumbnail_options.update({'size': size})

    if thumbnail_options != {}:
        thumbnailer = image.easy_thumbnails_thumbnailer
        image = thumbnailer.get_thumbnail(thumbnail_options)
        url = image.url
    data = {
        'url': url,
        'width': image.width,
        'height': image.height,
    }
    return http.HttpResponse(json.dumps(data), content_type="application/json")

def thumbnail_options(request):
    response_data = [{'id': opt.pk, 'name': opt.name} for opt in ThumbnailOption.objects.all()]
    return http.HttpResponse(json.dumps(response_data), content_type="application/json")