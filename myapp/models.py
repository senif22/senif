from django.db import models

# Create your models here.

class projectdetail(models.Model):
    g_no = models.IntegerField()
    roll_no = models.IntegerField(primary_key=True)
    enr_no = models.IntegerField()
    name = models.TextField()
    div = models.TextField()
    pro_det = models.TextField()
    class Meta:
        db_table = ("project_detail")
    
