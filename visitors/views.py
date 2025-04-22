from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from .models import Visitor
from .forms import VisitorForm
from django.utils import timezone
from django.contrib import messages
from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin


class VisitorListView(LoginRequiredMixin, ListView):
    model = Visitor
    template_name = 'visitors/visitor_list.html'
    context_object_name = 'visitors'

    def get_queryset(self):
        """Only show visitors for the current user"""
        return Visitor.objects.filter()

@login_required
@user_passes_test(lambda u: u.role == 'ADMIN')
def visitor_list(request):
    visitors = Visitor.objects.all()
    return render(request, 'visitors/visitor_list.html', {'visitors': visitors})


@login_required
def visitor_create(request):
    if request.method == 'POST':
        form = VisitorForm(request.POST)
        if form.is_valid():
            try:
                visitor = form.save(commit=False)
                visitor.created_at = timezone.now()
                visitor.user = request.user
                visitor.save()
                messages.success(request, "Visitor created successfully!")
                return redirect('visitor_list')
            except Exception as e:
                messages.error(request, f"Error creating visitor: {str(e)}")
    else:
        form = VisitorForm()
    
    return render(request, 'visitors/visitor_form.html', {'form': form})


@login_required
@user_passes_test(lambda u: u.role == 'ADMIN')
def visitor_update(request, pk):
    visitor = get_object_or_404(Visitor, pk=pk)
    if request.method == 'POST':
        form = VisitorForm(request.POST, instance=visitor)
        if form.is_valid():
            form.save()
            return redirect('visitor_list')
    else:
        form = VisitorForm(instance=visitor)
    return render(request, 'visitors/visitor_form.html', {'form': form})


@login_required
@user_passes_test(lambda u: u.role == 'ADMIN')
def visitor_delete(request, pk):
    visitor = get_object_or_404(Visitor, pk=pk)
    if request.method == 'POST':
        visitor.delete()
        return redirect('visitor_list')
    return render(request, 'visitors/visitor_confirm_delete.html', {'visitor': visitor})
