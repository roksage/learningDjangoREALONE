from django import forms


class ArticleForm(forms.Form):
    title = forms.CharField()
    content = forms.CharField()
    
    def clean_title(self):
        cleaned_data = self.cleaned_data

        title = cleaned_data.get('title')
        content = cleaned_data.get('content')
        
        return title
    
    def clean(self):
        cleaned_data = self.cleaned_data
        print(cleaned_data)
        return cleaned_data