from django.db import models
from django.conf import settings
from imagekit.models import ProcessedImageField
from imagekit.processors import Resize

from core.utils import company_image_thumbnail


class CompanyProfile(models.Model):
    slug = models.SlugField(max_length=255, blank=True, null=True)
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    company_name = models.CharField(max_length=500, blank=True, null=True)
    num_of_employees = models.CharField(blank=True, null=True)
    year_started = models.PositiveIntegerField(blank=True, null=True)
    about_company = models.TextField(blank=True, null=True)
    company_values = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.company_name} - {self.user}"


class CompanyProfileImages(models.Model):
    company_profile = models.ForeignKey(
        CompanyProfile, on_delete=models.CASCADE, related_name="company_images"
    )
    image = ProcessedImageField(
        upload_to=company_image_thumbnail,
        processors=[Resize(1920, 1080)],
        format="JPEG",
        options={"quality": 90},
    )
    comment = models.CharField(blank=True, null=True, max_length=100)

    def __str__(self):
        return str(self.company_profile)
