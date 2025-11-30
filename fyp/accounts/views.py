from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.utils import timezone
from .forms import UserRegistrationForm, UserLoginForm, UserProfileForm
from .models import User

def register_view(request):
    if request.user.is_authenticated:
        return redirect('certificates:dashboard')
    
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Registration successful! Welcome to the platform.')
            return redirect('certificates:dashboard')
    else:
        form = UserRegistrationForm()
    
    return render(request, 'accounts/register.html', {'form': form})


def login_view(request):
    if request.user.is_authenticated:
        return redirect('certificates:dashboard')
    
    if request.method == 'POST':
        form = UserLoginForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, f'Welcome back, {user.username}!')
                next_url = request.GET.get('next', 'certificates:dashboard')
                return redirect(next_url)
    else:
        form = UserLoginForm()
    
    return render(request, 'accounts/login.html', {'form': form})


@login_required
def logout_view(request):
    logout(request)
    messages.info(request, 'You have been logged out successfully.')
    return redirect('home')


@login_required
def profile_view(request):
    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully!')
            return redirect('accounts:profile')
    else:
        form = UserProfileForm(instance=request.user)
    
    return render(request, 'accounts/profile.html', {'form': form})


@login_required
def pending_institutions_view(request):
    if not (request.user.user_type == 'admin' or request.user.is_staff or request.user.is_superuser):
        messages.error(request, 'You do not have permission to access this page.')
        return redirect('certificates:dashboard')
    
    pending_institutions = User.objects.filter(user_type='institution', is_approved=False).order_by('-created_at')
    approved_institutions = User.objects.filter(user_type='institution', is_approved=True).order_by('-approval_date')
    
    context = {
        'pending_institutions': pending_institutions,
        'approved_institutions': approved_institutions,
    }
    return render(request, 'accounts/pending_institutions.html', context)


@login_required
def approve_institution_view(request, user_id):
    if not (request.user.user_type == 'admin' or request.user.is_staff or request.user.is_superuser):
        messages.error(request, 'You do not have permission to perform this action.')
        return redirect('certificates:dashboard')
    
    institution = get_object_or_404(User, id=user_id, user_type='institution')
    
    if request.method == 'POST':
        institution.is_approved = True
        institution.approval_date = timezone.now()
        institution.approved_by = request.user
        institution.save()
        
        messages.success(request, f'{institution.organization or institution.username} has been approved successfully!')
        return redirect('accounts:pending_institutions')
    
    return render(request, 'accounts/approve_institution.html', {'institution': institution})


@login_required
def revoke_approval_view(request, user_id):
    if not (request.user.user_type == 'admin' or request.user.is_staff or request.user.is_superuser):
        messages.error(request, 'You do not have permission to perform this action.')
        return redirect('certificates:dashboard')
    
    institution = get_object_or_404(User, id=user_id, user_type='institution')
    
    if request.method == 'POST':
        institution.is_approved = False
        institution.approval_date = None
        institution.approved_by = None
        institution.save()
        
        messages.warning(request, f'Approval for {institution.organization or institution.username} has been revoked.')
        return redirect('accounts:pending_institutions')
    
    return render(request, 'accounts/revoke_approval.html', {'institution': institution})

