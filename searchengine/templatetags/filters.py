#Custom filters 
from django import template
register = template.Library()

@register.filter
def getDictKey(dict, key):
   # Try to fetch from the dict, and if it's not found return an empty string.
   return dict.get(key, '')

