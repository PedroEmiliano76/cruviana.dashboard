import requests


def get_data(data):
    try:
        url = f'https://cruviana.ifpi.edu.br/oeiras/api/v1/leituras/?Data={data}'
        response = requests.get(url)

        # Verifique se a solicitação foi bem-sucedida (código de status 200)
        response.raise_for_status()

        return response.json()['results']
    except requests.exceptions.RequestException as e:
        print(f"Erro na requisição: {e}")
        return None
