from django.contrib.auth.views import LoginView as DjangoLoginView
from django.contrib.auth.views import LoginView as DjangoLogoutView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import LoginForm

class LoginView(DjangoLoginView):
    redirect_authenticated_user = True
    template_name = 'login.html'
    form_class = LoginForm

    def get_success_url(self):
        return reverse_lazy('home')
    
    def form_invalid(self, form):
        messages.error(self.request,'Usuario o contraseña incorrectos')
        return self.render_to_response(self.get_context_data(form=form))

class LogoutView(DjangoLogoutView):
    template_name = 'login.html'
    next_page = 'home'
    form_class = LoginForm
    def form_invalid(self, form):
        messages.error(self.request,'Usuario o contraseña incorrectos')
        return self.render_to_response(self.get_context_data(form=form))
