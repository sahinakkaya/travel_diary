from rest_framework import viewsets
from rest_framework import permissions
from .serializers import TravelSerializer
from .models import Travel
from .permissions import IsOwnerOrReadOnly


# Create your views here.


class TravelViewSet(viewsets.ModelViewSet):
    """
    This viewset provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.
    """
    queryset = Travel.objects.all()
    serializer_class = TravelSerializer
    permission_classes = [permissions.IsAuthenticated,
                          IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def retrieve(self, request, *args, **kwargs):
        viewer = request.user.username
        pk = kwargs["pk"]
        try:
            travel = Travel.objects.get(pk=pk)
        except Travel.DoesNotExist:
            # If travel does not exist there is nothing to log about.
            # We can just call the super() function
            pass
        else:
            owner = travel.owner.username
            if viewer != owner:
                print(f"{viewer} viewed {owner}'s travel about {travel.place} "
                      f"(travel id: {travel.id})")

        return super().retrieve(self, request, *args, **kwargs)
