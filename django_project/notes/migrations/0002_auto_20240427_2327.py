from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0001_initial'),
    ]

    operations = [
        migrations.RemoveConstraint(
            model_name='tag',
            name='tag_of_username',
        ),
        migrations.RemoveField(
            model_name='tag',
            name='owner',
        ),
    ]