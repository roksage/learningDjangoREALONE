from django.core.exceptions import ValidationError
from pint import UnitRegistry
from pint.errors import UndefinedUnitError
import os
valid_unit_measurments = ['punds', 'lbs', 'oz', 'gram']



ureg = UnitRegistry()

def validate_unit_of_measure(value):
        try:
            unit = ureg(value)
        except UndefinedUnitError as e:
            raise ValidationError(f'{e}')
        except:
             raise ValidationError(f'Ivyko nenumatyta klaida')
        

def validate_zip_extension(value):
    ext = os.path.splitext(value.name)[1]
    if ext.lower() != '.zip':
        raise ValidationError('Only zip files are allowed.')