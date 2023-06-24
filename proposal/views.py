from rest_framework.generics import CreateAPIView

from .models import Proposal
from .serializers import ProposalSerializer


class CreateProposal(CreateAPIView):
    queryset = Proposal.objects.all()
    serializer_class = ProposalSerializer
