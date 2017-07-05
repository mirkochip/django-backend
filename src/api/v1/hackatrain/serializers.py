from rest_framework import serializers


class SimplePostInputSerializer(serializers.Serializer):
    name = serializers.CharField(required=True)
    city = serializers.CharField(required=True)


class SimpleGetOutputChildOutputSerializer(serializers.Serializer):
    name = serializers.CharField(required=True)
    city = serializers.CharField(required=True)


class SimpleGetOutputSerializer(serializers.Serializer):
    developers_info = serializers.SerializerMethodField()

    @staticmethod
    def get_developers_info(obj):
        return SimpleGetOutputChildOutputSerializer(obj, many=True).data
