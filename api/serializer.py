from abc import ABCMeta, abstractproperty

from rest_framework import serializers
from rest_framework.fields import CurrentUserDefault
from api.models import Campaign, Chain, TaskStage, \
    ConditionalStage, Case, \
    Task, Rank, RankLimit, Track, RankRecord, CampaignManagement
from api.permissions import ChainAccessPolicy, ManagersOnlyAccessPolicy

base_model_fields = ['id', 'name', 'description']
stage_fields = ['chain', 'in_stages', 'out_stages', 'x_pos', 'y_pos']
schema_provider_fields = ['json_schema', 'ui_schema', 'library']


class CampaignSerializer(serializers.ModelSerializer):
    class Meta:
        model = Campaign
        fields = '__all__'


class CampaignValidationCheck:
    __metaclass__ = ABCMeta

    context = None

    def is_campaign_valid(self, value):
        request = self.context.get("request")
        if request and \
                hasattr(request, "user") and \
                ManagersOnlyAccessPolicy.is_user_campaign_manager(request.user,
                                                                  value.get_campaign()):
            return True
        else:
            return False


class ChainSerializer(serializers.ModelSerializer, CampaignValidationCheck):
    class Meta:
        model = Chain
        fields = base_model_fields + ['campaign']

    def validate_campaign(self, value):
        """
        Check that the created chain belongs to a campaign that user manages.
        """
        if self.is_campaign_valid(value):
            return value
        raise serializers.ValidationError("User may not add chain "
                                          "to this campaign")


class ConditionalStageSerializer(serializers.ModelSerializer,
                                 CampaignValidationCheck):
    class Meta:
        model = ConditionalStage
        fields = base_model_fields + stage_fields + ['conditions', 'pingpong']

    def validate_chain(self, value):
        """
        Check that the created stage belongs to a campaign that user manages.
        """
        if self.is_campaign_valid(value):
            return value
        raise serializers.ValidationError("User may not add stage "
                                          "to this chain")


class TaskStageReadSerializer(serializers.ModelSerializer):
    chain = ChainSerializer(read_only=True)

    class Meta:
        model = TaskStage
        fields = base_model_fields + stage_fields + schema_provider_fields + \
                 ['copy_input', 'allow_multiple_files', 'is_creatable',
                  'displayed_prev_stages', 'assign_user_by',
                  'assign_user_from_stage', 'rich_text', 'webhook_address',
                  'webhook_payload_field', 'webhook_params',
                  'webhook_response_field']


class TaskStageSerializer(serializers.ModelSerializer,
                          CampaignValidationCheck):
    class Meta:
        model = TaskStage
        fields = base_model_fields + stage_fields + schema_provider_fields + \
                 ['copy_input', 'allow_multiple_files', 'is_creatable',
                  'displayed_prev_stages', 'assign_user_by',
                  'assign_user_from_stage', 'rich_text', 'webhook_address',
                  'webhook_payload_field', 'webhook_params',
                  'webhook_response_field']

    def validate_chain(self, value):
        """
        Check that the created stage belongs to a campaign that user manages.
        """
        if self.is_campaign_valid(value):
            return value
        raise serializers.ValidationError("User may not add stage "
                                          "to this chain")


# class WebHookStageSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = WebHookStage
#         fields = base_model_fields + stage_fields + schema_provider_fields + \
#                  ['web_hook_address', ]


class CaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Case
        fields = '__all__'


class TaskEditSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['complete', 'responses']


class TaskDefaultSerializer(serializers.ModelSerializer):
    stage = TaskStageReadSerializer(read_only=True)

    class Meta:
        model = Task
        fields = '__all__'
        read_only_fields = ['case',
                            'in_tasks',
                            'assignee',
                            'stage',
                            'responses',
                            'complete']


class TaskCreateSerializer(serializers.ModelSerializer):
    assignee = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Task
        fields = '__all__'
        read_only_fields = ['case',
                            'in_tasks',
                            'assignee']


class TaskRequestAssignmentSerializer(serializers.ModelSerializer):
    assignee = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Task
        fields = '__all__'
        read_only_fields = ['case',
                            'in_tasks',
                            'assignee',
                            'stage',
                            'responses',
                            'complete']


class RankSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rank
        fields = '__all__'


class RankRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = RankRecord
        fields = '__all__'


class RankLimitSerializer(serializers.ModelSerializer, CampaignValidationCheck):
    class Meta:
        model = RankLimit
        fields = '__all__'

    def validate_stage(self, value):
        """
        Check that the created rank limit belongs to a stage that user manages.
        """
        if self.is_campaign_valid(value):
            return value
        raise serializers.ValidationError("User may not add rank limit "
                                          "to this campaign")


class TrackSerializer(serializers.ModelSerializer, CampaignValidationCheck):
    class Meta:
        model = Track
        fields = '__all__'

    def validate_campaign(self, value):
        """
        Check that the created track belongs to a campaign that user manages.
        """
        if self.is_campaign_valid(value):
            return value
        raise serializers.ValidationError("User may not add track "
                                          "to this campaign")


class CampaignManagementSerializer(serializers.ModelSerializer, CampaignValidationCheck):
    class Meta:
        model = CampaignManagement
        fields = '__all__'

    def validate_campaign(self, value):
        """
        Check that the created chain belongs to a campaign that user manages.
        """
        if self.is_campaign_valid(value):
            return value
        raise serializers.ValidationError("User may not add campaign management "
                                          "to this campaign")
