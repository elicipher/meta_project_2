from django.shortcuts import render , redirect , get_object_or_404
from django.views import View
from home.models import AboutUs , Service , StatsSection , Portfolio  ,Category ,  TeamMember , Contact
from django.views.generic import CreateView , DeleteView , ListView , UpdateView 
from django.urls import reverse_lazy
from .mixins import CancelUrlMixin , SuperUserOnlyMixin , DeleteSuccessMessageMixin , SuccessMessageMixin
from .forms import SocialLinkFormSet , PortfolioForm , SocialTeamMemberFormset , ContactForm , PostForm , CommentReplyForm , CommentConfirmeForm
from django.conf import settings
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from blog.models import Post  , Comment
from django.contrib import messages

# Create your views here.


class DashboardView(View):

    def get(self , request):
        return render(request , 'dashboard.html')
    
#AboutUs  ----------------------------------
class AboutUsUpdateView(UpdateView , SuccessMessageMixin ):
    model = AboutUs
    fields = '__all__'
    template_name = 'home-dashboard/aboutus_edit.html'
    success_url = reverse_lazy('dashboard:edit_about')

    def get_object(self, queryset=None):
        # همیشه فقط یک شیء رو برمی‌گردونه
        return AboutUs.objects.first()
    
    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form()
        formset = SocialLinkFormSet(instance=self.object)
        return render(request, self.template_name, {'form': form, 'formset': formset})
    
    def post(self , request , *args , **kwargs):
        self.object = self.get_object()
        form = self.get_form()
        formset = SocialLinkFormSet(request.POST,instance=self.object)
        if form.is_valid() and formset.is_valid():
            form.save()
            formset.save()
            return redirect(self.success_url)
        return render(request, self.template_name, {'form': form, 'formset': formset})
    


#Service  ------------------------------

class ServiceListView(ListView):
    model = Service
    template_name = 'home-dashboard/service_list.html'
    context_object_name = 'services'


class ServiceDeleteView(DeleteSuccessMessageMixin , DeleteView , CancelUrlMixin  ):
    model = Service
    template_name = 'shared/delete.html'
    success_url = reverse_lazy("dashboard:service_list")

  

class ServiceCreateView(SuccessMessageMixin ,CreateView):
    model = Service
    fields = '__all__'
    template_name = 'shared/create.html'
    success_url = reverse_lazy("dashboard:service_list")
    action = 'create'


 

class ServiceUpdateView(SuccessMessageMixin , UpdateView ):
    model = Service
    fields = '__all__'
    template_name = 'shared/update.html'
    success_url = reverse_lazy("dashboard:service_list")
    action = 'update'


#StatsSection  ----------------------------------
class StatsSectionListView(ListView):
    model = StatsSection
    template_name = 'home-dashboard/stats_list.html'
    context_object_name = 'statss'


class StatsSectionDeleteView(DeleteSuccessMessageMixin ,DeleteView , CancelUrlMixin ):
    model = StatsSection
    template_name = 'shared/delete.html'
    success_url = reverse_lazy("dashboard:stats_list")
  

class StatsSectionCreateView(SuccessMessageMixin , CreateView):
    action = 'create'
    model = StatsSection
    fields = '__all__'
    template_name = 'shared/create.html'
    success_url = reverse_lazy("dashboard:stats_list")

 

class StatsSectionUpdateView(SuccessMessageMixin ,UpdateView ):
    action = 'update'
    model = StatsSection
    fields = '__all__'
    template_name = 'shared/update.html'
    success_url = reverse_lazy("dashboard:stats_list")

#Portfolio  ----------------------------------
class PortfolioListView(ListView):
    model = Portfolio
    template_name = 'home-dashboard/portfolio_list.html'
    context_object_name = 'portfolios'

class PortfolioDeleteView(DeleteSuccessMessageMixin ,DeleteView , CancelUrlMixin ):
    model = Portfolio
    template_name = 'shared/delete.html'
    success_url = reverse_lazy("dashboard:portfolio_list")

class PortfolioCreateView(SuccessMessageMixin,CreateView):
    action = 'create'
    model = Portfolio
    form_class = PortfolioForm
    template_name = 'shared/create.html'
    success_url = reverse_lazy("dashboard:portfolio_list")

class PortfolioUpdateView(SuccessMessageMixin,UpdateView ):
    action = 'update'
    model = Portfolio
    form_class = PortfolioForm
    template_name = 'shared/update.html'
    success_url = reverse_lazy("dashboard:portfolio_list")

# Category Portfolio  ------------------------------
class PortfolioCategoryListView(ListView):
    model = Category
    template_name = 'home-dashboard/portfolio_category_list.html'
    context_object_name = 'categories'

class PortfolioCategoryDeleteView(DeleteSuccessMessageMixin,DeleteView , CancelUrlMixin ):
    model = Category
    template_name = 'shared/delete.html'
    success_url = reverse_lazy("dashboard:portfolio_category_list")

class PortfolioCategoryCreateView(SuccessMessageMixin,CreateView):
    action = 'create'
    model = Category
    fields = '__all__'
    template_name = 'shared/create.html'
    success_url = reverse_lazy("dashboard:portfolio_category_list")

class PortfolioCategoryUpdateView(SuccessMessageMixin,UpdateView ):
    action = 'update'
    model = Category
    fields = '__all__'
    template_name = 'shared/update.html'
    success_url = reverse_lazy("dashboard:portfolio_category_list")

# Team  ------------------------------

class TeamMemberListView(ListView , SuperUserOnlyMixin ):
    model = TeamMember
    template_name = 'home-dashboard/team_member/team_list.html'
    context_object_name = 'teams'

class TeamMemberDeleteView(DeleteSuccessMessageMixin,DeleteView , CancelUrlMixin , SuperUserOnlyMixin):
    model = TeamMember
    template_name = 'shared/delete.html'
    success_url = reverse_lazy("dashboard:team_list")

class TeamMemberCreateView(SuccessMessageMixin,CreateView , SuperUserOnlyMixin):
    model = TeamMember
    fields = '__all__'
    template_name = 'home-dashboard/team_member/team_create.html'
    success_url = reverse_lazy("dashboard:team_list")

    def get(self, request, *args, **kwargs):
        form = self.get_form()
        formset = SocialTeamMemberFormset()
        return render(request, self.template_name, {'form': form, 'formset': formset})

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        formset = SocialTeamMemberFormset(request.POST)
        if form.is_valid() and formset.is_valid():
            team_member = form.save()
            formset.instance = team_member
            formset.save()
            return redirect(self.success_url)
        return render(request, self.template_name, {'form': form, 'formset': formset})

class TeamMemberUpdateView(SuccessMessageMixin,UpdateView , SuperUserOnlyMixin ):
    model = TeamMember
    fields = '__all__'
    template_name = 'home-dashboard/team_member/team_update.html'
    success_url = reverse_lazy("dashboard:team_list")

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form()
        formset = SocialTeamMemberFormset(instance=self.object)
        return render(request, self.template_name, {'form': form, 'formset': formset})
    
    def post(self , request , *args , **kwargs):
        self.object = self.get_object()
        form = self.get_form()
        formset = SocialTeamMemberFormset(request.POST,instance=self.object)
        if form.is_valid() and formset.is_valid():
            form.save()
            formset.save()
            return redirect(self.success_url)
        return render(request, self.template_name, {'form': form, 'formset': formset})

# Contact  ------------------------------

class ContactListView(ListView):
    model = Contact
    template_name = 'home-dashboard/contact/contact_list.html'
    context_object_name = 'contacts'

class ContactDeleteView(DeleteSuccessMessageMixin,DeleteView , CancelUrlMixin ):
    model = Contact
    template_name = 'shared/delete.html'
    success_url = reverse_lazy("dashboard:contact_list")

class ContactReplyView(UpdateView ):
    model = Contact
    form_class = ContactForm
    template_name = 'home-dashboard/contact/contact_reply.html'
    success_url = reverse_lazy("dashboard:contact_list")

    def form_valid(self , form):
        obj = form.save(commit=False)
        if 'reply' in form.changed_data and obj.reply :
            obj.is_replied = True
            self.send_mail_to_user(obj)
        obj.save()
        return super().form_valid(form)

    def send_mail_to_user(request , contact):
    
        context = {
            'user_message': contact.message,
            'admin_response': contact.reply,

        }
        subject = 'پاسخ به پیام شما'
        from_email = settings.EMAIL_HOST_USER
        to_email = contact.email
        html_message = render_to_string('home-dashboard/contact/reply_email.html',context)
        plain_message = strip_tags(html_message)

        send_mail(subject ,plain_message, from_email , [to_email] ,html_message=html_message)

# Post --------------------------------------

class PostListView(ListView):
    model = Post
    template_name = 'blog-dashboard/post_list.html'
    context_object_name = 'posts'
    
class PostCreateView(SuccessMessageMixin,CreateView):
    model = Post
    form_class = PostForm
    template_name = 'shared/create.html'
    success_url = reverse_lazy("dashboard:post_list")


class PostDeleteView(DeleteSuccessMessageMixin,DeleteView):
    model = Post
    template_name = 'shared/delete.html'
    success_url = reverse_lazy("dashboard:post_list")

class PostUpdateView(SuccessMessageMixin,UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'shared/update.html'
    success_url = reverse_lazy("dashboard:post_list")

# Comments --------------------------------------------

class CommentListView(ListView):
    model = Comment
    template_name = 'blog-dashboard/comment_list.html'
    context_object_name = 'comments'

class CommentDeleteView(DeleteSuccessMessageMixin,DeleteView):
    model = Comment
    template_name = 'shared/delete.html'
    success_url = reverse_lazy("dashboard:comment_list")

class CommentReplyView(View):
    template_name = 'blog-dashboard/comment_reply.html'
    def get(self , request ,comment_id ):
        comment = get_object_or_404(Comment , pk = comment_id)
        form = CommentReplyForm
        return render(request , self.template_name , {'form':form , 'comment':comment})
    def post(self, request, comment_id):
        parent = get_object_or_404(Comment, id=comment_id)
        post = parent.post
        form = CommentReplyForm(request.POST)
        if form.is_valid():
            reply = form.save(commit=False)
            reply.user = request.user
            reply.post = post
            reply.is_reply = True
            reply.save()
            messages.success(request, "پاسخ با موفقیت ثبت شد 🌱")
            return redirect('dashboard:comment_list')  # یا هر صفحه‌ای که لیست کامنت‌هاست
        return render(request, self.template_name , {'form': form, 'comment': parent})

class CommentDetailView(View):
    template_name = 'blog-dashboard/comment_detail.html'
    form_class = CommentConfirmeForm
    def get(self , request , comment_id):
        comment = get_object_or_404(Comment , pk = comment_id)
        form = self.form_class(instance=comment)
        return render(request , self.template_name , {"form":form,"comment":comment})

    def post(self , request , comment_id = None):
        comment = get_object_or_404(Comment, pk=comment_id)
        form = self.form_class(request.POST , instance=comment)
        if form.is_valid():
            form.save()
            comment.save()
            messages.success(request , "نظر با موفقیت تایید شد", "success")
            return redirect("dashboard:comment_list")
        return render(request , self.template_name , {"form":form,"comment":comment})

