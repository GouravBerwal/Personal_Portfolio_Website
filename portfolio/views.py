import os
from django.conf import settings
from django.shortcuts import render, redirect
from django.http import JsonResponse, FileResponse, Http404
from django.contrib import messages
from django.views.decorators.http import require_POST
from .models import Profile, Skill, Project, Experience, ContactMessage
from .forms import ContactForm


def index(request):
    # Self-healing safeguard: if database is empty on serverless start, populate it
    try:
        if Skill.objects.count() == 0 or Project.objects.count() == 0:
            from django.core.management import call_command
            call_command('migrate', interactive=False, verbosity=0)
            call_command('seed_portfolio', interactive=False, verbosity=0)
    except Exception as e:
        print(f"Self-heal database notice: {e}")

    profile = Profile.objects.first()
    if not profile:
        profile = Profile.objects.create()

    skills = Skill.objects.all()
    projects = Project.objects.all()
    experiences = Experience.objects.all()
    form = ContactForm()

    context = {
        'profile': profile,
        'skills': skills,
        'projects': projects,
        'experiences': experiences,
        'form': form,
    }
    return render(request, 'index.html', context)


def resume_view(request):
    """
    Serves Gourav Berwal's updated Resume PDF inline in the browser
    or triggers download when ?download=1 is supplied.
    """
    candidate_paths = [
        os.path.join(settings.BASE_DIR, 'static', 'docs', 'Gourav_Berwal_Resume.pdf'),
        os.path.join(settings.BASE_DIR, 'static', 'docs', 'resume.pdf'),
        os.path.join(settings.BASE_DIR, 'media', 'resume', 'Gourav_Berwal_Resume.pdf'),
    ]

    for p in candidate_paths:
        if os.path.exists(p):
            disposition = 'attachment' if request.GET.get('download') == '1' else 'inline'
            response = FileResponse(open(p, 'rb'), content_type='application/pdf')
            response['Content-Disposition'] = f'{disposition}; filename="Gourav_Berwal_Resume.pdf"'
            return response

    raise Http404("Resume PDF not found on server.")


@require_POST
def contact_submit(request):
    is_ajax = (
        request.headers.get('x-requested-with') == 'XMLHttpRequest' or
        'application/json' in request.headers.get('Accept', '') or
        request.POST.get('ajax') == 'true'
    )

    form = ContactForm(request.POST)
    if form.is_valid():
        msg = form.save()
        if is_ajax:
            return JsonResponse({
                'status': 'success',
                'message': f'Thank you, {msg.name}! Your message has been sent successfully. I will get back to you soon.'
            })
        messages.success(request, f'Thank you, {msg.name}! Your message has been sent successfully.')
        return redirect('/#contact')
    else:
        errors = form.errors.as_json()
        if is_ajax:
            return JsonResponse({
                'status': 'error',
                'message': 'Please correct the errors in the form and try again.',
                'errors': form.errors
            }, status=400)
        messages.error(request, 'Please check your inputs and try again.')
        return redirect('/#contact')
