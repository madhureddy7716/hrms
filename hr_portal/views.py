from django.shortcuts import render, redirect, get_object_or_404

from employees.models import Employee
from leaves.models import Leave
from assets.models import Asset


def hr_dashboard(request):
    total_employees = Employee.objects.count()

    pending_leaves = Leave.objects.filter(
        status='Pending'
    ).count()

    approved_leaves = Leave.objects.filter(
        status='Approved'
    ).count()

    rejected_leaves = Leave.objects.filter(
        status='Rejected'
    ).count()

    total_assets = Asset.objects.count()

    assigned_assets = Asset.objects.filter(
        status='Assigned'
    ).count()

    available_assets = Asset.objects.filter(
        status='Available'
    ).count()

    returned_assets = Asset.objects.filter(
        status='Returned'
    ).count()

    return render(
        request,
        'hr_portal/dashboard.html',
        {
            'total_employees': total_employees,
            'pending_leaves': pending_leaves,
            'approved_leaves': approved_leaves,
            'rejected_leaves': rejected_leaves,
            'total_assets': total_assets,
            'assigned_assets': assigned_assets,
            'available_assets': available_assets,
            'returned_assets': returned_assets,
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


def leave_requests(request):
    leaves = Leave.objects.all().order_by('-id')

    return render(
        request,
        'hr_portal/leave_requests.html',
        {
            'leaves': leaves
        }
    )


def approve_leave(request, pk):
    leave = get_object_or_404(
        Leave,
        pk=pk
    )

    leave.status = 'Approved'
    leave.save()

    return redirect('leave_requests')


def reject_leave(request, pk):
    leave = get_object_or_404(
        Leave,
        pk=pk
    )

    leave.status = 'Rejected'
    leave.save()

    return redirect('leave_requests')


def disable_employee(request, pk):
    employee = get_object_or_404(
        Employee,
        pk=pk
    )

    employee.is_active = False
    employee.save()

    return redirect('employee_list')