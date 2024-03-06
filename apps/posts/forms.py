from .models import Article
from django.forms import ModelForm


class ArticleForm(ModelForm):
    error_class = 'error'

    class Meta:
        model = Article
        exclude = ['author', 'approved', 'likes']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'
