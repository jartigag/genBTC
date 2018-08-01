# genBTC
just glueing chunks of code<sup>[1,](#chunk-1)</sup><sup>[2,](#chunk-2)</sup><sup>[3](#chunk-3)</sup> to better understand [how bitcoin addresses work](https://en.bitcoin.it/wiki/Technical_background_of_version_1_Bitcoin_addresses)

---

<a name="chunk-1">1</a>: [https://bitcoin.stackexchange.com/questions/25024/how-do-you-get-a-bitcoin-public-key-from-a-private-key](https://bitcoin.stackexchange.com/questions/25024/how-do-you-get-a-bitcoin-public-key-from-a-private-key)   
<a name="chunk-2">2</a>: [https://stackoverflow.com/questions/47319779/generating-bitcoin-key-pair-in-python-3-6-from-public-key-to-public-address](https://stackoverflow.com/questions/47319779/generating-bitcoin-key-pair-in-python-3-6-from-public-key-to-public-address)  
<a name="chunk-3">3</a>: [https://www.reddit.com/r/Bitcoin/comments/7tzq3w/generate_your_own_private_key_5_lines_of_python/](https://www.reddit.com/r/Bitcoin/comments/7tzq3w/generate_your_own_private_key_5_lines_of_python/)

## example

```
>> python genBTCAddr.py 0C28FCA386C7A227600B2FE50B7CAE11EC86D3BF1FBE471BE89827E19D72AA1D

privKey (hex format) =  0xc28fca386c7a227600b2fe50b7cae11ec86d3bf1fbe471be89827e19d72aa1d
privKey (wif format) =  5HueCGU8rMjxEXxiPuD5BDku4MkFqeZyd4dZ1jvhTVqvbTLvyTJ
pubKey =                0x4d0de0aaeaefad02b8bdc8a01a1b8b11c696bd3d66a2c5f10780d95b7df42645cd85228a6fb29940e858e7e55842ae2bd115d1ed7cc0e82d934e929c97648cb0a
BTC-address =           1GAehh7TsJAHuUAeKZcXf5CnwuGuGgyX2S
```
([wif](https://en.bitcoin.it/wiki/Wallet_import_format) will pop up in qr-code)  
![](qr-example.png)
