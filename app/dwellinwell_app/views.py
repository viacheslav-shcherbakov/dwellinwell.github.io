from django.shortcuts import render

def show_name(request):
    name = 'mr.Anderson'

    context = {
        'name': name
    }
        
    return render(request=request, template_name='dwellinwell_app/index.html', context=context)