from django import forms

class DownloadVideoForm(forms.Form):
    link = forms.URLField(
        widget=forms.TextInput(attrs={'class': 'm-auto w-full h-auto rounded p-2 text-black break-words', 'id':'link'}))
    
    video = forms.BooleanField(label='video', required=False, initial=True, widget=forms.CheckboxInput(attrs={'class': 'm-auto rounded w-5 h-5 ', 'id':'video'}))

    audio = forms.BooleanField(label='audio', required=False, widget=forms.CheckboxInput(attrs={'class': 'm-auto rounded w-5 h-5', 'id':'audio'}))
