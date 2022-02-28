from rest_framework import serializers
from watchlist.models import WatchList, StreamPlatform


class WatchListSerializer(serializers.ModelSerializer):

    class Meta:
        model = WatchList
        fields = "__all__"


class StreamPlatformSerializer(serializers.ModelSerializer):

    class Meta:
        model = StreamPlatform
        fields = '__all__'



# class WatchListSerializer(serializers.ModelSerializer):
#
#     len_name = serializers.SerializerMethodField()
#
#     class Meta:
#         model = WatchList
#         fields = '__all__'
#         #fields = ['id', 'name', 'description']
#         #exclude = ['name']
#
#     def get_len_name(self, object):
#         return len(object.name)
#
#     def validate_name(self, value):
#         if len(value) < 2:
#             raise serializers.ValidationError('Name is too short!')
#         else:
#             return value
#
#     def validate(self, data):
#         if data['name'] == data['description']:
#             raise serializers.ValidationError('Name and Description must be different')
#         else: return data



#
# def desc_length(value):
#     if len(value) < 2:
#         raise serializers.ValidationError('Description is too short')
#     else: return value
#
# class MovieSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     name = serializers.CharField()
#     description = serializers.CharField(validators=[desc_length])
#     active = serializers.BooleanField()
#
#     def create(self, validated_data):
#         return Movie.objects.create(**validated_data)
#
#     def update(self, instance, validated_data):
#         instance.name = validated_data.get('name', instance.name)
#         instance.description = validated_data.get('description', instance.description)
#         instance.active = validated_data.get('active', instance.active)
#         instance.save()
#         return instance
#
#     def validate_name(self, value):
#         if len(value) < 2:
#             raise serializers.ValidationError('Name is too short!')
#         else:
#             return value
#
#     def validate(self, data):
#         if data['name'] == data['description']:
#             raise serializers.ValidationError('Name and Description must be different')
#         else: return data