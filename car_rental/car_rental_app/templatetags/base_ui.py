from django import template

register = template.Library()


@register.inclusion_tag('car_rental_app/base.html', takes_context=True)
def base_component(context, active):
    return {
        'active': active
    }



