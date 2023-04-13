from brownie import network, config, accounts, MockV3Aggregator
from web3 import Web3

DECIMALS = 18
Starting_PRICE = 2000
LOCAL_BLOCKCHAIN_DEVELOPMENTS = ["development", "ganachelocal"]
FORKED_LOCAL_ENVIROMENTS = ["mainnet-fork", "mainnet-fork-dev"]


def get_account():
    if (
        network.show_active() in LOCAL_BLOCKCHAIN_DEVELOPMENTS
        or network.show_active() in FORKED_LOCAL_ENVIROMENTS
    ):
        return accounts[0]
    else:
        return accounts.add(config["wallets"]["from_key"])


def deploy_mocks():
    print(f"THe active network is {network.show_active()}")
    print("Deploying mock ....")
    print(f" account : {get_account()}")
    if len(MockV3Aggregator) <= 0:
        print("len < 0 ")
        txn = MockV3Aggregator.deploy(
            DECIMALS, Web3.toWei(Starting_PRICE, "ether"), {"from": get_account()}
        )
    print("Mock deployed")
