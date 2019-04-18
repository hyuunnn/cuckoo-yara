from cuckoo.common.abstracts import Report
from cuckoo.common.exceptions import CuckooReportError

import os
import json
import codecs

class CuckooYara(Report):
    def run(self, results):
        try:
            report = codecs.open(os.path.join(self.reports_path, "report.txt"), "w", "utf-8")
            report.write(str(results))
            report.close()
        except (UnicodeError, TypeError, IOError) as e:
            raise CuckooReportError("Failed to generate Yara rule: %s" % e)
