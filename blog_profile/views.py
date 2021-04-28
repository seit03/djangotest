from django.views.generic import ListView, DetailView

from blog_profile.models import Profile


class ProfileView(ListView):
    model = Profile
    template_name = 'profile/profile_list.html'

    def get_queryset(self):
        return Profile.objects.all()


class ProfileDetailView(DetailView):
    model = Profile
    template_name = 'profile/profile_detail.html'
