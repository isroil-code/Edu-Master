from django import forms
from courses.models import Comment, CommentLike,Like

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('comment',)
        
        