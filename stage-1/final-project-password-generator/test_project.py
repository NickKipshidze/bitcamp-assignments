import project, tkinter

def test_generate_password():
    assert project.generate_password(length=-1) == ""
    assert len(project.generate_password(length=100)) == 100
    assert not any(char.isdigit() for char in project.generate_password(numbers=False))

def test_display_password():
    assert project.display_password(tkinter.Label(), tkinter.Button(), project.settings) == None

def test_set_setting():
    assert project.set_setting(64, "password_length") == None
    assert project.settings["password_length"] == 64