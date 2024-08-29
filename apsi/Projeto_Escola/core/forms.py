from django import forms
from .models import Aluno, Professor, Turma, Disciplina, Nota

class AlunoForm(forms.ModelForm):
    turma = forms.ModelChoiceField(queryset=Turma.objects.all(), required=True)
    
    class Meta:
        model = Aluno
        fields = ['nome', 'data_nascimento', 'turma']

class ProfessorForm(forms.ModelForm):
    class Meta:
        model = Professor
        fields = ['nome']

class TurmaForm(forms.ModelForm):
    class Meta:
        model = Turma
        fields = ['nome', 'ano', 'professores']

class DisciplinaForm(forms.ModelForm):
    class Meta:
        model = Disciplina
        fields = ['nome', 'professor']

class NotaForm(forms.ModelForm):
    class Meta:
        model = Nota
        fields = ['aluno', 'disciplina', 'nota', 'data_avaliacao']
