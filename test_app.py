
from student_app import predict_result


def test_pass_result():
    assert predict_result(5) == "Pass"


def test_low_study_hours():
    assert predict_result(1) == "Needs Improvement"


def test_boundary_value():
    assert predict_result(3) == "Pass"
