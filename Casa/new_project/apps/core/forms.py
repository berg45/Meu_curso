# forms.py
from django import forms
from .models import Pizza, Order

class PizzaForm(forms.ModelForm):
    class Meta:
        model = Pizza
        fields = ['tamanho', 'sabor', 'valor', 'imagem']
        widgets = {
            'tamanho': forms.Select(attrs={'class': 'form-select'}),
            'sabor': forms.TextInput(attrs={'class': 'form-control'}),
            'valor': forms.NumberInput(attrs={'class': 'form-control'}),
            'imagem': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }


class OrderForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super(OrderForm, self).__init__(*args, **kwargs)
        pizzas = Pizza.objects.all()
        for pizza in pizzas:
            field_name = f"pizza_{pizza.id}"
            self.fields[field_name] = forms.IntegerField(
                label=f"{pizza.get_tamanho_display()} {pizza.sabor} - R$ {pizza.valor}",
                min_value=0,
                required=False,
                initial=0,
                widget=forms.NumberInput(attrs={'class': 'form-control', 'style': 'width: 80px;'})
            )
            #self.fields[field_name].pizza = pizza  # Adiciona referência à pizza