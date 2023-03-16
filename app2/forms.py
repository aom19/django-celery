from django import forms


class ReviewForm(forms.Form):
	name =  forms.CharField(
		label= 'Name',
		max_length= 100,
		widget= forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your name'})

	)
	email = forms.EmailField(
		label= 'Email',
		max_length= 100,
		widget= forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Enter your email'})
	)
	review = forms.CharField(
		label= 'Review',
		max_length= 100,
		widget= forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter your review'})
	)
	def send_email(self):
		# send email using the self.cleaned_data dictionary
		send_feedback_email_task.delay(self.cleaned_data['name'], self.cleaned_data['email'], self.cleaned_data[
			'review'])


