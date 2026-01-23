from rest_framework import serializers
from .models import Sermon, VisitUsInfo, VisitationAudit, Staff, Preacher


class SermonListSerializer(serializers.ModelSerializer):
    preacher_id = serializers.IntegerField(read_only=True,source='preacher.pk')
    preacher_name = serializers.CharField(read_only=True,source='preacher.full_name')
    class Meta:
        model = Sermon
        fields = ['id','title','tags','preacher_id','preacher_name','date_preached']


class SermonDetailSerializer(serializers.ModelSerializer):
    preacher_id = serializers.IntegerField(read_only=True,source='preacher.pk')
    preacher_name = serializers.CharField(read_only=True,source='preacher.full_name')
    class Meta:
        model = Sermon
        exclude = ['preacher']


class VisitUsInfoSerializer(serializers.ModelSerializer):
    notes = serializers.CharField(allow_null=True,required=False)
    new_status = serializers.CharField(required=False)
    class Meta:
        model = VisitUsInfo
        fields = '__all__'


    def update(self, instance, validated_data):
        instance.full_name = validated_data.get('full_name',instance.full_name)
        instance.notes = validated_data.get('notes',instance.notes)
        instance.contact_number = validated_data.get('contact_number',instance.contact_number)
        instance.status = validated_data.get('status',instance.status)
        instance.intent_type = validated_data.get('intent_type',instance.intent_type)
        instance.timeframe = validated_data.get('timeframe',instance.timeframe)

        audit = VisitationAudit(
            visit_us_info = instance,
            previous_status = instance.status,
            new_status = validated_data.get('new_status')
        )
        audit.save()
        # create a new audit with a new status every time the record is updated.
        return instance


class VisitationAuditSerializer(serializers.ModelSerializer):
    class Meta:
        model = VisitationAudit
        fields = '__all__'


class ReachUsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Staff
        exclude = ['created_at','last_updated']

    def update(self, instance, validated_data):
        pass

    def create(self, validated_data):
        pass


class PreacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Preacher
        exclude = ['created_at','last_updated']