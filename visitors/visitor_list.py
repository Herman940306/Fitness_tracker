from django.views.generic import ListView
from .models import Visitor

class VisitorListView(ListView):
    model = Visitor
    template_name = 'visitors/visitor_list.html'
    context_object_name = 'visitors'
    
    def get_queryset(self):
        # Only show visitors for the current user
        return Visitor.objects.filter(user=self.request.user).order_by('-created_at')