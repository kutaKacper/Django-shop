from django import template

register = template.Library()

MONTH_NAMES_TRANSLATION = {
    'January': 'Styczeń',
    'February': 'Luty',
    'March': 'Marzec',
    'April': 'Kwiecień',
    'May': 'Maj',
    'June': 'Czerwiec',
    'July': 'Lipiec',
    'August': 'Sierpień',
    'September': 'Wrzesień',
    'October': 'Październik',
    'November': 'Listopad',
    'December': 'Grudzień',
}

@register.filter
def translate_month_name(month_name):
    return MONTH_NAMES_TRANSLATION.get(month_name, month_name)