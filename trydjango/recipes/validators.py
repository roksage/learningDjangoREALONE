from django.core.exceptions import ValidationError
from pint import UnitRegistry
from pint.errors import UndefinedUnitError

valid_unit_measurments = ['punds', 'lbs', 'oz', 'gram']



ureg = UnitRegistry()

def validate_unit_of_measure(value):
        try:
            unit = ureg(value)
        except UndefinedUnitError as e:
            raise ValidationError(f'{e}')
        except:
             raise ValidationError(f'Ivyko nenumatyta klaida')