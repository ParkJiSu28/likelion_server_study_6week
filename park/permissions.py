from rest_framework import permissions


class IsAuthorUpdateOrReadOnly(permissions.BasePermission):
    # 인증된 유조에 한해 , 조회.등록 허용
    def has_permission(self, request, view):
        return request.user.is_authenticated

    # 관리자만 삭제 권한 부여
    # 작성자 수정권한만부여
    def has_object_permission(self, request, view, obj):
        # 조회요청(GET,HEAD,OPTIONS)에 대해서는 인증여부에 상관없이 허용
        if request.method in permissions.SAFE_METHODS:
            return True

        # 삭제 요청의 경우 , 관리자만
        if request.method == 'DELETE':
            return request.user.is_superuser

        # PUT 요청에 대해 , 작성자일 경우에만 요청 허용
        return obj.author == request.user
