from applications.employee.models import Employee, UserCompany, UserTypeContract
from django.contrib.auth.models import User
from rest_framework import serializers

class EmployeeSerializer(serializers.ModelSerializer):
    """
    Serializer for the Employee model.
    Converts Employee instances into JSON format and vice versa.
    """

    class Meta:
        model = Employee
        fields = [
            'emp_id', 'user', 'emp_foreign', 'emp_nationality', 'emp_rut', 'emp_sex',
            'emp_birthdate', 'emp_civilstatus', 'emp_address', 'emp_personal_phone',
            'emp_personal_email', 'emp_corporative_email', 'emp_work_phone', 'country',
            'region', 'commune', 'emp_other_address', 'emp_latitude', 'emp_longitude',
            'emp_studies', 'emp_studiesstatus', 'emp_title', 'emp_paymentformat', 'bank',
            'emp_accounttype', 'emp_bankaccount', 'emp_drivellicense', 'emp_typelicense',
            'emp_active', 'emp_perfil_image'
        ]
        read_only_fields = ['emp_id']

    def to_representation(self, instance):
        """
        Custom representation of the Employee instance.
        Delegates field-specific logic to helper methods for better readability and maintainability.
        """
        return {
            "emp_id": instance.emp_id,
            "user": self.get_user_representation(instance),
            "emp_foreign": self.get_display_value(instance, 'emp_foreign'),
            "emp_nationality": instance.emp_nationality,
            "emp_rut": instance.emp_rut,
            "emp_sex": self.get_display_value(instance, 'emp_sex'),
            "emp_birthdate": instance.emp_birthdate,
            "emp_civilstatus": self.get_display_value(instance, 'emp_civilstatus'),
            "emp_address": instance.emp_address,
            "emp_personal_phone": instance.emp_personal_phone,
            "emp_personal_email": instance.emp_personal_email,
            "emp_corporative_email": instance.emp_corporative_email,
            "emp_work_phone": instance.emp_work_phone,
            "country": self.get_related_id(instance, 'country', 'cou_id'),
            "region": self.get_related_id(instance, 'region', 're_id'),
            "commune": self.get_related_id(instance, 'commune', 'com_id'),
            "emp_other_address": instance.emp_other_address,
            "emp_latitude": instance.emp_latitude,
            "emp_longitude": instance.emp_longitude,
            "emp_studies": self.get_display_value(instance, 'emp_studies'),
            "emp_studiesstatus": self.get_display_value(instance, 'emp_studiesstatus'),
            "emp_title": instance.emp_title,
            "emp_paymentformat": self.get_display_value(instance, 'emp_paymentformat'),
            "bank": self.get_related_id(instance, 'bank', 'ban_id'),
            "emp_accounttype": self.get_display_value(instance, 'emp_accounttype'),
            "emp_bankaccount": instance.emp_bankaccount,
            "emp_drivellicense": self.get_display_value(instance, 'emp_drivellicense'),
            "emp_typelicense": instance.emp_typelicense,
            "emp_active": self.get_display_value(instance, 'emp_active'),
            "emp_perfil_image": instance.emp_perfil_image
        }

    def get_user_representation(self, instance):
        """
        Returns the ID of the related user, or None if not present.
        """
        return instance.user.id if instance.user else None

    def get_display_value(self, instance, field_name):
        """
        Returns the display value for a choice field, or None if the field is not set.
        """
        field = getattr(instance, field_name, None)
        return field if not hasattr(instance, f'get_{field_name}_display') else getattr(instance, f'get_{field_name}_display')()

    def get_related_id(self, instance, related_field, id_field):
        """
        Returns the ID of a related object, or None if not present.
        """
        related_obj = getattr(instance, related_field, None)
        return getattr(related_obj, id_field, None) if related_obj else None


class UserCompanySerializer(serializers.ModelSerializer):
    """
    Serializer for the UserCompany model.
    Converts UserCompany instances into JSON format and vice versa.
    """

    class Meta:
        model = UserCompany
        fields = [
            'uc_id', 'user', 'company', 'position', 'subsidiary', 'contractType',
            'uc_is_boss', 'uc_estate_employee', 'uc_workertype', 'uc_contracttype',
            'uc_hiring_date', 'uc_daterenewalcontract', 'uc_weeklyhours', 'uc_agreedworkdays',
            'uc_familyassignment', 'uc_family_allowance_section', 'uc_familialloads',
            'uc_amountfamilyassignment', 'uc_simple_family_responsibilities',
            'uc_maternal_family_responsibilities', 'uc_family_responsibilities_disability',
            'uc_basesalary', 'uc_gratification', 'uc_typegratification', 'uc_semanacorrida',
            'uc_workersector', 'uc_type_of_work_day', 'us_type_of_work_modes', 'afp', 'health',
            'uc_ufisapre', 'uc_funisapre', 'change_type', 'uc_datenotificationletternotice',
            'uc_enddate', 'uc_causal', 'uc_foundation', 'uc_tiponotication', 'uc_type_user',
            'uc_heavy_work', 'uc_description_heavy_work'
        ]
        read_only_fields = ['uc_id']

    def to_representation(self, instance):
        """
        Custom representation of the UserCompany instance.
        Delegates field-specific logic to helper methods for better readability and maintainability.
        """
        return {
            "uc_id": instance.uc_id,
            "user": self.get_related_id(instance, 'user', 'id'),
            "company": self.get_related_id(instance, 'company', 'com_id'),
            "position": self.get_related_id(instance, 'position', 'pos_id'),
            "subsidiary": self.get_related_id(instance, 'subsidiary', 'sub_id'),
            "contractType": self.get_related_id(instance, 'contractType', 'ct_id'),
            "uc_is_boss": self.get_display_value(instance, 'uc_is_boss'),
            "uc_estate_employee": self.get_display_value(instance, 'uc_estate_employee'),
            "uc_workertype": self.get_display_value(instance, 'uc_workertype'),
            "uc_contracttype": self.get_display_value(instance, 'uc_contracttype'),
            "uc_hiring_date": instance.uc_hiring_date,
            "uc_daterenewalcontract": instance.uc_daterenewalcontract,
            "uc_weeklyhours": instance.uc_weeklyhours,
            "uc_agreedworkdays": instance.uc_agreedworkdays,
            "uc_familyassignment": self.get_display_value(instance, 'uc_familyassignment'),
            "uc_family_allowance_section": self.get_display_value(instance, 'uc_family_allowance_section'),
            "uc_familialloads": instance.uc_familialloads,
            "uc_amountfamilyassignment": float(instance.uc_amountfamilyassignment) if instance.uc_amountfamilyassignment else None,
            "uc_simple_family_responsibilities": instance.uc_simple_family_responsibilities,
            "uc_maternal_family_responsibilities": instance.uc_maternal_family_responsibilities,
            "uc_family_responsibilities_disability": instance.uc_family_responsibilities_disability,
            "uc_basesalary": float(instance.uc_basesalary) if instance.uc_basesalary else None,
            "uc_gratification": self.get_display_value(instance, 'uc_gratification'),
            "uc_typegratification": self.get_display_value(instance, 'uc_typegratification'),
            "uc_semanacorrida": self.get_display_value(instance, 'uc_semanacorrida'),
            "uc_workersector": self.get_display_value(instance, 'uc_workersector'),
            "uc_type_of_work_day": self.get_display_value(instance, 'uc_type_of_work_day'),
            "us_type_of_work_modes": self.get_display_value(instance, 'us_type_of_work_modes'),
            "afp": self.get_related_id(instance, 'afp', 'afp_id'),
            "health": self.get_related_id(instance, 'health', 'healt_id'),
            "uc_ufisapre": instance.uc_ufisapre,
            "uc_funisapre": instance.uc_funisapre,
            "change_type": self.get_related_id(instance, 'change_type', 'ct_id'),
            "uc_datenotificationletternotice": instance.uc_datenotificationletternotice,
            "uc_enddate": instance.uc_enddate,
            "uc_causal": self.get_related_id(instance, 'uc_causal', 'gt_id'),
            "uc_foundation": instance.uc_foundation,
            "uc_tiponotication": self.get_display_value(instance, 'uc_tiponotication'),
            "uc_type_user": self.get_display_value(instance, 'uc_type_user'),
            "uc_heavy_work": self.get_display_value(instance, 'uc_heavy_work'),
            "uc_description_heavy_work": instance.uc_description_heavy_work
        }

    def get_display_value(self, instance, field_name):
        """
        Returns the display value for a choice field, or None if the field is not set.
        """
        field = getattr(instance, field_name, None)
        return field if not hasattr(instance, f'get_{field_name}_display') else getattr(instance, f'get_{field_name}_display')()

    def get_related_id(self, instance, related_field, id_field):
        """
        Returns the ID of a related object, or None if not present.
        """
        related_obj = getattr(instance, related_field, None)
        return getattr(related_obj, id_field, None) if related_obj else None


class UserTypeContractSerializer(serializers.ModelSerializer):
    """
    Serializer for the UserTypeContract model.
    Converts UserTypeContract instances into JSON format and vice versa.
    """

    class Meta:
        model = UserTypeContract
        fields = [
            'utc_id', 'user', 'contractType', 
            'utc_maincontract', 'utc_signedcontract', 
            'utc_signedcontractdate'
        ]
        read_only_fields = ['utc_id']  # AutoField es de solo lectura

    def to_representation(self, instance):
        """
        Custom representation of the UserTypeContract instance.
        Delegates field-specific logic to helper methods for better readability and maintainability.
        """
        return {
            "utc_id": instance.utc_id,
            "user": self.get_related_id(instance, 'user', 'id'),
            "contractType": self.get_related_id(instance, 'contractType', 'ct_id'),
            "utc_maincontract": self.get_display_value(instance, 'utc_maincontract'),
            "utc_signedcontract": self.get_display_value(instance, 'utc_signedcontract'),
            "utc_signedcontractdate": instance.utc_signedcontractdate
        }

    def get_display_value(self, instance, field_name):
        """
        Returns the display value for a choice field, or None if the field is not set.
        """
        field = getattr(instance, field_name, None)
        return field if not hasattr(instance, f'get_{field_name}_display') else getattr(instance, f'get_{field_name}_display')()

    def get_related_id(self, instance, related_field, id_field):
        """
        Returns the ID of a related object, or None if not present.
        """
        related_obj = getattr(instance, related_field, None)
        return getattr(related_obj, id_field, None) if related_obj else None


class GetListUsersCompanySerializer(serializers.ModelSerializer):
    """
    Serializer for the UserCompany model.
    Converts UserCompany instances into JSON format and vice versa.
    """

    class Meta:
        model = UserCompany
        fields = [
            'uc_id', 'user', 'company', 'position', 'subsidiary', 'contractType',
            'uc_is_boss', 'uc_estate_employee', 'uc_workertype', 'uc_contracttype',
            'uc_hiring_date', 'uc_daterenewalcontract', 'uc_weeklyhours', 'uc_agreedworkdays',
            'uc_familyassignment', 'uc_family_allowance_section', 'uc_familialloads',
            'uc_amountfamilyassignment', 'uc_simple_family_responsibilities',
            'uc_maternal_family_responsibilities', 'uc_family_responsibilities_disability',
            'uc_basesalary', 'uc_gratification', 'uc_typegratification', 'uc_semanacorrida',
            'uc_workersector', 'uc_type_of_work_day', 'us_type_of_work_modes', 
            'afp', 'health'
        ]
        read_only_fields = ['uc_id']  # AutoField es de solo lectura


class ListUserCompanySerializer(serializers.ModelSerializer):
    """
    Serializer to list users with related Employee and UserCompany data.
    Combines data from User, Employee, UserCompany, Position, and ContractType models.
    """
    emp_rut = serializers.CharField(source='employee.emp_rut', read_only=True)
    emp_corporative_email = serializers.EmailField(source='employee.emp_corporative_email', read_only=True)
    position_name = serializers.CharField(source='usercompany.position.pos_name_position', read_only=True)
    contract_name = serializers.CharField(source='usercompany.contractType.ct_contractname', read_only=True)

    class Meta:
        model = User
        fields = [
            'id', 'first_name', 'last_name',  # Fields from User
            'emp_rut', 'emp_corporative_email',  # Fields from Employee
            'position_name', 'contract_name'  # Fields from UserCompany and related models
        ]