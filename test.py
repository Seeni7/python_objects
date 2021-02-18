import re
import glob
receipts = [f for f in glob.iglob("./new/receipts-*[0-99].json") ] #if re.match("./new/receipts-[0-99]*[24680].json", f) ]
print(receipts)