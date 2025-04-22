"""
This module contains views for managing members in the
fitness tracker application.
It includes functionality for listing, creating, updating,
and deleting members.
"""

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test
from django.utils import timezone
from django.contrib import messages
from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Member
from .forms import MemberForm


class MemberListView(LoginRequiredMixin, ListView):
    '''List view for members.
    This view displays a list of members for the logged-in user.'''
    model = Member
    template_name = 'members/member_list.html'
    context_object_name = 'members'

    def get_queryset(self):
        """Only show members for the current user"""
        return Member.objects.filter(user=self.request.user)


@login_required
@user_passes_test(lambda u: u.role == 'ADMIN')
def member_list(request):
    '''List view for members.
    This view displays a list of members for the logged-in user.'''
    members = Member.objects.all()
    messages.success(request, "Member list retrieved successfully.")
    return render(request, 'members/member_list.html', {'members': members})


@login_required
def member_create(request):
    '''Create a new member.
    This view handles the creation of a new member.'''
    if request.method == 'POST':
        form = MemberForm(request.POST)
        if form.is_valid():
            try:
                member = form.save(commit=False)
                member.created_at = timezone.now()
                member.user = request.user
                member.save()
                messages.success(request, "Member created successfully!")
                return redirect('members_list')
            except Exception as e:
                messages.error(request, f"Error creating member: {str(e)}")
    else:
        form = MemberForm()

    return render(request, 'members/member_form.html', {'form': form})


@login_required
@user_passes_test(lambda u: u.role == 'ADMIN')
def member_update(request, pk):
    '''Update an existing member.
    This view handles the update of an existing member.'''
    member = get_object_or_404(Member, pk=pk)
    if request.method == 'POST':
        form = MemberForm(request.POST, instance=member)
        if form.is_valid():
            form.save()
            return redirect('visitor_list')
    else:
        form = MemberForm(instance=member)
    return render(request, 'members/member_form.html', {'form': form})


@login_required
@user_passes_test(lambda u: u.role == 'ADMIN')
def member_delete(request, pk):
    '''Delete an existing member.
    This view handles the deletion of an existing member.'''
    member = get_object_or_404(Member, pk=pk)
    if request.method == 'POST':
        member.delete()
        messages.success(request, "Member deleted successfully!")
        return redirect('visitor_list')
    return render(request, 'members/member_confirm_delete.html',
                  {'member': member})
