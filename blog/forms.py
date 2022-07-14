from django import forms
from .models import Post, Category
from comment.models import Comment

# choices = Category.objects.all().values_list('name','name')
# choice_list = []
#
# for item in choices:
#     choice_list.append(item)


class AddPostForm(forms.ModelForm):
    category = forms.ModelChoiceField(queryset=Category.objects.all() ,to_field_name = 'name',
                                    empty_label="Select Category")

    class Meta:
        model = Post
        fields = ('title', 'author', 'slug', 'category', 'body', 'header_image')

        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'large-input',
                'name': 'name',
                # 'placeholder': 'Title',
                'required': ''
            }),
            'slug': forms.TextInput(attrs={
                'class': 'large-input',
                'name': 'name',
                # 'placeholder': 'Title',
                'type': 'hidden',
                'required': ''
            }),
            'author': forms.TextInput(attrs={
                'class': 'large-input',
                'name': 'name',
                'value': '',
                'id': 'admin',
                'type': 'hidden',
                'required': ''
            }),
            'category': forms.Select(attrs={
                'class': 'large-input',
                'name': 'name',
                # 'placeholder': 'category',
                'required': ''
            }),

            'body': forms.Textarea(attrs={
                'class': 'large-input',
                'name': 'comment',
                'rows': "5",
                'placeholder': 'Enter Your Post...',
            }),
        }

    def __init__(self, *args, **kwargs):
        super(AddPostForm, self).__init__(*args, **kwargs)

        self.fields['category'].widget.attrs['class'] = 'large-input'


class EditPostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'body')

        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'large-input',
                'name': 'name',
                'placeholder': 'Title',
                'required': ''
            }),
            'body': forms.Textarea(attrs={
                'class': 'large-input',
                'name': 'comment',
                'rows': "8",
                'placeholder': 'Enter Your Post...',
            }),
        }


class AddCategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ("name",)

        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'large-input',
                'name': 'name',
                'placeholder': 'Enter Your Category',
                'required': ''
            }),

        }




class AddCommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('creator', 'name', 'body')

        widgets = {

            'name': forms.TextInput(attrs={
                'class': 'medium-input border-radius-4px bg-white margin-30px-bottom',
                'name': 'name',
                'placeholder': "Enter your name"

            }),
            'creator': forms.TextInput(attrs={
                'class': 'medium-input border-radius-4px bg-white margin-30px-bottom',
                'value': '',
                'id': 'khaloei',
                'type': 'hidden'
                # 'placeholder': "Enter User"

            }),
            'body': forms.Textarea(attrs={
                'class': 'medium-textarea border-radius-4px bg-white h-120px margin-2-half-rem-bottom',
                'name': 'comment',
                'rows': "7",
                'placeholder': 'Enter Your Comment...',
            }),

        }
