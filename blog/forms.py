from django.forms import ModelForm
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset
from crispy_forms.bootstrap import *
from .models import Painel, Post

"""
    https://django-crispy-forms.readthedocs.io/en/latest/form_helper.html
    https://django-crispy-forms.readthedocs.io/en/latest/crispy_tag_forms.html
    https://django-crispy-forms.readthedocs.io/en/latest/layouts.html
    https://django-crispy-forms.readthedocs.io/en/latest/crispy_tag_formsets.html
    https://django-crispy-forms.readthedocs.io/en/latest/_modules/templatetags/crispy_forms_tags.html
    https://docs.djangoproject.com/en/1.8/_modules/django/forms/formsets/
    https://stackoverflow.com/questions/42481287/automatically-set-logged-in-user-as-the-author-in-django-using-createview-and-mo
    
    Examples of inlineformset_factory
    https://www.programcreek.com/python/example/54588/django.forms.models.inlineformset_factory
"""

class PainelForm(ModelForm):
    class Meta:
        model = Painel
        fields = ('hashtag', 'created_by', )

    @property
    def helper(self, *args, **kwargs):
        helper = FormHelper()
        helper.form_tag = False # This is crucial.
        helper.layout = Layout(
            Fieldset('Create New Post',
                    PrependedText('hashtag','#', placeholder="hashtag"),
                    ),
        )
        return helper

class PostFormHelper(FormHelper):
    def __init__(self, *args, **kwargs):
        super(PostFormHelper, self).__init__(*args, **kwargs)
        self.form_tag = False # This is crucial.
        self.render_required_fields = True
        self.layout = Layout(
            Fieldset("",
                    PrependedText('title','', placeholder="My Post"),
                    PrependedText('content_post','',placeholder="Descriptions"),
                    PrependedText('contact_number','', placeholder="countryCode + localCode + PhoneNumber"),
                    ),
        )

class HashtagForm(ModelForm):
    class Meta:
        model = Painel
        fields = ('hashtag',)
class PostForm(ModelForm): 
    class Meta:
        model = Post
        fields = ('author','painel','title','contact_number','content_post',)





