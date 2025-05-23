# Generated by Django 5.1.4 on 2025-04-07 20:20

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('questions', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserQuizAttempt',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('score', models.IntegerField()),
                ('date_taken', models.DateTimeField(auto_now_add=True)),
                ('topic', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='questions.quiztopic')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='UserAnswer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_correct', models.BooleanField()),
                ('answer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='questions.answer')),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='questions.question')),
                ('attempt', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_answers', to='analytics.userquizattempt')),
            ],
        ),
    ]
