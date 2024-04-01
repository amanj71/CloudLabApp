import random
import string
from django.utils.text import slugify


## Define your functions here
def generate_random_string(length):
    """
    Generates a random string of the specified length.

    Args:
        length (int): The desired length of the random string.

    Returns:
        str: A random string of the specified length.
    """
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for _ in range(length))


def original_generate_unique_slug(klass, field1, field2, instance=None):
    """
    return unique slug if origin slug is exist.
    eg: `foo-bar` => `foo-bar-1`
    :param `klass` is Class model.
    :param `field1` is specific field for title.
    :param `field2` is specific field for title.
    :param `instance` is instance object for excluding specific object.
    """
    origin_slug = slugify(f"{field1}{field2}")
    unique_slug = origin_slug
    numb = 1
    if instance is not None:
        while klass.objects.filter(slug=unique_slug).exclude(id=instance.id).exists():
            unique_slug = '%s-%d' % (origin_slug, numb)
            numb += 1
    else:
        while klass.objects.filter(slug=unique_slug).exists():
            unique_slug = '%s-%d' % (origin_slug, numb)
            numb += 1
    return unique_slug

def generate_unique_slug(klass, *args, instance=None):
    """
    return unique slug if origin slug is exist.
    eg: `foo-bar` => `foo-bar-1`
    :param `klass` is Class model.
    :param `*args` is specific field for title.
    :param `instance` is instance object for excluding specific object.
    """
    slug = "-".join(args)
    origin_slug = slugify(slug)
    unique_slug = origin_slug
    numb = 1
    if instance is not None:
        while klass.objects.filter(slug=unique_slug).exclude(id=instance.id).exists():
            unique_slug = '%s-%d' % (origin_slug, numb)
            numb += 1
    else:
        while klass.objects.filter(slug=unique_slug).exists():
            unique_slug = '%s-%d' % (origin_slug, numb)
            numb += 1
    return unique_slug
    