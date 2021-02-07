from django.forms import ModelForm
from django.forms.models import inlineformset_factory

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset
from .models import Painel, Post

class PainelForm(ModelForm):
    class Meta:
        model = Painel
        fields = ('hashtag', 'created_by', )

    @property
    def helper(self):
        helper = FormHelper()
        helper.form_tag = False # This is crucial.

        helper.layout = Layout(
            Fieldset('Create new Painel', 'hashtag'),
        )

        return helper


class PostFormHelper(FormHelper):
    def __init__(self, *args, **kwargs):
        super(PostFormHelper, self).__init__(*args, **kwargs)
        self.form_tag = False
        self.layout = Layout(
            Fieldset("Add Post",'title','content', 'url',),
            # Fieldset("Add Right Post", 'title','content', 'url',),
        )


CombinedFormSet = inlineformset_factory(
    Painel,
    Post,
    fields=('title','content', 'url', 'contact_number','author', 'painel', ), 
    extra=1,
    can_delete=False,
    max_num=1,
    validate_max= 1,
)




from django import forms
class HashtagForm(forms.ModelForm): # Father
    class Meta:
        model = Painel
        fields = ('hashtag',)

class PostForm(forms.ModelForm): # Son
    class Meta:
        model = Post
        fields = ('painel','title','content','url','contact_number',)