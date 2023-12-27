from django.contrib.auth import authenticate, login
from django.contrib.auth.models import Group
from django.db import models
from django.shortcuts import get_object_or_404


def model_records_amount(model) -> int:
    return model.objects.count()


def get_top_records(model, amount: int):
    return model.objects.filter()[:amount]


def add_user_to_group(user, group_name: str):
    Group.objects.get(name=group_name).user_set.add(user)
#
#
# def extract_patient_signup_data(form):
#     return {
#         "username": form.cleaned_data.get("username"),
#         "raw_password": form.cleaned_data.get("password1"),
#         "first_name": form.cleaned_data.get("first_name"),
#         "last_name": form.cleaned_data.get("last_name"),
#         "patronymic": form.cleaned_data.get("patronymic"),
#         "gender": form.cleaned_data.get("gender"),
#         "birth_date": form.cleaned_data.get("birth_date"),
#         "passport_id": form.cleaned_data.get("passport_id"),
#         "phone_number": form.cleaned_data.get("phone_number"),
#         "email": form.cleaned_data.get("email"),
#     }
#
#
def login_by_credentials(request, username, password):
    user = authenticate(username=username, password=password)
    login(request, user)
    return user


# def add_new_patient(request, form):
#     data = extract_patient_signup_data(form)
#
#     user = login_by_credentials(request, data["username"], data["password"])
#     add_user_to_group(user, "Пациент")
#
#     new_patient = Patient(
#         user=user,
#         full_name=data["last_name"]
#         + " "
#         + data["first_name"]
#         + " "
#         + data["patronymic"],
#         gender=data["gender"],
#         birth_date=data["birth_date"],
#         passport_id=data["passport_id"],
#         phone_number=data["phone_number"],
#         email=data["email"],
#     )
#     new_patient.save()
#
#
# def get_patient_and_visits(pk):
#     patient = get_object_or_404(Patient, pk=pk)
#     return patient, patient.appointment_set.all(), patient.medicaltest_set.all()


def is_user_in_group(user, group_name: str):
    return user.groups.filter(name=group_name).exists()


# def is_patient_matches_appointment(patient, appointment_pk):
#     appointment = get_object_or_404(Appointment, pk=appointment_pk)
#     return patient == appointment.patient


# def is_patient_matches_medical_test(patient, medical_test_pk):
#     medical_test = get_object_or_404(MedicalTest, pk=medical_test_pk)
#     return patient == medical_test.patient
#
#
def is_superuser(user):
    return is_user_in_group(user, "Администратор")


# def is_superuser_or_appointment(user, appointment_pk):
#     return (
#         is_user_in_group(user, "Пациент")
#         and is_patient_matches_appointment(user.patient, appointment_pk)
#     ) or is_superuser(user)
#
#
# def is_superuser_or_medical_test(user, medical_test_pk):
#     return (
#         is_user_in_group(user, "Пациент")
#         and is_patient_matches_medical_test(user.patient, medical_test_pk)
#     ) or is_superuser(user)
