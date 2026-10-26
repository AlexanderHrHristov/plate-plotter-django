from decimal import  Decimal, InvalidOperation
from django import template

register = template.Library()


@register.filter(name= 'euro')

def euro(value):
    if value is None or value == '':
        
        return '-/-'
    
    try:
        price = Decimal(str(value))
        return f'{price:.2f} €'
    except (InvalidOperation, ValueError, TypeError):
        
        return '-/-'
    
    
