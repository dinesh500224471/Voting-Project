from django.db import migrations, models

class Migration(migrations.Migration):

    initial = True

    dependencies = [
        # Dependencies for other migration files if any
    ]

    operations = [
        # Create the 'Question' model
        migrations.CreateModel(
            name='Question',   # Model name 'Question'
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),  # Auto-incremented primary key field
                ('question_text', models.CharField(max_length=200)),  # Field for the question text (limited to 200 characters)
                ('pub_date', models.DateTimeField(verbose_name='date published')),  # Field for the publication date of the question
            ],
        ),
        # Create the 'Choice' model
        migrations.CreateModel(
            name='Choice',   # Model name 'Choice'
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),  # Auto-incremented primary key field
                ('choice_text', models.CharField(max_length=200)),  # Field for the choice text (limited to 200 characters)
                ('votes', models.IntegerField(default=0)),  # Field for the number of votes (default value is 0)
                ('question', models.ForeignKey(on_delete=models.CASCADE, to='polls.Question')),  # ForeignKey to link each choice to its corresponding question
            ],
        ),
    ]
