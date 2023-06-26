from rest_framework import serializers

from .models import Proposal, Customer


class CustomerSerializer(serializers.ModelSerializer):
    cpf = serializers.CharField(min_length=11, max_length=11)
    address = serializers.CharField(min_length=7)

    class Meta:
        model = Customer
        fields = '__all__'


class ProposalSerializer(serializers.ModelSerializer):
    customer = CustomerSerializer()

    class Meta:
        model = Proposal
        exclude = ['approved', 'analyzed']

    def create(self, validated_data):
        customer_data = validated_data.pop('customer')
        customer = Customer.objects.create(**customer_data)
        proposal = Proposal.objects.create(customer=customer, **validated_data)
        return proposal
