from django.views.generic.base import ContextMixin
from django.contrib.auth.mixins import UserPassesTestMixin
from django.contrib import messages

class CancelUrlMixin(ContextMixin):
    success_url = None  # باید هر ویو خودش داشته باشه

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cancel_url'] = self.get_success_url()
        return context

class SuperUserOnlyMixin(UserPassesTestMixin):
    def test_func(self):
        return self.request.user.is_superuser
    
class SuccessMessageMixin:
    action = None

    def form_valid(self, form):
  
        if self.action == 'create':
            messages.success(self.request, f"با موفقیت ایجاد شد 🌱")
        elif self.action == 'update':
            object_display = str(self.get_object())
            messages.success(self.request, f"{object_display} با موفقیت ویرایش شد 🌱")
        return super().form_valid(form)
    
class DeleteSuccessMessageMixin:

    def delete(self, request, *args, **kwargs):
        object_display = str(self.get_object())  
        messages.success(self.request, f"{object_display} با موفقیت حذف شد 🌱")
        return super().delete(request, *args, **kwargs)