from django.shortcuts import redirect
from django.utils.deprecation import MiddlewareMixin


class AuthMiddleware(MiddlewareMixin):

    # 如果request没有返回值（返回None），继续往前走
    # 如果有返回值 HttpResponse、render、redirect，则不再继续向后执行
    def process_request(self, request):
        if request.path_info == '/login/':
            return

        info_dict = request.session.get('info')
        if not info_dict:
            return redirect('/login/')
        return

    def process_response(self, request, response):
        return response
