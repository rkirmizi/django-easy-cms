from easy_cms import widget


@widget
def content(context, name):
    from django.contrib.sites.models import Site
    from easy_cms.models import Content
    try:
        site = Site.objects.get_current()
        obj = Content.objects.get(name=name, site=site)
        return {'content': obj}, obj.template_name
    except Content.DoesNotExist:
        return {}, None
