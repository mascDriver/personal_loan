from rest_framework.serializers import ModelSerializer

from .models import Proposal, Customer


class CustomerSerializer(ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'


class ProposalSerializer(ModelSerializer):
    customer = CustomerSerializer()

    class Meta:
        model = Proposal
        exclude = ['approved', 'analyzed']

    def create(self, validated_data):
        customer_data = validated_data.pop('customer')
        customer = Customer.objects.create(**customer_data)
        proposal = Proposal.objects.create(customer=customer, **validated_data)
        return proposal
