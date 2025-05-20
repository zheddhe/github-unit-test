from wallet import Wallet, InsufficientAmount
import pytest

@pytest.fixture
def empty_wallet():
    '''Returns a Wallet instance with a zero balance'''
    return Wallet()

@pytest.fixture
def wallet():
    '''Returns a Wallet instance with a balance of 100'''
    return Wallet(50)

def test_wallet_default_initial_amount(empty_wallet):
    assert empty_wallet.balance == 0

def test_wallet_setting_initial_amount(wallet):
    assert wallet.balance == 50

def test_wallet_add_cash(wallet):
    wallet.add_cash(90)
    assert wallet.balance == 140

def test_wallet_spend_cash(wallet):
    wallet.spend_cash(10)
    assert wallet.balance == 40

def test_wallet_spend_cash_raises_exception_on_insufficient_amount(empty_wallet):
    with pytest.raises(InsufficientAmount):
        empty_wallet.spend_cash(100)

@pytest.mark.parametrize("earned,spent,expected", [(30, 10, 20), (20, 2, 18)])
def test_transactions(empty_wallet, earned, spent, expected):
    empty_wallet = Wallet()
    empty_wallet.add_cash(earned)
    empty_wallet.spend_cash(spent)
    assert empty_wallet.balance == expected