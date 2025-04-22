from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test
from .models import Visit
from .forms import VisitForm


@login_required
def visit_list(request):
    visits = Visit.objects.all()
    return render(request, 'visits/visit_list.html', {'visits': visits})


@login_required
def visit_create(request):
    if request.method == 'POST':
        form = VisitForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('visit_list')
    else:
        form = VisitForm()
    return render(request, 'visits/visit_form.html', {'form': form})


@login_required
def visit_update(request, pk):
    visit = get_object_or_404(Visit, pk=pk)
    if request.method == 'POST':
        form = VisitForm(request.POST, instance=visit)
        if form.is_valid():
            form.save()
            return redirect('visit_list')
    else:
        form = VisitForm(instance=visit)
    return render(request, 'visits/visit_form.html', {'form': form})


@login_required
def visit_delete(request, pk):
    visit = get_object_or_404(Visit, pk=pk)
    if request.method == 'POST':
        visit.delete()
        return redirect('visit_list')
    return render(request, 'visits/visit_confirm_delete.html', {'visit': visit})

@login_required
@user_passes_test(lambda u: u.role in ['ADMIN', 'STAFF'])
def visit_list(request):
    visits = Visit.objects.all()
    return render(request, 'visits/visit_list.html', {'visits': visits})
