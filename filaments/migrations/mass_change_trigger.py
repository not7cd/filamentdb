from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ('filaments', '0001_initial'),
    ]
    operations = [
        migrations.RunSQL(
            """CREATE TRIGGER spool_mass_change
            BEFORE UPDATE OF mass_net ON filaments_spool
            BEGIN
                INSERT INTO filaments_masschange (spool_id, mass_net, pub_date) VALUES
                (OLD.id, OLD.mass_net, datetime('now', 'utc'));
            END;"""
        )
    ]

