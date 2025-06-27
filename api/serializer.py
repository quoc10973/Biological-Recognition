from rest_framework import serializers

class ImageDTOSerializer(serializers.Serializer):
    predicted_class = serializers.CharField(max_length=255)
    confidence = serializers.FloatField()

    # Optional: Tùy chỉnh cách serialize output nếu cần
    def to_representation(self, instance):
        return {
            'predicted_class': instance.predicted_class,
            'confidence': round(instance.confidence, 2)
        }
    
class SimilarityDTOSerializer(serializers.Serializer):
    label = serializers.CharField()
    similarity = serializers.FloatField()

    def to_representation(self, instance):
        # if instance is a list, serialize each item by iterating through it
        if isinstance(instance, list):
            return [
                {
                    'label': item['label'],
                    'similarity': round(item['similarity'], 3)  # Làm tròn similarity tới 3 chữ số
                }
                for item in instance
            ]
        else:
            # If instance is a single dict, serialize it directly
            return {
                'label': instance['label'],
                'similarity': round(instance['similarity'], 3)
            }