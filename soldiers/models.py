from django.db import models

class Soldier(models.Model):
    contributor = models.CharField(max_length=40, blank=True, default="")
    unique_id = models.IntegerField(unique=True)
    pds_page_no = models.CharField(max_length=50, blank=True, default="")
    district = models.CharField(max_length=50)
    surname = models.CharField(max_length=100, blank=True)
    name = models.CharField(max_length=100, blank=True)
    rank = models.CharField(max_length=100, blank=True)
    desc = models.TextField(blank=True)
    unit_served = models.CharField(max_length=255, blank=True)
    service_no = models.CharField(max_length=40, blank=True)
    date_of_embarkation = models.DateTimeField(blank=True, null=True, default=None)
    died_in_service = models.CharField(max_length=40, blank=True, default="")

    #courage_under_fire = models.CharField(max_length=40, blank=True, default="")
    #letters_to_home = models.CharField(max_length=40, blank=True, default="")
    #survival_stories = models.CharField(max_length=40, blank=True, default="")
    #finished = models.CharField(max_length=40, blank=True, default="")

    def __str__(self):
        if self.rank:
            return self.rank + " " + self.name + " " + self.surname.upper()
        else:
            return self.name + "' " + self.surname.upper()
   
    # There probably is a better way to do this than hardcoding it
    def get_photo_url(self):
        filename = str(self.unique_id).zfill(4)
        #return "/static/soldier_photos/0" + filename + ".jpg"
        #return "0" + filename + ".jpg"
        return "soldier_photos/0" + filename + ".jpg"
