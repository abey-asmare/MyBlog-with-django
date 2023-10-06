from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from . import forms
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import Post, Comment
import os


# Create your views here.
class SignUpView(SuccessMessageMixin, CreateView):
    form_class = forms.SignUpForm
    success_url = reverse_lazy('blog:login')


class HomeView(ListView):
    model = Post


class PostDetailView(View):
    model = Post
    template_name=None

    def get(self, request, pk):
        post = get_object_or_404(self.model, pk=pk)
        form = forms.CommentForm()
        context = {'post':post,
                   'form':form}
        return render(request, self.template_name, context)

    def post(self, request, pk):
        post = get_object_or_404(self.model, pk=pk)
        form = forms.CommentForm(request.POST)
        if form.is_valid():
            form.instance.owner = request.user
            form = form.save()
            post.comment.add(form)
            # alternative way
            # comment = form.save(commit=False)
            # comment.owner = request.user
            # comment.post = post
            # comment.save()
            return redirect('blog:post_detail', pk=pk)
        context = {'post': post,
                   'form': form}
        return render(request, self.template_name, context)


class EditPostView(UserPassesTestMixin, UpdateView):
    model = Post
    form_class = forms.CreateUpdatePost
    template_name = None

    def test_func(self):
        post = self.get_object()
        return True if post.author == self.request.user else False


class DeletePostView(UserPassesTestMixin, DeleteView):
    model = Post
    success_url = reverse_lazy('blog:homes')
    def test_func(self):
        post = self.get_object()
        return True if post.author == self.request.user else False


class CreatePostView(LoginRequiredMixin, CreateView):
    form_class = forms.CreateUpdatePost
    model = Post

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class ContactView(LoginRequiredMixin, ListView):
    def get(self, req):
        return render(req, 'home/contact.html')
