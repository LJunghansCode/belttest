from __future__ import unicode_literals

from django.db import models
from ..login_reg_app.models import User
from datetime import datetime

# Create your models here.

class AppointmentManager(models.Manager):
	def create_appointment(self, data):
		errors = []
		date = datetime.strptime(data['date'],'%Y-%m-%d')
		time = datetime.strptime(data['time'], '%H:%M')
		print (date.date())
		print (time.time())

		current_datetime = datetime.now()
		current_date = current_datetime.date()
		current_time = current_datetime.time()
		print(current_time)
		print(current_date)

		if not data['date'] or not data['time'] or not data['task']:
			errors.append('Please enter something')
		if date.date() < current_date and time.time() < current_time:
			errors.append('Future please')
		if date.date() == current_date and time.time() < current_time:
			errors.append('You must be effecint! Sorry we already went past then.')

		response = {}

		if not errors:
			user = User.objects.filter(id = data['user'])
			new_appointment = self.create(task = data['task'], user = user[0], date=data['date'], time=data['time'])
			response["added"] = True
			response["new_appointment"] = new_appointment
		else:
			response["added"] = False
			response["errors"] = errors
		return response
		




	def delete_appointment(self, data):
		
		response = {}
		self.filter(id = data['getting_deleted']).delete()
		response["deleted"] = True
		return response


	def edit_appointment(self, data):
		
		response = {}
		if data["task"]:
			self.filter(id = data['getting_edited']).update(task = data["task"])
		if data["date"]:
			self.filter(id = data['getting_edited']).update(date = data["date"])
		if data["time"]:
			self.filter(id = data['getting_edited']).update(time = data["time"])
		if data["status"]:
			self.filter(id = data['getting_edited']).update(status = data["status"])


		response["edited"] = True
		return response





		





class Appointment(models.Model):
	task = models.CharField(max_length=500)
	user = models.ForeignKey(User, related_name = "appointments")
	status = models.CharField(max_length=30, default = "Pending")
	date = models.DateField(max_length=45)
	time = models.TimeField(max_length=45)

	objects = AppointmentManager()






