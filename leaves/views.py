from django.shortcuts import render, redirect
from .models import Leave
from django.shortcuts import render, redirect, get_object_or_404

def apply_leave(request):

    if request.method == 'POST':

        employee_name = request.POST.get('employee_name')
        leave_type = request.POST.get('leave_type')
        reason = request.POST.get('reason')

        Leave.objects.create(
            employee_name=employee_name,
            leave_type=leave_type,
            reason=reason
        )
        

        return redirect('/dashboard/')

    return render(
        request,
        'employees/apply_leave.html'
    )

def cancel_leave(request, pk):

    leave = get_object_or_404(
        Leave,
        id=pk
    )

    if leave.status == 'Pending':

        leave.delete()

    return redirect(
        'leave_history'
    )