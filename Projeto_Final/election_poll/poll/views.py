from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from .forms import PollForm, OptionForm
from .models import Poll, Option
from django.core.cache import cache
import hashlib

def poll_list(request):
    polls = Poll.objects.all().order_by('-created_at')
    return render(request, 'poll/poll_list.html', {'polls': polls})

def poll_detail(request, id):
    poll = get_object_or_404(Poll, id=id)
    return render(request, 'poll/poll_detail.html', {'poll': poll})

def create_poll(request):
    if request.method == 'POST':
        poll_form = PollForm(request.POST)
        option_forms = [OptionForm(request.POST, prefix=str(i)) for i in range(1, 4)]

        if poll_form.is_valid() and all(opt.is_valid() for opt in option_forms):
            poll = poll_form.save()
            for opt_form in option_forms:
                option = opt_form.save(commit=False)
                option.poll = poll
                option.save()
            return redirect('poll_list')
    else:
        poll_form = PollForm()
        option_forms = [OptionForm(prefix=str(i)) for i in range(1, 4)]

    return render(request, 'poll/create_poll.html', {
        'poll_form': poll_form,
        'option_forms': option_forms
    })

def delete_poll(request, id):
  
    poll = get_object_or_404(Poll, id=id)
    
    
    if request.method == 'POST':
        poll.delete()
        return redirect('poll_list')  
    
    return render(request, 'poll/delete_poll.html', {'poll': poll})

def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        return x_forwarded_for.split(',')[0]
    return request.META.get('REMOTE_ADDR')

def vote(request, id):
    if request.method == 'POST':
        poll = get_object_or_404(Poll, id=id)
        client_ip = get_client_ip(request)
        unique_id = hashlib.sha256(f'{client_ip}-{poll.id}'.encode()).hexdigest()
        
        
        if cache.get(unique_id):
            return JsonResponse({'message': 'Você já votou nesta enquete.'}, status=403)
        
      
        option_id = request.POST.get('option_id')
        if not option_id:
            return JsonResponse({'message': 'Opção de voto não selecionada.'}, status=400)
        
        
        option = get_object_or_404(Option, id=option_id)
        
        
        option.votes += 1
        option.save()
        
       
        cache.set(unique_id, True, 3600 * 24)
        
        return JsonResponse({'message': 'Voto computado com sucesso.'}, status=200)
    
    return JsonResponse({'message': 'Método de requisição inválido.'}, status=400)

def poll_results(request, id):
    poll = get_object_or_404(Poll, id=id)
    options = poll.options.all()
    total_votes = sum(option.votes for option in options)  # Total de votos
    return render(request, 'poll/poll_results.html', {'poll': poll, 'options': options, 'total_votes': total_votes})


