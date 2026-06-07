from app.services.function_service import FunctionService

def test_time_function():

    service = FunctionService()

    result = service.get_current_time()

    assert "current_time" in result