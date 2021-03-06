from django import forms

from apps.blog.models import Comment
from apps.onboarding.utils.xmodels import a


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        labels = {a(Comment.message): ""}
        widgets = {
            a(Comment.author): forms.HiddenInput,
            a(Comment.post): forms.HiddenInput,
            a(Comment.message): forms.Textarea(
                attrs={
                    "cols": 70,
                    "rows": 2,
                }
            ),
        }
        fields = [
            a(_f)
            for _f in (
                Comment.author,
                Comment.message,
                Comment.post,
            )
        ]
