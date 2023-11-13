from main import add_numbers

def test_add_numbers():

    result = add_numbers(3, 4)
    assert result == 7  # Ожидаем, что 3 + 4 = 7
