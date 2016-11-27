from django.shortcuts import render, redirect, reverse
from datetime import datetime, time, date
from .models import Appointment
from django.contrib import messages

# Create your views here.

def home(request):
	if 'user' not in request.session:
		return redirect(reverse('index'))

	user = request.session['user']['id']
	my_apts = Appointment.objects.filter(user = user)
	future_apts = Appointment.objects.filter(id = user)
	current_datetime = datetime.now()
	current_date = current_datetime.date()
	print(my_apts)
	context = {
		'appointments' : my_apts.order_by('date'),
		'future_appointments': my_apts.filter(date__gt = current_datetime)
	}


	return render(request, 'main/home.html', context)

###CREATEAPPOINTMENT###
def create(request):
	response = Appointment.objects.create_appointment(request.POST)
	if response["added"]:
		messages.success(request, 'Added new Appointment')
		return redirect(reverse('home'))
	else:
		for error in response['errors']:
			messages.error(request, error)
			return redirect(reverse('home'))
##DELAPPOINTMENT##
def delete_appointment(request):
	response = Appointment.objects.delete_appointment(request.POST)
	if response["deleted"]:
		messages.success(request, 'Deleted!')
		return redirect(reverse('home'))

##EDITSCREEN##
def edit(request, apt_id):
	request.session['current_edit'] = {
        'id' : request.POST['getting_edited']
       
    }
	return render(request, 'main/edit.html')


###EDITAPPOINTMENT###
def edit_appointment(request):
	response = Appointment.objects.edit_appointment(request.POST)
	if response["edited"]:
		messages.success(request, 'Edited!')
		return redirect(reverse('home'))
	else:
		return redirect(reverse('edit'))


	







	





####ERRORMESSAGES####
def print_messages(request, message_list):
    for message in message_list:
        messages.add_message(request, messages.INFO, message)


