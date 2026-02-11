import pytest
from src import calculator


import pytest
from src import calculator

def test_add_positive_integers():
    assert calculator.add(2, 3) == 5

def test_add_negative_integers():
    assert calculator.add(-2, -3) == -5

def test_add_zero():
    assert calculator.add(0, 5) == 5
    assert calculator.add(5, 0) == 5
    assert calculator.add(0, 0) == 0

def test_add_mixed_integers():
    assert calculator.add(-2, 5) == 3
    assert calculator.add(5, -2) == 3

def test_add_floats():
    assert calculator.add(0.1, 0.2) == pytest.approx(0.3)
    assert calculator.add(1.5, 2.5) == pytest.approx(4.0)
    assert calculator.add(-1.5, 0.5) == pytest.approx(-1.0)

def test_add_large_numbers():
    assert calculator.add(1000000, 2000000) == 3000000
    assert calculator.add(-1000000, 500000) == -500000


def test_sub():
    # AI failed: 429 RESOURCE_EXHAUSTED. {'error': {'code': 429, 'message': 'You exceeded your current quota, please check your plan and billing details. For more information on this error, head to: https://ai.google.dev/gemini-api/docs/rate-limits. To monitor your current usage, head to: https://ai.dev/rate-limit. \n* Quota exceeded for metric: generativelanguage.googleapis.com/generate_content_free_tier_requests, limit: 20, model: gemini-2.5-flash\nPlease retry in 10.957504428s.', 'status': 'RESOURCE_EXHAUSTED', 'details': [{'@type': 'type.googleapis.com/google.rpc.Help', 'links': [{'description': 'Learn more about Gemini API quotas', 'url': 'https://ai.google.dev/gemini-api/docs/rate-limits'}]}, {'@type': 'type.googleapis.com/google.rpc.QuotaFailure', 'violations': [{'quotaMetric': 'generativelanguage.googleapis.com/generate_content_free_tier_requests', 'quotaId': 'GenerateRequestsPerDayPerProjectPerModel-FreeTier', 'quotaDimensions': {'location': 'global', 'model': 'gemini-2.5-flash'}, 'quotaValue': '20'}]}, {'@type': 'type.googleapis.com/google.rpc.RetryInfo', 'retryDelay': '10s'}]}}
    pass
def test_add_function_scenarios():
    # Test positive integers
    assert calculator.add(1, 2) == 3
    assert calculator.add(100, 200) == 300

    # Test negative integers
    assert calculator.add(-1, -2) == -3
    assert calculator.add(-50, -30) == -80

    # Test mixed positive and negative integers
    assert calculator.add(5, -3) == 2
    assert calculator.add(-7, 10) == 3
    assert calculator.add(10, -10) == 0

    # Test with zero
    assert calculator.add(0, 0) == 0
    assert calculator.add(5, 0) == 5
    assert calculator.add(0, -8) == -8

    # Test floating-point numbers (using pytest.approx)
    assert calculator.add(0.1, 0.2) == pytest.approx(0.3)
    assert calculator.add(1.5, 2.5) == pytest.approx(4.0)
    assert calculator.add(-0.5, 0.5) == pytest.approx(0.0)
    assert calculator.add(10.0, -3.7) == pytest.approx(6.3)

    # Test large numbers
    assert calculator.add(1000000, 2000000) == 3000000
    assert calculator.add(-123456789, -987654321) == -1111111110

def test_div():
    # AI failed: 429 RESOURCE_EXHAUSTED. {'error': {'code': 429, 'message': 'You exceeded your current quota, please check your plan and billing details. For more information on this error, head to: https://ai.google.dev/gemini-api/docs/rate-limits. To monitor your current usage, head to: https://ai.dev/rate-limit. \n* Quota exceeded for metric: generativelanguage.googleapis.com/generate_content_free_tier_requests, limit: 20, model: gemini-2.5-flash\nPlease retry in 10.854618549s.', 'status': 'RESOURCE_EXHAUSTED', 'details': [{'@type': 'type.googleapis.com/google.rpc.Help', 'links': [{'description': 'Learn more about Gemini API quotas', 'url': 'https://ai.google.dev/gemini-api/docs/rate-limits'}]}, {'@type': 'type.googleapis.com/google.rpc.QuotaFailure', 'violations': [{'quotaMetric': 'generativelanguage.googleapis.com/generate_content_free_tier_requests', 'quotaId': 'GenerateRequestsPerDayPerProjectPerModel-FreeTier', 'quotaDimensions': {'location': 'global', 'model': 'gemini-2.5-flash'}, 'quotaValue': '20'}]}, {'@type': 'type.googleapis.com/google.rpc.RetryInfo', 'retryDelay': '10s'}]}}
    pass
