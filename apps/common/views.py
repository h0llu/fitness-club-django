import datetime

from django.contrib.auth import authenticate, get_user_model, login
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.urls import reverse, reverse_lazy
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from .forms import *
from .models import *
from .services import *


def index(request):
    fitness_program_amount = model_records_amount(Program)
    trainer_amount = model_records_amount(Trainer)

    fitness_program_list = get_top_records(Program, amount=3)
    trainer_list = get_top_records(Trainer, amount=3)
    return render(
        request,
        'index.html',
        context={
            "fitness_program_amount": fitness_program_amount,
            "trainer_amount": trainer_amount,
            "fitness_program_list": fitness_program_list,
            "trainer_list": trainer_list,
        })


# @login_required
# @user_passes_test(lambda user: is_user_in_group(user, "Администратор"))
# def unregister(request, client_pk, workout_pk):
#     print(request.path)
#     get_object_or_404(Workout, pk=workout_pk).client.remove(get_object_or_404(Client, pk=client_pk))
#     return redirect('workout-detail', pk=workout_pk)
@login_required
@user_passes_test(lambda user: is_user_in_group(user, "Администратор"))
def unregister(request):
    get_object_or_404(Workout, pk=request.POST["workout_pk"]).client.remove(
        get_object_or_404(Client, pk=request.POST["client_pk"]))
    if request.POST["redirect"] == 'workout':
        return redirect('workout-detail', pk=request.POST["workout_pk"])
    else:
        return redirect('client-workouts', pk=request.POST["client_pk"])


class PositionListView(LoginRequiredMixin, UserPassesTestMixin, generic.ListView):
    model = Position
    template_name = "position_list.html"
    paginate_by = 10

    def test_func(self):
        return is_user_in_group(self.request.user, "Администратор")


class PositionCreate(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = Position
    fields = "__all__"
    template_name = "position_create.html"
    success_url = "/positions"

    def test_func(self):
        return is_user_in_group(self.request.user, "Администратор")


class PositionUpdate(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Position
    fields = "__all__"
    template_name = "position_update.html"
    success_url = "/positions"

    def test_func(self):
        return is_user_in_group(self.request.user, "Администратор")


class PositionDelete(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Position
    success_url = "/positions"

    def test_func(self):
        return is_user_in_group(self.request.user, "Администратор")


class ProgramListView(generic.ListView):
    model = Program
    template_name = "common/program_list.html"
    paginate_by = 10


class ProgramDetailView(generic.DetailView):
    model = Program
    template_name = "program_detail.html"


class ProgramCreate(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = Program
    fields = "__all__"
    template_name = "program_create.html"

    def get_success_url(self):
        return reverse('program-detail', kwargs={'pk': self.object.id})

    def test_func(self):
        return is_user_in_group(self.request.user, "Администратор")


class ProgramUpdate(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Program
    fields = "__all__"
    template_name = "program_update.html"

    def get_success_url(self):
        return reverse('program-detail', kwargs={'pk': self.object.id})

    def test_func(self):
        return is_user_in_group(self.request.user, "Администратор")


class ProgramDelete(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Program
    success_url = "/programs"

    def test_func(self):
        return is_user_in_group(self.request.user, "Администратор")


class WorkoutListView(LoginRequiredMixin, UserPassesTestMixin, generic.ListView):
    model = Workout
    template_name = "workout_list.html"
    paginate_by = 10

    def test_func(self):
        return is_user_in_group(self.request.user, "Администратор")


class WorkoutDetailView(LoginRequiredMixin, UserPassesTestMixin, generic.DetailView):
    model = Workout
    template_name = "workout_detail.html"

    def test_func(self):
        return is_user_in_group(self.request.user, "Администратор") or (
                is_user_in_group(self.request.user, "Клиент") and Client.objects.get(
            fitness_user_id=FitnessUser.objects.get(user_id=self.request.user.id).id).workout_set.contains(
            self.get_object()))


class WorkoutCreate(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = Workout
    fields = "__all__"
    template_name = "workout_create.html"

    def get_success_url(self):
        return reverse('workout-detail', kwargs={'pk': self.object.id})

    def test_func(self):
        return is_user_in_group(self.request.user, "Администратор")


class WorkoutUpdate(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Workout
    fields = "__all__"
    template_name = "workout_update.html"

    def get_success_url(self):
        return reverse('workout-detail', kwargs={'pk': self.object.id})

    def test_func(self):
        return is_user_in_group(self.request.user, "Администратор")


class WorkoutDelete(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Workout
    success_url = "/workouts"

    def test_func(self):
        return is_user_in_group(self.request.user, "Администратор")


class TrainerListView(generic.ListView):
    model = Trainer
    template_name = "trainer_list.html"
    paginate_by = 10


class TrainerDetailView(generic.DetailView):
    model = Trainer
    template_name = "trainer_detail.html"

    # def test_func(self):
    #     return is_user_in_group(self.request.user, "Администратор") or (
    #             is_user_in_group(self.request.user,
    #                              "Тренер") and self.request.user.id == self.get_object().fitness_user.user.id)


# class TrainerCreate(LoginRequiredMixin, UserPassesTestMixin, CreateView):
#     model = Trainer
#     fields = "__all__"
#     template_name = "trainer_create.html"
#
#     def get_success_url(self):
#         return reverse('trainer-detail', kwargs={'pk': self.object.id})
#
#     def test_func(self):
#         return is_user_in_group(self.request.user, "Администратор")


class TrainerUpdate(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Trainer
    fields = "__all__"
    template_name = "trainer_update.html"

    def get_success_url(self):
        return reverse('trainer-detail', kwargs={'pk': self.object.id})

    def test_func(self):
        return is_user_in_group(self.request.user, "Администратор")


class TrainerDelete(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Trainer
    success_url = "/trainers"

    def test_func(self):
        return is_user_in_group(self.request.user, "Администратор")


class ClientListView(LoginRequiredMixin, UserPassesTestMixin, generic.ListView):
    model = Client
    template_name = "client_list.html"
    paginate_by = 10

    def test_func(self):
        return is_user_in_group(self.request.user, "Администратор")


class ClientCreate(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = Client
    fields = "__all__"
    template_name = "client_create.html"
    success_url = '/clients'

    def test_func(self):
        return is_user_in_group(self.request.user, "Администратор")


class ClientUpdate(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Client
    fields = "__all__"
    template_name = "client_update.html"
    success_url = '/clients'

    def test_func(self):
        return is_user_in_group(self.request.user, "Администратор")


class ClientDelete(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Client
    success_url = "/clients"

    def test_func(self):
        return is_user_in_group(self.request.user, "Администратор")


@login_required
@user_passes_test(lambda user: is_user_in_group(user, "Администратор") or is_user_in_group(user, "Тренер"))
def client_workouts(request, pk):
    client = get_object_or_404(Client, pk=pk)
    workouts = client.workout_set.all()
    curr_datetime = datetime.datetime.now()
    return render(
        request,
        "client_workouts.html",
        context={
            "client": client,
            "workouts": workouts,
            "current_datetime": curr_datetime,
        }
    )


@login_required
@user_passes_test(lambda user: is_user_in_group(user, "Клиент"))
def personal_workouts(request):
    user_object = get_object_or_404(User, pk=request.user.id)
    client = Client.objects.filter(fitness_user=FitnessUser.objects.filter(user=user_object).first()).first()
    workouts = client.workout_set.all()
    curr_datetime = datetime.datetime.now()
    return render(
        request,
        "client_workouts.html",
        context={
            "client": client,
            "workouts": workouts,
            "current_datetime": curr_datetime,
        }
    )
