from rest_framework.generics import CreateAPIView

from .models import Proposal
from .serializers import ProposalSerializer
from .tasks import analyse_proposal


class CreateProposal(CreateAPIView):
    queryset = Proposal.objects.all()
    serializer_class = ProposalSerializer

    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        analyse_proposal.apply_async()
        return response
