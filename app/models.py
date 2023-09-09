from django.db import models

# Create your models here.
class Feedback(models.Model):
    feedback=((1,'Bug_Type'),
         (2,'Feature_request'),
                    (3,'General Feedback'),
                    (4,"Userability_issue"),
                    (5,"other"))
    severity=((1,'low'),(2,"medium"),(3,"high"),(4,'critical'))
    reproduce=((1,'always'),(2,'sometimes'),(3,'rarely'),(4,'unable_to_reproduce'))
    os=((1,'window'),(2,'macOs'),(3,'android'),(4,'ios'),(5,'other'))
    overall=((1,'very_satisfied'),(2,'satisfied'),(3,'neutral'),(4,"unsatisfied"),(5,"very_unsatisfied"))
    api=((1,'paymeny_gateway'),(2,'social_media'),(3,'weather_data_api'))
    def nameFile(instance,filename):
        return '/'.join(['images',str(instance.Email),filename])

    Name=models.CharField(max_length=100,blank=True)
    Email=models.EmailField(max_length=100)
    Company=models.CharField(max_length=100,blank=True)
    Api=models.IntegerField(choices=api)
    Feedback=models.IntegerField(choices=feedback)
    FeedbackDetail = models.TextField(blank=True)
    Feedback_detail=models.CharField(max_length=100)
    severity=models.IntegerField(choices=severity)
    reproducibility=models.IntegerField(choices=reproduce)
    step_to_reproduce=models.CharField(max_length=100)
    attachment=models.FileField(upload_to=nameFile,max_length=255,null=True,blank=True)
    os=models.IntegerField(choices=os)
    browser=models.CharField(max_length=100)
    api_version=models.CharField(max_length=100)
    overall_satisfication=models.IntegerField(choices=overall)
    comment=models.CharField(max_length=100)
    contacted=models.BooleanField()
    def save(self, *args, **kwargs):
        # Set FeedbackDetail to empty string if a specific option is selected
        if self.Feedback != 5:  # 5 corresponds to "Other"
            self.FeedbackDetail = ""
        super().save(*args, **kwargs)
class Contact(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField(max_length=100)
    detail=models.CharField(max_length=1000)
