from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test
from .models import Staff
from .forms import StaffForm


@login_required
@user_passes_test(lambda u: u.role == 'ADMIN')
def staff_list(request):
    staff_members = Staff.objects.all()
    return render(request, 'staff/staff_list.html', {'staff_members': staff_members})


@login_required
@user_passes_test(lambda u: u.role == 'ADMIN')
def staff_create(request):
    if request.method == 'POST':
        form = StaffForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('staff_list')
    else:
        form = StaffForm()
    return render(request, 'staff/staff_form.html', {'form': form})


@login_required
@user_passes_test(lambda u: u.role == 'ADMIN')
def staff_update(request, pk):
    staff = get_object_or_404(Staff, pk=pk)
    if request.method == 'POST':
        form = StaffForm(request.POST, instance=staff)
        if form.is_valid():
            form.save()
            return redirect('staff_list')
    else:
        form = StaffForm(instance=staff)
    return render(request, 'staff/staff_form.html', {'form': form})


@login_required
@user_passes_test(lambda u: u.role == 'ADMIN')
def staff_delete(request, pk):
    staff = get_object_or_404(Staff, pk=pk)
    if request.method == 'POST':
        staff.delete()
        return redirect('staff_list')
    return render(request, 'staff/staff_confirm_delete.html', {'staff': staff})
