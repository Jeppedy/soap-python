#!/usr/bin/env python

from pysimplesoap.client import SoapClient

mywsdl="http://soaptest.parasoft.com/calculator.wsdl"
client = SoapClient(wsdl=mywsdl,trace=False)
response = client.add(1.4,23.9)
#print response
result = response['Result']
print result

mywsdl="http://www.webservicex.net/geoipservice.asmx?WSDL"
client = SoapClient(wsdl=mywsdl,trace=False)
response = client.GetGeoIP("8.8.8.8")
#print response
result = response['GetGeoIPResult']['CountryName']
print result

