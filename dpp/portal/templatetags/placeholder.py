from django import template
register = template.Library()

# def placeholder(value, token):
#     value.field.widget.attrs["placeholder"] = token
#     return value

# register.filter(placeholder)

@register.filter
def placeholder(value, token):
	value.field.widget.attrs["value"]=token
	return(value)