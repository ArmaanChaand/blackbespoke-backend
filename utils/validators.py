import re
from django.core.exceptions import ValidationError
def only_svg_png_images(value):
    # Get the file name
    file_name = value.name.lower()

    # Check if the file has a valid extension
    if not file_name.endswith(('.svg', '.png')):
        raise ValidationError('Only SVG and PNG files are allowed.')

def validate_letters_and_spaces(input_string):    
    pattern = re.compile("^[a-zA-Z\s]+$")

    if pattern.match(input_string):
        return True
    else:
        return False
