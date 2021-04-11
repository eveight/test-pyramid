import formencode
from formencode import validators



class Form(formencode.Schema):

    test = formencode.validators.NotEmpty()
    name = formencode.validators.NotEmpty()
    chislo = formencode.validators.Int(min=5)


def validate(**kwargs):
    print(kwargs)



x = {
    'test': 'ne test',
    'name': 'dont dict'
}

validate(**x)
# h-a-h-h-ha-ha
