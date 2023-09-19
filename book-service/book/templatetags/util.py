from django.template.defaulttags import register

@register.filter('reportkey')
def reportkey(dict_data, key):
    return dict_data.get(key)



