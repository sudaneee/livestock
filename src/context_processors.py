from .models import *

def universal_data(request):
    
    return {
        'header_logo': Picture.objects.get(title='header-logo'),
        'logo': Picture.objects.get(title='logo'),
        'about': About.objects.first(),
        'news': News.objects.all(),
        'mandate': Paragraph.objects.get(title="Our Mandate"),
        'vision': Paragraph.objects.get(title="Our Vision"),
        'mission': Paragraph.objects.get(title="Our Mission"),
        'agencies': Agency.objects.all(),    
        }