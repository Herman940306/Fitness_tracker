"""
Pre-conditions:
- The user is authenticated for all views (enforced by @login_required).
- For `visit_update` and `visit_delete`, the `pk` parameter corresponds to an
existing Visit object.
- For `admin_visit_list`, the user must have a role of 'ADMIN' or 'STAFF'
(enforced by @user_passes_test).

Post-conditions:
- `visit_list` renders a list of visits for the logged-in user.
- `visit_create` creates a new Visit object if the form is valid and redirects
to the visit list.
- `visit_update` updates an existing Visit object if the form is valid and
redirects to the visit list.
- `visit_delete` deletes an existing Visit object and redirects
to the visit list.
- `admin_visit_list` renders a list of all visits in the system
for admin and staff users.
"""
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test
from .models import Visit
from .forms import VisitForm


# This module handles visit listing, creation, updating, and deletion of visits
@login_required
def visit_list(request):
    """ List all visits for the logged-in user. """
    visits = Visit.objects.all()
    return render(request, 'visits/visit_list.html', {'visits': visits})


# This view is to create a new visit
# It is accessible only to logged-in users
@login_required
def visit_create(request):
    """ Create a new visit for the logged-in user. """
    if request.method == 'POST':
        form = VisitForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('visit_list')
    else:
        form = VisitForm()
    return render(request, 'visits/visit_form.html', {'form': form})


# This view is to update an existing visit
@login_required
def visit_update(request, pk):
    """ Update an existing visit for the logged-in user. """
    visit = get_object_or_404(Visit, pk=pk)
    if request.method == 'POST':
        form = VisitForm(request.POST, instance=visit)
        if form.is_valid():
            form.save()
            return redirect('visit_list')
    else:
        form = VisitForm(instance=visit)
    return render(request, 'visits/visit_form.html', {'form': form})


# This view is to delete an existing visit
# It is accessible only to logged-in users
@login_required
def visit_delete(request, pk):
    """ Delete an existing visit for the logged-in user. """
    visit = get_object_or_404(Visit, pk=pk)
    if request.method == 'POST':
        visit.delete()
        return redirect('visit_list')
    return render(request, 'visits/visit_confirm_delete.html',
                  {'visit': visit})


# This view is for staff and admin users only
# It lists all visits in the system
@login_required
@user_passes_test(lambda u: u.role in ['ADMIN', 'STAFF'])
def admin_visit_list(request):
    """ List all visits in the system for admin and staff users. """
    visits = Visit.objects.all()
    return render(request, 'visits/visit_list.html', {'visits': visits})
