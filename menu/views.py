from django.views.generic import ListView, DetailView, TemplateView
from .models import *


class MainView(TemplateView):
    template_name = 'menu/index.html'


class MenuView(TemplateView):
    template_name = 'menu/menu.html'


class MenuView(ListView):
    model = Menu
    template_name = 'menu/show_menu.html'

    def get_user_context(self, **kwargs):
        menu = Menu.objects.all()
        context = kwargs

        context['menu'] = menu
        return context

    def get_context_data(self, *, object_list=None, **kwargs):
        print("MENUVIEW", self.kwargs)
        context = {
            'slug': self.kwargs['menu_slug']
        }
        return context


class CategoryView(DetailView):
    model = Category
    template_name = 'menu/category.html'
    slug_url_kwarg = 'category_slug'
    context_object_name = 'category'

    def get_user_context(self, **kwargs):
        context = kwargs
        menu = Menu.objects.filter(slug=self.kwargs['menu_slug'])
        print("CATVIEW", self.kwargs)
        context['menu'] = menu
        context['menu_slug'] = self.kwargs['menu_slug']
        return context

    def get_context_data(self, *, object_list=None, **kwargs):
        print("CATVIEW", self.kwargs)
        return dict(list(super().get_context_data(**kwargs).items()) + list(self.get_user_context().items()))
