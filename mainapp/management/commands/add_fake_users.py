from django.core.management import BaseCommand


class Command(BaseCommand):
    def handle(self, *args, **options):
        print(" Start adding fake user data ".center(79, '-'))

