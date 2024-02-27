# myapp/management/commands/create_permissions.py

from django.core.management.base import BaseCommand
from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType
from hotelservice.models import Contactus
class Command(BaseCommand):
    help = 'Create custom permissions'

    def handle(self, *args, **options):
        content_type = ContentType.objects.get_for_model(Contactus)  # Replace YourModel with your model
        permission = Permission.objects.create(
            codename='custom_view_permission',
            name='Custom View on Frontend',
            content_type=content_type,
        )
        self.stdout.write(self.style.SUCCESS('Custom view permission created successfully for hotel service'))
