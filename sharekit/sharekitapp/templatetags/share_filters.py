from django import template
from django import template
from nepse_func import share_data

register = template.Library()

@register.filter(name='getkey')
def getkey(value, arg):
    """ returns value of key from a dict """
    return value[arg]

@register.filter
def total_amt(share):
    """ returns total amount of the share """
    try:
        return share.quantity * share_data.get(share.scrip).get("Closing Price")
    except:
        return None

@register.filter
def grand_total(shares):
    total = 0
    try:
        for share in shares:
            total += share.quantity * share_data.get(share.scrip).get("Closing Price")
        return total
    except:
        return None

@register.filter
def check_change(share):
    try:
        if share_data.get(share.scrip).get("Difference Rs.") > 0:
            return "table-success"
        elif share_data.get(share.scrip).get("Difference Rs.") < 0:
            return "table-danger"
        else:
            return "table-primary"
    except:
        return "None"

@register.filter
def is_success(result, boid):
    print(boid)
    message = result.get(boid)
    print(message)
    if "Sorry" in message:
        return "table-danger"
    else:
        return "table-success"