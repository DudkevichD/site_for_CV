from django.views.generic import ListView, DetailView
from .models import Post, FeedbackModels
from .utils import MyMixin
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm, UserLoginForm, FeedbackForm
from django.contrib.auth import login, logout


class HomeView(ListView):
    model = Post
    context_object_name = 'posts'
    template_name = 'main_app/home_page.html'
    paginate_by = 4

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = self.__class__.__name__
        return context


class PostByCategory(MyMixin, ListView):
    paginate_by = 4

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = self.__class__.__name__
        return context

    def get_queryset(self):
        return Post.objects.filter(category__slug=self.kwargs['slug'])


class PostByTag(MyMixin, ListView):
    paginate_by = 4

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = self.__class__.__name__
        return context

    def get_queryset(self):
        return Post.objects.filter(tag__slug=self.kwargs['slug'])


class GetOnePost(MyMixin, DetailView):
    template_name = 'main_app/deep_page.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = self.__class__.__name__
        from django.db.models import F
        self.object.views = F('views') + 1
        self.object.save()
        self.object.refresh_from_db()
        return context


class Search(MyMixin, ListView):

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = self.__class__.__name__
        return context

    def get_queryset(self):
        return Post.objects.filter(title__icontains=self.request.GET.get('s'))


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Вы успешно зарегистрировались')
            return redirect('home')
        else:
            messages.error(request, 'Ошибка регистрации')
    else:
        form = UserRegisterForm()

    return render(request, 'main_app/register.html', {'form': form})


def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            print(request.user.is_authenticated)
            return redirect('home')
    else:
        form = UserLoginForm()
    return render(request, 'main_app/login.html', {'form': form})


def user_logout(request):
    logout(request)
    return redirect('login')


def feedback(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = FeedbackForm()
    return render(request, 'main_app/feedback.html', {'form':form})


