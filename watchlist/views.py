# from django.shortcuts import render
# from django.views import View
# from .models import Movie
# from django.http import JsonResponse
# # Create your views here.
#
#
# class MovieList(View):
#
#     def get(self, request):
#         movies = Movie.objects.all()
#         ctx = {
#             'movies': list(movies.values())
#         }
#
#         return JsonResponse(ctx)
#
# class MovieDetail(View):
#
#     def get(self, request, pk):
#         movie = Movie.objects.get(pk=pk)
#         ctx = {
#             'name': movie.name,
#             'description': movie.description,
#             'active': movie.active,
#         }
#
#         return JsonResponse(ctx)
#