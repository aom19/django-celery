from django.shortcuts import render

# Create your views here.
from app2.forms import ReviewForm
from django.views.generic.edit import FormView
from django.http import HttpResponse

class ReviewFormView(FormView):
	template_name = 'review.html'
	form_class = ReviewForm

	def form_valid(self, form):
		form.send_email()
		msg = 'Thank you for your review'
		return HttpResponse(msg)



