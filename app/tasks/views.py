from django.http import HttpResponse, Http404
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .tasks import tasks, START_KEY
from .forms import SolutionForm
from .models import UnlockedKey


@login_required
def task(request, task_key):
    if task_key not in tasks:
        raise Http404()

    user_keys = {START_KEY}

    user_keys.update(request.user.unlocked_keys.values_list('key', flat=True))

    if tasks.get_task_lock(task_key) not in user_keys:
        raise Http404()

    task = tasks.get_task(task_key)(request.user.username)
    code_invalid = False
    if request.method == 'POST':
        form = SolutionForm(request.POST)
        if form.is_valid():
            code = form.cleaned_data['code']
            if task.is_solution(code):
                if task_key not in user_keys:
                    new_key = UnlockedKey(user=request.user, key=task_key)
                    new_key.save()
                messages.success(request, task.success_message(code))
                return redirect('task_view', tasks.get_task_key(task_key))
            else:
                messages.error(request, task.get_hint(code))
        else:
            messages.error(request, 'Pusty ciąg znakowy nie jest poprawnym'
                           ' rozwiązaniem... ;)')
        code_invalid = True
    else:
        form = SolutionForm()

    user_tasks = tasks.get_user_tasks(user_keys)

    ctx = {
        'task_id': task_key,
        'task': task,
        'form': form,
        'code_invalid': code_invalid,
        'tasks': user_tasks,
    }
    return render(request, "tasks/task_view.html", ctx)

@login_required
def task_files(request, task_key):
    if task_key not in tasks:
        raise Http404()

    user_keys = {START_KEY}
    user_keys.update(request.user.unlocked_keys.values_list('key', flat=True))

    if tasks.get_task_lock(task_key) not in user_keys:
        raise Http404()

    task = tasks.get_task(task_key)(request.user.username)

    return HttpResponse(task.challenge(),
                        content_type='text/x-python; charset=utf-8')


@login_required
def tasks_home(request):
    user_keys = {START_KEY}

    user_keys.update(request.user.unlocked_keys.values_list('key', flat=True))

    user_tasks = tasks.get_user_tasks(user_keys)

    ctx = {
        'tasks': user_tasks,
    }
    return render(request, "tasks/task_view_all.html", ctx)
