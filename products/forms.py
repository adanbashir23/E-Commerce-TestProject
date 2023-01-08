"""Product forms"""
from crispy_forms.bootstrap import Field
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Div, Fieldset, Layout, Submit
from django import forms

from .models import Comment


class CommentForm(forms.ModelForm):
    """Enable users to leave comments for products"""

    class Meta:
        """Meta for CommentForm"""

        model = Comment
        fields = ["comment"]
        widgets = {
            "message": forms.TextInput(
                attrs={id: "comment-text", "rows": 4, "cols": 15}
            ),
        }

    def __init__(self, *args, **kwargs):
        super(CommentForm, self).__init__(*args, **kwargs)
        # create form structure using crispy forms
        self.helper = FormHelper()
        self.helper.form_action = "create_comment"
        self.helper.form_id = "product-review-form"
        self.helper.form_method = "POST"
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
                "Add a product review",
                Div(
                    Field(
                        "comment",
                        wrapper_class="col-12 col-md-10",
                        rows=5,
                        placeholder="Add your review here",
                    ),
                    css_class="row",
                ),
            )
        )
