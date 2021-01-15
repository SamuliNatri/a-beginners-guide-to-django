from django.contrib import messages
from django.contrib.auth.decorators import permission_required
from django.shortcuts import render, redirect, get_object_or_404
from .forms import FeedbackForm, FeedbackDeleteForm
from .models import Feedback

# function-based views example, check pizzas app views.py for a class-based example


def feedback_add(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST, 
                            request.FILES or None)
        if form.is_valid():
            form.save()
            messages.success(request, 'Thank you for the feedback!')
            return redirect('pages:home')
    else:
        form = FeedbackForm()
    return render(request,
                  'feedback/add.html',
                  {
                      'form': form
                  })


@permission_required('feedback.change_feedback', 
                     raise_exception=True)
def feedback_edit(request, pk=None):
    feedback = get_object_or_404(Feedback, pk=pk)
    if request.method == "POST":
        form = FeedbackForm(request.POST,
                            request.FILES or None,
                            instance=feedback)
        if form.is_valid():
            form.save()
            return redirect('pages:home')
    else:
        form = FeedbackForm(instance=feedback)

    return render(request,
                  'feedback/edit.html',
                  {
                      'form': form,
                      'feedback': feedback
                  })


@permission_required('feedback.delete_feedback', 
                     raise_exception=True)
def feedback_delete(request, pk=None):
    feedback = get_object_or_404(Feedback, pk=pk)
    if request.method == "POST":
        form = FeedbackDeleteForm(request.POST,
                                  instance=feedback)
        if form.is_valid():
            feedback.delete()
            return redirect('pages:home')
    else:
        form = FeedbackDeleteForm(instance=feedback)

    return render(request, 'feedback/delete.html',
                  {
                      'form': form,
                      'feedback': feedback,
                  })