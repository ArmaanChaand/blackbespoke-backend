from django.core.validators import FileExtensionValidator

def only_svg_png_images(value):
    valid_extensions = ['.svg', '.png']

    validator = FileExtensionValidator(
        allowed_extensions=valid_extensions,
        message='Only SVG and PNG files are allowed.'
    )

    validator(value)