from calculate.view import View

def test_should_print_menu(capsys):
    View.print_menu()
    out, err = capsys.readouterr()
    expect_value =  ("\n=========== MENU ==========="
                  "\n1 - Addition"
                  "\n2 - Soustraction"
                  "\n3 - Multiplication"
                  "\n4 - Division"
                  "\n5 - Quitter"
                  "\n============================\n\n")
    assert out == expect_value


def test_should_print_message(capsys):
    View.end_message()
    out, err = capsys.readouterr()
    expect_value = "=========== GOOD-BYE ===========\n"
    assert out == expect_value


    # more to come ...