from django.db import models

# Create your models here.

class Taxonomy(models.Model):
    taxonomy_id = models.PositiveIntegerField(unique=True, null=False, blank=False)
    organism_name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.organism_name
    
    
class Gene(models.Model):
    name = models.CharField(max_length=20, unique=True, null=False, blank=False)
    
    def __str__(self):
        return self.name
    
class GeneOntology(models.Model):
    TYPE = [(0, "CC"), (1, "BP"), (2, "MF")]
    
    go_id = models.CharField(unique=True, max_length=10, null=False, blank=False)
    name = models.CharField(max_length=50)
    go_type = models.PositiveIntegerField(choices=TYPE)
    
    def __str__(self):
        return "%s: %s" % (self.go_id, self.go.name)
    
    
class Pfam(models.Model):
    pfam_id = models.CharField(unique=True, max_length=7, null=False, blank=False)
    nome = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name

    
class UniprotKb(models.Model):
    accession = models.CharField(max_length=12, null=False, blank=False, unique=True)
    sequence = models.TextField(null=False, blank=False)
    lenght = models.PositiveIntegerField(null=True, blank=True)
    
    taxonomy = models.ForeignKey(Taxonomy, on_delete=models.CASCADE)
    gos = models.ManyToManyField(GeneOntology)
    pfam = models.ManyToManyField(Pfam)
    gene = models.ForeignKey(Gene, on_delete=models.CASCADE)
    
    def save(self, *args, **kwargs):
        self.length = len(self.sequence)
        super().save(*args, **kwargs)

        
class PDB(models.Model):
    METHOD_CHOICES = [(0, "NMR"), (1, "X_Ray C"), (2, "Cryo-EM")]
    
    accession = models.CharField(max_length=4, unique=True, blank=False, null=False)
    resolution =  models.FloatField()
    method = models.PositiveIntegerField(choices=METHOD_CHOICES)
    
    uniprot = models.ForeignKey(UniprotKb, on_delete=models.CASCADE)

