from django.views.generic import TemplateView
from shop import models


class ListView(TemplateView):
    template_name = 'shop/list.tpl'
    model = None
    key = None

    def get_list(self, object_id=None):
        if not object_id:
            return self.model.objects.all()
        return self.model.objects.filter(**{self.key: object_id}).all()
        

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['objects'] = self.get_list(kwargs.get('object_id', None))
        context['route'] = self.model.__name__.lower()

        return context


class IndexView(ListView):
    model = models.Category
    

class CategoryView(ListView):
    model = models.Item
    key = 'category_id'


class ItemView(TemplateView):
    template_name = 'shop/item.tpl'

    def get_context_data(self, object_id, **kwargs):
        context = super().get_context_data(**kwargs)
        context['item'] = models.Item.objects.get(id=object_id)

        return context