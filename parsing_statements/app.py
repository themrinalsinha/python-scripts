from os   import path
from csv  import DictReader, DictWriter
from yaml import load

class ParseCSV(object):
    def __init__(self, infile):
        self.infile   = infile
        self.filepath = path.dirname(path.abspath(infile))
        self.filename = path.basename(infile)
        self.outfile  = path.join(self.filepath, 'out_{}'.format(self.filename))
        self.mapping  = load(open('header_mapping.yml')) if path.exists('header_mapping.yml') else None

    def header_mapped(self):
        if self.mapping:
            related      = {}
            self.data    = DictReader(open(self.infile))
            self.headers = self.data.fieldnames
            for header in self.headers:
                for key, value in self.mapping.items():
                    if header in value:
                        related.setdefault(key, header)
            return related
        return None

    def stitch(self, fix_field, stitch_field):
        header_map = self.header_mapped()
        if header_map:
            if stitch_field in header_map.keys() and fix_field in header_map.keys():
                stitched_data  = []
                required_data  = list(self.data)
                defined_keys   = header_map.values()
                undefined_keys = set(self.headers).difference(defined_keys)

                for d in required_data:
                    for k in list(d):
                        if k in undefined_keys:
                            del d[k]

                for row in required_data:
                    if row[header_map[fix_field]] not in ['', ' ', None]:
                        stitched_data.append(row)
                    else:
                        stitched_data[-1][header_map[stitch_field]] += ' ' + row[header_map[stitch_field]]
                return stitched_data
            return 'Field do not exist'
        return 'Header mapping do not exist'

    def stitch_and_write(self, fix_field, stitch_field):
        stitched_data = self.stitch(fix_field, stitch_field)
        if stitched_data and isinstance(stitched_data, list):
            with open(self.outfile, 'w') as csvfile:
                writer = DictWriter(csvfile, fieldnames=self.header_mapped().values())
                writer.writeheader()
                for record in tqdm(stitched_data):
                    writer.writerow(record)
