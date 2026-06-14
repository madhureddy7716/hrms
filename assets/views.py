from django.shortcuts import render, redirect, get_object_or_404

from .models import Asset, AssetHistory
from .forms import AssetForm


def asset_list(request):
    assets = Asset.objects.all()

    return render(
        request,
        'assets/asset_list.html',
        {
            'assets': assets
        }
    )


def asset_add(request):

    if request.method == 'POST':

        form = AssetForm(request.POST)

        if form.is_valid():

            print("FORM VALID")

            form.save()

            return redirect('asset_list')

        else:

            print(form.errors)

    else:

        form = AssetForm()

    return render(
        request,
        'assets/asset_add.html',
        {'form': form}
    )


def asset_update(request, pk):
    asset = get_object_or_404(
        Asset,
        pk=pk
    )

    if request.method == 'POST':
        form = AssetForm(
            request.POST,
            instance=asset
        )

        if form.is_valid():
            asset = form.save(commit=False)

            if asset.employee:
                asset.status = 'Assigned'

            asset.save()

            AssetHistory.objects.create(
                asset=asset,
                employee=asset.employee,
                action='Updated'
            )

            return redirect('asset_list')

    else:
        form = AssetForm(instance=asset)

    return render(
        request,
        'assets/asset_form.html',
        {
            'form': form
        }
    )

def asset_return(request, pk):

    asset = get_object_or_404(
        Asset,
        pk=pk
    )

    AssetHistory.objects.create(
        asset=asset,
        employee=asset.employee,
        action='Returned'
    )

    asset.status = 'Returned'

    asset.employee = None

    asset.save()

    return redirect(
        'asset_list'
    )


def asset_history(request):
    history = AssetHistory.objects.all().order_by(
        '-action_date'
    )

    return render(
        request,
        'assets/asset_history.html',
        {
            'history': history
        }
    )


def asset_delete(request, pk):
    asset = get_object_or_404(
        Asset,
        pk=pk
    )

    if request.method == 'POST':
        asset.delete()
        return redirect('asset_list')

    return render(
        request,
        'assets/asset_delete.html',
        {
            'asset': asset
        }
    )