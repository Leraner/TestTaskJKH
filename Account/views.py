from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from .serializer import AccountSerializer
from .models import Account
from .services import find_all_actions, find_last_actions, format_actions, format_information


class AccountView(ModelViewSet):
    serializer_class = AccountSerializer
    queryset = Account.objects.all()

    @action(detail=False, methods=["GET"])
    def get_last_move(self, request):
        information = []

        for user in Account.objects.all():
            all_actions = find_all_actions(user.sessions.all())
            if all_actions:
                last_actions = find_last_actions(all_actions)
                formatted_actions = format_actions(all_actions, True, last_actions)
                information.append(format_information(user, formatted_actions))
            else:
                formatted_actions = format_actions(all_actions, False)
                information.append(format_information(user, formatted_actions))

        return Response({"information": information})

