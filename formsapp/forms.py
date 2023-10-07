from django import forms


class Forma1(forms.Form):
    name = forms.CharField(label='Имя')
    age = forms.IntegerField(required=False, min_value=1, max_value=100, label='Возраст')


class Forma2(forms.Form):
    VIBOR = (('Русский', 'RU'), ('English', 'EN'), ('France', "FR"))
    name = forms.CharField(label='Имя')
    num = forms.FloatField(min_value=0, max_value=5, label='Рейтинг')
    email = forms.EmailField(label='Почта')
    check1 = forms.BooleanField(label='Подписка на рассылку', required=False)
    check2 = forms.NullBooleanField(label='Подтвердить', required=False)
    lang = forms.TypedChoiceField(label='язык', choices=VIBOR)
    file = forms.ImageField(label='Фото')


class Forma3(forms.Form):
    name = forms.CharField(label='Имя птицы')
    family = forms.CharField(label='К какому виду отностися птиц')
    age = forms.FloatField(min_value=0, max_value=30, label='Возраст')
    color = forms.CharField(label='Описание окраса')
    food = forms.CharField(label='Описание любимой еды')
    file = forms.ImageField(label='Фото')
