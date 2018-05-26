from django import forms
from polls.models import *

class QuestionForm(forms.ModelForm):
	class Meta:
		model = Question
		fields = ['pub_date','question_text']
	def clean_question_text(self):
		que = self.cleaned_data['question_text']
		l=len(que)
		str = que.strip('')[l-1]
		#import pdb;pdb.set_trace()
		if str!='?':
			raise forms.ValidationError("You must enter '?'")
		return que

class NewForm(forms.Form):
	your_name = forms.CharField(label="Your_name",max_length=100,required=False)

	def clean_your_name(self):
		n = self.cleaned_data['your_name']
		l=len(n)
		if l<=2:
			raise forms.ValidationError("Your name is too short")
		return n
class RegForm(forms.ModelForm):
    class Meta:
        model = RegModel
        fields = ['user']

class AuthorForm(ModelForm):
	class Meta:
		model = Author
		field




