import random 
from django.utils.text import slugify


def slugify_instance_title(instance, save=False, new_slug = None):

    if new_slug is not None:
        slug = new_slug
    else:
        slug = slugify(instance.title)

    Klass = instance.__class__
    qs = Klass.objects.filter(slug=slug).exclude(id=instance.id)
    if qs.exists():
        slug = f"{slug}-{random.randint(100,100000)}"
        return slugify_instance_title(instance, save = save, new_slug= slug)
    instance.slug = slug


    if save:
        instance.save()

    return instance
