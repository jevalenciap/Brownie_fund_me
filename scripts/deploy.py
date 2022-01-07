from brownie import FundMe, network, config, accounts


def deploy_fund_me():
    account = accounts.load("developer")
    fund_me = FundMe.deploy({"from": account}, publish_source=True)
    print(f"Contract deployed to {fund_me.address}")


def main():
    deploy_fund_me()
