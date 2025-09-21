from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET'])
def test_api(request):
    return Response({
        "status": "success",
        "message": "Test API is working!",
        "environment": "staging"
    })



@api_view(['GET'])
def cricket_report(request):
    return Response({
        "status": "success",
        "message": "Cricket Results",
        "environment": "feature"
    })

