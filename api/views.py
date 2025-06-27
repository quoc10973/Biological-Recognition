from rest_framework.decorators import api_view,parser_classes
from rest_framework.response import Response
from rest_framework import status
from .serializer import ImageDTOSerializer, SimilarityDTOSerializer
from rest_framework.parsers import MultiPartParser
from .service import predict_image_class_v2

# @api_view(['POST'])
# @parser_classes([MultiPartParser])  # Để nhận file
# def predict_view(request):
#     if 'image' not in request.FILES:
#         return Response({'error': 'No image uploaded'}, status=status.HTTP_400_BAD_REQUEST)

#     image_file = request.FILES['image'].read()
#     result = predict_image_class(image_file)

#     serializer = ImageDTOSerializer(result)
#     return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['POST'])
@parser_classes([MultiPartParser])
def predict_view_2(request):
    if 'image' not in request.FILES:
        return Response({'error': 'No image uploaded'}, status=status.HTTP_400_BAD_REQUEST)

    image_file = request.FILES['image'].read()
    result = predict_image_class_v2(image_file)  # Trả về dict {'label': ..., 'similarity': ...}

    serializer = SimilarityDTOSerializer(result)
    return Response(serializer.data, status=status.HTTP_200_OK)