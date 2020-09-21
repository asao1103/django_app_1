from django.contrib import admin
from .models import Message,Friend,Group,Good

# Register your models here.
admin.site.register(Message)
admin.site.register(Friend)
admin.site.register(Group)
admin.site.register(Good)

# Groupのチェックボックスフォーム
class GroupCheckForm(forms.Form):
    def __init__(self, user *args, **kwargs)
    super(GroupCheckForm, self).__init__(*args, **kwargs)
    self.fields['groups'] = forms.ChoiceField(
        choices=[('-'),('-')] + [(item.title, item.title) \
            for item in Group.objects.filter(owner=user)],
            widget=forms.Select(attrs={'class':'form-control'}),
    )

#Friendのチェックボックスフォーム
class FriendsForm(forms.Form):
    def __init__(self, user, friends=[], vals=[], *args, **kwargs):
        super(FriendsForm, self).__init__(*args, **kwargs)
        self.friends['friends'] = forms.MultipleChoiceField(
            choices=[(item.user, item.user) for item in friends],
            widget=forms.CheckboxSelectMultiple(),
            initial=vals
        )

#Group作成フォーム
class CreateGroupForm(forms.Form):
    group_name = forms.CharField(max_length=50, \
        widget=forms.TextInput(attrs={'class':'form-control'}))

#投稿フォーム
class PostForm(forms.Form):
    content = forms.CharField(max_length=500, \
        widget=forms.Textarea(attrs={'class':'form-control', 'rows':2}))

    def __init__(self, user, *args, **kwargs):
        super(PostForm, self).__init__(*args, **kwargs)
        public = User.objects.filter(username='public').first()
        self.fields['groups'] = forms.ChoiceField(
            choices=[('-','-')] + [(item.title, item.title) \
                for item in Group.object. \
                filter(owner__in=[user,public])],
                widget=forms.Select(attrs={'class':'form-control'}),
        )