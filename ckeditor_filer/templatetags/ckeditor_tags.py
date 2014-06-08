from django.template import Context, Template, Library
from django.template.defaultfilters import stringfilter
from filer.models import File

register = Library()

@register.filter
@stringfilter
def render(value):
    return Template(value).render(Context())

@register.filter
def file_url(value):
	return File.objects.get(pk=value).url
