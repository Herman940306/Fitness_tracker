from django.views.generic import ListView
from .models import Member


class MemberListView(ListView):
    model = Member
    template_name = 'members/member_list.html'
    context_object_name = 'members'

    def get_queryset(self):
        # Only show members for the current user
        return Member.objects.filter(
            user=self.request.user
        ).order_by('-created_at')
