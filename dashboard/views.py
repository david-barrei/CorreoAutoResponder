from django.shortcuts import render, redirect
from django.views.generic import View,TemplateView
from newsletters.models import Newsletter
from newsletters.forms import NewsletterCreationForm
from django.conf import settings
from django.core.mail import send_mail, EmailMultiAlternatives, EmailMessage

# Create your views here.

class DashboardHomeView(TemplateView):
    template_name = 'dashboard/index.html'


class NewslettersDashboardHomeView(View):
     def get(self, rquest, *args, **kwargs):
          newsletters = Newsletter.objects.all()
          context= {
               'newsletters':newsletters

          }
          return render(self.request, 'dashboard/list.html', context)

class NewslettersCreateView(View):
     def get(self, request, *args, **kwargs):
          form = NewsletterCreationForm()
          context = {
               'form':form,
          }
          return render(request, 'dashboard/created.html', context)
     
     def post(self, request, *args, **kwargs):

          if request.method=='POST':
               form = NewsletterCreationForm(request.POST or None)
               if form.is_valid():
                    instance=form.save()
                    newsletter=Newsletter.objects.get(id=instance.id)
                    
                    if newsletter.status=='Published':
                         subject = newsletter.subject
                         body = newsletter.body
                         from_email = settings.EMAIL_HOST_USER
                         for email in newsletter.email.all():
                              send_mail(subject=subject, from_email=from_email, recipient_list=[email], message=body ,fail_silently=True)
               
                    return redirect ('dashboard:list')


          context = {
                'form':form,
          }
          return render(request, 'dashboard/created.html', context)