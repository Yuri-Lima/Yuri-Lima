from django.forms import ModelForm
from django.forms.models import inlineformset_factory

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, Submit
from crispy_forms.bootstrap import *
from django.http import request
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
            Fieldset("TestPaginations",
                    PrependedText('title','', placeholder="My Post"),
                    PrependedText('content','',placeholder="Descritions"),
                    PrependedText('url','', placeholder="www.example.com"),
                    
                    ),
        )

class HashtagForm(ModelForm): # Father
    class Meta:
        model = Painel
        fields = ('hashtag',)
class PostForm(ModelForm): # Son
    class Meta:
        model = Post
        fields = ('author','painel','title','content','url','contact_number',)





