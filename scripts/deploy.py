from brownie import FundMe, network, config, MockV3Aggregator
from scripts.helpful_scripts import (
    get_account,
    deploy_mocks,
    LOCAL_BLOCKCHAIN_DEVELOPMENTS,
    FORKED_LOCAL_ENVIROMENTS,
)
from web3 import Web3


def deploy_FundMe():
    account = get_account()
    # pass the price feed
    if (
        network.show_active() not in LOCAL_BLOCKCHAIN_DEVELOPMENTS
        or network.show_active() in FORKED_LOCAL_ENVIROMENTS
    ):
        price_feed_address = config["networks"][network.show_active()][
            "eth_usd_price_feed"
        ]
        print(f"price feed contract : {price_feed_address}")
    else:
        deploy_mocks()
        price_feed_address = MockV3Aggregator[-1].address
    fund_me = FundMe.deploy(
        price_feed_address,
        {"from": account},
        publish_source=config["networks"][network.show_active()].get("verify"),
    )
    print(f"Contract deployed to {fund_me.address}")
    return fund_me


def main():
    deploy_FundMe()
