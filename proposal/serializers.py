from rest_framework.serializers import ModelSerializer

from .models import Proposal, Client


class ClientSerializer(ModelSerializer):
    class Meta:
        model = Client
        fields = '__all__'


class ProposalSerializer(ModelSerializer):
    client = ClientSerializer()

    class Meta:
        model = Proposal
        exclude = ['approved', 'analyzed']

    def create(self, validated_data):
        client_data = validated_data.pop('client')
        client = Client.objects.create(**client_data)
        proposal = Proposal.objects.create(client=client, **validated_data)
        return proposal
