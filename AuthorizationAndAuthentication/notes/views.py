from msilib.schema import ListView

from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views.generic import DetailView

from notes.models import Note


# Create your views here.


class NoteListView(LoginRequiredMixin, ListView):
    def get_queryset(self):
        qs = Note.objects.select_related('owner')

        if not self.request.user.has_perm('notes.can_access_all_notes'):
            return qs.filter(owner=self.request.user)

        return qs


class NoteDetailView(LoginRequiredMixin, DetailView):
    queryset = Note.objects.select_related('owner')

    def test_func(self):
        return (
                self.request.user.has_perm('notes.can_access_all_notes')
                or
                self.get_object().owner == self.request.user
        )
