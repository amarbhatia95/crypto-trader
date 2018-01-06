import requests
import numpy as np

def fetchExchangeData(url):
    exchangeData = requests.get(url)
    return exchangeData.json()
def getBalanceAfterFees(balanceBeforeFees, feeRate):
    fee = balanceBeforeFees * feeRate
    balanceAfterFees = balanceBeforeFees - fee
    return balanceAfterFees
# def getGdaxQuote(pair):

def tradeGdaxBtcUsd(usdBalance):
    btcUsdData = fetchExchangeData('https://api.gdax.com/products/BTC-USD/ticker')
    btcUsdRate = float(btcUsdData['price'])
    takerFeeRate = 0.0025
    btcBalanceBeforeFees = usdBalance / btcUsdRate
    btcBalanceAfterFees = getBalanceAfterFees(btcBalanceBeforeFees, takerFeeRate)
    return btcBalanceAfterFees
def tradeKrakenXrpBtc(btcBalance):
    xrpBtcData = fetchExchangeData('https://api.kraken.com/0/public/Ticker?pair=XRPXBT')['result']['XXRPXXBT']
    xrpBtcRate = float(xrpBtcData['c'][0])
    makerFeesRate = 0.0026
    xrpBalanceBeforeFees = btcBalance / xrpBtcRate
    xrpBalanceAfterFees = getBalanceAfterFees(xrpBalanceBeforeFees, makerFeesRate)
    return xrpBalanceAfterFees
def initialize():
    exchanges = np.array(['gdax', 'kraken', 'bitsane', 'bitso'])
    exchangePairsUrls = {
        'gdax': 'https://api.gdax.com/products',
        'kraken': 'https://api.kraken.com/0/public/AssetPairs',
        'bitsane': 'https://bitsane.com/api/public/assets/pairs',
        'bitso': 'https://api.bitso.com/v3/available_books/'
    }
    exchangePairs = {}
    for exchange in exchanges:
        exchangePairs[exchange] = fetchExchangeData(exchangePairsUrls[exchange])
    print('exchangePairs: ', exchangePairs)
    # define var that returns all pairs for respective exchanges exchanges
    # gdaxBtcBalanceAfterFees = tradeGdaxBtcUsd(10000)
    # print(gdaxBtcBalanceAfterFees)
    #
    # krakenXrpBalanceAfterFees = tradeKrakenXrpBtc(gdaxBtcBalanceAfterFees)
    # print(krakenXrpBalanceAfterFees)
initialize()

# import json, requests
# import pandas as pd
# import numpy as np
# # Changelly: btc, bch, eth, xmr, zec, dash, ltc
# ''' BTC'''
# # Coinbase: BTC, BCH, ETH, LTC
# def coinbaseBTC_USD():
#     coinBaseTick = requests.get('https://api.coinbase.com/v2/prices/btc-usd/spot') # replace buy with spot, sell
#     return coinBaseTick.json()['data']['amount'] # replace amount with currency etc
#
# def krakenXRP_BTC():
#     krakenTick = requests.get('https://api.kraken.com/0/public/Ticker?pair=XRPXBT')
#
#     return krakenTick.json()['result']['XXRPXXBT']['c'][0]
# print(krakenXRP_BTC())
# ''' RIPPLE '''
# # Kraken: BTC, XRP, LTC, DASH, XMR, BCH
# def krakenBTC_USD():
#     krakenTick = requests.get('https://api.kraken.com/0/public/Ticker?pair=XBTUSD')
#     return krakenTick.json()['result']['XXBTZUSD']['c'][0]
#
# def krakenXRP_USD():
#     krakenTick = requests.get('https://api.kraken.com/0/public/Ticker?pair=XRPUSD')
#     return krakenTick.json()['result']['XXRPZUSD']['c'][0]
#
# # Bitsane: BTC, BCH, LTC, DASH
# def bitsaneXRP_BTC():
#     bitsaneTick = requests.get('https://bitsane.com/api/public/ticker')
#     return bitsaneTick.json()['XRP_BTC']['last']
# print(bitsaneXRP_BTC())
#
# # Binance: Everything
# def binanceXRP_BTC():
#     binanceTick = requests.get('https://api.binance.com/api/v1/ticker/allPrices')
#     return binanceTick.json()[93]['price']
# print(binanceXRP_BTC())
#
# # Bitfinex: Everything
# def bitfinex(currency_pair):
#     ''' Enter currency pair as btcusd'''
#     bitfinex = requests.get('https://api.bitfinex.com/v1/pubticker/{}'.format(currency_pair))
#     return bitfinex.json()['last_price']
# #print(bitfinex('xrpbtc'))
#
# # BITSO: btc, xrp, eth, bch, ltc
# def bitso(currency_pair):
#     ''' currency_pair can only take btc_mxn, eth_mxn, xrp_btc, xrp_mxn, eth_btc, bch_btc, ltc_btc, ltc_mxn'''
#     bitso = requests.get('https://api.bitso.com/v3/ticker/', params={'book': currency_pair})
#     return bitso.json()['payload']['last']
# #print(bitso('xrp_btc'))
#
# # ETC, LSK, FCT, XMR, REP, XRP, ZEC, XEM, LTC, DASH, BCH
# def coincheck(currency_pair):
#     ''' Enter currency pair as btc_usd'''
#     coincheckTick = requests.get('https://coincheck.com/api/rate/{}'.format(currency_pair))
#     return coincheckTick.json()['rate']
# print(coincheck('xrp_btc'))
