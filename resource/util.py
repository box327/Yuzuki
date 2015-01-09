# -*- coding: utf-8 -*-
from twisted.web.http import NOT_FOUND

from helper.resource import YuzukiResource
from helper.template import generate_error_message


class PageNotFound(YuzukiResource):
    isLeaf = False

    def render_GET(self, request):
        request.setResponseCode(NOT_FOUND)
        return generate_error_message(request, NOT_FOUND, u"페이지를 찾을 수 없습니다")

    def render_POST(self, request):
        request.setResponseCode(NOT_FOUND)
        return generate_error_message(request, NOT_FOUND, u"페이지를 찾을 수 없습니다")

    def render_DELETE(self, request):
        request.setResponseCode(NOT_FOUND)
        return generate_error_message(request, NOT_FOUND, u"페이지를 찾을 수 없습니다")

    def getChildWithDefault(self, path, request):
        return self