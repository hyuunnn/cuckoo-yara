# cuckoo-yara

## Settings
<a href="https://yara.readthedocs.io/en/v3.9.0/gettingstarted.html">Link</a>

``` bash
sudo apt-get install automake libtool make gcc flex bison libssl-dev libjansson-dev libmagic-dev
wget https://github.com/VirusTotal/yara/archive/v3.9.0.tar.gz
tar -xvf yara-3.9.0.tar.gz
cd yara-3.9.0
./build.sh --enable-cuckoo --enable-magic --enable-dotnet
make
sudo make install

(Optional)
pip install yara-python

or

git clone https://github.com/VirusTotal/yara-python
cd yara-python
python setup.py build --enable-cuckoo
python setup.py install
```

```
cuckooyara.py : /usr/local/lib/python2.7/dist-packages/cuckoo/reporting/cuckooyara.py
config.py : /usr/local/lib/python2.7/dist-packages/cuckoo/common/config.py
reporting.conf : .cuckoo/conf/reporting.conf
```

## How to use YARA's cuckoo module
<a href="https://yara.readthedocs.io/en/v3.9.0/modules/cuckoo.html">Link</a>

``` bash
$yara -x cuckoo=behavior_report_file rules_file pe_file
```

``` py
import yara
rules = yara.compile('./rules_file')
report_file = open('./behavior_report_file')
report_data = report_file.read()
rules.match(pe_file, modules_data={'cuckoo': bytes(report_data)})
```

### test.yar
``` 
import "cuckoo"

rule test
{
    condition:
        cuckoo.network.dns_lookup(/\.com/) or
        cuckoo.network.http_request(/\.com/)
}
```
![1](/images/1.png)

cuckoo module uses the value of report.json to compare.

last argument does not affect the cuckoo rule.

Virustotal Intelligence supported YARA's cuckoo module. (<a href="https://support.virustotal.com/hc/en-us/articles/360000363717-VT-Hunting">Link</a>)