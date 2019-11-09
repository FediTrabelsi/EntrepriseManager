from .serializers import EntrepriseSerializer

def custom_jwt_response_handler(token, entreprise=None, request=None):
    return {
        'token' : token,
        'entreprise' : EntrepriseSerializer(entreprise, context={'request' : request}).data
    }