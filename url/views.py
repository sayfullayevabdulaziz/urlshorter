import random
from django.http import HttpResponse
from django.shortcuts import redirect, render, get_object_or_404

from .forms import UrlForm, UrlCounterForm, ReportForm, ContactForm
from .models import ContactModel, UrlModel, ReportLinkModel
from .utils import generate_token
# Create your views here.

def indexView(request):
    forms = UrlForm(request.POST or None)
    if request.method == 'POST':
        if forms.is_valid(): 
            url = forms.cleaned_data['url']
            slug = generate_token()
            urlset = UrlModel()
            urlset.url = url
            urlset.slug = slug
            urlset.save()
            shortener = "localhost:8000/" + slug
            return render(request,'shortener.html',{'old_url':url,'new_url':shortener})
        return render(request,'url-error.html',{})
    return render(request,'index.html',{})


def shortToOriginal(request, slug):
    slugs = get_object_or_404(UrlModel, slug=slug)
    url = slugs.url
    slugs.counter +=1
    slugs.save()
    return redirect(url, status=301)


def urlcounter(request):
    form = UrlCounterForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            try:
                slug = form.cleaned_data['url'][15:]
                all_slug = UrlModel.objects.get(slug=slug)
                counter = all_slug.counter
                return render(request, 'url-total-clicks.html', {'counter':counter})
            except UrlModel.DoesNotExist:
                return HttpResponse('Url is incorrect')
    print(dir(request))
    return render(request, 'url-click-counter.html', {'form':form})

def terms_service(request):
    return render(request, 'terms-of-service.html',{})

def privacy_policy(request):
    return render(request, 'privacy-policy.html',{})

val = {'a':0, 'b':0}

def report(request):
    global val
    form = ReportForm(request.POST or None)
    val1 = val
    if request.method == "POST":
        if form.is_valid():
            print(val1)
            url = form.cleaned_data['url']
            comment = form.cleaned_data['comment']
            summa = int(form.cleaned_data['result'])
            # print(val1.get('a') , val1.get('b'))
            if (val1.get('a') + val1.get('b')) == summa:
                report = ReportLinkModel()
                report.url = url
                report.comment = comment
                report.save()
                return render(request, 'sender.html')
        return render(request, 'failed.html')
    
    val['a'] = random.randint(1,9)
    val['b'] = random.randint(1,9)
    return render(request, 'report.html', {'a':val.get('a'), 'b':val.get('b'), 'form':form})

val2 = {'a':0, 'b':0}
def contact_view(request):
    global val2
    form = ContactForm(request.POST or None)
    val1 = val2
    if request.method == 'POST':
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            summa = int(form.cleaned_data['result'])
            print(message)
            if (val1.get('a') + val1.get('b')) == summa:
                report = ContactModel()
                report.name = name
                report.email = email
                report.message = message
                report.save()
                return render(request, 'sender.html')
        return render(request, 'failed.html')
    val2['a'] = random.randint(1,9)
    val2['b'] = random.randint(1,9)
    return render(request, 'contact.html', {'a':val2.get('a'), 'b':val2.get('b'), 'form':form})