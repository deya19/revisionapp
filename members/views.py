from django.http import HttpResponse
from django.template import loader
from .models import Member


def members(request):
  template = loader.get_template('myFirst.html')
  return HttpResponse(template.render())



def allMembers(request):
  myMembers = Member.objects.all().values()
  template = loader.get_template('all_members.html')
  context = {
    'myMembers': myMembers,
  }
  return HttpResponse(template.render(context, request))



def details(request, slug):
  myMember = Member.objects.get(slug=slug)
  template = loader.get_template('details.html')
  context = {
    'myMember': myMember,
  }
  return HttpResponse(template.render(context, request))


def main(request):
  template = loader.get_template('main.html')
  return HttpResponse(template.render())



# def testing(request):
#     myData = Member.objects.values_list('firstname')
#     # Iterate over the QuerySet and extract the first element of each tuple
#     myMembers = [firstname for (firstname,) in myData]
#     template = loader.get_template('template.html')
#     context = {
#         'myMembers': myMembers,
#     }
#     return HttpResponse(template.render(context, request))



def testing(request):
  template = loader.get_template('template.html')
  context = {
    'fruits': ['Apple', 'Banana', 'Cherry'],   
  }
  return HttpResponse(template.render(context, request))            