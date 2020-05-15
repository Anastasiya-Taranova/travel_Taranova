from django.db.models import Q

from periodic import get_auth_profile_model
from periodic import tasks
from periodic.app import app


@app.task
def invite_all_users():  # pragma: no cover
    print(f"BEGIN | {invite_all_users.__name__}")

    auth_profile_model = get_auth_profile_model()

    criteria = Q(verified_at__isnull=True) & Q(notified_at__isnull=True)

    auth_profiles = auth_profile_model.objects.filter(criteria)

    print(f"IN | {invite_all_users.__name__} | auth profiles: {auth_profiles.count()}")

    emails = {_prof.user.email for _prof in auth_profiles}

    for email in emails:
        tasks.invite_single_user.delay(email)
        print(f"IN | {invite_all_users.__name__} | sent {email} to processing")

    print(f"END | {invite_all_users.__name__}")
