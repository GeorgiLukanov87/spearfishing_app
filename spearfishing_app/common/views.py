import pyperclip

from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404

from django.urls import reverse
from django.views import generic

from spearfishing_app.common.helpers.dirty_words_validator import validate_dirty_words
from spearfishing_app.common.forms import CommentForm, SearchForm
from spearfishing_app.common.models import Like, Comment, Video
from spearfishing_app.photos.models import Photo

UserModel = get_user_model()


# common/views.py

def index(request):
    all_photos = Photo.objects.all().order_by('-id')
    comment_form = CommentForm()
    search_form = SearchForm()

    if request.method == 'POST':
        search_form = SearchForm(request.POST)
        if search_form.is_valid():
            all_photos = all_photos.filter(photo__icontains=search_form.cleaned_data['user_name'])

    per_page = 4
    paginator = Paginator(all_photos, per_page)
    page = request.GET.get('page')

    try:
        all_photos = paginator.page(page)
    except PageNotAnInteger:
        all_photos = paginator.page(1)
    except EmptyPage:
        all_photos = paginator.page(paginator.num_pages)

    context = {
        'all_photos': all_photos,
        'comment_form': comment_form,
        'search_form': search_form,
    }

    return render(
        request,
        'common/home-page.html',
        context,
    )


@login_required
def like_functionality(request, photo_id):
    liked_object = Like.objects.filter(to_photo_id=photo_id, user_id=request.user.pk)

    if liked_object:
        liked_object.delete()
    else:
        Like.objects.create(
            to_photo_id=photo_id,
            user_id=request.user.pk,
        )

    return redirect(request.META['HTTP_REFERER'])


def share(request, photo_id):
    photo_details_url = reverse('photo-details', kwargs={
        'pk': photo_id
    })

    pyperclip.copy(request.META['HTTP_HOST'] + photo_details_url)

    return redirect(request.META['HTTP_REFERER'] + f'#{photo_id}')


@login_required
def add_comment(request, photo_id):
    if request.method == 'POST':
        photo = Photo.objects.filter(pk=photo_id).get()
        form = CommentForm(request.POST)

        if form.is_valid():
            comment = form.save(commit=False)
            comment.to_photo = photo
            comment.user = request.user
            comment.text = validate_dirty_words(comment.text)
            comment.save()

        return redirect(request.META['HTTP_REFERER'] + f'#{photo_id}')
    else:
        return redirect('index')


@login_required
def delete_comment(request, photo_id, comment_pk):
    photo = get_object_or_404(Photo, pk=photo_id)
    comment = Comment.objects.filter(to_photo=photo, pk=comment_pk)
    comment.delete()

    return redirect(request.META['HTTP_REFERER'] + f'#{photo_id}')


class AllUsersCBV(generic.ListView):
    template_name = 'common/users-list.html'
    model = UserModel
    paginate_by = 4

    def get_queryset(self):
        queryset = super().get_queryset()

        search = self.request.GET.get('search', '')
        queryset = queryset.filter(username__icontains=search).order_by('id')
        return queryset

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        context['search'] = self.request.GET.get('search', '')
        return context


class BandCalculator(generic.TemplateView):
    template_name = 'common/Band-calculator.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['video2'] = Video.objects.all()[1]
        return context


class ApneaTrainer(generic.TemplateView):
    template_name = 'common/apnea-trainer.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['video4'] = Video.objects.all()[3]
        return context


@login_required
def admin_panel(request):
    return HttpResponseRedirect(
        "http://127.0.0.1:8000/admin/"
    )
