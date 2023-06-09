from __future__ import annotations

import secrets

import requests

from .persistence import session
from .utils import BearerAuth

ACCESS_TOKEN = 'access_token'
REFRESH_TOKEN = 'refresh_token'

LOGIN = '/api/auth/login'
REFRESH = '/api/auth/refresh'
LOGOUT = '/api/auth/logout'


def gen_api_key(nbytes: int = None):
    return secrets.token_urlsafe(nbytes=nbytes)


def get_proxy_from_port(host: str, port: int):
    return {
        'http': f'{host}:{port}',
        'https': f'{host}:{port}',
    }


def login(pw: str, user: str = None, *, host: str, proxies: dict = None, port: int = None, endpoint: str = None):
    assert proxies is None or port is None, 'Specifying both proxies and port at the same time is invalid.'
    if port is not None:
        proxies = get_proxy_from_port(host, port)
    if endpoint is None:
        endpoint = LOGIN

    request_obj = {'pw': pw}
    if user is not None:
        request_obj['user'] = user

    resp = requests.post(f'{host}{endpoint}', proxies=proxies, json=request_obj)
    if resp.status_code == 201:
        tokens = resp.json()
        access_token = tokens[ACCESS_TOKEN]
        refresh_token = tokens[REFRESH_TOKEN]
        session[ACCESS_TOKEN] = access_token
        session[REFRESH_TOKEN] = refresh_token


def refresh(*, host: str, proxies: dict = None, port: int = None, endpoint: str = None):
    assert proxies is None or port is None, 'Specifying both proxies and port at the same time is invalid.'
    if port is not None:
        proxies = get_proxy_from_port(host, port)
    if endpoint is None:
        endpoint = REFRESH

    refresh_token = session[REFRESH_TOKEN]

    resp = requests.post(f'{host}{endpoint}', proxies=proxies, auth=BearerAuth(token=refresh_token))
    if resp.status_code == 201:
        tokens = resp.json()
        access_token = tokens[ACCESS_TOKEN]
        session[ACCESS_TOKEN] = access_token


def logout(*, host: str, proxies: dict = None, port: int = None, endpoint: str = None):
    assert proxies is None or port is None, 'Specifying both proxies and port at the same time is invalid.'
    if port is not None:
        proxies = get_proxy_from_port(host, port)
    if endpoint is None:
        endpoint = LOGOUT

    auth = None
    access_token = session.get(ACCESS_TOKEN, None)
    if access_token is not None:
        auth = BearerAuth(token=access_token)

    resp = requests.delete(f'{host}{endpoint}', proxies=proxies, auth=auth)
    if resp.status_code == 204:
        session.clear()
