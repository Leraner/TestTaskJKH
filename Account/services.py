from .models import ActionsType


def quick_sort(array: list) -> list:
    if len(array) < 2:
        return array
    else:
        pivot = array[0]
        less = [i for i in array[1:] if i.created_at <= pivot.created_at]
        greater = [i for i in array[1:] if i.created_at > pivot.created_at]
        return quick_sort(less) + [pivot] + quick_sort(greater)


def find_all_actions(sessions: list) -> dict:
    """ Find all user's actions """
    if not sessions:
        return {}

    all_actions = {
        'read': [],
        'create': [],
        'update': [],
        'delete': []
    }
    for session in sessions:
        for key in ActionsType:
            all_actions[f'{key.value}'] = session.actions.filter(type=key)
    return all_actions


def find_last_actions(all_actions: dict) -> dict:
    """ Find all user's last actions (create, delete, update, read) """
    last_actions = {}
    for action in all_actions:
        sorted_actions = quick_sort(all_actions[action])[::-1]
        if sorted_actions:
            last_action = sorted_actions[0]

            last_actions.update({f'{action}': last_action})
        else:
            last_actions.update({f'{action}': 0})

    return last_actions


def format_actions(all_actions: dict, is_sessions: bool, last_actions: dict = None) -> list:
    """ Formatting actions for response template """
    if not is_sessions:
        return []

    information = []
    for action in all_actions:
        information.append({
            "type": action,
            "last": {"created_at": last_actions[action].created_at} if last_actions[action] else 'null',
            "count": len(all_actions[action])
        })

    return information


def format_information(user, formatted_actions: list) -> dict:
    """ Formatting response information """
    return {
        "number": f'{user.number.country_code}{user.number.national_number}',
        "actions": formatted_actions
    }
