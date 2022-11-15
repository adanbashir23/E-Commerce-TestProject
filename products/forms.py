from .models import Comment
from django import forms

from crispy_forms.bootstrap import Field
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Div, Fieldset, Layout


class CommentForm(forms.ModelForm):
    """Enable users to leave comments for products"""

    class Meta:
        model = Comment
        fields = ['comment']

    def __init__(self, *args, **kwargs):
        super(CommentForm, self).__init__(*args, **kwargs)
        # create form structure using crispy forms
        self.helper = FormHelper()
        self.helper.form_id = "product-comment-form"
        self.helper.form_method = "post"
        self.helper.form_class = "mt-4"
        self.helper.add_input(
            Submit(
                "submit",
                "Add Comment",
                css_class="btn btn-primary \
            float-right",
            )
        )
        self.helper.layout = Layout(
            Fieldset(
                "Add a comemmt",
                Div(
                    Field(
                        "comment",
                        wrapper_class="col-12 col-md-10",
                        rows=5,
                        placeholder="Add your comment here",
                    ),
                    css_class="row",
                ),
            )
        )
