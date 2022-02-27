from django.shortcuts import render

# Create your views here.

class Queue:
  def __init__(self, customer_name, model, serial,):
    self.customer_name = customer_name
    self.model = model
    self.serial = serial


queue_list = [
Queue('Samantha', 'FX 7.1 Gravel', 'WTU3459CJO9'),
Queue('Brandon', 'Vintage Fuji', 'FUJ124JLJ'),
Queue('Ashley', 'REI Road', 'SJXK123DFA')
]

def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def queue_index(request):
  return render(request, 'queue/index.html', { 'queue_list': queue_list })