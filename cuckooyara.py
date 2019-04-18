from cuckoo.common.abstracts import Report
from cuckoo.common.exceptions import CuckooReportError

import os
import json
import codecs

class CuckooYara(Report):

    def httpRequest(self, data):
        rule = "rule httpRequest\n"
        rule += "{\n"
        rule += "   condition:\n"
        for i in data['network']['http']:
            rule += "       cuckoo.network.http_request(/{}/) or\n".format(i['host'])
        
        rule = rule[:-4] + "\n}\n"
        return rule

    def dnsLookup(self, data):
        rule = "rule dnsLookup\n"
        rule += "{\n"
        rule += "   condition:\n"
        for i in data['network']['dns']:
            if i['answers']:
                rule += "       cuckoo.network.dns_lookup(/{}/) or\n".format(i['request'])
        
        rule = rule[:-4] + "\n}\n"
        return rule

    def run(self, results):
        try:
            report = codecs.open(os.path.join(self.reports_path, "result.yar"), "w", "utf-8")

            rule = "import \"cuckoo\"\n\n"
            rule += self.httpRequest(results)
            rule += self.dnsLookup(results)

            report.write(rule)
            report.close()
        except (UnicodeError, TypeError, IOError) as e:
            raise CuckooReportError("Failed to generate Yara rule: %s" % e)
