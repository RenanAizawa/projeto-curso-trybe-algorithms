import pytest
from challenges.challenge_encrypt_message import encrypt_message


base_message = "banana"
invalid_message= 1000
r3_message= "nab_ana"
r4_message= "an_anab"
rN_message="ananab"

def test_encrypt_message():
    with pytest.raises(TypeError, match="tipo inválido para key"):
        encrypt_message(base_message, "b")
    with pytest.raises(TypeError, match="tipo inválido para message"):
        encrypt_message(invalid_message, 3)
    # chamadas mal sucedidas
    assert encrypt_message(base_message, 3) != r4_message
    assert encrypt_message(base_message, 4) != rN_message
    assert encrypt_message(base_message, 10) != r3_message
    # chamadas bem sucedidas
    assert encrypt_message(base_message, 3) == r3_message
    assert encrypt_message(base_message, 4) == r4_message
    assert encrypt_message(base_message, 10) == rN_message
