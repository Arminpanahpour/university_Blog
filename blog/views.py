from django.http import HttpResponseRedirect, HttpRequest
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from .models import Post, Category
from comment.models import Comment
from .forms import AddPostForm, EditPostForm, AddCommentForm, AddCategoryForm


def LikeView(request, pk):
    post = get_object_or_404(Post, id=request.POST.get('post_id'))
    liked = False
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
        liked = False
    else:
        post.likes.add(request.user)
        liked = True
    return HttpResponseRedirect(reverse('detail-post', args=[post.slug]))


class HomeView(ListView):
    model = Post
    template_name = 'blog/index.html'
    ordering = ['-post_date']

    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all()
        context = super(HomeView, self).get_context_data(*args, **kwargs)
        context['cat_menu'] = cat_menu
        return context


def CategoryView(request, cats):
    post_category = Post.objects.filter(category=cats)
    cat_menu = Category.objects.all()
    return render(request, 'blog/category.html', {'cats': cats, 'post_category': post_category, 'cat_menu': cat_menu})


class AddCategoryView(CreateView):
    model = Category
    form_class = AddCategoryForm
    template_name = 'blog/add_category.html'


class DetailPostView(DetailView):
    model = Post
    template_name = 'blog/detail_post.html'

    def get_context_data(self, *args, **kwargs):
        instance = get_object_or_404(Post, slug=self.kwargs['slug'])
        cat_menu = Category.objects.all()
        comment = instance.comments
        post_order = Post.objects.all().order_by('-post_date')[:3]
        context = super(DetailPostView, self).get_context_data(**kwargs)
        total_likes = instance.total_likes()
        liked = False
        if instance.likes.filter(id=self.request.user.id).exists():
            liked = True
        context['post_order'] = post_order
        context['total_likes'] = total_likes
        context['cat_menu'] = cat_menu
        context['liked'] = liked
        context['comment'] = comment
        return context


class AddPostView(CreateView):
    model = Post
    form_class = AddPostForm
    template_name = 'blog/add_post.html'


class AddCommentView(CreateView):
    model = Comment
    form_class = AddCommentForm
    template_name = 'blog/add_comment.html'

    def form_valid(self, form):
        form.instance.post_id = self.kwargs['pk']
        return super().form_valid(form)

    success_url = reverse_lazy('home')


class EditPostView(UpdateView):
    model = Post
    form_class = EditPostForm
    template_name = 'blog/edit_post.html'


class DeletePostView(DeleteView):
    model = Post
    template_name = 'blog/delete_post.html'
    success_url = reverse_lazy('home')
