import requests

def post_card(cpf):
    headers = {
        'Host': 'servicos-cloud.saude.gov.br',
        'Sec-Ch-Ua': '"Not/A)Brand";v="8", "Chromium";v="126"',
        'Accept': 'application/json, text/plain, */*',
        'Accept-Language': 'pt-BR',
        'Sec-Ch-Ua-Mobile': '?0',
        'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX25hbWUiOiIwMDAwMjA3MjA5MiIsIm9yaWdlbSI6IlNDUEEiLCJpc3MiOiJzYXVkZS5nb3YuYnIiLCJub21lIjoiQ0FST0xJTkEgREUgVkFTQ09OQ0VMTE9TIEZSRUlUQVMgUEVTQ0UiLCJhdXRob3JpdGllcyI6WyJST0xFX1NJLVBOSV9PRVNDIiwiUk9MRV9TQ1BBU0lTVEVNQV9HRVMiLCJST0xFX1NJLVBOSSIsIlJPTEVfU0NQQV9HRVMiLCJST0xFX1NDUEFfVVNSIiwiUk9MRV9TQ1BBU0lTVEVNQSIsIlJPTEVfU0ktUE5JX0dFU0EiLCJST0xFX1NDUEEiXSwiY2xpZW50X2lkIjoiU0ktUE5JIiwic2NvcGUiOlsiQ05TRElHSVRBTCIsIkdPVkJSIiwiU0NQQSJdLCJjbmVzIjoibnVsbCIsIm9yZ2FuaXphdGlvbiI6IkRBVEFTVVMiLCJjcGYiOiIwMDAwMjA3MjA5MiIsImV4cCI6MTcyMzA0MDk1MywianRpIjoiOWVmYzc0NWYtMDdiOS00YTFlLWExZjUtYTNjYjhjNjI1NGM5Iiwia2V5IjoiNDU5NTIxIiwiZW1haWwiOiJjYXJvbGluYTgxdmFzY29uY2VsbG9zQGhvdG1haWwuY29tIn0.K-mpHvWXxEvg9XUSPCpRmT2QUqMj2A7M0Y59pJvO79M',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.6478.127 Safari/537.36',
        'Sec-Ch-Ua-Platform': '"Windows"',
        'Origin': 'https://si-pni.saude.gov.br',
        'Sec-Fetch-Site': 'same-site',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Dest': 'empty',
        'Referer': 'https://si-pni.saude.gov.br/',
        # 'Accept-Encoding': 'gzip, deflate, br',
        'Priority': 'u=1, i',
    }
    response = requests.get(f'https://servicos-cloud.saude.gov.br/pni-bff/v1/cidadao/cpf/{cpf}', headers=headers, verify=False)
    print(f'Codigo da resposta {response.status_code}', )
    try:
        print(f'Json recebido com sucesso!\n{response.json()}\n\n')
    except:
        print('Erro ao processar json!')
    return response