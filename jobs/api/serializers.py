from rest_framework import serializers

from jobs.models import Job, Seeker


class SeekerSerializer(serializers.ModelSerializer):
    slug = serializers.StringRelatedField(read_only=True)
    user = serializers.StringRelatedField(read_only=True)
    user_profile_image = serializers.SerializerMethodField()
    name = serializers.SerializerMethodField()

    class Meta:
        model = Seeker
        exclude = ["job"]

    def get_user_profile_image(self, instance):
        return instance.user.profile_pic.url

    def get_name(self, instance):
        return f"{instance.user.first_name} {instance.user.last_name}"


class JobSerializer(serializers.ModelSerializer):
    slug = serializers.StringRelatedField(read_only=True)
    num_applicants = serializers.SerializerMethodField()
    company = serializers.StringRelatedField(read_only=True)
    company_name = serializers.SerializerMethodField()
    company_slug = serializers.SerializerMethodField()
    company_profile_image = serializers.SerializerMethodField()

    class Meta:
        model = Job
        fields = "__all__"

    def get_num_applicants(self, instance):
        return instance.seekers.count()

    def get_company_name(self, instance):
        return instance.company.company_name

    def get_company_slug(self, instance):
        return instance.company.slug

    def get_company_profile_image(self, instance):

        return instance.company.user.profile_pic.url
