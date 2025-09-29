from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Study
import logging

logger = logging.getLogger(__name__)


def study_list(request):
    try:
        studies = Study.objects.all().order_by('-created_at')
        return render(request, 'list_study.html', {'studies': studies})
    except Exception as e:
        logger.error(f"Error fetching studies: {str(e)}")
        messages.error(request, "Error loading studies")
        return render(request, 'list_study.html', {'studies': []})


def study_add(request):
    if request.method == 'POST':
        try:
            study = Study(
                study_name=request.POST.get('study_name'),
                study_phase=request.POST.get('study_phase'),
                sponsor_name=request.POST.get('sponsor_name'),
                study_description=request.POST.get('study_description')
            )
            study.save()
            messages.success(request, "Study added successfully")
            logger.info(f"Study created: {study.study_name}")
            return redirect('study_list')
        except Exception as e:
            logger.error(f"Error creating study: {str(e)}")
            messages.error(request, "Error adding study")

    sponsors = Study.objects.values_list('sponsor_name', flat=True).distinct()
    phases = ['Phase I', 'Phase II', 'Phase III', 'Phase IV']
    return render(request, 'form_study.html', {
        'sponsors': sponsors,
        'phases': phases,
        'action': 'Add'
    })


def study_view(request, pk):
    """View study details"""
    try:
        study = get_object_or_404(Study, pk=pk)
        return render(request, 'view_study.html', {'study': study})
    except Exception as e:
        logger.error(f"Error viewing study: {str(e)}")
        messages.error(request, "Study not found")
        return redirect('study_list')


def study_edit(request, pk):
    try:
        study = get_object_or_404(Study, pk=pk)

        if request.method == 'POST':
            study.study_name = request.POST.get('study_name')
            study.study_phase = request.POST.get('study_phase')
            study.sponsor_name = request.POST.get('sponsor_name')
            study.study_description = request.POST.get('study_description')
            study.save()
            messages.success(request, "Study updated successfully")
            logger.info(f"Study updated: {study.study_name}")
            return redirect('study_list')

        sponsors = Study.objects.values_list('sponsor_name', flat=True).distinct()
        phases = ['Phase I', 'Phase II', 'Phase III', 'Phase IV']
        return render(request, 'form_study.html', {
            'study': study,
            'sponsors': sponsors,
            'phases': phases,
            'action': 'Edit'
        })
    except Exception as e:
        logger.error(f"Error editing study: {str(e)}")
        messages.error(request, "Error updating study")
        return redirect('study_list')


def study_delete(request, pk):
    try:
        study = get_object_or_404(Study, pk=pk)
        study_name = study.study_name
        study.delete()
        messages.success(request, f"Study '{study_name}' deleted successfully")
        logger.info(f"Study deleted: {study_name}")
    except Exception as e:
        logger.error(f"Error deleting study: {str(e)}")
        messages.error(request, "Error deleting study")

    return redirect('study_list')


def study_delete_bulk(request):
    ids = request.GET.get("ids", "").split(",")
    try:
        studies = Study.objects.filter(pk__in=ids)
        count = studies.count()
        studies.delete()
        messages.success(request, f"{count} studies deleted successfully")
        logger.info(f"Deleted studies with IDs: {ids}")
    except Exception as e:
        logger.error(f"Error deleting studies: {str(e)}")
        messages.error(request, "Error deleting selected studies")

    return redirect("study_list")
