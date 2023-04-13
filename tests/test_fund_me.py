from scripts.helpful_scripts import get_account, LOCAL_BLOCKCHAIN_DEVELOPMENTS
from scripts.deploy import deploy_FundMe
from brownie import network, accounts, exceptions
import pytest


def test_can_fund_and_withdraw():
    account = get_account()
    fund_me = deploy_FundMe()
    entrance_fee = fund_me.getEntranceFee() + 100
    tx = fund_me.fund({"from": account, "value": entrance_fee})
    tx.wait(1)
    assert fund_me.addressToAmountFunded(account.address) == entrance_fee
    tx2 = fund_me.withdraw({"from": account})
    tx2.wait(1)


def test_only_owner_can_withdraw():
    if network.show_active() not in LOCAL_BLOCKCHAIN_DEVELOPMENTS:
        pytest.skip("only for local testing")
    fund_me = deploy_FundMe()
    bad_actor = accounts.add()
    with pytest.raises(exceptions.VirtualMachineError):
        fund_me.withdraw({"from": bad_actor})
