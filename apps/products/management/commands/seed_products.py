from django.core.management.base import BaseCommand
from faker import Faker
import random

from apps.products.models import Product, Category

fake = Faker()

class Command(BaseCommand):
    help = "Generate fake product data"

    def add_arguments(self, parser):
        parser.add_argument(
            "--count",
            type=int,
            default=50,
            help="Number of products to create"
        )

    def handle(self, *args, **options):
        count = options["count"]

        # Make sure categories exist
        categories = list(Category.objects.all())

        if not categories:
            self.stdout.write(
                self.style.ERROR("❌ No categories found. Create categories first.")
            )
            return

        Product.objects.all().delete()

        products = []

        for _ in range(count):
            products.append(
                Product(
                    category=random.choice(categories),   # ✅ REQUIRED
                    name=fake.word().capitalize(),
                    price=random.randint(500, 100000),
                    is_active=random.choice([True, False])
                )
            )

        Product.objects.bulk_create(products)

        self.stdout.write(
            self.style.SUCCESS(f"✅ {count} fake products created successfully")
        )
