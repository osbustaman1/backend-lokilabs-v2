from rest_framework import serializers
from applications.security.models import Country, Region, Commune
from applications.company.models import (
    MutualSecurity, 
    BoxesCompensation, 
    Company, 
    Subsidiary, 
    Area, 
    Department, 
    Position, 
    CenterCost, 
    Health,
    Afp
)

class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = '__all__'
        read_only_fields = ['cou_id']  # AutoField es de solo lectura


class RegionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Region
        fields = '__all__'
        read_only_fields = ['re_id']  # AutoField es de solo lectura


class CommuneSerializer(serializers.ModelSerializer):
    class Meta:
        model = Commune
        fields = '__all__'
        read_only_fields = ['com_id']  # AutoField es de solo lectura


class MutualSecuritySerializer(serializers.ModelSerializer):
    class Meta:
        model = MutualSecurity
        fields = '__all__'
        read_only_fields = ['ms_id']  # AutoField es de solo lectura


class BoxesCompensationSerializer(serializers.ModelSerializer):
    class Meta:
        model = BoxesCompensation
        fields = '__all__'
        read_only_fields = ['bc_id']  # AutoField es de solo lectura


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = '__all__'
        read_only_fields = ['com_id']  # AutoField es de solo lectura

    def to_representation(self, instance):
        return {
            "com_id": instance.com_id,
            "com_rut": instance.com_rut,
            "com_representative_name": instance.com_representative_name,
            "com_rut_representative": instance.com_rut_representative,
            "com_is_state": instance.get_com_is_state_display(),
            "com_name_company": instance.com_name_company,
            "com_social_reason": instance.get_com_social_reason_display(),
            "com_twist_company": instance.com_twist_company,
            "com_address": instance.com_address,
            "com_department_office": instance.com_department_office,
            "country": instance.country.cou_id if instance.country else None,
            "region": instance.region.re_id if instance.region else None,
            "commune": instance.commune.com_id if instance.commune else None,
            "com_latitude": instance.com_latitude,
            "com_longitude": instance.com_longitude,
            "com_zip_code": instance.com_zip_code,
            "com_phone_one": instance.com_phone_one,
            "com_mail_one": instance.com_mail_one,
            "com_phone_two": instance.com_phone_two,
            "com_mail_two": instance.com_mail_two,
            "com_date_ingress": instance.com_date_ingress,
            "com_is_holding": instance.get_com_is_holding_display(),
            "com_id_parent_company": instance.com_id_parent_company.com_id if instance.com_id_parent_company else None,
            "com_active": instance.get_com_active_display(),
            "com_rut_counter": instance.com_rut_counter,
            "com_name_counter": instance.com_name_counter,
            "com_company_image": instance.com_company_image,
            "mutual_security": instance.mutual_security.ms_id if instance.mutual_security else None,
            "boxes_compensation": instance.boxes_compensation.bc_id if instance.boxes_compensation else None
        }


class SubsidiarySerializer(serializers.ModelSerializer):
    class Meta:
        model = Subsidiary
        fields = '__all__'
        read_only_fields = ['sub_id']  # AutoField es de solo lectura

    def to_representation(self, instance):
        return {
            "sub_id": instance.sub_id,
            "sub_name": instance.sub_name,
            "company": instance.company.com_id if instance.company else None,
            "sub_mail": instance.sub_mail,
            "sub_phone": instance.sub_phone,
            "sub_address": instance.sub_address,
            "country": instance.country.cou_id if instance.country else None,
            "region": instance.region.re_id if instance.region else None,
            "commune": instance.commune.com_id if instance.commune else None,
            "sub_latitude": instance.sub_latitude,
            "sub_longitude": instance.sub_longitude,
            "sub_matrixhouse": instance.get_sub_matrixhouse_display(),
            "sub_active": instance.get_sub_active_display()
        }

    
class AreaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Area
        fields = '__all__'
        read_only_fields = ['ar_id']  # AutoField es de solo lectura

    def to_representation(self, instance):
        return {
            "ar_id": instance.ar_id,
            "ar_name": instance.ar_name,
            "company": instance.company.com_id if instance.company else None,
            "ar_active": instance.get_ar_active_display()  # Muestra el valor legible del choice
        }


class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = '__all__'
        read_only_fields = ['dep_id']  # AutoField es de solo lectura

    def to_representation(self, instance):
        return {
            "dep_id": instance.dep_id,
            "dep_name": instance.dep_name,
            "area": instance.area.ar_id if instance.area else None,
            "dep_description": instance.dep_description,
            "dep_active": instance.get_dep_active_display()  # Muestra el valor legible del choice
        }


class PositionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Position
        fields = '__all__'
        read_only_fields = ['pos_id']  # AutoField es de solo lectura

    def to_representation(self, instance):
        return {
            "pos_id": instance.pos_id,
            "pos_name_position": instance.pos_name_position,
            "departament": instance.departament.dep_id if instance.departament else None,
            "post_description": instance.post_description,
            "pos_active": instance.get_pos_active_display()  # Muestra el valor legible del choice
        }


class CenterCostSerializer(serializers.ModelSerializer):
    class Meta:
        model = CenterCost
        fields = '__all__'
        read_only_fields = ['cencost_id']  # AutoField es de solo lectura

    def to_representation(self, instance):
        return {
            "cencost_id": instance.cencost_id,
            "company": instance.company.com_id if instance.company else None,
            "cencost_name": instance.cencost_name,
            "cencost_active": instance.get_cencost_active_display()  # Muestra valor legible del choice
        }


class HealthSerializer(serializers.ModelSerializer):
    class Meta:
        model = Health
        fields = '__all__'
        read_only_fields = ['healt_id']  # AutoField es de solo lectura

    def to_representation(self, instance):
        return {
            "healt_id": instance.healt_id,
            "healt_name": instance.healt_name,
            "healt_rut": instance.healt_rut,
            "healt_code": instance.healt_code,
            "healt_entity_type": instance.get_healt_entity_type_display(),  # Muestra el valor legible
            "healt_active": instance.get_healt_active_display()
        }


class AfpSerializer(serializers.ModelSerializer):
    class Meta:
        model = Afp
        fields = [
            'afp_id', 'afp_code_previred', 'afp_name', 
            'afp_dependent_worker_rate', 'afp_sis', 
            'afp_self_employed_worker_rate', 'afp_active'
        ]
        read_only_fields = ['afp_id']  # AutoField es de solo lectura

    def to_representation(self, instance):
        return {
            "afp_id": instance.afp_id,
            "afp_code_previred": instance.afp_code_previred,
            "afp_name": instance.afp_name,
            "afp_dependent_worker_rate": instance.afp_dependent_worker_rate,
            "afp_sis": instance.afp_sis,
            "afp_self_employed_worker_rate": instance.afp_self_employed_worker_rate,
            "afp_active": instance.get_afp_active_display()  # Valor legible del choice
        }
