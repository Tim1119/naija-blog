from django.forms import ModelForm
from .models import Comment


class CommentForm(ModelForm):

    class Meta:
        model = Comment
        exclude = ['article', 'author']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'


    # def validate_image(fieldfile_obj):
    #     filesize = fieldfile_obj.file.size
    #     megabyte_limit = 2.0
    #     if filesize > megabyte_limit*1024*1024:
    #         raise ValidationError("Max file size is %sMB" % str(megabyte_limit))