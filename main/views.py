from django.shortcuts import render, redirect
from django.template import Context, Template
from django.contrib.auth import logout as auth_logout

# Create your views here.
def index(request):
    if not request.user.is_authenticated:
        url = Template("{% url 'social:begin' 'google-oauth2' %}")
        return redirect(str(url.render(Context({}))))

    return render(request, template_name='index.html')

def logout(request):
    auth_logout(request)
    return render(request, 'logout.html')

