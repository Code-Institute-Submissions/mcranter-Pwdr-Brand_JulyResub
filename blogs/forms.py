from django import forms
from .models import Post


class PostForm(forms.ModelForm):
    """
    Create a form for users to add reviews
    """

    class Meta:
        model = Post
        exclude = (
            "slug",
            "updated_on",
            "created",
            "status",
        )

    def __init__(self, *args, **kwargs):
        """
        Add placeholders for the review form
        """
        super().__init__(*args, **kwargs)
