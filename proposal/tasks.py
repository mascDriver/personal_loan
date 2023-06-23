from celery import shared_task

from .models import Proposal


@shared_task
def analyse_proposal():
    proposals = Proposal.objects.filter(analyzed=False)

    for proposal in proposals.iterator():
        if proposal.id % 2 == 0:
            proposal.approved = True
        else:
            proposal.approved = False
        proposal.analyzed = True
        proposal.save()
