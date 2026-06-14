from django.shortcuts import render, redirect, get_object_or_404
from .models import Employee
from .forms import EmployeeForm
from leaves.models import Leave
from django.contrib.auth import update_session_auth_hash
from django.contrib import messages
from django.contrib.auth.decorators import login_required
def dashboard(request):

    pending_count = Leave.objects.filter(
        status='Pending'
    ).count()

    approved_count = Leave.objects.filter(
        status='Approved'
    ).count()

    rejected_count = Leave.objects.filter(
        status='Rejected'
    ).count()

    employee = Employee.objects.first()

    recent_leaves = Leave.objects.order_by(
        '-id'
    )[:5]

    return render(
        request,
        'employees/dashboard.html',
        {
            'pending_count': pending_count,
            'approved_count': approved_count,
            'rejected_count': rejected_count,
            'employee': employee,
            'recent_leaves': recent_leaves,
        }
    )

def employee_list(request):

    employees = Employee.objects.all()

    return render(
        request,
        'hr_portal/employee_list.html',
        {
            'employees': employees
        }
    )

def employee_add(request):

    if request.method == 'POST':

        form = EmployeeForm(
    request.POST,
    request.FILES
)

        if form.is_valid():

            form.save()

            return redirect('/employees/')

    else:

        form = EmployeeForm()

    return render(
        request,
        'employees/employee_form.html',
        {
            'form': form
        }
    )


def employee_update(request, pk):

    employee = get_object_or_404(
        Employee,
        pk=pk
    )

    if request.method == 'POST':

        form = EmployeeForm(
    request.POST,
    request.FILES,
    instance=employee
)

        if form.is_valid():

            form.save()

            return redirect('/employees/')

    else:

        form = EmployeeForm(
            instance=employee
        )

    return render(
        request,
        'employees/employee_form.html',
        {
            'form': form
        }
    )


def employee_delete(request, pk):

    employee = get_object_or_404(
        Employee,
        pk=pk
    )

    if request.method == 'POST':

        employee.delete()

        return redirect('/employees/')

    return render(
        request,
        'employees/employee_delete.html',
        {
            'employee': employee
        }
    )
def profile(request):

    employee = Employee.objects.first()

    return render(
        request,
        'employees/profile.html',
        {
            'employee': employee
        }
    )

def edit_profile(request):

    employee = Employee.objects.first()

    if request.method == 'POST':

        form = EmployeeForm(
            request.POST,
            request.FILES,
            instance=employee
        )

        if form.is_valid():

            form.save()

            print("PROFILE SAVED SUCCESSFULLY")

            return redirect('profile')

        else:

            print(form.errors)

    else:

        form = EmployeeForm(
            instance=employee
        )

    return render(
        request,
        'employees/edit_profile.html',
        {
            'form': form
        }
    )

def apply_leave(request):

    if request.method == 'POST':

        Leave.objects.create(
            employee_name=request.POST.get('employee_name'),
            leave_type=request.POST.get('leave_type'),
            from_date=request.POST.get('from_date'),
            to_date=request.POST.get('to_date'),
            reason=request.POST.get('reason'),
            status='Pending'
        )

        return render(
            request,
            'employees/apply_leave.html',
            {
                'success': True
            }
        )

    return render(
        request,
        'employees/apply_leave.html'
    )


def leave_history(request):

    leaves = Leave.objects.all().order_by('-id')

    return render(
        request,
        'employees/leave_history.html',
        {
            'leaves': leaves
        }
    )


@login_required
def change_password(request):

    if request.method == 'POST':

        old_password = request.POST.get(
            'old_password'
        )

        new_password = request.POST.get(
            'new_password'
        )

        confirm_password = request.POST.get(
            'confirm_password'
        )

        user = request.user

        if not user.check_password(
            old_password
        ):

            messages.error(
                request,
                'Old Password Incorrect'
            )

        elif new_password != confirm_password:

            messages.error(
                request,
                'Passwords Do Not Match'
            )

        else:

            user.set_password(
                new_password
            )

            user.save()

            update_session_auth_hash(
                request,
                user
            )

            messages.success(
                request,
                'Password Changed Successfully'
            )

        return redirect(
            'change_password'
        )

    return render(
        request,
        'employees/change_password.html'
    )
def hr_dashboard(request):

    return render(
    request,
    'hr_portal/dashboard.html'
)

def logout_view(request):

    return redirect('/')