from django import template

register = template.Library()

@register.filter
def gs(valor):
    """
    Formatea a Guaraníes:
    2600000 -> Gs. 2.600.000
    """
    try:
        # convertir Decimal/str a número
        valor = float(valor)
        # miles con coma, luego cambiamos coma por punto
        return "Gs. " + f"{valor:,.0f}".replace(",", ".")
    except:
        return valor
