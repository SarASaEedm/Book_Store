
from django import forms
from bookindex.models import Book

class BookForm(forms.Form):
    title = forms.CharField(
        max_length=100
    )
    no_of_pages = forms.IntegerField()
    price = forms.DecimalField()

    def clean_title(self):
        title = self.cleaned_data['title']
        if len(title) <3 or len(title) > 100:
            raise forms.ValidationError("Name must be between 3 and 100 characters")
        # found = Book.objects.filter(title=title).exists()
        # if found:
        #     raise forms.ValidationError("A Book with this Title already exists")
        #
        return title


class BookModelForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = '__all__'

    def clean_title(self):
        title = self.cleaned_data['title']
        if len(title) < 3 or len(title) > 100:
            raise forms.ValidationError("Name must be between 3 and 100 characters")
        # found = Book.objects.filter(title=title).exists()
        # if found:
        #     raise forms.ValidationError("A Book with this Title already exists")
        return title