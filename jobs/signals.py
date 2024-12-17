from django.db.models.signals import pre_save
from django.dispatch import receiver
from .models import Job, Seeker
from django.utils.text import slugify
from core.utils import generate_random_string


@receiver(pre_save, sender=Job)
def create_slug(sender, instance, *args, **kwargs):
    if instance and not instance.slug:
        slug = slugify(instance.company.company_name)
        random_string = generate_random_string(length=12)
        instance.slug = slug + "-" + random_string


@receiver(pre_save, sender=Seeker)
def create_seeker_slug(sender, instance, *args, **kwargs):
    if instance and not instance.slug:
        random_string = generate_random_string(length=24)
        instance.slug = random_string
