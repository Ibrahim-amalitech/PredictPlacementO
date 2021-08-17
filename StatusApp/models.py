from django.db import models
import pickle

# Create your models here.
class Placement(models.Model):
    first_name = models.CharField(max_length=10)
    last_name = models.CharField(max_length=10)
    sec_score=models.IntegerField("Secondary School Score",default=0)
    highSec_score=models.IntegerField("Higher Secondary School Score",default=0)
    degree_score=models.IntegerField("Degree Score",default=0)
    etest_score=models.IntegerField("Electronic Test Score",default=0)
    mba_score=models.IntegerField("MBA Score",default=0)
    Placement_status=models.CharField("Placement Status",max_length=20,editable=False, blank=True)
    
    # method for generating predictions
    @property
    def getPredictions(self):
      x=[self.sec_score, self.highSec_score, self.degree_score, self.etest_score, self.mba_score]
      model=pickle.load(open("Job_Placement_ml_model.sav", "rb"))
      scaled = pickle.load(open("scaler.sav", "rb"))
      prediction = model.predict(scaled.transform([x]))
      if prediction == 0:
        return "NOT PLACED"
      elif prediction == 1:
        return "PLACED"
      else:
        return "error"
    
     

    # saving placement_status field derived from fuction
    def save(self,*args,**kwargs):
        self.Placement_status=self.getPredictions
        super(Placement,self).save(*args,**kwargs)

    def __str__(self):
        return self.first_name +" " + self.last_name

    def get_absolute_url(self):
      return "list"