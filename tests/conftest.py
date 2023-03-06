"""fixtures"""
import pytest

def base_url(request):
    return request.config.getoption("--url")
