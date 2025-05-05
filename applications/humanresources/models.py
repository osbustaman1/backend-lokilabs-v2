from django.db import models
from model_utils.models import TimeStampedModel
from django.contrib.auth.models import User

from applications.company.models import Company, InstitutionsApv
from remunerations.choices import (
    CLASSIFICATION, 
    TYPE_CONTRACT, 
    PAYMENT_TYPE_APV, 
    REGIMENT_TYPE_APV, 
    REMUNERATION_TYPE, 
    SEARCH_FIELDS, 
    TYPE_CLASSIFICATION, 
    TYPE_PLAN_APV,
    TYPE_VACATION, 
    TYPE_VARIABLE, 
    YES_NO_OPTIONS,
    ESTATE_VACATION
)

class Vacation(TimeStampedModel):
    vac_id = models.AutoField("Key", primary_key=True)
    collaborator = models.ForeignKey(User, verbose_name="Usuario", db_column="vac_user_id", on_delete=models.PROTECT)
    vac_vacation_days = models.DecimalField("Días", max_digits=5, decimal_places=2)
    vac_noon_days = models.DecimalField("Medio día", max_digits=5, decimal_places=2, null=True, blank=True)
    vac_start_date = models.DateField("Fecha inicio")
    vac_end_date = models.DateField("Fecha término")
    vac_response_date = models.DateTimeField("Fecha respuesta", null=True, blank=True)
    vac_request_status = models.IntegerField("Estado", choices=ESTATE_VACATION, default=1)
    vac_half_day_time = models.CharField("Medio día", max_length=50, null=True, blank=True)
    vac_type_vacations = models.IntegerField("Tipo de vacaciones", choices=TYPE_VACATION, null=True, blank=True)
    vac_status = models.CharField("Activo", max_length=1, choices=YES_NO_OPTIONS, default="Y")
    
    def __str__(self):
        return f"{self.collaborator.username} - {self.vac_vacation_days} días"
    
    def save(self, *args, **kwargs):
        super(Vacation, self).save(*args, **kwargs)
    
    class Meta:
        db_table = "hr_Vacation"
        ordering = ['vac_id']


class ChangeType(models.Model):
    cht_id = models.AutoField("Key", primary_key=True)
    cht_name = models.CharField(max_length=50, unique=True)
    
    def __str__(self):
        return self.cht_name

    def save(self, *args, **kwargs):
        super(ChangeType, self).save(*args, **kwargs)
    
    class Meta:
        db_table = "hr_ChangeType"
        ordering = ['cht_id']


class FunMovement(models.Model):
    user = models.ForeignKey(User, verbose_name="Usuario", db_column="ct_user_id", on_delete=models.PROTECT, null=True, blank=True)
    employer = models.ForeignKey(Company, verbose_name="Company",
                                db_column="ct_employer_id", on_delete=models.PROTECT)
    change_type = models.ForeignKey(ChangeType, db_column="ct_change_type_id", on_delete=models.PROTECT)  # Relación con el tipo de cambio
    fv_change_date = models.DateField("Fecha", null=True, blank=True)
    fv_details = models.TextField("Detalle", blank=True, null=True)
    
    def __str__(self):
        return f"{self.change_type.cht_name} - {self.user.username}"
    
    def save(self, *args, **kwargs):
        super(FunMovement, self).save(*args, **kwargs)
    
    class Meta:
        db_table = "hr_FunMovement"


class ContractType(TimeStampedModel):
    ct_id = models.AutoField("Key", primary_key=True)
    ct_contractcode = models.CharField("Código contrato", max_length=25, null=True, blank=True)
    ct_contractname = models.CharField("Nombre contrato", max_length=100)
    company = models.ForeignKey(Company, verbose_name="Company",
                                db_column="ct_company_id", on_delete=models.PROTECT)
    ct_contract = models.TextField("Texto del contrato")
    ct_typecontract = models.IntegerField("Tipo de contrato", choices=TYPE_CONTRACT, default=1)
    ct_active = models.CharField(
        "activo", choices=YES_NO_OPTIONS, max_length=1, default="Y")

    def __int__(self):
        return self.ct_id

    def __str__(self):
        return f'{self.ct_contractname}'

    def save(self, *args, **kwargs):
        super(ContractType, self).save(*args, **kwargs)

    class Meta:
        db_table = "hr_ContractType"
        ordering = ['ct_id']


class Concept(TimeStampedModel):

    conc_id = models.AutoField("Key", primary_key=True)
    conc_name = models.CharField("Nombre", max_length=255)
    conc_clasificationconcept = models.IntegerField("Clasificación concepto", choices=CLASSIFICATION)
    conc_typeconcept = models.IntegerField("Tipo concepto", choices=TYPE_CLASSIFICATION)
    conc_remuneration_type = models.IntegerField("Tipo de remuneración", choices=REMUNERATION_TYPE)
    conc_search_field = models.CharField("Campo de busqueda", null=True, blank=True, default='0', max_length=50, choices=SEARCH_FIELDS)
    conc_default = models.CharField(
        "Concepto por defecto", choices=YES_NO_OPTIONS, max_length=1, default="N")
    conc_active = models.CharField(
        "Concepto activo", choices=YES_NO_OPTIONS, max_length=1, default="Y")

    def __int__(self):
        return self.conc_id

    def __str__(self):
        return f"{self.conc_id} - {self.conc_name}"

    def save(self, *args, **kwargs):
        super(Concept, self).save(*args, **kwargs)

    class Meta:
        db_table = 'hr_Concept'
        ordering = ['conc_id']


class ConfigVariableRemunerations(TimeStampedModel):
    
    cvr_id = models.AutoField("Key", primary_key=True)
    cvr_name = models.CharField("Nombre variable", max_length=255)
    cvr_valueone = models.CharField("Valor uno", max_length=255, null=True, blank=True)
    cvr_valuetwo = models.CharField("Valor dos", max_length=255, null=True, blank=True)

    cvr_vartype = models.IntegerField(
        "Tipo de variable", choices=TYPE_VARIABLE, default=0)

    cvr_active = models.CharField(
        "Variable activa", choices=YES_NO_OPTIONS, max_length=1, default="Y")

    def __int__(self):
        return self.cvr_id

    def __str__(self):
        return f"{self.cvr_id} - {self.cvr_name}"

    def save(self, *args, **kwargs):
        super(ConfigVariableRemunerations, self).save(*args, **kwargs)

    class Meta:
        db_table = 'hr_ConfigVariableRemunerations'
        ordering = ['cvr_id']


class MonthlyPreviredData(TimeStampedModel):

    dpm_id = models.AutoField("Key", primary_key=True)
    dpm_json = models.TextField("json data", null=True, blank=True)
    dpm_active = models.CharField(
        "Variable activa", choices=YES_NO_OPTIONS, max_length=1, default="Y")
    
    def __int__(self):
        return self.dpm_id

    def __str__(self):
        return f"{self.dpm_id} - {self.dpm_name}"

    def save(self, *args, **kwargs):
        super(MonthlyPreviredData, self).save(*args, **kwargs)

    class Meta:
        db_table = 'hr_MonthlyPreviredData'
        ordering = ['dpm_id']


class VoluntarySavingsAPV(TimeStampedModel):

    vs_id = models.AutoField("Key", primary_key=True)
    user = models.ForeignKey(User, verbose_name="Usuario", db_column="vs_user_id", on_delete=models.PROTECT, null=True, blank=True)
    institutions_apv = models.ForeignKey(InstitutionsApv, verbose_name="InstitutionsApv", db_column="vs_institutions_apv_id", on_delete=models.PROTECT, null=True, blank=True)
    vs_value_plan = models.DecimalField("Valor Plan", max_digits=10, decimal_places=2, null=True, blank=True)
    vs_money_type = models.IntegerField("Tipo de moneda", choices=TYPE_PLAN_APV, null=True, blank=True, default=None)
    vs_payment_type = models.IntegerField("Tipo de pago", choices=PAYMENT_TYPE_APV, null=True, blank=True, default=None)
    vs_regimen_type = models.IntegerField("Tipo de regiment", choices=REGIMENT_TYPE_APV, null=True, blank=True, default=None)
    vs_document_number = models.CharField("N° de documento", max_length=100, blank=True, null=True)
    vs_month_start = models.CharField("Mes de inicio", max_length=7, null=True, blank=True)
    vs_month_end = models.CharField("Mes de término", max_length=7, null=True, blank=True)

    def __int__(self):
        return self.vs_id

    def save(self, *args, **kwargs):
        super(VoluntarySavingsAPV, self).save(*args, **kwargs)

    class Meta:
        db_table = 'hr_VoluntarySavingsAPV'
        ordering = ['vs_id']


class SavingsVoluntaryCollective(TimeStampedModel):

    svc_id = models.AutoField("Key", primary_key=True)
    user = models.ForeignKey(User, verbose_name="Usuario", db_column="vs_user_id", on_delete=models.PROTECT, null=True, blank=True)
    institutions_apv = models.ForeignKey(InstitutionsApv, verbose_name="InstitutionsApv", db_column="vs_institutions_apv_id", on_delete=models.PROTECT, null=True, blank=True)
    svc_type_plan = models.IntegerField("Tipo de plan", choices=TYPE_PLAN_APV, null=True, blank=True)
    svc_employer_amount = models.DecimalField("Monto empleador", max_digits=10, decimal_places=2, null=True, blank=True)
    svc_employee_amount = models.DecimalField("Monto empleado", max_digits=10, decimal_places=2, null=True, blank=True)
    svc_contract_number = models.CharField("Número de contrato", max_length=50, null=True, blank=True)
    svc_contract = models.CharField("Ruta contrato", max_length=255, null=True, blank=True)
        
    def __int__(self):
        return self.svc_id

    def save(self, *args, **kwargs):
        super(SavingsVoluntaryCollective, self).save(*args, **kwargs)

    class Meta:
        db_table = 'hr_SavingsVoluntaryCollective'
        ordering = ['svc_id']


class ConceptsRemunerations(TimeStampedModel):

    TYPE_CONCEPTS = (
        (1, "Imponible"),
        (2, "No imponible"),
    )

    cr_id = models.AutoField("Key", primary_key=True)
    cr_name = models.CharField("Nombre", max_length=255)
    cr_type = models.IntegerField("Tipo", choices=TYPE_CONCEPTS)

    def __int__(self):
        return self.cr_id
    
    def __str__(self):
        return f"{self.cr_id} - {self.cr_name}"
    
    def save(self, *args, **kwargs):
        super(ConceptsRemunerations, self).save(*args, **kwargs)

    class Meta:
        db_table = 'hr_ConceptsRemunerations'
        ordering = ['cr_id']


class ConceptsUserRemunerations(TimeStampedModel):
    
    TYPE_CONCEPTS = (
        (1, "SI"),
        (2, "No"),
    )

    cur_id = models.AutoField("Key", primary_key=True)
    user = models.ForeignKey(User, verbose_name="Usuario", db_column="cur_user_id", on_delete=models.PROTECT, null=True, blank=True)
    concept = models.ForeignKey(ConceptsRemunerations, verbose_name="Concepto", db_column="cur_concept_id", on_delete=models.PROTECT)
    cur_value = models.DecimalField("Valor", max_digits=10, decimal_places=2)
    cur_type = models.IntegerField("Descuento?", choices=TYPE_CONCEPTS, default=2)

    def __int__(self):
        return self.cur_id
    
    def __str__(self):
        return f"{self.cur_id} - {self.user.username} - {self.concept.cr_name}"
    
    def save(self, *args, **kwargs):
        super(ConceptsUserRemunerations, self).save(*args, **kwargs)

    class Meta:
        db_table = 'hr_ConceptsUserRemunerations'
        ordering = ['cur_id']