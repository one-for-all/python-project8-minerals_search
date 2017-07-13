from django import template


register = template.Library()


@register.inclusion_tag('minerals/render_field.html')
def render_mineral_field(mineral, field):
    value = field.value_to_string(mineral)
    return {'value': value, 'field': field}
