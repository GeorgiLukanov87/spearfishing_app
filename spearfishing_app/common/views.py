import pyperclip
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import generic

from spearfishing_app.common.forms import CommentForm, SearchForm
from spearfishing_app.common.models import Like
from spearfishing_app.photos.models import Photo

UserModel = get_user_model()


# common/views.py

def index(request):
    all_photos = Photo.objects.all()
    comment_form = CommentForm()
    search_form = SearchForm()

    if request.method == 'POST':
        search_form = SearchForm(request.POST)
        if search_form.is_valid():
            all_photos = all_photos.filter(photo__icontains=search_form.cleaned_data['user_name'])

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

    return redirect(request.META['HTTP_REFERER'] + f'#{photo_id}')


def get_photo_url(request, photo_id):
    return request.META['HTTP_REFERER'] + f'#photo-{photo_id}'


def share(request, photo_id):
    photo_details_url = reverse('photo-details', kwargs={
        'pk': photo_id
    })
    pyperclip.copy(photo_details_url)
    return redirect(get_photo_url(request, photo_id))


@login_required
def add_comment(request, photo_id):
    if request.method == 'POST':
        photo = Photo.objects.filter(pk=photo_id).get()

        form = CommentForm(request.POST)

        if form.is_valid():
            comment = form.save(commit=False)
            comment.to_photo = photo
            comment.user = request.user
            comment.save()

        return redirect(
            request.META['HTTP_REFERER'] + f'#{photo_id}'
        )


@login_required
def redirect_to_index(request):
    return redirect('index')


class AllUsersCBV(generic.ListView):
    template_name = 'common/users-list.html'
    model = UserModel
    paginate_by = 5

    def get_queryset(self):
        queryset = super().get_queryset()

        search = self.request.GET.get('search', '')
        queryset = queryset.filter(username__icontains=search)
        return queryset

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['search'] = self.request.GET.get('search', '')
        return context
