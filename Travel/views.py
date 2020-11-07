from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from .forms import ContactForm
from .models import Destination
from django.views.generic import TemplateView, ListView, DetailView, FormView



# Create your views here.
class HomepageView(ListView):
    model = Destination
    template_name = "Travel/homepage.html"


class AboutView(TemplateView):
    template_name = "Travel/about.html"


########################################################################################

# def descriptionView(request, name):
#     destination = get_object_or_404(Destination, name=name)
#     context = {'destination': destination}
#     return render(request, 'Travel/destination_detail.html', context)


class DescriptionView(DetailView):
    model = Destination

    def get_object(self):
        return get_object_or_404(Destination, name=self.kwargs['name'])

##########################################################################################


class ContactView(FormView):
    template_name = "Travel/contact.html"
    form_class = ContactForm
    success_url = '/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        content = messages.info(self.request, 'We will contact you! Thankyou for your time')
        context['message'] = content
        return context
