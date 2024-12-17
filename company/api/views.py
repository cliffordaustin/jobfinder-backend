from rest_framework import generics
from .serializers import (
    CompanyProfileSerializer,
    CompanyProfileImageSerializer,
)
from company.models import CompanyProfile, CompanyProfileImages
from rest_framework.exceptions import PermissionDenied
from rest_framework.permissions import IsAuthenticated
from .permissions import IsCompanyInstanceProfileImage, IsUserInstance


class CompanyProfileListView(generics.ListAPIView):
    serializer_class = CompanyProfileSerializer
    queryset = CompanyProfile.objects.all()


class CompanyProfileCreateView(generics.CreateAPIView):
    serializer_class = CompanyProfileSerializer
    queryset = CompanyProfile.objects.all()
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        if self.request.user.is_company:
            return serializer.save(user=self.request.user)
        else:
            raise PermissionDenied(
                "Your account isn't a company account, create a company account if you want to add a company profile"
            )


class CompanyProfileDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CompanyProfileSerializer
    permission_classes = [IsUserInstance]
    lookup_field = "slug"

    def get_queryset(self):
        queryset = CompanyProfile.objects.all()
        slug = self.kwargs.get("slug")

        if slug is not None:
            queryset = CompanyProfile.objects.filter(slug=slug)
        return queryset


class UserCompanyProfile(generics.RetrieveUpdateDestroyAPIView):
    model = CompanyProfile
    serializer_class = CompanyProfileSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        queryset = generics.get_object_or_404(CompanyProfile, user=self.request.user)
        return queryset


class CompanyProfileImageListView(generics.ListAPIView):
    serializer_class = CompanyProfileImageSerializer
    queryset = CompanyProfileImages.objects.all()


class CompanyProfileImageCreateView(generics.CreateAPIView):
    serializer_class = CompanyProfileImageSerializer
    queryset = CompanyProfileImages.objects.all()
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        company_profile_slug = self.kwargs.get("company_profile_slug")
        company_profile = generics.get_object_or_404(
            CompanyProfile, slug=company_profile_slug
        )

        if company_profile.user != self.request.user:
            raise PermissionDenied("You can't add to image profile to this Company")

        return serializer.save(company_profile=company_profile)


class CompanyProfileImageDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CompanyProfileImageSerializer
    permission_classes = [IsCompanyInstanceProfileImage]

    def get_queryset(self):
        queryset = CompanyProfileImages.objects.all()
        return queryset
