from django.contrib.auth.models import User
from rest_framework import serializers

from applications.security.models import ListItems, ListSubItems, Menu, MenuItems

class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = ['m_id', 'm_user', 'm_name', 'm_active']
        read_only_fields = ['m_id']  # AutoField es de solo lectura

    def to_representation(self, instance):
        return {
            "m_id": instance.m_id,
            "m_user": instance.m_user.id if instance.m_user else None,
            "m_name": instance.m_name,
            "m_active": instance.get_m_active_display()  # Muestra el valor legible del choice
        }
    

class ListItemsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ListItems
        fields = [
            'li_id', 'li_name', 'li_short_name', 
            'li_order', 'li_icon', 'li_active'
        ]
        read_only_fields = ['li_id']  # AutoField es de solo lectura

    def to_representation(self, instance):
        return {
            "li_id": instance.li_id,
            "li_name": instance.li_name,
            "li_short_name": instance.li_short_name,
            "li_order": instance.li_order,
            "li_icon": instance.li_icon,
            "li_active": instance.get_li_active_display()  # Muestra valor legible del choice
        }
    

class ListSubItemsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ListSubItems
        fields = [
            'lsi_id', 'lsi_name', 'lsi_short_name', 
            'lsi_order', 'lsi_url', 'lsi_items', 'lsi_active'
        ]
        read_only_fields = ['lsi_id']

    def to_representation(self, instance):
        return {
            "lsi_id": instance.lsi_id,
            "lsi_name": instance.lsi_name,
            "lsi_short_name": instance.lsi_short_name,
            "lsi_order": instance.lsi_order,
            "lsi_url": instance.lsi_url,
            "lsi_items": instance.lsi_items.li_id if instance.lsi_items else None,
            "lsi_active": instance.get_lsi_active_display()
        }
    

class MenuItemsSerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuItems
        fields = ['id', 'mi_menu', 'mi_items']  # 'id' es AutoField generado por Django
        read_only_fields = ['id']

    def to_representation(self, instance):
        return {
            "id": instance.id,
            "mi_menu": instance.mi_menu.m_id if instance.mi_menu else None,
            "mi_items": instance.mi_items.li_id if instance.mi_items else None
        }