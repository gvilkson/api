# api/views.py
from django.http import JsonResponse
from django.views.decorators.http import require_GET
from .utils import post_card

@require_GET
def pesquisar_cpf(request):
    cpf = request.GET.get('cpf')  # Extrai o CPF dos parâmetros da URL
    if not cpf:
        return JsonResponse({'error': 'CPF is required'}, status=400)
    
    response = post_card(cpf)  # Chama a função utilitária para buscar os dados do CPF
    try:
        data = response.json()  # Tenta processar a resposta como JSON
    except ValueError:
        data = {'error': 'Could not process JSON'}

    return JsonResponse(data, status=response.status_code)  # Retorna a resposta JSON com o status adequado
