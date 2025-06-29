from rest_framework.decorators import api_view,parser_classes
from rest_framework.response import Response
from rest_framework import status
from .serializer import ImageUploadSerializer, SimilarityDTOSerializer
from rest_framework.parsers import MultiPartParser
from .service import predict_image_class_v2
from drf_spectacular.utils import OpenApiExample, OpenApiTypes, extend_schema

# @api_view(['POST'])
# @parser_classes([MultiPartParser])  # Để nhận file
# def predict_view(request):
#     if 'image' not in request.FILES:
#         return Response({'error': 'No image uploaded'}, status=status.HTTP_400_BAD_REQUEST)

#     image_file = request.FILES['image'].read()
#     result = predict_image_class(image_file)

#     serializer = ImageDTOSerializer(result)
#     return Response(serializer.data, status=status.HTTP_200_OK)
@extend_schema(
    request=ImageUploadSerializer,
    responses=SimilarityDTOSerializer,
    description="Upload file ảnh (multipart/form-data), trả về label và similarity",
    methods=["POST"],
    # 👇 THÊM DÒNG NÀY 👇
    examples=[
        OpenApiExample(
            name="Example Input",
            description="Gửi file ảnh dạng multipart/form-data",
            value={"image": "<binary image file>"},
            request_only=True,
        )
    ],
)
@api_view(['POST'])
@parser_classes([MultiPartParser])
def predict_view_2(request):
    if 'image' not in request.FILES:
        return Response({'error': 'No image uploaded'}, status=status.HTTP_400_BAD_REQUEST)

    image_file = request.FILES['image'].read()
    result = predict_image_class_v2(image_file)  # Trả về dict {'label': ..., 'similarity': ...}

    serializer = SimilarityDTOSerializer(result)
    return Response(serializer.data, status=status.HTTP_200_OK)