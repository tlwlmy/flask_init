#!/usr/bin/env python
#-*- coding: utf-8 -*-
# vim:fenc=utf-8
# @author tlwlmy
# @version 2016-09-11

from flask import request, make_response, render_template, jsonify
from app.error import error
from app.config_params.functions import allow_cross_domain

@error.app_errorhandler(400)
@allow_cross_domain
def bad_request(error):
    if request.accept_mimetypes.accept_json and \
            not request.accept_mimetypes.accept_html:
        if not isinstance(error.description, dict):
            error.description = {
                'c': -400,
                'message': error.description
            }

        response = jsonify(dict({'error': 'Bad_Request'}, **error.description))
        return response, 400

    response = make_response(render_template('error/400.html'))
    response.headers['X-Status-Reason'] = error.description
    return response, 400


@error.app_errorhandler(401)
@allow_cross_domain
def unauthorized(error):
    if request.accept_mimetypes.accept_json and \
            not request.accept_mimetypes.accept_html:

        if not isinstance(error.description, dict):
            error.description = {
                'c': -401,
                'message': error.description
            }

        response = jsonify(dict({'error': 'Unauthorized'}, **error.description))
        return response, 401

    response = make_response(render_template('error/401.html'))
    response.headers['X-Status-Reason'] = error.description
    return response, 401


@error.app_errorhandler(403)
@allow_cross_domain
def forbidden(error):
    if request.accept_mimetypes.accept_json and \
            not request.accept_mimetypes.accept_html:
        # response = jsonify(dict({'error': 'Forbidden'}, **error.description))

        if not isinstance(error.description, dict):
            error.description = {
                'c': -401,
                'message': error.description
            }

        response = jsonify(dict({'error': 'Forbidden'}, **error.description))

        return response, 403

    response = make_response(render_template('error/403.html'))
    response.headers['X-Status-Reason'] = error.description
    return response, 403


@error.app_errorhandler(404)
@allow_cross_domain
def not_found(error):
    if request.accept_mimetypes.accept_json and \
            not request.accept_mimetypes.accept_html:

        if not isinstance(error.description, dict):
            error.description = {
                'c': -404,
                'message': error.description
            }

        response = jsonify(dict({'error': 'Not_Found'}, **error.description))
        return response, 400

    response = make_response(render_template('error/404.html'))
    response.headers['X-Status-Reason'] = error.description
    return response, 404


@error.app_errorhandler(500)
@allow_cross_domain
def internal_server_error(error):
    if request.accept_mimetypes.accept_json and \
            not request.accept_mimetypes.accept_html:
        response = jsonify({'error': 'Internal_Server_Error'})
        # response.status_code = 500
        # return response
        return response, 500
    return render_template('error/500.html'), 500


@error.app_errorhandler(501)
@allow_cross_domain
def not_implemented(error):
    if request.accept_mimetypes.accept_json and \
            not request.accept_mimetypes.accept_html:
        response = jsonify({'error': 'Not_Implemented'})
        response.status_code = 501
        return response
    return render_template('error/501.html'), 501
