from django.urls import re_path

from . import views

urlpatterns = [
    # INDEX
    re_path(r'^$', views.index, name='index'),
    # re_path(r'^unregister/(?P<client_pk>\d+)/(?P<workout_pk>\d+)$', views.unregister, name='unregister'),
    re_path(r'^unregister$', views.unregister, name='unregister'),

    # POSITIONS
    re_path(r'^positions/$', views.PositionListView.as_view(), name='positions'),
    re_path(r'^position/create/$', views.PositionCreate.as_view(), name='create-position'),
    re_path(r'^position/(?P<pk>\d+)/update/$', views.PositionUpdate.as_view(), name='update-position'),
    re_path(r'^position/(?P<pk>\d+)/delete/$', views.PositionDelete.as_view(), name='delete-position'),

    # PROGRAMS
    re_path(r'^programs/$', views.ProgramListView.as_view(), name='programs'),
    re_path(r'^program/(?P<pk>\d+)$', views.ProgramDetailView.as_view(), name='program-detail'),
    re_path(r'^program/create/$', views.ProgramCreate.as_view(), name='create-program'),
    re_path(r'^program/(?P<pk>\d+)/update/$', views.ProgramUpdate.as_view(), name='update-program'),
    re_path(r'^program/(?P<pk>\d+)/delete/$', views.ProgramDelete.as_view(), name='delete-program'),

    # WORKOUTS
    re_path(r'^workouts/$', views.WorkoutListView.as_view(), name='workouts'),
    re_path(r'^workout/(?P<pk>\d+)$', views.WorkoutDetailView.as_view(), name='workout-detail'),
    re_path(r'^workout/create/$', views.WorkoutCreate.as_view(), name='create-workout'),
    re_path(r'^workout/(?P<pk>\d+)/update/$', views.WorkoutUpdate.as_view(), name='update-workout'),
    re_path(r'^workout/(?P<pk>\d+)/delete/$', views.WorkoutDelete.as_view(), name='delete-workout'),

    # TRAINERS
    re_path(r'^trainers/$', views.TrainerListView.as_view(), name='trainers'),
    re_path(r'^trainer/(?P<pk>\d+)$', views.TrainerDetailView.as_view(), name='trainer-detail'),
    # re_path(r'^trainer/create/$', views.TrainerCreate.as_view(), name='create-trainer'),
    re_path(r'^trainer/(?P<pk>\d+)/update/$', views.TrainerUpdate.as_view(), name='update-trainer'),
    re_path(r'^trainer/(?P<pk>\d+)/delete/$', views.TrainerDelete.as_view(), name='delete-trainer'),

    # CLIENTS
    re_path(r'^clients/$', views.ClientListView.as_view(), name='clients'),
    re_path(r'^client/(?P<pk>\d+)/workouts$', views.client_workouts, name='client-workouts'),
    re_path(r'^client/create/$', views.ClientCreate.as_view(), name='create-client'),
    re_path(r'^client/(?P<pk>\d+)/update/$', views.ClientUpdate.as_view(), name='update-client'),
    re_path(r'^client/(?P<pk>\d+)/delete/$', views.ClientDelete.as_view(), name='delete-client'),

    re_path(r'^my-workouts/$', views.personal_workouts, name='personal-workouts'),


    ###################### ОСТАЛЬНОЕ ######################

    #
    # # PATIENTS SIGNUP
    # re_path(r'^signup/$', views.patient_signup, name='patient-signup'),
    #
    # # USERS
    # re_path(r'^users/$', views.UserListView.as_view(), name='users'),
    # re_path(r'^user/create/$', views.UserCreate.as_view(), name='create-user'),
    # re_path(r'^user/(?P<pk>\d+)/update/$', views.UserUpdate.as_view(), name='update-user'),
    # # re_path(r'^user/(?P<pk>\d+)/delete/$', views.UserDelete.as_view(), name='delete-user'),
    #
    # # SERVICES
    # re_path(r'^services/$', views.ServiceListView.as_view(), name='services'),
    # re_path(r'^service/(?P<pk>\d+)$', views.ServiceDetailView.as_view(), name='service-detail'),
    # re_path(r'^service/create/$', views.ServiceCreate.as_view(), name='create-service'),
    # re_path(r'^service/(?P<pk>\d+)/update/$', views.ServiceUpdate.as_view(), name='update-service'),
    # # re_path(r'^service/(?P<pk>\d+)/delete/$', views.ServiceDelete.as_view(), name='delete-service'),
    #
    # # DOCTORS
    # re_path(r'^doctors/$', views.DoctorListView.as_view(), name='doctors'),
    # re_path(r'^doctor/(?P<pk>\d+)$', views.DoctorDetailView.as_view(), name='doctor-detail'),
    # re_path(r'^doctor/create/$', views.DoctorCreate.as_view(), name='create-doctor'),
    # re_path(r'^doctor/(?P<pk>\d+)/update/$', views.DoctorUpdate.as_view(), name='update-doctor'),
    # # re_path(r'^doctor/(?P<pk>\d+)/delete/$', views.DoctorDelete.as_view(), name='delete-doctor'),
    #
    # # POSITIONS
    # re_path(r'^positions/$', views.PositionListView.as_view(), name='positions'),
    # re_path(r'^position/create/$', views.PositionCreate.as_view(), name='create-position'),
    # re_path(r'^position/(?P<pk>\d+)/update/$', views.PositionUpdate.as_view(), name='update-position'),
    # # re_path(r'^position/(?P<pk>\d+)/delete/$', views.PositionDelete.as_view(), name='delete-position'),
    #
    # # SPECIALIZATIONS
    # re_path(r'^specializations/$', views.SpecializationListView.as_view(), name='specializations'),
    # re_path(r'^specialization/create/$',
    #         views.SpecializationCreate.as_view(), name='create-specialization'),
    # re_path(r'^specialization/(?P<pk>\d+)/update/$',
    #         views.SpecializationUpdate.as_view(), name='update-specialization'),
    # # re_path(r'^specialization/(?P<pk>\d+)/delete/$',
    # #         views.SpecializationDelete.as_view(), name='delete-specialization'),
    #
    # # PATIENTS
    # re_path(r'^patients/$', views.PatientListView.as_view(), name='patients'),
    # re_path(r'^patient/(?P<pk>\d+)/personal/$', views.patient_personal, name='patient-personal'),
    # re_path(r'^patient/create/$', views.PatientCreate.as_view(), name='create-patient'),
    # re_path(r'^patient/(?P<pk>\d+)/update/$', views.PatientUpdate.as_view(), name='update-patient'),
    # # re_path(r'^patient/(?P<pk>\d+)/delete/$', views.PatientDelete.as_view(), name='delete-patient'),
    #
    # # EMPLOYEES
    # re_path(r'^employees/$', views.EmployeeListView.as_view(), name='employees'),
    # re_path(r'^employee/create/$', views.EmployeeCreate.as_view(), name='create-employee'),
    # re_path(r'^employee/(?P<pk>\d+)/update/$', views.EmployeeUpdate.as_view(), name='update-employee'),
    # # re_path(r'^employee/(?P<pk>\d+)/delete/$', views.EmployeeDelete.as_view(), name='delete-employee'),
    #
    # # PERSONAL
    # re_path(r'^personal/$', views.personal, name='personal'),
    #
    # # APPOINTMENTS
    # re_path(r'^personal/appointment/(?P<pk>\d+)/$', views.AppointmentDetailView.as_view(), name='appointment-detail'),
    # re_path(r'^personal/appointment/create/$', views.AppointmentCreate.as_view(), name='create-appointment'),
    # re_path(r'^personal/appointment/(?P<pk>\d+)/update/$', views.AppointmentUpdate.as_view(),
    #         name='update-appointment'),
    #
    # # MEDICAL TESTS
    # re_path(r'^personal/medicaltest/(?P<pk>\d+)/$', views.MedicalTestDetailView.as_view(), name='medicaltest-detail'),
    # re_path(r'^personal/medicaltest/create/$', views.MedicalTestCreate.as_view(), name='create-medicaltest'),
    # re_path(r'^personal/medicaltest/(?P<pk>\d+)/update/$', views.MedicalTestUpdate.as_view(),
    #         name='update-medicaltest'),
]

