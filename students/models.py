from django.db import models

# Create your models here.
#
# class Student(models.Model):
#     first_name = models.CharField(max_length=30,blank=True,null=True)
#     last_name = models.CharField(max_length=30,blank=True,null=True)
#     phone = models.CharField(max_length=30,blank=True,null=True)
#     address = models.CharField(max_length=30,blank=True,null=True)
#     email = models.CharField(max_length=30,blank=True,null=True)
#     active = models.BooleanField(default=True)
#     fathername = models.CharField(max_length=30,blank=True,null=True)
#
# class Subject(models.Model):
#     name = models.CharField(max_length=30,blank=True,null=True)

class Album(models.Model):
    name = models.CharField(max_length=200, blank=True, null= True)
    artist = models.CharField(max_length=200, blank=True, null= True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Music(models.Model):
    album = models.ForeignKey(Album, on_delete= models.CASCADE, related_name= "musics_album")
    name = models.CharField(max_length=200, blank=True, null= True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class PropertyMasterApi(models.Model):
    # index_key = models.AutoField()
    index_key = models.IntegerField(primary_key=True)
    urlid = models.CharField(max_length=50)
    daystamp = models.DateField(blank=True, null=True)
    timestamp = models.DateTimeField(blank=True, null=True)
    url = models.CharField(max_length=50, blank=True, null=True)
    url_source = models.CharField(max_length=200, blank=True, null=True)
    page = models.IntegerField(blank=True, null=True)
    line_order = models.IntegerField(blank=True, null=True)
    page_order = models.IntegerField(blank=True, null=True)
    line_loop = models.IntegerField(blank=True, null=True)
    location_tree = models.CharField(max_length=124, blank=True, null=True)
    tree_1 = models.CharField(max_length=45, blank=True, null=True)
    tree_2 = models.CharField(max_length=45, blank=True, null=True)
    tree_3 = models.CharField(max_length=45, blank=True, null=True)
    tree_4 = models.CharField(max_length=45, blank=True, null=True)
    tree_5 = models.CharField(max_length=45, blank=True, null=True)
    tree_6 = models.CharField(max_length=45, blank=True, null=True)
    location_zone = models.CharField(max_length=100, blank=True, null=True)
    location_exact = models.CharField(max_length=20, blank=True, null=True)
    longitude = models.DecimalField(max_digits=10, decimal_places=7, blank=True, null=True)
    latitude = models.DecimalField(max_digits=10, decimal_places=7, blank=True, null=True)
    title = models.CharField(max_length=96, blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    price_down = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    price_percen = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    advertiser_type = models.CharField(max_length=51, blank=True, null=True)
    advertiser_firstname = models.CharField(max_length=58, blank=True, null=True)
    advertiser_name = models.CharField(max_length=63, blank=True, null=True)
    advertiser_loc = models.CharField(max_length=19, blank=True, null=True)
    advertiser_url = models.CharField(max_length=63, blank=True, null=True)
    phonenumber_0 = models.CharField(max_length=37, blank=True, null=True)
    phonenumber_1 = models.CharField(max_length=440, blank=True, null=True)
    tex_ref = models.CharField(max_length=105, blank=True, null=True)
    charac_basic = models.CharField(max_length=462, blank=True, null=True)
    charac_equip = models.CharField(max_length=107, blank=True, null=True)
    image_01 = models.CharField(max_length=101, blank=True, null=True)
    image_02 = models.CharField(max_length=97, blank=True, null=True)
    image_03 = models.CharField(max_length=97, blank=True, null=True)
    stats = models.CharField(max_length=144, blank=True, null=True)
    stats_date_act = models.CharField(max_length=10, blank=True, null=True)
    stats_visit = models.CharField(max_length=50, blank=True, null=True)
    stats_send = models.CharField(max_length=50, blank=True, null=True)
    stats_email = models.CharField(max_length=50, blank=True, null=True)
    stats_fav = models.CharField(max_length=50, blank=True, null=True)
    ad_address_locationid = models.CharField(db_column='ad_address_locationId', max_length=21, blank=True, null=True)  # Field name made lowercase.
    ad_address_locationlevel = models.CharField(db_column='ad_address_locationLevel', max_length=50, blank=True, null=True)  # Field name made lowercase.
    ad_address_municipalityid = models.CharField(db_column='ad_address_municipalityId', max_length=21, blank=True, null=True)  # Field name made lowercase.
    ad_address_provinceid = models.CharField(db_column='ad_address_provinceId', max_length=10, blank=True, null=True)  # Field name made lowercase.
    ad_builttype = models.IntegerField(db_column='ad_builtType', blank=True, null=True)  # Field name made lowercase.
    ad_characteristics_bathnumber = models.IntegerField(db_column='ad_characteristics_bathNumber', blank=True, null=True)  # Field name made lowercase.
    ad_characteristics_constructedarea = models.IntegerField(db_column='ad_characteristics_constructedArea', blank=True, null=True)  # Field name made lowercase.
    ad_characteristics_hasgarden = models.CharField(db_column='ad_characteristics_hasGarden', max_length=4, blank=True, null=True)  # Field name made lowercase.
    ad_characteristics_hasparking = models.IntegerField(db_column='ad_characteristics_hasParking', blank=True, null=True)  # Field name made lowercase.
    ad_characteristics_hasswimmingpool = models.IntegerField(db_column='ad_characteristics_hasSwimmingPool', blank=True, null=True)  # Field name made lowercase.
    ad_characteristics_hasterrace = models.IntegerField(db_column='ad_characteristics_hasTerrace', blank=True, null=True)  # Field name made lowercase.
    ad_characteristics_roomnumber = models.IntegerField(db_column='ad_characteristics_roomNumber', blank=True, null=True)  # Field name made lowercase.
    ad_energycertification_suffix = models.CharField(db_column='ad_energyCertification_suffix', max_length=12, blank=True, null=True)  # Field name made lowercase.
    ad_energycertification_type = models.CharField(db_column='ad_energyCertification_type', max_length=9, blank=True, null=True)  # Field name made lowercase.
    ad_id = models.CharField(max_length=8, blank=True, null=True)
    ad_media_photonumber = models.IntegerField(db_column='ad_media_photoNumber', blank=True, null=True)  # Field name made lowercase.
    ad_media_videonumber = models.IntegerField(db_column='ad_media_videoNumber', blank=True, null=True)  # Field name made lowercase.
    ad_operation = models.CharField(max_length=50, blank=True, null=True)
    ad_origin = models.CharField(max_length=7, blank=True, null=True)
    ad_owner_commercialid = models.CharField(db_column='ad_owner_commercialId', max_length=32, blank=True, null=True)  # Field name made lowercase.
    ad_owner_contactpreference = models.IntegerField(db_column='ad_owner_contactPreference', blank=True, null=True)  # Field name made lowercase.
    ad_owner_type = models.IntegerField(blank=True, null=True)
    ad_price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    ad_typology = models.CharField(max_length=50, blank=True, null=True)
    comment = models.CharField(max_length=500, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'property_master_api'

