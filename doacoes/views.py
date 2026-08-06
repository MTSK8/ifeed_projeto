import json
from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Doacao

def home(request):
    return render(request, 'index.html')

def index_view(request):
    return render(request, 'index.html')

def login_view(request):
    return render(request, 'login.html')

def app_view(request):
    return render(request, 'app.html')


@csrf_exempt
def listar_doacoes(request):
    if request.method == 'GET':
        doacoes = Doacao.objects.all().values()
        return JsonResponse({'status': 'sucesso', 'dados': list(doacoes)})
    
    elif request.method == 'POST':
        try:
            dados = json.loads(request.body)
            
            
            nova_doacao = Doacao.objects.create(
                nome_alimento=dados.get('nome_alimento'),
                quantidade=dados.get('quantidade'),
                data_validade=dados.get('data_validade')
            )
            
            return JsonResponse({
                'status': 'sucesso', 
                'mensagem': 'Doação salva com sucesso!', 
                'id_doacao': nova_doacao.id
            })
            
        except Exception as e:
            return JsonResponse({'status': 'erro', 'mensagem': str(e)}, status=400)