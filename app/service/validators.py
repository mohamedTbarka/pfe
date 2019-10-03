from django.core.exceptions import ValidationError


def minimum_size(image, width=None, height=None):
    # width = 1600
    # height = 600
    # print(image.file.__dict__)
    from django.core.files.images import get_image_dimensions
    image_info = {}
    errors = []
    image_info['width'], image_info['height'] = get_image_dimensions(image)
    if width and image_info['width'] < width:
        errors.append('Image Width should be > {} px.'.format(width))
    if height and image_info['height'] < height:
        errors.append('Image Height should be > {} px.'.format(height))
    if not (round(height / width, 1) == round(image_info['height'] / image_info['width'], 1)):
        errors.append('Image Height/Width ratio should be > {}.'.format(height / width))
    if errors:
        raise ValidationError(errors)


def exact_size(width=None, height=None):
    def validator(image):
        if not image.is_image():
            raise ValidationError('File should be image.')

        errors, image_info = [], image.info()['image_info']
        if width is not None and image_info['width'] == width:
            errors.append('Width should be > {} px.'.format(width))
        if height is not None and image_info['height'] == height:
            errors.append('Height should be > {} px.'.format(height))
        raise ValidationError(errors)

    return validator


def max_size(width=None, height=None):
    def validator(image):
        if not image.is_image():
            raise ValidationError('File should be image.')

        errors, image_info = [], image.info()['image_info']
        if width is not None and image_info['width'] >= width:
            errors.append('Width should be > {} px.'.format(width))
        if height is not None and image_info['height'] >= height:
            errors.append('Height should be > {} px.'.format(height))
        raise ValidationError(errors)

    return validator


def file_size(limit=2):
    def validator(image):
        file_size = image.file.size
        if file_size > limit * 1024 * 1024:
            raise ValidationError("Max size of file is %s MB" % limit)

    return validator
