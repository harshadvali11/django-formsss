from django import forms

value=[('Male','Male'),['Female',"female"]]

co=[['Python','Python'],['Django','Django'],('Sql',"SQL")]

#('Male','Male')=(data to be stored in Data base,Data to shown in Front end)

class New_Form(forms.Form):
    #name=forms.CharField(max_length=200,help_text='enter ur name',label_suffix='of student',required=True)
    #age=forms.IntegerField()
    #email=forms.EmailField()
    #url=forms.URLField()
    #date=forms.DateField()
    #datetime=forms.DateTimeField()
    #time=forms.TimeField()
    password=forms.CharField(max_length=50,widget=forms.PasswordInput)
    address=forms.CharField(max_length=200,widget=forms.Textarea(attrs={'cols':5,'rows':5}))
    gender=forms.ChoiceField(choices=value)# drop down list
    course=forms.MultipleChoiceField(choices=co)
    gender1=forms.ChoiceField(choices=value,widget=forms.RadioSelect)
    checkbox=forms.MultipleChoiceField(choices=co,widget=forms.CheckboxSelectMultiple)