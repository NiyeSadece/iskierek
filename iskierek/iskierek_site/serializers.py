from rest_framework import serializers
from .models import DiscordUser, Student, Extracurricular, Sport, Club, Spark, Professor


class DiscordUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = DiscordUser
        fields = [
            'name',
            'discord_id',
            'is_active',
            'exp',
            'lvl',
        ]
        extra_kwargs = {'name': {'required': False}}


class ExtracurricularSerializer(serializers.ModelSerializer):
    name_display = serializers.SerializerMethodField()
    special_display = serializers.SerializerMethodField()

    class Meta:
        model = Extracurricular
        fields = ['name_display', 'special_display']

    def get_name_display(self, obj):
        return obj.get_name_display()

    def get_special_display(self, obj):
        return obj.get_special_display()


class ClubSerializer(serializers.ModelSerializer):
    name_display = serializers.SerializerMethodField()
    special_display = serializers.SerializerMethodField()

    class Meta:
        model = Club
        fields = ['name_display', 'special_display']

    def get_name_display(self, obj):
        return obj.get_name_display()

    def get_special_display(self, obj):
        return obj.get_special_display()


class SparkSerializer(serializers.ModelSerializer):
    name_display = serializers.SerializerMethodField()

    class Meta:
        model = Spark
        fields = ['name_display']

    def get_name_display(self, obj):
        return obj.get_name_display()


class SportSerializer(serializers.ModelSerializer):
    name_display = serializers.SerializerMethodField()
    special_display = serializers.SerializerMethodField()

    class Meta:
        model = Sport
        fields = ['name_display', 'special_display']

    def get_name_display(self, obj):
        return obj.get_name_display()

    def get_special_display(self, obj):
        return obj.get_special_display()


class StudentSerializer(serializers.ModelSerializer):
    element_display = serializers.SerializerMethodField()
    living_display = serializers.SerializerMethodField()
    major_display = serializers.SerializerMethodField()
    major2_display = serializers.SerializerMethodField()
    faculty_display = serializers.SerializerMethodField()
    faculty2_display = serializers.SerializerMethodField()
    year_display = serializers.SerializerMethodField()
    year2_display = serializers.SerializerMethodField()
    extracurricular_display = ExtracurricularSerializer(source='extracurricular', read_only=True)
    club_display = ClubSerializer(source='club', read_only=True)
    sport_display = SportSerializer(source='sport', read_only=True)
    spark_display = SparkSerializer(source='spark', read_only=True)
    age = serializers.SerializerMethodField()

    class Meta:
        model = Student
        fields = [
            'name',
            'last_name',
            'dob',
            'age',
            'element_display',
            'spark_display',
            'extracurricular_display',
            'club_display',
            'sport_display',
            'living_display',
            'major_display',
            'major2_display',
            'faculty_display',
            'faculty2_display',
            'year_display',
            'year2_display',
            'photo',
        ]
        extra_kwargs = {'name': {'required': False}}

    def get_element_display(self, obj):
        return obj.get_element_display()

    def get_living_display(self, obj):
        return obj.get_living_display()

    def get_major_display(self, obj):
        return obj.get_major_display()

    def get_major2_display(self, obj):
        return obj.get_major2_display()

    def get_faculty_display(self, obj):
        return obj.get_faculty_display()

    def get_faculty2_display(self, obj):
        return obj.get_faculty2_display()

    def get_year_display(self, obj):
        return obj.get_year_display()

    def get_year2_display(self, obj):
        return obj.get_year2_display()

    def get_age(self, obj):
        return obj.age()


class ProfessorSerializer(serializers.ModelSerializer):
    teaching_duration_1 = serializers.SerializerMethodField()
    teaching_duration_2 = serializers.SerializerMethodField()
    element_display = serializers.SerializerMethodField()
    living_display = serializers.SerializerMethodField()
    major_display = serializers.SerializerMethodField()
    major2_display = serializers.SerializerMethodField()
    faculty_display = serializers.SerializerMethodField()
    faculty2_display = serializers.SerializerMethodField()
    year_display = serializers.SerializerMethodField()
    extracurricular_display = ExtracurricularSerializer(source='extracurricular', read_only=True)
    club_display = ClubSerializer(source='club', read_only=True)
    sport_display = SportSerializer(source='sport', read_only=True)
    spark_display = SparkSerializer(source='spark', read_only=True)
    age = serializers.SerializerMethodField()
    dorm_display = serializers.SerializerMethodField()
    dorm_special_display = serializers.SerializerMethodField()

    class Meta:
        model = Professor
        fields = [
            'name',
            'last_name',
            'dob',
            'element_display',
            'spark_display',
            'living_display',
            'major_display',
            'major2_display',
            'faculty_display',
            'faculty2_display',
            'year_display',
            'photo',
            'dorm_display',
            'dorm_special_display',
            'how_long',
            'how_long2',
            'teaching_duration_1',
            'teaching_duration_2',
            'extracurricular_display',
            'club_display',
            'sport_display',
            'age'
        ]

    def get_teaching_duration_1(self, obj):
        return obj.teaching()

    def get_teaching_duration_2(self, obj):
         return obj.teaching2()

    def get_age(self, obj):
        return obj.age()

    def get_element_display(self, obj):
        return obj.get_element_display()

    def get_living_display(self, obj):
        return obj.get_living_display()

    def get_major_display(self, obj):
        return obj.get_major_display()

    def get_major2_display(self, obj):
        return obj.get_major2_display()

    def get_faculty_display(self, obj):
        return obj.get_faculty_display()

    def get_faculty2_display(self, obj):
        return obj.get_faculty_display()

    def get_year_display(self, obj):
        return obj.get_year_display()

    def get_dorm_display(self, obj):
        return obj.get_dorm_display()

    def get_dorm_special_display(self, obj):
        return obj.get_dorm_display()